---
name: Podxero Enterprise GEO
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3b4b3b'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6b7b69'
  outline-variant: '#bacbb7'
  surface-tint: '#006e2a'
  primary: '#006e2a'
  on-primary: '#ffffff'
  primary-container: '#00ed64'
  on-primary-container: '#006626'
  inverse-primary: '#00e560'
  secondary: '#096c4d'
  on-secondary: '#ffffff'
  secondary-container: '#9ff4cd'
  on-secondary-container: '#167253'
  tertiary: '#476271'
  on-tertiary: '#ffffff'
  tertiary-container: '#b6d2e3'
  on-tertiary-container: '#405b6a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#69ff87'
  primary-fixed-dim: '#00e560'
  on-primary-fixed: '#002108'
  on-primary-fixed-variant: '#00531e'
  secondary-fixed: '#9ff4cd'
  secondary-fixed-dim: '#84d7b2'
  on-secondary-fixed: '#002115'
  on-secondary-fixed-variant: '#005139'
  tertiary-fixed: '#cae7f8'
  tertiary-fixed-dim: '#afcadc'
  on-tertiary-fixed: '#001e2b'
  on-tertiary-fixed-variant: '#304a58'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
  surface-subtle: '#f9fbfa'
  surface-soft: '#f4f7f6'
  surface-feature: '#e3fcef'
  hairline: '#e1e5e8'
  hairline-strong: '#c1ccd6'
  text-secondary: '#3d4f5b'
  text-muted: '#5c6c7a'
typography:
  hero-display:
    fontFamily: Inter
    fontSize: 64px
    fontWeight: '500'
    lineHeight: 70px
    letterSpacing: -1.2px
  hero-display-mobile:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '500'
    lineHeight: 44px
    letterSpacing: -0.5px
  heading-1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '500'
    lineHeight: 58px
    letterSpacing: -0.5px
  heading-1-mobile:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
    letterSpacing: -0.3px
  heading-2:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '500'
    lineHeight: 45px
    letterSpacing: -0.4px
  heading-3:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
  heading-4:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: '500'
    lineHeight: 30px
  subtitle:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  button-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 18px
  caption:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  micro-uppercase:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 1px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 2rem
  margin: 1.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

This design system powers Podxero (podxero.com), an enterprise Generative Engine Optimization (GEO) and AI Search Optimization platform tailored for the Simplified Chinese market. The brand personality is technical, authoritative, and precision-engineered—built to convey measurable control over how enterprise brands appear in AI-generated answers and search citations.

The target audience includes enterprise marketing directors, SEO/GEO leads, and growth engineers who rely on structured data, clear benchmarks, and transparent pricing. The UI evokes confidence, analytical clarity, and modern reliability.

The design style blends **Corporate / Modern** structure with **Minimalism**:
- **High-Contrast Light Canvas:** Stark white (`#ffffff`) primary surfaces paired with subtle light gray (`#f9fbfa`, `#f4f7f6`) section bands for effortless long-form reading in Simplified Chinese.
- **Crisp Technical Precision:** `1px` hairline borders (`#e1e5e8`), structured comparison tables, and `12px` rounded cards create a clean, documentation-grade hierarchy.
- **Unmistakable Action Signals:** Bright green (`#00ed64`) pill-shaped CTAs paired with deep navy-teal (`#001e2b`) text ensure primary actions stand out immediately without visual clutter.

## Colors

The color palette is anchored in a high-contrast light mode architecture:
- **Primary (`#00ed64`)**: Reserved exclusively for primary pill CTAs, active feature highlights, and key interactive indicators. Always pair with deep navy-teal (`#001e2b`) text for accessible contrast.
- **Secondary (`#00684a`)**: Used for inline text links, active segmented tab indicators, and `2px` input focus rings.
- **Tertiary (`#001e2b`)**: Serves as the primary ink color for headlines and body copy on light surfaces, as well as the background for high-contrast code/telemetry mockups and dark footer bands.
- **Neutral (`#ffffff`)**: The default page canvas, card background, and input surface, supported by `surface-subtle` (`#f9fbfa`) and `surface-soft` (`#f4f7f6`) for quiet section separation.
- **Borders & Text**: `hairline` (`#e1e5e8`) defines card and table boundaries, while `hairline-strong` (`#c1ccd6`) frames inputs and secondary buttons. Secondary copy uses `#3d4f5b` and `#5c6c7a`.

## Typography

`Inter` is used across all headline, body, and label roles, paired with system Simplified Chinese fallbacks (`PingFang SC`, `Microsoft YaHei`, `Noto Sans SC`, sans-serif) to ensure crisp, balanced rendering for bilingual Chinese/English enterprise copy.

