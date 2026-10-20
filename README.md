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

Open `index.html` to pick a version. The Home item inside the app carries the
primer and reading list, and `documentation/index.html` has the session plans and
missions. Those two pages are plain HTML and are not generated.

The playground covers name, role and state (WCAG 4.1.2), ARIA overriding native
semantics, text alternatives, keyboard access, bypass blocks (2.4.1), page titles
(2.4.2), focus order (2.4.3), focus visibility (2.4.7) and status messages (4.1.3).

The list of seeded bugs is deliberately not in this repository.
