

```Markdown
# Context
We are making a single-page web app to access on a phone. The app is a counter for a bouncer working at a club checking the number of people going in.
# Prompt
Make a Web app which is styled to look similar to ChatGPT n terms of colours, font, etc. Add a light and dark mode with a toogle button. Add a large increment button and smaller reset button.
Don't use any external libraries.
```

###### Resulting code:

``` html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>Club Counter</title>
  <meta name="theme-color" content="#202123" />

  <style>
    /* =========================
       ChatGPT-like Design System
       ========================= */
    :root {
      /* Dark mode (default) */
      --bg: #202123;
      --bg-elev: #2a2b32;
      --panel: #343541;
      --text: #e5e7eb;       /* light gray */
      --text-dim: #cbd5e1;
      --accent: #10a37f;     /* ChatGPT green */
      --accent-hover: #0e8f70;
      --border: #3f414a;
      --shadow: 0 8px 30px rgba(0,0,0,0.35);
      --focus: 0 0 0 3px rgba(16,163,127,0.35);
    }

    :root.light {
      --bg: #f6f7f9;
      --bg-elev: #ffffff;
      --panel: #ffffff;
      --text: #111827;       /* gray-900 */
      --text-dim: #4b5563;
      --accent: #10a37f;
      --accent-hover: #0e8f70;
      --border: #e5e7eb;
      --shadow: 0 8px 24px rgba(0,0,0,0.08);
      --focus: 0 0 0 3px rgba(16,163,127,0.4);
    }

    html, body {
      height: 100%;
      background: var(--bg);
      color: var(--text);
      margin: 0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue",
                   Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
      -webkit-tap-highlight-color: transparent;
    }

    .app {
      min-height: 100%;
      display: grid;
      grid-template-rows: auto 1fr auto;
      gap: 16px;
    }

    header {
      position: sticky;
      top: 0;
      z-index: 10;
      background: linear-gradient(to bottom, var(--bg), color-mix(in oklab, var(--bg) 85%, transparent));
      border-bottom: 1px solid var(--border);
      padding: env(safe-area-inset-top) 16px 12px 16px;
    }

    .bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      max-width: 720px;
      margin: 0 auto;
    }

    .title {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      letter-spacing: 0.2px;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 26px;
      height: 26px;
      border-radius: 6px;
      background: var(--panel);
      border: 1px solid var(--border);
      color: var(--accent);
      font-weight: 700;
      font-size: 14px;
    }

    .mode-toggle {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: var(--panel);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 8px 12px;
      border-radius: 10px;
      cursor: pointer;
      box-shadow: var(--shadow);
      transition: transform 0.06s ease;
      user-select: none;
    }
    .mode-toggle:active { transform: scale(0.98); }
    .mode-toggle:focus-visible { outline: none; box-shadow: var(--focus); }

    main {
      display: grid;
      place-items: center;
      padding: 12px 16px;
    }

    .card {
      width: min(680px, 100%);
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 16px;
      box-shadow: var(--shadow);
      padding: 18px;
    }

    .count-wrap {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      gap: 8px;
      margin: 8px 0 16px;
    }

    .count-label {
      color: var(--text-dim);
      font-size: 14px;
      letter-spacing: .2px;
    }

    .count {
      font-variant-numeric: tabular-nums;
      font-size: clamp(48px, 16vw, 96px);
      font-weight: 800;
      text-align: center;
      line-height: 1;
    }

    .controls {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 12px;
      margin-top: 8px;
    }

    .btn {
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      font-size: 18px;
      font-weight: 700;
      cursor: pointer;
      transition: transform 0.06s ease, background-color 0.15s ease, border-color 0.15s ease;
      user-select: none;
      color: var(--text);
      background: var(--bg-elev);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }
    .btn:active { transform: scale(0.99); }
    .btn:focus-visible { outline: none; box-shadow: var(--focus); }

    .btn-primary {
      background: var(--accent);
      color: white;
      border-color: color-mix(in oklab, var(--accent) 85%, black);
      padding: 22px;
      font-size: clamp(18px, 3.8vw, 22px);
    }
    .btn-primary:hover { background: var(--accent-hover); }

    .btn-secondary {
      background: var(--bg-elev);
      color: var(--text);
      min-width: 92px;
    }
    .btn-secondary:hover { border-color: color-mix(in oklab, var(--border) 60%, var(--text)); }

    .hint {
      margin-top: 12px;
      color: var(--text-dim);
      font-size: 12px;
      text-align: center;
    }

    footer {
      padding: 8px 16px calc(env(safe-area-inset-bottom) + 12px);
      color: var(--text-dim);
      font-size: 12px;
      text-align: center;
    }

    /* Prefer reduced motion */
    @media (prefers-reduced-motion: reduce) {
      .btn, .mode-toggle { transition: none !important; }
    }
  </style>
</head>
<body>
  <div class="app">
    <header>
      <div class="bar" role="toolbar" aria-label="App bar">
        <div class="title" aria-label="App title">
          <span class="badge" aria-hidden="true">C</span>
          <span>Club Counter</span>
        </div>

        <button id="themeBtn" class="mode-toggle" type="button" aria-pressed="false" aria-label="Toggle dark or light mode">
          <span id="themeIcon" aria-hidden="true">🌙</span>
          <span id="themeText">Dark</span>
        </button>
      </div>
    </header>

    <main>
      <section class="card" aria-labelledby="counterHeading">
        <div class="count-wrap">
          <div class="count-label">Inside</div>
          <h1 id="counterHeading" class="count" aria-live="polite" aria-atomic="true">0</h1>
          <div></div>
        </div>

        <div class="controls">
          <button id="incBtn" class="btn btn-primary" type="button" aria-label="Add one person">
            <span aria-hidden="true">➕</span>
            <span>Increment</span>
          </button>

          <button id="resetBtn" class="btn btn-secondary" type="button" aria-label="Reset count to zero">Reset</button>
        </div>

        <div class="hint">Tip: tap anywhere on the large button to count people in.</div>
      </section>
    </main>

    <footer>
      <span>Made for quick, reliable counting. Theme & count are saved on this device.</span>
    </footer>
  </div>

  <script>
    (function () {
      const COUNT_KEY = 'clubCounter.count';
      const THEME_KEY = 'clubCounter.theme'; // 'dark' | 'light'

      const countEl = document.getElementById('counterHeading');
      const incBtn = document.getElementById('incBtn');
      const resetBtn = document.getElementById('resetBtn');
      const themeBtn = document.getElementById('themeBtn');
      const themeIcon = document.getElementById('themeIcon');
      const themeText = document.getElementById('themeText');

      // ---------- Utilities ----------
      const prefersDark = () =>
        window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

      function getTheme() {
        return localStorage.getItem(THEME_KEY) || (prefersDark() ? 'dark' : 'light');
      }

      function setTheme(theme) {
        const root = document.documentElement;
        if (theme === 'light') {
          root.classList.add('light');
          document.querySelector('meta[name="theme-color"]').setAttribute('content', '#FFFFFF');
          themeBtn.setAttribute('aria-pressed', 'true');
          themeIcon.textContent = '🌞';
          themeText.textContent = 'Light';
        } else {
          root.classList.remove('light');
          document.querySelector('meta[name="theme-color"]').setAttribute('content', '#202123');
          themeBtn.setAttribute('aria-pressed', 'false');
          themeIcon.textContent = '🌙';
          themeText.textContent = 'Dark';
        }
        localStorage.setItem(THEME_KEY, theme);
      }

      function vibrate(ms = 15) {
        if (navigator.vibrate) {
          navigator.vibrate(ms);
        }
      }

      function getCount() {
        const raw = localStorage.getItem(COUNT_KEY);
        const n = Number(raw);
        return Number.isFinite(n) && n >= 0 ? n : 0;
      }

      function setCount(n) {
        n = Math.max(0, Math.floor(n));
        localStorage.setItem(COUNT_KEY, String(n));
        countEl.textContent = n;
      }

      // ---------- Init ----------
      setTheme(getTheme());
      setCount(getCount());

      // ---------- Events ----------
      incBtn.addEventListener('click', () => {
        const n = getCount() + 1;
        setCount(n);
        vibrate(12);
      });

      // Enable space/enter to trigger when focused
      incBtn.addEventListener('keydown', (e) => {
        if (e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          incBtn.click();
        }
      });

      resetBtn.addEventListener('click', () => {
        // Simple confirmation guard without modal
        const old = getCount();
        if (old === 0) return;
        setCount(0);
        vibrate(8);
      });

      themeBtn.addEventListener('click', () => {
        const next = document.documentElement.classList.contains('light') ? 'dark' : 'light';
        setTheme(next);
      });

      // Update theme if system setting changes (optional nicety)
      if (window.matchMedia) {
        try {
          const mq = window.matchMedia('(prefers-color-scheme: dark)');
          mq.addEventListener('change', (e) => {
            if (!localStorage.getItem(THEME_KEY)) {
              setTheme(e.matches ? 'dark' : 'light');
            }
          });
        } catch {}
      }

      // Prevent accidental zoom on double-tap (iOS)
      let lastTouch = 0;
      document.addEventListener('touchend', (e) => {
        const now = Date.now();
        if (now - lastTouch <= 300) e.preventDefault();
        lastTouch = now;
      }, { passive: false });
    })();
  </script>
</body>
</html>
```