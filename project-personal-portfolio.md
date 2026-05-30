# Project — Personal Portfolio
## Case study content & Claude Code instructions

---

## Meta

```
Client:  Personal project
Role:    UX/UI Designer + Frontend
Year:    2025
Type:    Portfolio Design · Design to Code
```

---

## Challenge

My previous portfolio ran on Figma Sites — a monthly subscription
with limited flexibility and no real ownership of the output.
I needed a faster, cheaper solution I could fully control
and use as a proof of concept for client delivery.

---

## What I Delivered

**UX & UI Design**
Defined the full information architecture, wireframes,
and visual direction — cream palette, Satoshi typography,
and a custom illustrated character as the brand element.

**Iterative Build with Claude Code**
Used Claude Code to translate the design into a clean
index.html through iterative prompting and feedback loops.
Each section was reviewed, adjusted, and refined
until it matched the intended design.

**Deployment via GitHub and Vercel**
Connected the project to GitHub for version control
and deployed on Vercel for fast, free hosting
with a custom domain.

---

## Old vs New

| | Old portfolio | New portfolio |
|---|---|---|
| Platform | Figma Sites | Custom HTML/CSS/JS |
| Cost | Monthly subscription | Free |
| Flexibility | Limited | Full control |
| Delivery method | Figma export | GitHub + Vercel |
| Load speed | Slow | Fast |

---

## Impact

Full ownership of the codebase with zero monthly cost.
A repeatable delivery workflow I can now offer to clients
as a Design to Code service.

---

## Claude Code instructions

### Assets

```
assets/portfolio-project.jpg   → cover image for project card on homepage
assets/old-portfolio.png       → screenshot of old Figma Sites portfolio
                                  use in "Old vs New" comparison section
assets/new-portfolio.png       → screenshot of new portfolio
                                  use in "Old vs New" comparison section
```

### Project card on homepage

```
Cover:       assets/portfolio-project.jpg
Title:       Personal Portfolio
Descriptor:  UX/UI Design · Design to Code · 2025
Link:        /work/personal-portfolio
```

### Comparison section layout

Two side-by-side images with labels below.

```
Left:   assets/old-portfolio.png   label: "Previous — Figma Sites"
Right:  assets/new-portfolio.png   label: "Current — Claude Code + Vercel"
```

Image style:
```css
border: 1px solid #E0D9CE;
border-radius: 12px;
object-fit: cover;
width: 100%;
```

Mobile: stack vertically, old on top, new below.
