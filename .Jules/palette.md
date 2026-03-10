## 2024-05-15 - Explicit Focus Outline with Custom Cursors
**Learning:** When using `cursor: none;` on the `body` to implement custom cursor feedback, the browser's native cursor is disabled. If you do not also implement explicit and high-contrast `:focus-visible` styles, keyboard navigation becomes completely invisible and inaccessible to users since they rely on focus indicators when the cursor is gone.
**Action:** Always verify keyboard focus states and add a global `:focus-visible` rule using theme highlight variables (e.g. `--cyan`) whenever implementing a custom cursor.
