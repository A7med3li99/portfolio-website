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

def test_gsap_elements_present(page):
    # Load index.html
    path = os.path.abspath("index.html")
    page.goto(f"file://{path}", wait_until="domcontentloaded")

    # Select all elements with GSAP animation classes
    gsap_selectors = [
        ".gsap-reveal",
        ".gsap-slide-up",
        ".gsap-slide-left",
        ".gsap-slide-right",
        ".gsap-scale",
    ]
    total = sum(page.locator(sel).count() for sel in gsap_selectors)
    assert total > 0, "No elements with GSAP animation classes found"

if __name__ == "__main__":
    pytest.main([__file__])
