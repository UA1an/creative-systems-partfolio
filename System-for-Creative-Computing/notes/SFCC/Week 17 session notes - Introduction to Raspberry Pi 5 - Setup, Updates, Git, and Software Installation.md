
Completion requirements

## Session overview

### Aims

- Assemble Raspberry Pi 5 hardware and complete first‑boot configuration.
- Perform updates using `apt` and configure a reusable update alias.
- Configure Git and clone the module repository via HTTPS.
- Install software with `apt`, the GUI, and Flatpak; verify core tools.

### Learning outcomes

- Understand the Raspberry Pi 5 hardware stack (cooling, storage, I/O).
- Apply Linux package management safely and reproducibly.
- Use Git effectively from the terminal using HTTPS authentication.
- Compare installation methods and justify when to use each.

## Hardware: the Raspberry Pi 5 at a glance

### Key components

- **Broadcom SoC** with improved CPU/GPU for media/creative workloads.
- **Active cooling** is recommended; the Pi 5 runs hotter than prior models.
- **Storage options**:
    - **microSD**: inexpensive, simple, sufficient for teaching.
    - **USB 3.0 SSD**: faster and more durable for long‑term projects.

### Creative computing context

- Real‑time audio, live visuals, sensor input, and installation work benefit from sustained performance and reliable I/O.

## Hardware: fitting the fan and case

### Rationale

- Stable thermals reduce throttling, especially during compilation, audio DSP, or rendering tasks.

### Steps

1. **Orient the fan** so airflow pulls warm air away from the CPU/heat sink (check arrows on the fan body).
2. **Mount the fan** to the case lid with the supplied screws—avoid overtightening.
3. **Place the board** into the case, aligning ports and standoffs.
4. **Connect the fan header** to the correct 5 V/GND pins as indicated in your case guide.
5. **Close the case** and verify that cabling is strain‑free.

### Checks

- Fan spins on boot; no cable fouling the fan blades; case not flexing PCB.

## Storage and boot media

### Today

- We'll use **pre‑flashed microSD cards** for consistency and time efficiency.

### Later

- Consider **USB 3.0 SSD** for:
    - Faster read/write throughput (project assets, samples, libraries).
    - Improved durability compared to microSD under heavy write cycles.

### Tip

- Keep a second microSD with a clean image as a recovery/fallback medium.

## OS imaging: overview

- **Raspberry Pi Imager** workflow (conceptual):
    1. Choose _Raspberry Pi OS (64‑bit)_.
    2. Select target (microSD or flash drive).
    3. Use advanced options to pre‑set hostname, user, Wi‑Fi, locale, and optionally enable SSH.
    4. Write, verify, and safely eject.

## First boot: guided configuration

### Sequence

- Connect HDMI, keyboard/mouse, power.
- On first‑boot wizard:
    - **Locale and keyboard**: ensure correct UK settings.
    - **Wi‑Fi**: connect to institutional network where permitted.
    - **User**: confirm the pre‑configured account.

### Post‑wizard

- Let the desktop load fully; wait for any background initialisation before proceeding.

## Eduroam

