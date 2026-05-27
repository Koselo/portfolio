# Visual Design Brief
## Michal Podskoč — Portfolio

---

## Visual direction

**One-sentence description:**
Structured, cream portfolio with clean Satoshi typography and a dominant hand-drawn blob character as the main visual element of the hero section.

**Inspiration:**
- Layout & typography: Clara Fois (clarafois.com) — clean, structured, professional
- Character: Dirtybarn style — blob character with a face and tiny legs, gestural terracotta line, organic shape

**Keywords:**
clean · warm · structured · playful · confident · human

**What this portfolio is NOT:**
- Not chaotic or expressive in layout
- Not corporate or cold
- Not dark or dramatic
- Not generically white with blue
- The character is NOT a small decorative detail — it is the dominant visual element of the hero section

---

## Color palette

```
--color-bg:        #F5F0E8   Background — cream, warm base
--color-text:      #1A1A1A   Text — near black, not pure black
--color-accent:    #F04E46   Red — character fill color, CTA, hover states
--color-muted:     #8A8178   Muted text — metadata, labels, captions
--color-border:    #E0D9CE   Borders, dividers, card outlines
--color-surface:   #EDE8DF   Cards, hover state on background elements
```

**Color usage rules:**
- Accent (`#F04E46`) used SPARINGLY — character, one CTA button, hover underline on links, card hover states
- Never use accent as background for large areas
- Text is always `#1A1A1A`, never pure `#000000`
- Background is always `#F5F0E8`, never pure `#FFFFFF`

---

## Typography

**Font:** Satoshi (Fontshare)
**Import:** `https://api.fontshare.com/v2/css?f[]=satoshi@700,500,400&display=swap`

```
Display / Hero headline:
  font-family: 'Satoshi', sans-serif
  font-weight: 700
  font-size: clamp(40px, 7vw, 96px)
  line-height: 1.05
  letter-spacing: -0.02em

Section headline (H2):
  font-weight: 700
  font-size: clamp(28px, 4vw, 48px)
  line-height: 1.1
  letter-spacing: -0.01em

Card title / H3:
  font-weight: 500
  font-size: 18px
  line-height: 1.3

Body text:
  font-weight: 400
  font-size: 16px
  line-height: 1.7
  color: #1A1A1A

Small / Meta / Labels:
  font-weight: 400
  font-size: 12px
  line-height: 1.5
  color: #8A8178
  letter-spacing: 0.06em
  text-transform: uppercase (section labels only)
```

---

## Spacing system (8px grid)

```
--space-xs:   8px
--space-sm:   16px
--space-md:   24px
--space-lg:   48px
--space-xl:   80px
--space-2xl:  120px
--space-3xl:  160px
```

Sections: padding top/bottom `--space-2xl` (120px) desktop, `--space-xl` (80px) mobile.

---

## Layout

```
Max-width container: 1200px
Horizontal padding:  40px desktop / 20px mobile
Grid:                12 columns, gap 24px

Work grid:    2 columns desktop / 1 column mobile
Process grid: 2 columns desktop / 1 column mobile
About layout: [photo 280px] [text 1fr] gap 60px
```

---

## Navigation

```
Position: fixed, top: 0, width: 100%
Height: 64px
Background: transparent on hero / #F5F0E8 + border-bottom after scroll
Transition: background 0.3s ease

Desktop:
  Left:  "Michal Podskoč" — Satoshi 500, 15px
  Right: "Work · About · Contact" — Satoshi 400, 14px, letter-spacing 0.02em

Mobile:
  Left:  name
  Right: hamburger icon (24px)
  Open:  full-screen overlay, #F5F0E8 bg, nav links centered, large (32px)
```

---

## Components

### CTA Button (primary)
```css
display: inline-flex;
padding: 12px 28px;
border: 1.5px solid #1A1A1A;
border-radius: 100px;
font-size: 14px;
font-weight: 500;
color: #1A1A1A;
background: transparent;
transition: all 0.2s ease;

/* Hover */
background: #1A1A1A;
color: #F5F0E8;
```

### Project card
```css
border: 1px solid #E0D9CE;
border-radius: 12px;
overflow: hidden;
background: #F5F0E8;
transition: transform 0.25s ease, box-shadow 0.25s ease;

/* Hover */
transform: translateY(-4px);
box-shadow: 0 12px 32px rgba(26,26,26,0.08);

/* Thumb */
height: 280px desktop / 200px mobile
background: #EDE8DF
object-fit: cover

/* Body */
padding: 20px 24px;
```

### Section label
```css
font-size: 11px;
font-weight: 500;
letter-spacing: 0.1em;
text-transform: uppercase;
color: #8A8178;
margin-bottom: 40px;
```

### Divider
```css
height: 1px;
background: #E0D9CE;
margin: 60px 0;
```

### Process step card
```css
border: 1px solid #E0D9CE;
border-radius: 10px;
padding: 24px;
background: #F5F0E8;

/* Number */
font-size: 11px;
color: #8A8178;
margin-bottom: 8px;

/* Title */
font-size: 16px;
font-weight: 500;
margin-bottom: 8px;

/* Description */
font-size: 14px;
color: #8A8178;
line-height: 1.6;
```

