# CodeSim
CodeSim is a command-line tool designed to help programming students practice their knowledge through exam-like challenges.
Users answer coding questions, earn points for correct solutions, and progress through levels until achieving a perfect score of 100.

The project is inspired by exam environments such as the 42 exam shell, focusing on learning through practice and repetition.

## Requirements
Before installing CodeSim, make sure you have:
- Python 3.10 or newer
- pip
- Git
You can check your Python version with:
```bash
python --version
```

## Installation
### Clone the repository
```bash
git clone https://github.com/vgomes-p/CodeSim.git
```

### Navigate to the directory 'program'
```bash
cd CodeSim/program
```
### Install required libs
```bash
make requirements
```

### Install the program
```bash
make install
```

After installation, the codesim command will be available globally.

## Running CodeSim
### To start the program, run:
```bash
codesim
```
or
```bash
codesim --start
```
CodeSim will guide you through the available options directly in the terminal.

### call --help to see all the flags
```bash
codesim --help
```
or
```bash
codesim -h
```

## Uninstalling
### On your terminal, run:

```bash
sudo pip uninstall codesim
```

## Project Status
This project is currently in beta and under active development.
Features, structure, and commands may change over time.

## How to contribute 🤝
### If you would like to contribute, you can read the [![Contribution Guide](https://img.shields.io/badge/Contribution%20guide-green?style=for-the-badge)](CONTRIBUTING.md)