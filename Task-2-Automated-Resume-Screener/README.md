# Task 4 - Automated Resume Screener

## About the Project

This is a beginner-friendly Python project that checks text-based resumes against required skills and education. It reads resume files from a folder and displays a matching score for each resume.

## Features

- Reads resumes saved as `.txt` files
- Checks required skills
- Checks required education
- Calculates a matching score
- Displays shortlisted and non-shortlisted resumes
- Counts the resumes checked

## Technologies Used

- Python
- `os` module
- File handling
- Loops and conditions
- String operations

## Project Structure

```text
Task-4-Automated-Resume-Screener/
├── resume_screener.py
├── README.md
└── resumes/
    ├── resume1.txt
    └── resume2.txt
```

## How to Run

1. Install Python on your computer.
2. Open a terminal in this project folder.
3. Run:

```bash
python resume_screener.py
```

4. Add your resume text files to the `resumes` folder.
5. Enter the required skills separated by commas.
6. Enter the required education.

## Example

```text
Automated Resume Screener
Enter required skills: python, communication
Enter required education: bachelor's

Resume: resume1.txt
Matching score: 3
Status: Shortlisted

Total resumes checked: 1
```

## How Scoring Works

Each matching skill adds one point. If the required education appears in the resume, one additional point is added. A score of 2 or more is marked as shortlisted.

## Learning Objectives

This project helps practice Python file handling, lists, loops, conditions, string methods, and working with folders.
