# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mannwhitneyu

# Set the theme of plots
sns.set_theme(style= 'darkgrid', palette='Set2')

# Read dataset (you need to provide the related file path where your files saved)
yearly_data = pd.read_csv('./data/yearly_deaths_by_clinic.csv')
print(yearly_data)

# Read dataset (you need to provide the related file path where your files saved)
clinic1 = pd.read_csv('./data/monthly_deaths.csv')
print(clinic1.sample(5))

# Check data types
clinic1.info()

# Check NaNs
print(clinic1.isna().sum())

# Change the data type of date column
clinic1['date'] = pd.to_datetime(clinic1['date'])

# Add a column to show proportion of death
yearly_data['death_per'] = (yearly_data['deaths'] / yearly_data['births'] * 100).round(2)

# Sort the data by death_per to find the highest ratio
highest_year = yearly_data.sort_values('death_per', ascending= False).head(1)['year'].iloc[0]

# Print the answer
print(f'{highest_year} had the highest yearly proportion of deaths.')

# Visualize yearly death proportion for each clinic
# Set the size of the plot
plt.figure(figsize=(8,6))

# Create the plot, change the title and legend
sns.barplot(data= yearly_data, x= 'year', y= 'death_per', hue= 'clinic')
plt.title('Yearly Proportion Of Deaths For Each Clinic', fontsize= 18)
plt.legend(title= 'Clinic')

# Change labels and their settings
plt.xlabel('Year', fontsize= 14)
plt.xticks(fontsize= 12)
plt.ylabel('Yearly Death Proportion')
plt.yticks(fontsize= 12)

# Show the plot
plt.show();

# Add a column to show whether data was recorded before or after hand washing began
handwashing_start = pd.to_datetime('1847-06-01')
clinic1['handwashing_started'] = clinic1['date'] >= handwashing_start

# Add a column to show proportion of death
clinic1['death_proportion'] = (clinic1['deaths'] / clinic1['births'] * 100).round(2)

# Calculate the average death ratio before and after handwashing_start 
monthly_summary = clinic1.groupby('handwashing_started')['death_proportion'].mean().round(2)

# Visualize monthly death proportion for clinic 1
# Set the size of the plot
plt.figure(figsize=(12,10))

# Create the plot, change the title
ax = sns.lineplot(data= clinic1, x= 'date', y= 'death_proportion', linewidth= 2.5)
plt.title('Monthly Proportion Of Deaths For Clinic 1', fontsize= 18)

# Add a vertical reference line at the handwashing start date
ax.axvline(x= handwashing_start, color='orange', linestyle='--')

# Annotate the reference line
ax.annotate(
    'Start of Handwashing', # The text to display
    xy=(handwashing_start, clinic1['death_proportion'].max()), # Point of annotation (x, y)
    xytext=(handwashing_start + pd.Timedelta(days=50), clinic1['death_proportion'].max() + 0.03), # Position of the text
    fontsize=12, color='dimgray'
)

# Change labels and their settings
plt.xlabel('Year', fontsize= 14)
plt.xticks(fontsize= 12)
plt.ylabel('Monthly Death Proportion')
plt.yticks(fontsize= 12)

# Show the plot
plt.show();

## Is the monthly death proportion before handwashing started bigger than after handwashing started? 
# H0 = There is no difference in monthly death proportions between before and after handwashing started.
# H1 = The monthly death proportion before handwashing started is bigger than after handwashing started.

# Filter data as before and after
before = clinic1.loc[clinic1['handwashing_started'] == False, 'death_proportion']
after = clinic1.loc[clinic1['handwashing_started'] == True, 'death_proportion']

# Statistical Testing
# Set alpha, confidence interval is 95%
alpha = 0.05 # Common significance level

# Mann-Whitney U test as an alternative for non-normal distributions with unequal sample sizes
u_stat, p_val_mannwhitney = mannwhitneyu(before, after, alternative='greater')

# Print the result
print(f"Mann-Whitney U test: U-statistic = {u_stat}, p-value = {p_val_mannwhitney}")

if p_val_mannwhitney < alpha:
    print("Reject the null hypothesis: Significant difference, and death proportions were higher before handwashing.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the groups.")