- **Line Height & Readability**: Body text (`body-md` at `16px` / `26px` line-height, `body-sm` at `14px` / `22px` line-height) provides generous vertical breathing room for dense Simplified Chinese characters.
- **Responsive Scaling**: Headlines larger than `32px` (`hero-display`, `heading-1`) step down on mobile viewports (`< 768px`) to `36px` and `32px` respectively, preventing awkward line wrapping on narrow screens.
- **Technical & Metric Alignment**: Tabular numerals (`font-variant-numeric: tabular-nums`) should be applied to all AI visibility scores, pricing tiers, and comparison tables.

## Layout & Spacing

The layout uses a **12-column fluid grid** constrained to a `1280px` maximum container width, with `2rem` (`32px`) column gutters and `1.5rem` (`24px`) outer canvas margins.

- **Spacing Rhythm**: Built on a `4px` (`0.25rem`) base unit. Cards and feature panels use `1.5rem` (`24px`) to `2rem` (`32px`) internal padding, while major marketing sections are separated by `4rem` (`64px`) to `6rem` (`96px`) of vertical rhythm.
- **Breakpoints & Reflow**:
  - **Desktop (`>= 1024px`)**: Full 12-column grid; 3-column pricing and feature card rows; 6-column footer.
  - **Tablet (`768px – 1023px`)**: 8-column adaptation; 3-column grids reflow to 2-column; footer collapses to 3 columns.
  - **Mobile (`< 768px`)**: Single-column stack with `1rem` (`16px`) outer margins and `1rem` (`16px`) gutters; comparison tables scroll horizontally within their container.

## Elevation & Depth

Visual hierarchy relies primarily on **low-contrast outlines** and **tonal surface shifts** rather than heavy drop shadows:
- **Flat Hairline Surfaces (Default)**: Standard cards, pricing tiers, and comparison tables sit flat on `#ffffff` or `#f9fbfa` with a crisp `1px solid #e1e5e8` border and zero shadow.
- **Subtle Hover Elevation**: Interactive tiles and clickable cards transition to a diffused ambient shadow (`0px 4px 12px rgba(0, 30, 43, 0.08)`) on hover.
- **Floating Mockups & Overlays**: Elevated AI citation telemetry cards and dropdown/modal overlays use a deeper, low-opacity navy-tinted shadow (`0px 12px 24px -4px rgba(0, 30, 43, 0.12)`) to separate them cleanly from the canvas.

## Shapes

The shape language balances approachable modernity with technical precision:
- **Standard Cards & Containers**: Use `12px` (`0.75rem`) rounded corners (`card-base`, pricing tiers, testimonial cards, and telemetry mockups) to soften the `1px` hairline grid.
- **Inputs & Search**: Use `8px` (`0.5rem`) corners for text fields, search pills, and comparison table wrappers.
- **Pill CTAs & Status Badges**: All primary and secondary buttons, filter pills, and status badges use full pill rounding (`9999px`).

## Components

- **Buttons**:
  - *Primary*: Pill-shaped (`9999px`), `#00ed64` fill, `#001e2b` `button-md` text, `12px 24px` padding. Hover shifts to `#00b545`; pressed shifts to `#008c34`.
  - *Secondary*: Pill-shaped, `#ffffff` fill, `1px solid #c1ccd6` border, `#001e2b` text.
  - *Ghost / Link*: Transparent background, `#00684a` text with subtle underline on hover.
- **Chips & Badges**: Pill-shaped (`9999px`) with `13px` (`600` weight) text. Use `#e3fcef` background with `#00684a` text for active status, or `#001e2b` background with `#00ed64` text for "推荐 / Popular" tier badges.
- **Cards**: `12px` border radius, `#ffffff` background, `1px solid #e1e5e8` border, and `24px` (`space-lg`) padding. Featured pricing cards use `#e3fcef` background with a `2px solid #00ed64` border.
- **Input Fields**: `8px` border radius, `#ffffff` background, `1px solid #c1ccd6` border, `12px 16px` padding, and `#001e2b` text. Focus state applies a `2px solid #00684a` border.
- **Checkboxes & Radio Buttons**: `18px` controls with `1px solid #c1ccd6` border at rest; `#00684a` fill with `#ffffff` checkmark/dot when selected.
- **Lists & Comparison Tables**: `8px` rounded outer container with `1px solid #e1e5e8` border and `1px solid #eceff1` horizontal row dividers.
- **Product-Specific Components**:
  - *AI Visibility Scorecard*: `12px` rounded card displaying tabular KPI metrics (e.g., AI 引用率, 品牌提及度) in `#001e2b` with `#00684a` positive trend indicators.
  - *Citation Telemetry Mockup*: `#001e2b` dark-surface card (`12px` radius) floating over light sections to showcase live AI search engine responses and structured schema snippets.