Taken from [https://myport.port.ac.uk/it-support/student-it-support/connecting-to-campus-wireless-wi-fi-network-student-instructions](https://myport.port.ac.uk/it-support/student-it-support/connecting-to-campus-wireless-wi-fi-network-student-instructions):

- Wi-fi security: **WPA & WPA2 Enterprise**
- Authentication: **Protected EAP (PEAP)**
- CA certificate: **No CA certificate is required** -- tick the box
- PEAP version: **Automatic**
- Inner authentication: **MSCHAPv2**

Use your normal username and password to authenticate.

## Desktop navigation essentials

### Key areas

- **Main menu**: applications and system settings.
- **File manager**: home directory, hidden files (`Ctrl + H`), permissions.
- **Terminal**: open from the menu or `Ctrl + Alt + T`.

### Task: personalise appearance

- GUI path: _Appearance Settings → Desktop_ (change wallpaper and theme).
- Terminal alternative: `bash sudo raspi-config`

Use to explore configuration modules (don't change advanced options yet). You can use `grim` to take screenshots, either from the Terminal or using the 'print screen' key.

## `sudo` and the principle of least privilege

### Concept

- `sudo` executes commands with elevated privileges for administrative tasks.
- **Least privilege**: use `sudo` only when necessary; prefer user‑level operations for safety.

### Security notes

- Read prompts carefully; package operations affect system stability.
- Use audited commands; avoid copy‑pasting from untrusted sources.

## sudo make me a sandwich

![[xkcd 149](https://xkcd.com/149/)](https://imgs.xkcd.com/comics/sandwich.png)

## Package management with `apt`

### Core commands

- Update package index: `bash sudo apt update`
- Upgrade installed packages: `bash sudo apt upgrade -y`
- Perform a full upgrade (handles dependencies, may add/remove): `bash sudo apt full-upgrade -y`

### Why both `upgrade` and `full-upgrade`?

- `upgrade` is conservative; `full-upgrade` resolves dependency changes—use judiciously.

## One‑line chained update and alias

### Chained command

```
sudo apt update && sudo apt upgrade -y && sudo apt full-upgrade -y
```

### Add to `.bash_aliases`

```
nano ~/.bash_aliases
```

Append:

```
alias ,updatepi="sudo apt update && sudo apt upgrade -y && sudo apt full-upgrade -y"
```

Reload:

```
source ~/.bashrc
```

### Outcome

- Reusable, consistent update routine: `bash ,updatepi`

## Software installation pathways

### Three methods

1. **`apt`** (Debian packages, maintained by distro):
    - Pros: integrated, tested, updates flow via `apt`.
    - Cons: versions may lag upstream.
2. **GUI (Add/Remove Software)**:
    - Pros: discoverability, visual confirmation.
    - Cons: same repos as `apt`; slower for bulk tasks.
3. **Flatpak** (sandboxed, Flathub catalogue):
    - Pros: newer app versions, cross‑distro, per‑app sandbox.
    - Cons: larger disk use; theming/integration can vary.

### Guideline

- Prefer `apt` for core system packages; use Flatpak when newer app versions or unavailable packages are needed.

## `apt` in practice

### Search and install

```
apt search <term>
sudo apt install <package-name>
```

### Remove

```
sudo apt remove <package-name>
```

### Clean up

```
sudo apt autoremove -y
sudo apt clean
```

### Example

```
sudo apt install gimp -y
```

## GUI installer: Add/Remove Software

### When to use

- To browse categories and read brief descriptions.
- For users unfamiliar with package names.

### Caveats

- Mirrors and indexing can make search slower than terminal.
- Power users tend to prefer `apt` for speed and scripting.

## Flatpak: what and why

### Definition

- A universal packaging system that bundles dependencies and runs apps in a **sandbox**.

### Use cases

- Obtain newer upstream versions (e.g., editors, creative tools) not in Debian/Raspberry Pi OS repos.
- Install applications with complex dependency trees without polluting system libraries.

### Security note

- Sandboxing reduces risk but does not replace good operational hygiene.

## Flatpak: installation

### Install Flatpak and add Flathub

```
sudo apt install flatpak -y
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

### Log out/in

- Some desktops require a session restart for full integration.

### List remotes and apps

```
flatpak remotes
flatpak list
```

## Flatpak: test with Obsidian

### Search and install

```
flatpak search obsidian
flatpak install flathub md.obsidian.Obsidian
```

### Run

```
flatpak run md.obsidian.Obsidian
```

### Why Flatpak here?

- Rapid access to upstream features; cross‑device parity for notes/workflows.

## Verification checklist

### After installations, confirm:

- `updatepi` alias runs without errors and reports up‑to‑date.
- Obsidian (Flatpak) launches correctly.

### Troubleshooting

- Network issues: retry `sudo apt update`; check DNS.
- Permission errors: avoid `sudo` for Git operations; only use for package management.

## Weekly task: documentation and evidence

### Instructions

1. In your GitHub module repository, create:  
    `creative-tools-test/`
2. Add:
    - `SETUP.md` documenting:
        - `apt` commands used,
        - your `,updatepi` alias,
        - Flatpak setup steps,
        - verification notes (what you launched, what you saw).
    - Screenshots of **Obsidian** running on your Pi.
3. Commit and push: `bash git add . git commit -m "Week 17 Raspberry Pi setup" git push`

### Assessment focus

- Clarity, reproducibility, and correctness of technical steps.

# Optional extensions (if time allows)

## Installing creative tools: Pure Data (Pd)

### Install

```
sudo apt install puredata -y
```

### Verify

- Launch from menu or: `bash puredata`
- Create a new patch; test **DSP** on/off.

---

## Installing creative tools: SuperCollider

### Install

```
sudo apt install supercollider -y
```

### Run server and test

1. Start `sclang`.
2. Evaluate: `supercollider s.waitForBoot { { SinOsc.ar(440) * 0.1 }.play; };`
3. Stop: `supercollider s.freeAll;`

---

## Git: installation and identity

### Git should be installed by default, but if not...

```
sudo apt install git -y
```

### Set global identity

```
git config --global user.name "yourusername"
git config --global user.email "youremail"
```

### Verify

```
git config --global --list
```

Use the username and email that you have used for your GitHub account.

## Git: SSH keys

### Generate an SSH key

```
ssh-keygen -t ed25519 -C "yourGitHubemail"
```

### View your public key

```
cat ~/.ssh/id_ed25519.pub
```

### Add to GitHub

- GitHub → _Settings_ → _SSH and GPG Keys_.

### Test

```
ssh -T git@github.com
```

## Next steps and reading

### For next week

- Image a spare microSD or flash drive yourself using Raspberry Pi Imager.
- Experiment with installing one additional Flatpak app relevant to your practice.
- Optional: explore making a **system image backup** of your SD card with `dd`

## Q&A and wrap‑up

### Key takeaways

- Git via HTTPS simplifies early‑stage workflows.
- Choose the right installation pathway: `apt` for core system packages, Flatpak for newer sandboxed apps.
- Document as you work; future you will be grateful!