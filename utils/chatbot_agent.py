import json
import logging
import os
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

# Check if google-adk is available and key is set
ADK_AVAILABLE = False
try:
    from google.adk.agents import Agent
    from google.adk.runners import Runner
    from google.adk.sessions import InMemorySessionService
    from google.genai import types  # noqa: F401

    ADK_AVAILABLE = True
except ImportError:
    logger.warning("google-adk package is not installed. Falling back to rule-based engine.")

from utils.database import (
    get_city_by_name,
    get_city_details,
    get_country_by_name,
    get_country_details,
    search_locations,
)

# ---------------------------------------------------------
# Define Tools for Agent Kit
# Type hints and docstrings are crucial because ADK uses them
# to generate the JSON schemas for the model's function calls.
# ---------------------------------------------------------


def get_country_info(country_name: str) -> Dict[str, Any]:
    """
    Retrieves complete travel details for a country by name.
    Use this to look up capital, currency, language, timezone, emergency numbers,
    visa regulations, traffic/legal rules, cultural etiquette, or safety guidelines.
    """
    country = get_country_by_name(country_name)
    if not country:
        return {"error": f"Country '{country_name}' not found in database."}
    return dict(country)


def get_city_info(city_name: str) -> Dict[str, Any]:
    """
    Retrieves detailed information for a city by name.
    Use this to look up city descriptions, transit guidelines, cuisines, dining,
    tourist spots/attractions, hotels, shopping areas, airport details, or safety warnings.
    """
    city = get_city_by_name(city_name)
    if not city:
        return {"error": f"City '{city_name}' not found in database."}

    # Safely parse JSON strings for food, places, and hotels
    res = dict(city)
    for field in ["food_info", "tourist_places", "hotel_info"]:
        if field in res and isinstance(res[field], str):
            try:
                res[field] = json.loads(res[field])
            except Exception:  # nosec B110
                pass
    return res


def search_destinations(query: str) -> Dict[str, Any]:
    """
    Searches the travel database for matching countries or cities.
    Use this if the user is looking for destinations matching a keyword (like 'shrine' or 'beach').
    """
    return search_locations(query)


# ---------------------------------------------------------
# Agent Kit Setup
# ---------------------------------------------------------

_runner_instance: Optional[Any] = None


def get_agent_runner() -> Optional[Any]:
    global _runner_instance
    if not ADK_AVAILABLE:
        return None

    if _runner_instance is None:
        try:
            # Check for API Key in env or Streamlit secrets
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                # Try streamlit secrets if available
                try:
                    import streamlit as st

                    api_key = st.secrets.get("GEMINI_API_KEY")
                except Exception:  # nosec B110
                    pass

            if not api_key:
                logger.warning("GEMINI_API_KEY not found. Agent Kit cannot be initialized.")
                return None

            # Create Agent instance
            travel_agent = Agent(
                name="travel_mate_agent",
                model="gemini-2.5-flash",
                instruction=(
                    "You are TravelMate AI – a smart, helpful travel companion chatbot. "
                    "Use the database tools provided (get_country_info, get_city_info, search_destinations) "
                    "to answer user queries accurately. Answer clearly and structure your responses with markdown. "
                    "If the user asks a question about food, rules, safety, attractions, hotels, transit, or visa, "
                    "make sure to call the correct tool for the city/country they are asking about. "
                    "If the user's query does not mention a country or city, refer to the Active Context "
                    "provided in the system message or user prompt to determine the relevant destination."
                ),
                tools=[get_country_info, get_city_info, search_destinations],
            )

            # Create Runner instance
            _runner_instance = Runner(agent=travel_agent, session_service=InMemorySessionService())
        except Exception as e:
            logger.error(f"Failed to initialize Agent Kit: {e}")
            _runner_instance = None

    return _runner_instance


def is_agent_enabled() -> bool:
    """Returns True if google-adk is installed and GEMINI_API_KEY is configured."""
    if not ADK_AVAILABLE:
        return False
    return get_agent_runner() is not None


async def run_agent_query_async(
    user_id: str,
    session_id: str,
    query_text: str,
    active_country_id: Optional[int] = None,
    active_city_id: Optional[int] = None,
) -> str:
    """Runs the query using the ADK Agent Runner asynchronously."""
    runner = get_agent_runner()
    if not runner:
        raise RuntimeError("Agent runner is not initialized.")

    # Retrieve active context descriptions to feed to the agent
    context_str = ""
    if active_city_id:
        city = get_city_details(active_city_id)
        if city:
            context_str += f"Active City Context: {city['city_name']}. "
    if active_country_id:
        country = get_country_details(active_country_id)
        if country:
            context_str += f"Active Country Context: {country['country_name']}. "

    # Prepend active context to guide the agent in case of general queries
    full_prompt = query_text
    if context_str:
        full_prompt = f"[{context_str.strip()}]\n{query_text}"

    from google.genai import types

    content = types.Content(role="user", parts=[types.Part(text=full_prompt)])

    final_response = ""
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response = event.content.parts[0].text
                break

    if not final_response:
        final_response = "I couldn't process the query with the Agent. Please try again."

    return final_response


def run_agent_query(
    user_id: str,
    session_id: str,
    query_text: str,
    active_country_id: Optional[int] = None,
    active_city_id: Optional[int] = None,
) -> str:
    """Synchronous entry point to run the agent query."""
    import asyncio
    from concurrent.futures import ThreadPoolExecutor

    coro = run_agent_query_async(user_id, session_id, query_text, active_country_id, active_city_id)
    try:
        # Check if an event loop is already running in this thread
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        # Run in a separate thread so we don't block the main event loop
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(asyncio.run, coro)
            return future.result()
    else:
        return asyncio.run(coro)
