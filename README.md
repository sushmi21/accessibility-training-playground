# Accessibility training playground

A small fake application for practising accessibility checks, used in the
Accessibility Champions training. Live at
<https://sushmi21.github.io/accessibility-training-playground/>.

It exists in two versions that look the same:

- `accessible/`: the reference. Native HTML first, ARIA only where it adds something.
- `broken/`: the same screens with deliberate accessibility bugs, for self-exploration and demos.

Both are generated from one template, `src/template.html`, so they stay visually
identical. Edit the template, then run:

```sh
python3 build.py
```

The site root forwards to the accessible version, which opens on its Home page:
the primer and reading list, with links to the seeded version and to
`documentation/index.html`, where the session plans and missions live. Those two
pages are plain HTML and are not generated.

The playground covers name, role and state (WCAG 4.1.2), ARIA overriding native
semantics, text alternatives, keyboard access, bypass blocks (2.4.1), page titles
(2.4.2), focus order (2.4.3), focus visibility (2.4.7) and status messages (4.1.3).
The Settings page adds page structure: headings and landmarks (1.3.1, 2.4.6), link
purpose (2.4.4) and language of parts (3.1.2).
The Monitoring page is a design handed over for implementation review: the seeded
version is the handoff as received, the accessible version the revised proposal
after design review. It covers text contrast (1.4.3), content that moves on its
own (2.2.2), reflow (1.4.10), a text alternative for a chart (1.1.1), error
identification and suggestion (3.3.1, 3.3.3) and status messages (4.1.3), plus
the questions a reviewer has to ask when the design leaves states unspecified.
A second batch of panels, loaded on demand from the same page, adds timing
(2.2.1), use of colour (1.4.1), non-text contrast (1.4.11), text spacing
(1.4.12), images of text (1.4.5), sensory characteristics (1.3.3), consistent
identification (3.2.4), link purpose (2.4.4), target size (2.5.8), content on
hover (1.4.13), labels and instructions (3.3.2) and dragging movements (2.5.7).

The list of seeded bugs is deliberately not in this repository.
