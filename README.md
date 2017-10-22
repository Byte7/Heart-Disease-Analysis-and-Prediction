# Heart-Disease-Analysis-and-Prediction

See project site at [byte7.github.io](http://byte7.github.io/projects/heart_disease_analysis/index.html) for a description of the results.

Jupyter notebooks and files used to generate the results and plots for the project :-

1. **convert\_ssv\_to\_csv.py**: Converts a file with space-separated values into a file with comma-separated values.

1. **join\_files.py**: Joins files downloaded from the UC Irvine Machine Learning Repository into a single file for processing by the iPython notebook below.

1. **Heart\_Disease\_Analysis\_Complete.ipynb**: Jupyter notebook to read in the data, store it in a Pandas dataframe for initial processing and plots, and analyze with a logistic regression model.

The initial processing steps of this project are as follows:

`curl -o data/cleveland14.csv https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data`

`curl -o data/hungarian14r.ssv https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/reprocessed.hungarian.data`

`curl -o data/switzerland14.csv https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.switzerland.data`

`curl -o data/long_beach_va14.csv https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.va.data`

`python convert_ssv_to_csv.py hungarian14r`

`python join_files.py`

The output of join\_files.py is file data/heart\_disease\_all14.csv and is ready for processing by Heart\_Disease\_Analysis\_Complete.ipynb.
