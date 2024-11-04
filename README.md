## Does Handwashing Save Lives?
### Analyzing The Data Behind One Of The Most Important Discoveries Of Dr. Semmelweis: Handwashing

Hungarian physician Dr. Ignaz Semmelweis worked at the Vienna General Hospital with childbed fever patients. Childbed fever is a deadly disease affecting women who have just given birth, and in the early 1840s, as many as 10% of the women giving birth died from it at the Vienna General Hospital. Dr. Semmelweis discovered that it was the contaminated hands of the doctors delivering the babies, and on **June 1st, 1847**, he decreed that everyone should wash their hands, an unorthodox and controversial request; nobody in Vienna knew about bacteria.

In this project, we will analyze the data that made Semmelweis discover the importance of handwashing and its impact on the hospital and the number of deaths. We will also test our hypothesis which says there is no difference in monthly death rates between before and after handwashing started.

**Dataset:** The data is stored as two CSV files in the `data` folder and their formats are as follows. The dataset used in this project can be downloaded from [here](https://projects.datacamp.com/projects/2526).

`data/yearly_deaths_by_clinic.csv` contains the number of women giving birth at the two clinics at the Vienna General Hospital between the years 1841 and 1846.

| Column | Description |
|--------|-------------|
|`year`  |Years (1841-1846)|
|`births`|Number of births|
|`deaths`|Number of deaths|
|`clinic`|Clinic 1 or clinic 2|

`data/monthly_deaths.csv` contains data from 'Clinic 1' of the hospital where most deaths occurred.

| Column | Description |
|--------|-------------|
|`date`|Date (YYYY-MM-DD)
|`births`|Number of births|
|`deaths`|Number of deaths|

To get started on analyzing in Python, we will need some packages below:
- `pandas`: It is a data analysis and manipulation library that provides data structures and tools.
- `matplotlib.pyplot`: It is a plotting library for creating visualizations in Python.
- `seaborn`: It provides a high-level interface for drawing attractive and informative statistical graphics.
- `scipy.stats`: It contains a large number of probability distributions, summary and frequency statistics, correlation functions and statistical tests, and more.


## Goals
- The goals of this project are to understand the importance of handwashing rule of Dr. Semmelweis and its impact on the hospital and the number of deaths by analyzing the data and to test our hypothesis regarding the impact of handwashing rule.

## Tools and Technologies Used
`python`

`pandas` for data manipulation 

`matplotlib` and `seaborn` for data visualization

`scipy.stats` for statistical testing 

## How to Run
clone:
```sh
git clone https://github.com/handebasaka/discovery-of-handwashing
```
open the solution file:
```bash
cd discovery-of-handwashing
```
run python script:
```bash
python3 discovery-of-handwashing.py
```
