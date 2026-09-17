# Data Card: Personal Finance Expenses

This Data Card documents the personal finance expense dataset used in this exploratory data analysis project.

It follows the general transparency goals of Google's
Data Cards Playbook:
describe dataset provenance, composition,
intended use, limitations, and considerations
not apparent from the data.

## Dataset Summary

| Item                                | Description                    |
| ----------------------------------- | ------------------------------ |
| Dataset                             | Personal Finance Expenses      |
| Data file                           | `Expenses_clean.csv`           |
| Observations                        | 938 transactions               |
| Categories                          | 14 expense categories          |
| Variables                           | 6 columns                      |
| Grain                               | one expense transaction        |
| Primary use here                    | exploratory data analysis      |

## Purpose

The Personal Finance Expenses dataset contains individual expense transactions organized into different spending categories.

This dataset is used in this project to practice exploratory data analysis and investigate how transaction amounts and frequency differ across expense categories.

The analysis can help identify which categories occur most frequently and which categories account for the greatest total spending.

## Provenance

The dataset used for this project was obtained from Kaggle.

It is published as the "Financial Transactions Dataset (Expenses & Income)" and contains financial transaction data that can be used to explore spending and income patterns

For this project, the `Expenses_clean.csv` file was selected for exploratory data analysis.

## Dataset Composition

The dataset contains 938 observations representing individual expense transactions.

The dataset contains six variables:

- `date_time`
- `category`
- `account`
- `amount`
- `currency`
- `tags`

The transactions are organized into 14 expense categories.

## Missing Data

No missing values were detected in the 938 expense transactions.

The data quality check also identified 145 duplicate rows. These rows were not automatically removed because repeated transactions may represent legitimate expenses rather than data errors.


## Intended Use

The dataset is appropriate for:

- education
- exploratory data analysis
- visualization
- examining spending transactions
- comparing transaction frequency and total spending across categories
- demonstrating reproducible analytical workflows

In this repository, the dataset is used to explore personal expense transactions and identify patterns in transactoin amounts and spending categories.

## Additional Exploration

Other reasonable analytical questions include:

- examining spending patterns over time
- identifying unusually large expense transactions
- comparing average transaction amounts across categories
- examining spending patterns across different accounts
- investigating the 145 duplicate rows more closely

These questions could provide additional insight into spending behavior and the characteristics of the transactions in the dataset.

## Limitations

The dataset represents a limited collection of personal financial transactions and should not be assumed to represent typical spending behavior for a broader population.

The dataset does not provide complete context for why individual transactions were made. Additionally, 145 duplicate rows were identified, and further investigation would be needed to determine whether they represent legitimate repeated transactions or duplicate records.

All transactions in the expense file use the same currency, so comparisons between currencies cannot be made.

## Representation Considerations

The expense categories are not represented equally in the dataset. Some categories contain many more transactions than others.

Because of this, transaction frequency alone does not show which categories account for the greatest amount of spending. Both the number of transactions and the transaction amounts should be considered when interpreting the data.

## Project-Specific Use

This project focuses on comparing transaction frequency and total spending across expense categories.

The purpose is to determine whether the categories with the most frequent transactions are also the categories that account for the greatest total spending.

## Project Data Processing

The project:

1. loads the `Expenses_clean.csv` dataset
2. observes the available columns and data types
3. checks for missing values and duplicate rows
4. summarizes the `amount` variable
5. visualizes numeric and categorical distributions
6. groups transactions by `category` and calculates total spending
7. records observations and saves the generated charts

## References

- [Data Cards Playbook (toolkit)](https://pair-code.github.io/datacardsplaybook/)
- Data Cards convention: Pushkarna, Zaldivar, and Kjartansson (2022),
  _Data Cards:_
  _Purposeful and Transparent Dataset Documentation for Responsible AI_,
  ACM FAccT. <https://doi.org/10.1145/3531146.3533231>
- [Financial Transactions Dataset (Expenses & Income) - Kaggle](https://www.kaggle.com/datasets/artemkabseu/financial-transactions-dataset-expenses-and-income)

---

[◄ Back to Home](index.md)
