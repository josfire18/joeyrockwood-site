# joeyrockwood.fyi — personal résumé site

A single-page résumé / portfolio site for Joseph (Joey) Rockwood, Software Engineer.

## Stack
- **One static `index.html`.** No build step, no framework, no dependencies. All CSS
  and JS are inline, and the headshot is embedded directly in the HTML as a base64
  data URI — so the whole site is genuinely one self-contained file (~290 KB).
- **Dark teal theme**, fully responsive, accessible (semantic HTML, keyboard focus,
  `prefers-reduced-motion` respected). The dark palette is intentional: it renders
  identically regardless of the device's light/dark mode.

## Repository layout
```
.
├── index.html                 # the entire site (image embedded inside)
├── _headers                   # Netlify: serves the Bluesky file as text/plain
├── .well-known/
│   └── atproto-did            # Bluesky handle verification (plain DID, no newline)
├── .gitignore
└── README.md
```

## Hosting
Currently deployed on **Netlify**. Custom domain **joeyrockwood.fyi** with automatic
HTTPS (Let's Encrypt). `www` redirects to the apex.

Today it's deployed by dragging the folder/zip into the Netlify **Deploys** tab. The
goal of moving this into GitHub is to enable **continuous deploy** — once the repo is
linked in Netlify, every `git push` redeploys automatically. See
`CLAUDE_CODE_HANDOFF.md` for the steps.

## Bluesky handle
The domain doubles as a Bluesky handle (`@joeyrockwood.fyi`). Verification uses the
file at `/.well-known/atproto-did`, which contains only the DID
(`did:plc:lla4hza55imtkebepzuduqxz`) as plain text with **no trailing newline**. The
`_headers` file makes Netlify serve it as `text/plain`, which Bluesky requires.
This is independent of the website and the DNS records — all three coexist.

> Alternative: instead of this file, a DNS `TXT` record at `_atproto.joeyrockwood.fyi`
> with value `did=did:plc:lla4hza55imtkebepzuduqxz` does the same job. Use one or the
> other, not both is fine either way.

## Editing
- Content (experience, skills, etc.) lives as plain HTML in `index.html`.
- To swap the headshot, re-embed a new base64 data URI in the hero `<img>` (or switch
  it to a file reference and add an `images/` folder).
