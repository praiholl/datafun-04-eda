"""src/datafun/app.py - Project script (example).

Author: Holly Praiswater
Date: 2026-09

RUN:

Open this project folder in VS Code.
Open an integrated Terminal in the root project folder
and paste the following command.

uv run python -m datafun.app

DOMAIN: Personal Finance

Explore a dataset of personal expense transactions using a simple,
repeatable exploratory data analysis (EDA) process.

EDA:

Exploratory Data Analysis helps us understand a new dataset.
A simple EDA process is:

1. LOAD the data.
2. INSPECT the data.
3. CHECK data quality.
4. DESCRIBE numeric variables.
5. VISUALIZE distributions.
6. EXPLORE spending by category.
7. SUMMARIZE what you found.
8. DISPLAY the visualizations.

DESIGN:

Use this file to document your analysis
and orchestrate the work.

The reusable functions that do the data work live in utils_eda.py.
Reusable visualization functions come from eda-vizkit.
We import functions and pass in what they need.

SKILLS:

This project illustrates several core Python and analytics skills:

- calling functions in another file
- passing information to functions
- working with pandas DataFrames
- exploratory data analysis

"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header
from eda_vizkit import (
    save_chart,
    show_categorical_distribution,
    show_missing_values,
    show_numeric_distribution,
)
import matplotlib.pyplot as plt
import pandas as pd

from datafun.utils_eda import (
    build_data_dictionary,
    get_duplicate_count,
    get_missing_counts,
    get_numeric_summary,
    inspect,
    load_csv_data,
)

# === CONFIGURE LOGGER ONCE FOR THE APPLICATION ===

LOG: logging.Logger = get_logger("P04", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

# Some global variables are CONSTANT.
# They do NOT change while the program runs.
# By convention, constants use UPPERCASE_WITH_UNDERSCORES.
# Final indicates that the value should not be reassigned.

CHART_DIR: Final[Path] = Path("docs") / "images"
CHART_DIR.mkdir(parents=True, exist_ok=True)

# === DEFINE THE DATASET ===

DATASET_NAME: Final[str] = "personal finance expenses"
DATA_FILE: Final[Path] = Path("data") / "raw" / "Expenses_clean.csv"

# === DETERMINE WHAT ONE ROW REPRESENTS ===

# This is the GRAIN of the dataset.
# Grain answers:
# What does one row represent?

GRAIN: Final[str] = "one expense transaction"

# === CHOOSE IMPORTANT NUMERIC VARIABLES ===

# These are continuous numeric variables
# we want to inspect during EDA.

NUMERIC_COLUMNS: Final[list[str]] = [
    "amount",
]

# === CHOOSE IMPORTANT CATEGORICAL VARIABLES ===

CATEGORICAL_COLUMNS: Final[list[str]] = [
    "category",
    "account",
    "currency",
    "tags",
]


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """The main entry point where execution begins.

    Arguments:
        None.

    Returns:
        None.
    """
    log_header(LOG, "P04 - EXPLORATORY DATA ANALYSIS")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    LOG.info("-------------------------------")
    LOG.info("01. LOAD the data.")
    LOG.info("-------------------------------")

    df: pd.DataFrame = load_csv_data(
        file_path=str(DATA_FILE),
        log=LOG,
    )

    LOG.info("-------------------------------")
    LOG.info("02. INSPECT the data.")
    LOG.info("-------------------------------")

    inspection_string: str = inspect(
        df=df,
        grain=GRAIN,
        log=LOG,
    )

    LOG.info(inspection_string)

    LOG.info("-------------------------------")
    LOG.info("03. CHECK data quality.")
    LOG.info("-------------------------------")

    # Call the imported function build_data_dictionary()
    # to create a starter data dictionary.
    # Pass in the df and the logger.

    data_dictionary: pd.DataFrame = build_data_dictionary(
        df=df,
        log=LOG,
    )
    LOG.info(f"\n{data_dictionary}")

    # Call the imported function get_missing_counts()
    # to count missing values in each column.
    # Pass in the df and the logger.
    missing_counts: pd.Series = get_missing_counts(
        df=df,
        log=LOG,
    )

    LOG.info(f"\nMissing values:\n{missing_counts}")

    # Call the imported function get_duplicate_count()
    # to count duplicate rows.
    # Pass in the df and the logger.
    duplicate_count: int = get_duplicate_count(
        df=df,
        log=LOG,
    )

    LOG.info(f"Duplicate rows: {duplicate_count}")

    # Call the imported function show_missing_values()
    # to visualize missing values.
    # Pass in the df.
    # get back the Axes object so we can save the chart.
    missing_ax = show_missing_values(df)

    # Save the missing values chart to the designated directory.
    save_chart(
        missing_ax,
        CHART_DIR / "missing-values.png",
    )

    LOG.info("-------------------------------")
    LOG.info("04. DESCRIBE numeric variables.")
    LOG.info("-------------------------------")

    numeric_summary: pd.DataFrame = get_numeric_summary(
        df=df,
        numeric_columns=NUMERIC_COLUMNS,
        log=LOG,
    )

    LOG.info(f"\n{numeric_summary.to_string()}")

    LOG.info("-------------------------------")
    LOG.info("05. VISUALIZE distributions.")
    LOG.info("-------------------------------")

    # For each column in the list of numeric columns,
    # call the imported function show_numeric_distribution()
    # to visualize the distribution of the column.

    for column in NUMERIC_COLUMNS:
        numeric_ax = show_numeric_distribution(
            df,
            column=column,
        )

        # Save the numeric distribution chart to the designated directory.
        save_chart(
            numeric_ax,
            CHART_DIR / f"{column}-distribution.png",
        )

    # For each column in the list of categorical columns,
    # call the imported function show_categorical_distribution()
    # to visualize the distribution of the column.

    for column in CATEGORICAL_COLUMNS:
        categorical_ax = show_categorical_distribution(df, column=column)

        # Save the categorical distribution chart to the designated directory.
        save_chart(
            categorical_ax,
            CHART_DIR / f"{column}-distribution.png",
        )

    LOG.info("-------------------------------")
    LOG.info("06. EXPLORE spending by category.")
    LOG.info("-------------------------------")

    spending_by_category = df.groupby("category")["amount"].sum()

    LOG.info(
        msg=f"\nTotal spending by category:\n{spending_by_category.sort_values(ascending=False)}"
    )

    spending_by_category_sorted = spending_by_category.sort_values(ascending=False)

    plt.figure()

    spending_ax = spending_by_category_sorted.plot(
        kind="bar",
    )

    spending_ax.set_title("Total Spending by Category")
    spending_ax.set_xlabel("Category")
    spending_ax.set_ylabel("Total Amount")

    save_chart(
        spending_ax,
        CHART_DIR / "total-spending-by-category.png",
    )

    LOG.info("-------------------------------")
    LOG.info("07. SUMMARIZE what you found.")
    LOG.info("-------------------------------")

    # Run this app first.
    # Get some insights into data.
    # After seeing the information, record your CUSTOM observations
    # in a simple multi-line (triple-quoted) raw string (see the leading `r`).

    LOG.info(r"""CUSTOM OBSERVATIONS:
    The dataset contains 938 personal expense transactions across 14 categories. There were no missing values, but 145 duplicate rows were detected.

    Most transactions were small, with a median amount of 2 and 75% of transactions at 10 or less. A few larger expenses caused the distribution to be strongly skewed.

    Public transport was the most frequent expense category, but it did not have the highest total spending. Loan given had the highest total spending, followed by Other. This showed that the category with the most transactions is not necessarily where the most money is spent.

    Based on this EDA, I would next like to investigate spending patterns over time and look more closely at the large expense transactions.
    """)

    LOG.info("-------------------------------")
    LOG.info("08. DISPLAY the charts.")
    LOG.info("-------------------------------")

    # eda-vizkit just returns Matplotlib Axes objects.
    # The client (like this script or a marimo notebook),
    # determines how and when to display the plots).

    LOG.info("In a script, call plt.show() at the end to display all charts.")
    LOG.info("Close all chart windows (with the close button) to continue.")

    plt.show()

    LOG.info("===================================")
    LOG.info("END main() - Executed successfully!")
    LOG.info("===================================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If this file is run as a script, call main().
#
# If another file imports this module,
# Python can reuse its definitions without automatically
# running the entire analysis.

if __name__ == "__main__":
    main()
