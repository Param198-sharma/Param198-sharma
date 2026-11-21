# 🛠️ Developer Profile Dashboard Setup & Workflow Guide

This repository (`Param198-sharma/Param198-sharma`) serves as the official **GitHub Profile Overview Dashboard** for **Pritam Sharma** (`Param198-sharma`).

---

## 🚀 Key Highlights & Architecture

1. **Zero External Dependence Failure**:
   - Primary analytics, the animated hero banner, featured repositories, language breakdown, and the contribution heatmap are generated as **standalone SVG assets** directly in `assets/generated/`.
   - Dynamic real-time badges (GitHub Readme Stats, Streak Stats, GitHub Trophies) are coupled alongside self-rendered SVG cards for the ultimate resilient dashboard.
2. **Automated Continuous Telemetry**:
   - `.github/workflows/update-profile.yml` runs daily at `00:00 UTC` and on manual trigger via `workflow_dispatch`.
   - It fetches public repositories, authentic language byte totals, stars, and followers, updating SVGs seamlessly without requiring personal access tokens.
3. **Pure GitHub README Compatible**:
   - 100% compliant with GitHub flavored Markdown and sanitized HTML rendering. No broken scripts, no external hosting fees, no Next.js/React servers.

---

## 📦 File Structure

```
Param198-sharma/
├── .github/
│   └── workflows/
│       └── update-profile.yml      # GitHub Actions daily automated updater
├── assets/
│   └── generated/
│       ├── hero-banner.svg         # Animated glowing HUD banner
│       ├── stats-card.svg          # Real-time repository metrics & counters
│       ├── languages.svg           # Donut chart & progress bar distribution
│       ├── activity-graph.svg      # 12-month contribution cadence graph
│       ├── repository-cards.svg    # Production architecture showcases
│       └── section-divider.svg     # Futuristic glowing separator
├── scripts/
│   └── generate_dashboard.py       # Python script generating authentic SVG assets
├── README.md                       # The master profile dashboard
└── SETUP_GUIDE.md                  # This setup documentation
```

---

## ⚡ How to Deploy / Push to GitHub

To publish this dashboard to your GitHub profile, run these commands from your local repository:

```bash
# 1. Stage all changes
git add .

# 2. Commit the new dashboard
git commit -m "feat: launch elite developer dashboard README and telemetry actions"

# 3. Push to GitHub
git push origin main
```

Once pushed, visit: **`https://github.com/Param198-sharma`** — your Profile Overview tab will immediately render your new elite developer dashboard!

---

## 🔄 How the Auto-Updater Works

- **Scheduled Execution**: GitHub Actions triggers `.github/workflows/update-profile.yml` every 24 hours.
- **Manual Trigger**:
  1. Go to your repository on GitHub: `https://github.com/Param198-sharma/Param198-sharma/actions`
  2. Click on **Update Developer Profile Dashboard**.
  3. Click **Run workflow** -> Select `main` branch -> Click green **Run workflow** button.
  4. The workflow will update `assets/generated/*.svg` with the latest stars, repositories, and language stats.
