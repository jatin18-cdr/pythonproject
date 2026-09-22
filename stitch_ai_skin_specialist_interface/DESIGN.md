---
name: Clinical Azure Specialist
colors:
  surface: '#f8f9ff'
  surface-dim: '#c4dcff'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d2e4ff'
  on-surface: '#001c37'
  on-surface-variant: '#414754'
  inverse-surface: '#19324d'
  inverse-on-surface: '#eaf1ff'
  outline: '#727785'
  outline-variant: '#c1c6d6'
  surface-tint: '#005bc0'
  primary: '#005bbf'
  on-primary: '#ffffff'
  primary-container: '#1a73e8'
  on-primary-container: '#ffffff'
  inverse-primary: '#adc7ff'
  secondary: '#006398'
  on-secondary: '#ffffff'
  secondary-container: '#5bb8fe'
  on-secondary-container: '#00476e'
  tertiary: '#006a61'
  on-tertiary: '#ffffff'
  tertiary-container: '#00857a'
  on-tertiary-container: '#ffffff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc7ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#cce5ff'
  secondary-fixed-dim: '#93ccff'
  on-secondary-fixed: '#001d31'
  on-secondary-fixed-variant: '#004b73'
  tertiary-fixed: '#89f5e7'
  tertiary-fixed-dim: '#6bd8cb'
  on-tertiary-fixed: '#00201d'
  on-tertiary-fixed-variant: '#005049'
  background: '#f8f9ff'
  on-background: '#001c37'
  surface-variant: '#d2e4ff'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 30px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.25rem
  gutter-mobile: 0.75rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.25rem
---

## Brand & Style

This design system establishes a high-trust, medical-grade aesthetic tailored for an AI-powered dermatological diagnostic and consultation interface. Built for Gradio's structural container paradigm, it fuses contemporary clinical clarity with approachable human warmth.

### Emotional Disposition & Tone
- **Authoritative & Medically Precise:** Eliminates ambiguity through clean visual hierarchy, crisp metadata, and unmistakable state changes.
- **Empathetic & Calming:** Leverages soft, cool azure tints to lower user stress during personal health evaluations and skin image submissions.
- **Advanced Diagnostic Intelligence:** Conveys state-of-the-art computational dermatopathology through subtle ambient glows, structured data readouts, and fluid multimodal feedback (audio/visual waveforms).

### Visual Direction
The design relies on **Modern Clinical Tonalism**—a fusion of clinical minimalism, structured tonal cards, and subtle luminous depth. Surfaces are treated with layered, cool-white and soft-sky containers, avoiding stark medical sterility while maintaining rigorous diagnostic legibility.

## Colors

The palette is anchored by deep navy typographical tones, authoritative azure blue primaries, and soft sky-blue diagnostic plates.

### Structural Roles
- **Canvas Base:** `#FFFFFF` (pure diagnostic white) with ambient backing zones tinted in `#F8FAFC`.
- **Card Surfaces:** Primary cards rest on `#F0F7FD`; nested interactive sub-blocks use `#E8F2FC`.
- **Primary Text:** `#102A45` for crisp readability exceeding WCAG AAA contrast standards against white and light-blue surfaces.
- **Secondary / Supporting Text:** `#5B6B82` for anatomical metadata, timestamping, model confidence scores, and field descriptors.
- **Action / Interactive Blue:** `#1A73E8` for primary triage submissions and upload triggers; `#0284C7` for auxiliary clinical tools and selected modes.
- **Borders & Dividers:** Subtle cool-gray outlines `#DCE7F3` with a 1px footprint to anchor cards without visual noise.

### Diagnostic & Status Accents
- **Normal / Healthy / Low Risk:** `#059669` (Emerald) with soft backing `#ECFDF5`.
- **Requires Review / Moderate Concern:** `#D97706` (Amber) with soft backing `#FFFBEB`.
- **Urgent Clinical Triage:** `#DC2626` (Crimson) with soft backing `#FEF2F2`.
- **Multimodal Signal (Audio/AI Processing):** `#6366F1` (Indigo/Cobalt pulse).

## Typography

Typography prioritizes swift clinical scanning and zero cognitive fatigue. 

- **Primary & Display Type (`Plus Jakarta Sans`):** Chosen for its balanced geometric clarity, open counters, and humanistic warmth. It delivers high legibility across mobile touchscreens and desktop monitors.
- **Monospaced Technical Sub-Type (`JetBrains Mono`):** Applied strictly to confidence percentages, lesion dimension metrics, millimetric scales, audio timecodes, and classification tags to reinforce mathematical precision.

## Layout & Spacing

The structural model leverages a **fixed-column diagnostic grid** optimized for Gradio's `Row`, `Column`, and `Blocks` layout engine.

