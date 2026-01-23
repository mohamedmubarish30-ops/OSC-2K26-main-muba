# 🐍 OSC-2K26 PyExpo Event

Welcome to the Open Source Connect 2026 application repository! This project is designed to help you get started with Open Source contributions, Git, GitHub, and practical Python programming.

Follow this step-by-step guide to participate in the event.

---

## 🚀 Participation Guide

### 1️⃣ Fork the Repository
1.  Click the **Fork** button at the top right corner of this repository page.
2.  This creates a copy of this repository in your own GitHub account.

### 2️⃣ Clone the Repository
1.  Go to your forked repository.
2.  Click the **Code** button and copy the URL.
3.  Open your terminal or Git Bash.
4.  Run the following command:
    ```bash
    git clone <your-forked-repo-url>
    ```
5.  Navigate into the project folder:
    ```bash
    cd OSC-2K26
    ```

---

### 3️⃣ Step 1: Registration (First Contribution)
1.  Navigate to the `readme/` folder.
2.  Open the `CONTRIBUTORS.md` file.
3.  Add your **Name** and **Roll Number** to the table.
4.  Save the file.
5.  Commit and push your changes:
    ```bash
    git add readme/CONTRIBUTORS.md
    git commit -m "Added <Your Name> to contributors list"
    git push origin main
    ```

---

### 4️⃣ Step 2: Solve Problems (Debugging)
1.  Navigate to the `problems/` folder.
2.  Choose a problem from `easy`, `medium`, or `advanced` folders.
3.  Read the problem description and run the code to see the error.
4.  Fix the logical or syntax error to produce the expected output.
5.  Verify your solution.
6.  Commit and push your solution:
    ```bash
    git add problems/<difficulty>/<problem_file>.py
    git commit -m "Fixed problem <number>"
    git push origin main
    ```

---

### 5️⃣ Create an Issue
Before submitting your work, it's good practice to create an issue to track your contribution.
1.  Go to the **Issues** tab in the original repository (not your fork).
2.  Click **New Issue**.
3.  Give it a title like "Fixed Problem #XYZ" or "Added details to Contributors".
4.  Describe what you are working on.
5.  Submit the issue and note the Issue Number (e.g., #12).

---

### 6️⃣ Create a Pull Request (PR)
Once you have pushed your changes to your fork, it's time to submit them to the main repository.
1.  Go to your forked repository on GitHub.
2.  You should see a banner saying "This branch is 'N' commits ahead of...". Click **Contribute** > **Open Pull Request**.
3.  If you don't see the banner, go to the **Pull requests** tab and click **New pull request**.
4.  Ensure the "base repository" is the original repo and "head repository" is your fork.
5.  Click **Create pull request**.
6.  In the description, link the issue you created (e.g., "Closes #12").
7.  Click **Create pull request** to submit.

---

## 📂 Repository Structure
- `readme/`: Area for your first contribution (Registration).
- `problems/`: Contains 300+ practical Python problems to solve.
  - `easy/`: Beginners start here.
  - `medium/`: Intermediate practical scenarios.
  - `advanced/`: Complex application logic.

Happy Coding! 💻
