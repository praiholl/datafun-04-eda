# datafun-04-eda

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://docs.astral.sh/ruff/)
[![Jupyter](https://img.shields.io/badge/Jupyter-notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![marimo](https://img.shields.io/badge/marimo-reactive_notebook-FF6B6B)](https://docs.marimo.io/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: exploratory data analysis

This project conducts an exploratory data analysis of personal finance transactions using Python and Jupyter.

The analysis combines Python code, visualizations, and Markdown narrative to examine data quality, transaction amounts, expense categories, and spending patterns.

## Motivation

When analysts receive a new dataset,
they need to get to know it before deciding what questions it can answer.
We look through the data, check its quality,
examine how values are distributed, compare groups, and
investigate patterns that might be interesting.

This project uses a repeatable process to exploe a new dataset.

The analysis combines Python, visualizations, results, and written observations in a Jupyter notebook.

## This Project

This project applies these EDA techniques to a personal finance expense dataset. The analysis examines data quality, transaction distributions, expense category frequency, total spending by category, and unusually large transactions.

## Produced Artifacts

This project includes a Jupyter notebook that combines Python code, visualizations, and written observations from the exploratory data analysis.

- [**Personal Finance EDA Jupyter Notebook**](./notebooks/eda_holly.ipynb)
  - explores transaction amounts, expense categories, data quality, and spending patterns
- [**Data Card**](./docs/data-card.md)
  - documents the dataset, its source, intended use, and limitations

## Initial Results

The personal finance dataset contains 938 expense transactions across 14 categories. No missing values were found, although 145 duplicate rows were detected.

Most transactions were relatively small. The median transaction amount was 2, and 75% of transactions had an amount of 10 or less.

![Distribution of transaction amounts](docs/images/amount-distribution.png)

Public transport was the most frequent expense category, but it did not account for the greatest total spending. Loan given had the highest total spending, followed by Other.

![Total spending by category](docs/images/total-spending-by-category.png)

![Bar chart of missing values by variable](docs/images/missing-values.png)


## Important Folders and Files

- **docs/** - the project narrative and documentation
- **src/datafun** - Python code used for the exploratory data analysis
- **notebooks/** - Jupyter notebook analysis
- **zensical.toml** - configuration for the project documentation site

## Common Workflow

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
carefully.

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages,
and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have the example project,
running on your machine.
A new file `project.log` will appear in the root project folder
and running the example script will print out:

```shell
===================================
END main() - Executed successfully!
===================================
```

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

Open a machine terminal in your `Repos` folder:

```shell
git clone https://github.com/praiholl/datafun-04-eda

cd datafun-04-eda
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal**
in the root project folder.
Copy each command, paste into your terminal, and hit ENTER,
to run each command one at a time.

```shell
uv self update
uv python pin 3.14

uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made by pre-commit tasks
git add -A
uv run pre-commit run --all-files

# run the Python module
uv run python -m datafun.app

# run marimo nb as a reactive app
# press Ctrl + C in the terminal to exit
uv run marimo run src/datafun/notebook.py

# Or: run marimo nb as a notebook
uv run marimo edit src/datafun/notebook.py

# Also: See notebooks/ for Jupyter notebooks

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress as you work
git add -A
git commit -m "your message here"
# repeat if changes were made (try the UP ARROW)
git add -A
git commit -m "your message here"

git push -u origin main
```

</details>

## Helpful Tips

- Use the **UP ARROW** and **DOWN ARROW** in the terminal
  to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Much Can Be Ignored

- You do not need to add to or modify `tests/`.
  Tests are recommended and provided for example only.
- Many files are silent helpers.
  [Explore](https://denisecase.github.io/professional-python-project-explainer/)
  as you like, but most files are never touched.
- You do NOT need to understand everything;
  let understanding build over time.

## As Needed

If VS Code does not automatically use the new `.venv` environment:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Python: Select Interpreter**.
3. Select the interpreter from this project's `.venv` folder.

If VS Code still does not recognize the environment or newly installed tools:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Developer: Reload Window**.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Documentation

- [Documentation](https://praiholl.github.io/datafun-04-eda/)

## Data Card

- [Personal Finance Expenses Data Card](./docs/data-card.md)

## Annotations

- [.annotations/annotations.md](./.annotations/annotations.md)

## Citation

- [CITATION.cff](./CITATION.cff)

## License

This project is licensed under the [MIT License](./LICENSE).
