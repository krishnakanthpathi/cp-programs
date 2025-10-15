## Repo summary

This repository is a collection of competitive programming solutions (mostly Python, some Jupyter notebooks, C++ and Java). Files are small, standalone problem solutions intended to be run from the command line and read input from stdin.

## What an AI coding agent should know

- Primary language: Python (most files are single-file solutions). Expect simple scripts that parse stdin using `input()` and `map`/`split`.
- Typical structure: a `main()` or top-level script that reads input and prints results. Many files assume single-run or multiple testcases (first line `t`).
- No unified build system or tests. Run individual files with `python filename.py` or open notebooks with Jupyter.

## Key patterns & examples

- Input parsing: look for `int(input())`, `map(int, input().split())`, `for _ in range(t): main()`.
  - Example: `900/luntiksequencs.py` reads `n = int(input())` then a single-line array.
  - Example: `practice/roomallocation.py` expects `n` followed by `n` interval lines; it uses `heapq` and prints allocation.

- Algorithm style: in-place, procedural, minimal external dependencies (standard library only: `heapq`, `collections`, `defaultdict`, `math`). Avoid adding heavy dependencies.

- Filenames and locations: problems are grouped by folders like `practice/`, `dp/`, `contests/`, `800/`, `900/`. When modifying or adding files, mirror this existing grouping.

## Conventions for edits and new solutions

- Keep solutions single-file and self-contained. If creating helper modules, place them under a new `lib/` or `utils/` folder and update README.
- Preserve the common input/output style (stdin, stdout). Do not convert solutions to web APIs or CLIs unless requested.
- Use minimal imports. Prefer the standard library.

## Debugging & running locally

- Run a single solution with:
  ```bash
  python path/to/file.py
  ```
- Notebook files (`.ipynb`) are present (`kmeans.ipynb`, `naivebayes.ipynb`) and should be opened in Jupyter for interactive work.

## What to avoid

- Do not reorganize whole repo or rename many files. The repository is a flat collection of solved problems—large refactors are out of scope.
- Avoid introducing large framework dependencies or tests that change the project's intent.

## Integration points & external dependencies

- No external services or CI configuration found. Solutions run locally. Keep changes local and minimal.

## Examples to reference in edits

- `practice/arraydiv.py` — binary-search partition template.
- `practice/roomallocation.py` — interval scheduling with `heapq` and index-preserving output.
- `900/luntiksequencs.py` — typical single-testcase or multi-testcase pattern.

If anything in this guidance is unclear or you'd like broader changes (tests, CI, packaging), tell me which areas to expand and I will iterate.
