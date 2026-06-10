from unittest.mock import MagicMock

from utils import styles


def describe_styles_module():
    def it_renders_html_for_main_view(monkeypatch):
        mock_st = MagicMock()
        monkeypatch.setattr(styles, "st", mock_st)

        styles.render_html("<div>Hello</div>", sidebar=False)
        mock_st.markdown.assert_called_once_with("<div>Hello</div>", unsafe_allow_html=True)
        mock_st.sidebar.markdown.assert_not_called()

    def it_renders_html_for_sidebar(monkeypatch):
        mock_st = MagicMock()
        monkeypatch.setattr(styles, "st", mock_st)

        styles.render_html("<div>Hello</div>", sidebar=True)
        mock_st.sidebar.markdown.assert_called_once_with("<div>Hello</div>", unsafe_allow_html=True)
        mock_st.markdown.assert_not_called()

    def it_injects_global_css(monkeypatch):
        mock_render = MagicMock()
        monkeypatch.setattr(styles, "render_html", mock_render)

        styles.inject_global_css()
        assert mock_render.called
        assert "<style>" in mock_render.call_args[0][0]

    def it_returns_empty_string_for_invalid_image_path():
        res = styles.get_image_base64("nonexistent_image.png")
        assert res == ""

    def it_encodes_existing_image_to_base64(tmp_path):
        dummy_img = tmp_path / "test.png"
        dummy_img.write_bytes(b"dummy image data")
        res = styles.get_image_base64(str(dummy_img))
        assert res.startswith("data:image/png;base64,")

    def it_renders_hero_section(monkeypatch):
        mock_render = MagicMock()
        monkeypatch.setattr(styles, "render_html", mock_render)

        styles.render_hero("Test Title", "Test Subtitle")
        mock_render.assert_called_once()
        assert "Test Title" in mock_render.call_args[0][0]
        assert "Test Subtitle" in mock_render.call_args[0][0]

    def it_renders_card(monkeypatch):
        mock_render = MagicMock()
        monkeypatch.setattr(styles, "render_html", mock_render)

        styles.render_card("Card Title", "Card Content", badges="4.8", price_badge="$$")
        mock_render.assert_called_once()
        html_output = mock_render.call_args[0][0]
        assert "Card Title" in html_output
        assert "Card Content" in html_output
        assert "4.8" in html_output
        assert "$$" in html_output
