# FIFA 21 Player Data Analysis

This repository contains a Python script for analyzing data from the FIFA 21 video game. The script performs data cleaning, transformation, and visualization to explore relationships between player attributes such as weight, height, value, and wage.

## Dataset

The dataset used in this script is `fifa21.csv`, which includes various details about football players featured in FIFA 21. Note that the dataset is not included in this repository due to licensing restrictions.

## Features

The script includes the following features:
- **Data Cleaning:** Converts weight from pounds to kilograms and height from feet and inches to centimeters.
- **Data Transformation:** Converts string data types to appropriate numeric and datetime types.
- **Visualization:** Creates a scatter plot to analyze the relationship between a player's market value and their wage.
- **Filtering:** Identifies players who have been with their club for more than ten years.

## Prerequisites

Before running this script, ensure you have the following:
- Python 3.6 or higher
- pandas library
- matplotlib library

You can install the required libraries using pip:

```bash
pip install pandas matplotlib
