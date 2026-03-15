# Palette's Journal

## 2024-05-14 - Initial Setup
**Learning:** Initializing palette journal.
**Action:** Ready to paint some UX improvements.

## 2024-05-14 - Custom Cursors & Keyboard Accessibility
**Learning:** Sites with custom cursors (e.g., `cursor: none` on `body`) suppress the browser's native cursor feedback. This necessitates explicit and high-contrast `:focus-visible` styles for keyboard navigation, as users lack standard visual cues for focus state.
**Action:** Always verify keyboard accessibility and add explicit `:focus-visible` styles (e.g., `*:focus-visible { outline: 2px solid var(--primary-color); }`) when implementing custom cursors.
