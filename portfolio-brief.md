# Portfolio — Michal Podskoč
## Site IA, structure & content brief for implementation

---

## Project type
One-page portfolio with separate project detail pages.
**Tech:** Custom web, own domain.
**Language:** English throughout.

---

## Site structure

```
/                          → One-page home
  #hero
  #work
  #about
  #process
  #contact

/about                     → Full about page (optional, linked from nav)

/work/talendly             → Project detail
/work/nda-1                → Project detail
/work/nda-2                → Project detail
```

---

## Navigation

Fixed, top. Transparent over hero, solid background after scroll.

```
Left:  Michal Podskoč
Right: Work · About · Contact
```

Mobile: hamburger → full-screen overlay nav.

---

## Section: #hero

Full viewport height (100vh).

```
Michal Podskoč
UX/UI Designer

I make the world more beautiful.
At least the digital one.

[See my work ↓]   ← smooth scroll to #work
```

Large blob character visible in hero — dominant visual element, not decoration.
Scroll indicator at bottom, animated.

---

## Section: #work

Two-column grid (desktop), one column (mobile).
Each project card: cover image/visual → project name → descriptor → year → arrow ↗
On hover: overlay with "View project".
On click: navigate to `/work/[slug]`.

**Cards:**

```
Talendly
Design system & UI · HR platform · 2024

NDA Project 01
UI design & component library · Fintech · [year]
Visual: anonymized / grayscale / abstract placeholder

NDA Project 02
UI design & design system · B2B SaaS · [year]
Visual: anonymized / grayscale / abstract placeholder
```

Divider line after project cards.

Section label "Employment" below divider.
Two side-by-side non-clickable cards:

```
Slovenská sporiteľňa
UX/UI Designer · 2023 – present
Designing internal banking tools and digital products
for one of Slovakia's largest financial institutions.

Sygic
UX/UI Designer · [year] – [year]
Navigation and mobility products
used by millions of users worldwide.
```

---

## Section: #about

Two-column layout: photo left (160×190px), text right.
Mobile: small circle photo top, text below.

```
[Photo]    UX/UI designer with five years of experience.
           Currently at Slovenská sporiteľňa, previously
           at Sygic. I design interfaces, UX flows, and
           design systems for products that need to be
           both visually clean and genuinely easy to use.

           I also run a small freelance practice —
           working with clients in fintech, e-commerce,
           and HR platforms.

           Tools & skills
           Figma · Tokens Studio · FigJam · Principle
           UX research · Design systems · Developer handoff
```

---

## Section: #process

Section label: "How I work"
Two-column grid of 6 steps. Each step: number + title + 2-sentence description.

```
01 Briefing
I listen first. Goals, constraints, users, technical
limits — I want the full picture.

02 Proposal
Clear phases and deliverables.
Transparent scope, honest timeline.

03 Research
Competitors, patterns, user problems.
AI helps me speed up analysis and surface what matters.

04 Design & Ideation
Sketches and wireframes in multiple directions.
Together we pick the one that fits.

05 Prototyping
Interactive prototype close to the real thing.
We refine details and logic together.

06 Delivery
Clean Figma file, developer-ready specs, all states
covered. If something needs fixing, I handle it.
```

---

## Section: #contact

Centered. Single CTA.

```
Have a project in mind?
Let's talk.

hello@michalpodskoc.com    ← mailto link
```

---

## Footer

```
Left:  © 2025 Michal Podskoč
Right: Work · About · LinkedIn
```

---

## Project detail pages — template

Applies to all 3 projects. URL pattern: `/work/[slug]`

Layout top to bottom:

```
1. Hero
   Large cover visual + project name + year + type tag
   e.g. "Design System · UX/UI"

2. Meta strip
   3–4 items inline: Client · Role · Year · Platform

3. Challenge
   What was the problem before I got involved.

4. What I Delivered
   List of deliverables, each with a short description paragraph.

5. Process glimpse (optional)
   1–3 visuals: screenshots, wireframes, component details.
   NDA projects: anonymized, blurred, or abstract visuals only.

6. Impact
   Bullet list of outcomes.

7. Next project →
   Link to next project in sequence.
```

**NDA project rules:**
- No product screenshots
- Cover visual: blurred, grayscale, or abstract
- Component details or color palettes may be shown without context

---

## Project content — Talendly

```
Client:  Talendly / Solvedio
Role:    Lead UX/UI Designer
Year:    2024
Type:    Design System · UX/UI
```

**Challenge**

Talendly was growing fast — but without a consistent design foundation. Components were created ad hoc, visual style varied across screens, and the gap between design and development was slowing the team down. The product needed a scalable design system before the inconsistencies became technical debt.

**What I Delivered**

*Design System from Scratch*
Built the entire design foundation — visual principles, color system, typography, spacing, layout rules, interaction patterns, and component behavior. A single source of truth for the whole product.

*Pixel-Perfect UI Design*
Delivered clean, precise UI for key features and screens with a strong focus on visual clarity and consistency.

*UX & UI Consulting*
Ongoing reviews of user flows and information architecture — keeping the product intuitive as it grew.

*Component Library*
Flexible, scalable component library built for designer-developer collaboration. Every component systematic, reusable, and ready for implementation.

**Impact**
- Faster development cycles with less back-and-forth between design and engineering.
- Unified visual language across the entire interface.
- Clear design rules that scale with the team.

---

## Project content — NDA Project 01

```
Client:  NDA
Role:    UX/UI Designer
Year:    [year]
Type:    UI Design · Component Library
```

**Challenge**

The product had an existing design foundation, but UI quality wasn't keeping pace with the product's ambitions. Components were inconsistent, the library had accumulated debt, and the gap between design and production was creating friction. My role was to elevate quality and bring structure back to the system.

**What I Delivered**

*Pixel-Perfect UI Design*
Precise, detail-oriented screens focused on clarity, consistency, and a modern visual standard — prepared for clean developer handoff.

*Design Library Management*
Maintained and optimized the existing design library — reducing inconsistencies, cleaning up debt, keeping the system easy to use for designers and developers.

*Component Expansion*
Extended the library with new reusable components that improved design speed and strengthened consistency as the product evolved.

**Impact**
- Higher UI quality and visual consistency across the product.
- Faster design and development — fewer decisions to make from scratch.
- A cleaner library the team can actually maintain.

---

## Project content — NDA Project 02

```
Client:  NDA
Role:    UX/UI Designer
Year:    [year]
Type:    UI Design · Design System
```

**Challenge**

The product had a design system in place, but it had grown organically — without clear conventions, inconsistent naming, and components that didn't map cleanly to what developers were building. The system needed refinement, not a rebuild.

**What I Delivered**

*Pixel-Perfect UI Design*
Polished UI screens with precise visual execution — consistent, clear, and built with implementation in mind.

*Design System Refinement*
Reviewed and restructured the existing system — clarified naming conventions, resolved inconsistencies, and aligned component logic with how developers actually use it.

**Impact**
- A design system the team can navigate without a guide.
- Tighter alignment between design files and production.
- More efficient collaboration across the team.

---

## Placeholders to fill before build

| Item | Status |
|---|---|
| Email | `hello@michalpodskoc.com` — confirm |
| Sygic years | fill in |
| NDA Project 01 — year and sector | fill in |
| NDA Project 02 — year and sector | fill in |
| Photo | upload final photo |
| Cover visual — Talendly | screenshot or mockup |
| Cover visual — NDA 01 | anonymized placeholder |
| Cover visual — NDA 02 | anonymized placeholder |
| LinkedIn URL | add to footer |
