## 1. Always Start by Syncing (Fetch & Pull)

Before you write a single line of code, make sure you have your team's latest updates.

- Open GitHub Desktop and ensure your "Current branch" is set to `main`.
- Click **Fetch origin** at the top right.
- If it changes to **Pull origin**, click it again to download your teammates' latest merged work.

## 2. Never Work on `Main` (Create a Branch)

To keep the `main` project safe, you must do your work in an isolated space called a branch.

- Click the **Current Branch** dropdown at the top.
- Click **New Branch**.
- Name it something specific to your task (e.g., `feature-midi-parser` or `add-audio-assets`).
- Click **Create Branch**. You are now safe to start working on your files!

## 3. Save Your Progress (Commit)

As you edit and save files in your code editor, GitHub Desktop will detect the changes. Group these changes into "Commits" (which act like save checkpoints).

- In the bottom-left corner of GitHub Desktop, type a short, clear summary (e.g., "Added basic MIDI mapping").
- (Optional) Add a longer description if the changes are complex.
- Click the blue **Commit to [branch-name]** button. Do this often!

## 4. Send Your Work to the Cloud (Push)

Committing only saves the work to your local computer. To share it with your team, you need to push it online.

- Click **Publish branch** (if it's your first time pushing this branch) or **Push origin** at the top right.

## 5. Propose Your Changes (Open a Pull Request)

Once your feature is complete, you need to ask to merge it into the `main` branch. This creates the evidence required for your individual mark.

- After pushing, GitHub Desktop will show a **Create Pull Request** button. Click it.
- This will open GitHub in your web browser.
- Review the changes, add a description of what you accomplished, and click the green **Create pull request** button to open a Pull Request into the `main` branch.

## 6. Review and Merge (Team Effort)

Do not merge your own Pull Request!

- Ask one of your _SfCC_ / _Designing Tomorrow_ teammates to look at your PR.
- They should review your code, ensuring it works and doesn't break the system.
- Once approved, your teammate clicks **Merge pull request** in the browser.