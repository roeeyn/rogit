# Rogit
This is a little automation for lazy devs like me.<br>
This will do `git add -A && git commit -m "YourMeaningfulCommitMessage" && git push origin YourCurrentBranch`.
You will be prompted for the commit message and for the branch name (the default is your current branch).

## Installation
```bash
pip3 install rogit
```

## Usage
Inside your terminal, at the folder of your code, type
```bash
rogit
```
And it will prompt for the necessary info (mainly the commit message). Or you can use the -m flag

```bash
rogit -m "Your meaningful commit message"
```

Made with 💙 from 🇲🇽
