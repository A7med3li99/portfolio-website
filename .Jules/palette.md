## 2024-03-14 - Custom Cursor Keyboard Accessibility
**Learning:** Using `cursor: none` to implement a custom cursor removes the browser's native cursor feedback, which makes it incredibly difficult for keyboard users to track their focus without explicit `:focus-visible` styling.
**Action:** Always implement explicit, high-contrast `:focus-visible` outlines (using theme variables like `--cyan`) globally when overriding the native cursor.
