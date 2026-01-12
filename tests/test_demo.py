def test_demo(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