---

## Character — brand mascot

### Description
Blob/flower character with organic rounded shape, filled red (`#F04E46`), dark outline (`#231F20`). Simple face — oval eyes, curved smile. Already created and available as SVG. Two files: `Asset_1.svg` (main character) and `Asset_3.svg` (variation).

**SVG color values:**
- Fill: `#F04E46` (red)
- Outline/stroke: `#231F20` (near black)
- Background: transparent ✓

### Hero section — layout with character
The character is LARGE — minimum 40–50% of hero section height. Not beside the text as decoration, but as an equal visual element.

```
Option A — text left, character right:
[Michal Podskoč        ] [                  ]
[UX/UI Designer        ] [   blob character  ]
[subline               ] [                   ]
[See my work ↓         ] [                   ]

Option B — character below headline, centered:
[      Michal Podskoč · UX/UI Designer      ]
[             blob character                ]
[   I make the world more beautiful.        ]
[        At least the digital one.          ]
[             See my work ↓                 ]
```

### Where the character appears
1. **Hero section** — dominant, large version (min 300px height)
2. **Contact section** — waving pose, medium version (150px)
3. **404 page** — confused pose
4. *(Optional)* NDA project cards — holding "NDA" sign, small version (80px)

### Recraft.ai prompt — main (blob style)

```
Simple hand-drawn blob character with tiny legs and a smiley face,
minimal gestural crayon-like strokes, warm terracotta red lines,
transparent background, organic rounded chubby body shape,
small stubby legs at the bottom, simple dot eyes and curved smile,
loose imperfect lines, no fill, outline only,
flat 2D illustration, SVG vector style,
friendly mascot character, Dirtybarn illustration style
```

### Recraft.ai prompt — pose variations

**Waving (contact section):**
```
Same blob character, one arm raised waving,
friendly greeting gesture, hand-drawn crayon style,
terracotta red outline, transparent background
```

**Confused (404 page):**
```
Same blob character, confused pose, tilted to one side,
arms out questioning gesture, hand-drawn crayon style,
terracotta red outline, transparent background
```

### Export & usage
- Export as SVG (not PNG) — scales to any size
- If AI generates PNG: vectorize via Adobe Illustrator "Image Trace" or vectorizer.io
- On web: `<img src="character.svg">` or inline SVG for animations
- SVG stroke color: `stroke="#C84B31"`, `fill="none"`

### Simple CSS float animation (optional)
```css
.character {
  animation: float 4s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-10px); }
}
```

---

## Loading screen

Shows on **first visit only**. Use `localStorage` key `"mp_visited"`.
If key exists → skip loader, go straight to page.

```
Background:   #1A1A1A — full screen overlay, z-index 1000
Content:      centered text block

Animation — lines appear one by one, translateY 100% → 0 + opacity 0 → 1:
  Line 1: "I make the world"          color #F5F0E8   delay 300ms
  Line 2: "more beautiful."           color #F5F0E8   delay 650ms
  Line 3: "At least the digital one." color #F04E46   delay 1000ms

Typography:   Satoshi 700, clamp(28px, 4vw, 56px), letter-spacing -0.02em

Progress line below text:
  width 40px, height 1px, background #333
  fills left to right in #F04E46, duration 2s, starts at 400ms

Loader fade out:   at 2800ms, opacity transition 0.6s ease
After loader hides: hero content animates in — fade + translateY(-12px → 0), duration 0.6s
```

---

## Micro-interactions

```
Nav links hover:       underline slide-in, color #C84B31, 0.2s
Project card hover:    translateY(-4px) + subtle shadow, 0.25s
CTA button hover:      fill black, text cream, 0.2s
Section links hover:   opacity 0.6, 0.15s
Smooth scroll:         scroll-behavior: smooth on html
Page load:             fade-in on hero content, 0.4s delay
```

---

## NDA project cards — visual rules

```
Thumb background: #EDE8DF
Pattern:          diagonal stripe, #E0D9CE, opacity 0.6
Overlay text:     "NDA" — 11px uppercase, #8A8178
Character:        holding "NDA" sign (SVG, small version)
```

---

## Mobile breakpoints

```
Desktop:  > 1024px
Tablet:   768px – 1024px  (2-column grid stays)
Mobile:   < 768px          (1-column grid, reduced spacing)
```

---

## Do NOT use

```
❌ Heavy box-shadows (this is a portfolio, not a SaaS landing page)
❌ Gradients
❌ Pure #000000 or #FFFFFF
❌ Icon libraries (Heroicons, Feather) — only if absolutely necessary
❌ Animations longer than 0.4s
❌ More than 3 type sizes on one page
❌ Accent color on large background areas
```

---

## Assets to prepare before build

```
[x] Asset_1.svg                — main character, hero section
[x] Asset_3.svg                — character variation (contact / 404)
[ ] photo.jpg                  — about section (min 800×1000px)
[ ] talendly-cover.jpg         — project card + detail hero
[ ] nda1-cover.jpg             — anonymized / abstract visual
[ ] nda2-cover.jpg             — anonymized / abstract visual
[ ] favicon.svg                — small character or initials "MP"
```
