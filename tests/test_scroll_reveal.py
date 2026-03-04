import os
import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Abort external requests to avoid timeouts
        page.route("**/*", lambda route: route.abort() if "localhost" not in route.request.url and "file://" not in route.request.url else route.continue_())
        yield page
        browser.close()

def test_scroll_reveal(page):
    # Load index.html
    path = os.path.abspath("index.html")
    page.goto(f"file://{path}", wait_until="domcontentloaded")

    # Select all elements with class 'sr'
    srs = page.locator(".sr")
    count = srs.count()
    assert count > 0, "No elements with class 'sr' found"

    # Wait for the fallback timeout (800ms in code + some buffer)
    page.wait_for_timeout(1500)

    # Check that all elements with class 'sr' now have class 'on'
    on_count = page.locator(".sr.on").count()
    assert on_count == count, f"Expected {count} elements to have 'on' class, but found {on_count}"

if __name__ == "__main__":
    pytest.main([__file__])
