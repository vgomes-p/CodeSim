# 🤝 Contribution Guide
## Contributing to CodeSim

Thank you for your interest in contributing to CodeSim!
This project is open to improvements, ideas, and experimentation, especially from students and developers who enjoy CLI tools and educational software.

## How You Can Contribute
You can contribute in several ways:
- Improving or refactoring existing code
- Adding new features or exercises
- Fixing bugs
- Improving documentation
- Suggesting ideas or enhancements

## Getting Started
1. Fork the repository on GitHub
2. Clone your fork locally running `git clone https://github.com/your-username/CodeSim.git` then `cd CodeSim/program`
3. Create a new branch for your changes: `git checkout -b feature/my-feature-name`

## Become a known contributor
Add your profile on contributors list with the following structure:
```md
***
## YOUR NAME
[![github](https://img.shields.io/badge/github-blue?style=for-the-badge)](https://github.com/username) <!-- you can change the color by changing the color name after 'USERNAME-' -->
### Top 3 Skills
- List your top skills
### Work with
- List what you prefer to work with (structure, data, error treating, QA)
### Features
- List all features you created, co-developed or fix and add a tag on it (e.g: [created] Login system)
<!-- If you improved a feature, your are a co-developer from it -->

```
[![Add your profile](https://img.shields.io/badge/add_my_contributor_profile-purple?style=for-the-badge)](contributors.md)

## Development Guidelines

- Follow Python best practices (readability matters)
- Feel free to update functions
	- without changing the final purpose
	- without pushing it broken
- Keep functions as small and well-defined as you can
- Keep fuctions in English
	- You may contact a contributor how have translation as a top skill to translate it for you.
- Keep fuctions with descriptions
	- e.g: `def function(text: str, length: int) -> tuple(bool, str):`
- Avoid unnecessary dependencies
- Write clear commit messages
- Test your changes before submitting
- Update the [program files map](program_files_roadmap.txt)
- If your contribution introduces a new feature, try to explain why it exists and how it should be used.
- If you need help on a features, you may contact one contributor from [contributors list](contributors.md) for development co.lab

#### Here is the actual program files roadmap (also in [program_files_roadmap.txt](program_files_roadmap.txt))
```txt
CodeSim/ /*github repository*/
├── program/
│	├── codesim/
│	│	├── eval/
│	│	│	├── __init__.py
│	│	│	└── eval.py
│	│	├── main/
│	│	│	├── __init__.py
│	│	│	├── main.py
│	│	│	└── simshell.py
│	│	├── utils/
│	│	│	├── __init__.py
│	│	│	├── colors.py
│	│	│	├── countdown.py
│	│	│	├── database.py
│	│	│	└── utils_fun.py
│	│	├── assignments/ /*not created*/
│	│	│	└── python_coding_subjects/
│	│	│		├── lv0
│	│	│		├── lv1
│	│	│		└── lv2...
│	│	└── __init__.py
│	├── README.md (for long discription)
│	└── setup.py
├── .gitignore
├── CONTRIBUTING.md
├── CONTRIBUTORS.md
├── LICENSE
├── program_files_roadmap.txt
└── README.md
```

## Submitting Changes
1. Push your branch to your fork: `git push origin feature/my-feature-name`
2. Open a Pull Request on the main repository
3. Clearly describe:
	- What you changed
	- Why you changed it
	- Any known limitations

## Code of Conduct
Be respectful and constructive. This project aims to be a learning space for everyone.