- **Desktop (>= 1024px):** 2-column or 3-column asymmetric layout (e.g., Column 1: Image intake & audio symptoms [span 5]; Column 2: Diagnostic summary, differential analysis, & prescription guidance [span 7]). Outer margins sit at `2rem` with a maximum content container of `1280px`.
- **Tablet (768px - 1023px):** Balanced stacked layout with 1.5rem outer padding, converting multi-column Gradio sections into a sequential pipeline.
- **Mobile (< 768px):** Single-column stacked triage flow. Margins collapse to `1rem`, element gaps reduce to `space-sm` (`0.5rem`), keeping consultation submission triggers sticky at the screen bottom.

## Elevation & Depth

Visual hierarchy is maintained via **tonal stratification paired with diffused medical drop shadows**. Harsh dark shadows are prohibited; all elevations use cold navy tints.

### Elevation Levels
- **Level 0 (Flat / Canvas):** Pure white background (`#FFFFFF`) or tinted workflow track (`#F8FAFC`). No shadow.
- **Level 1 (Clinical Diagnostic Panels):** Background `#F0F7FD`, border `1px solid #DCE7F3`, shadow: `0 2px 8px -2px rgba(16, 42, 69, 0.04), 0 1px 3px 0 rgba(16, 42, 69, 0.02)`. Used for base consultation modules, chat inputs, and intake sections.
- **Level 2 (Active Cards & Lesion Previews):** Background `#FFFFFF`, border `1px solid #D1E1F1`, shadow: `0 10px 25px -5px rgba(16, 42, 69, 0.06), 0 4px 10px -3px rgba(16, 42, 69, 0.03)`. Used for focused image views, upload dropzones during interaction, and risk summaries.
- **Level 3 (Modals & Overlays):** Background `#FFFFFF`, shadow: `0 20px 40px -10px rgba(16, 42, 69, 0.12)`. Used for full-resolution dermoscopic zooms and diagnostic confirmation sheets.

## Shapes

The design system employs a **Rounded (Level 2)** standard, creating approachable surfaces that remove clinical rigidity without appearing childish.

- **Major Diagnostic Containers & Large Cards:** `1.5rem` (`rounded-2xl`).
- **Interactive Blocks, Inputs, & Previews:** `1rem` (`rounded-xl`).
- **Buttons, Badges, & Status Chips:** `0.5rem` to full pill (`9999px`) for triage badges and audio status pills.
- **Image Targets & Lesion Crops:** `1rem` radius with an inner inset ring (`box-shadow: inset 0 0 0 1px rgba(16, 42, 69, 0.08)`).

## Components

### Buttons
- **Primary (Diagnostic Submission / Action):** Solid `#1A73E8`, text `#FFFFFF`, font-weight 600. Height 44px (desktop) / 48px (mobile). Subtle focus ring: `0 0 0 3px rgba(26, 115, 232, 0.25)`.
- **Secondary (Tools / Resets):** Background `#E8F2FC`, text `#102A45`, border `1px solid #D1E1F1`. Hover switches background to `#DCECFB`.
- **Destructive / Reset:** Ghost button with `#DC2626` text, hovering to faint pink-red `#FEF2F2`.

### Cards & Gradio Blocks
- Wrapped in `rounded-2xl` borders, outer background `#F0F7FD`, inner container padding `space-lg` (`1.5rem`).
- Header blocks inside cards feature an upper baseline badge with a micro-icon, bold title (`title-sm`), and right-aligned clinical confidence rating.

### Chips & Clinical Status Badges
- Constructed with pill geometry (`border-radius: 9999px`), padding `0.25rem 0.75rem`, typed in `JetBrains Mono` (`label-sm`).
- **Triage Low:** Background `#ECFDF5`, text `#065F46`, left-hand 6px dot `#059669`.
- **Triage Medium:** Background `#FFFBEB`, text `#92400E`, left-hand 6px dot `#D97706`.
- **Triage High:** Background `#FEF2F2`, text `#991B1B`, left-hand 6px dot `#DC2626`.

### Inputs & Dermatological Upload Zones
- **Text & Prompt Fields:** White background (`#FFFFFF`), `1px solid #DCE7F3`, text `#102A45`, placeholder `#5B6B82`. Active state triggers `#1A73E8` border with a 3px diffused glow.
- **Image Dropzone:** Dotted border `2px dashed #93C5FD`, surface `#F8FAFC`, transitioning on drag-over to solid `#1A73E8` over `#EFF6FF`. Includes explicit instructions: "High-resolution macro or dermoscopic image required".

### Audio Consultation & Waveform Components
- **Voice Symptom Recorder:** Soft pill card featuring a pulsing record node (`#DC2626` when live, `#1A73E8` when idle).
- **Waveform Canvas:** Rendered using smooth 2px vertical bars with a 2px gap, filled with `#0284C7` (played) and `#D1E1F1` (unplayed track). Timestamp rendered via `JetBrains Mono` (`label-sm`).

### Checkboxes & Segmented Radios
- **Checkbox:** `rounded` (6px), border `2px solid #DCE7F3`. Selected state is filled `#1A73E8` with a white checkmark.
- **Segmented Consultation Options:** Pill-shaped sliding segmented bar with an active tab pill in pure `#FFFFFF` over an `#E8F2FC` trough, elevation Level 1.