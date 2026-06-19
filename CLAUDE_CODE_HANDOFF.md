# Handoff brief for Claude Code

Paste this whole file (or point Claude Code at it) after opening Claude Code **inside
this folder**. It explains the project and exactly what to do.

---

## Context
This is a finished, single-file static résumé site (`index.html`) for Joseph "Joey"
Rockwood. It's already live on **Netlify** at **joeyrockwood.fyi** (HTTPS working,
`www` redirects to apex). Right now it's deployed by manually dragging files into the
Netlify Deploys tab.

**Goal:** get this project into GitHub under the account **`josfire18`**, then (ideally)
link that repo to the existing Netlify site so pushes auto-deploy.

## Important notes before you touch anything
- `index.html` is intentionally **one self-contained file (~290 KB)**. The headshot is
  embedded as a base64 data URI inside an `<img>` tag. **Do not** "optimize," reformat,
  or minify in a way that alters or line-wraps that data URI — it will break the image.
- `.well-known/atproto-did` must stay **exactly 32 bytes, plain ASCII, no trailing
  newline** (it's the Bluesky handle verification — content is the DID only). Don't let
  an editor add a final newline.
- `_headers` is a Netlify config file; leave it at the repo root.

## Tasks

### 1. Initialize the repo and make the first commit
```bash
git init
git add -A
git commit -m "Initial commit: joeyrockwood.fyi résumé site"
git branch -M main
```

### 2. Create the GitHub repo under josfire18 and push
If the GitHub CLI (`gh`) is installed and authenticated:
```bash
gh repo create josfire18/joeyrockwood-site --public --source=. --remote=origin --push
```

If `gh` is **not** available, create an empty repo named `joeyrockwood-site` at
https://github.com/new (owner: josfire18, no README/.gitignore — this folder already
has them), then:
```bash
git remote add origin https://github.com/josfire18/joeyrockwood-site.git
git push -u origin main
```

> Repo name is just a suggestion — anything works since hosting is Netlify, not GitHub
> Pages. (If you ever wanted a free GitHub Pages backup, naming a repo
> `josfire18.github.io` would auto-serve it.)

### 3. (Manual, in the Netlify dashboard) Link the repo for auto-deploy
This part can't be done from the CLI — it's a dashboard click. Tell Joey to do this:
1. Netlify → the existing **joeyrockwood.fyi** site → **Site configuration →
   Build & deploy → Continuous deployment → Link repository**.
2. Choose GitHub → authorize → pick `josfire18/joeyrockwood-site`.
3. Build settings: **no build command**; **publish directory = `.` (root)**. It's a
   plain static site.
4. Deploy. From then on, every `git push` to `main` redeploys automatically, and the
   manual drag-and-drop is no longer needed.

### 4. Verify
- `git log` shows the commit; `git remote -v` shows the GitHub origin.
- After the Netlify link + a test push, confirm https://joeyrockwood.fyi reflects the
  change and https://joeyrockwood.fyi/.well-known/atproto-did returns the plain DID.

## Future edits workflow (for Joey)
Edit `index.html`, then:
```bash
git add -A && git commit -m "describe the change" && git push
```
Netlify redeploys within seconds.
