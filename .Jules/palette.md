## 2025-03-05 - Accessibility improvements for Interactive Elements
**Learning:** Custom interactive elements like pagination dots were implemented as `<span>`s without keyboard focus support, which breaks accessibility. Also, removing default outlines via `outline: none` or general CSS resets without providing an alternative like `:focus-visible` removes focus visibility globally.
**Action:** Used `<button>` instead of `<span>` for interactive pagination controls and introduced a global `*:focus-visible` style to restore keyboard focus outlines across the app.
