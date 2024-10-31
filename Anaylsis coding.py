# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the CSV file
csv_file_path = 'global-energy-substitution.csv'
energy_data = pd.read_csv(csv_file_path)

# Set visualization style for clarity
sns.set_style("whitegrid")

# Statistical Analysis
# Summary statistics
summary_statistics = energy_data.describe(include='all')

# Correlation (only for numeric columns)
numeric_data = energy_data.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_data.corr()

# Skewness and Kurtosis for numeric features
skewness = numeric_data.skew()
kurtosis = numeric_data.kurtosis()

def plot_energy_trends(data):
    """
    Plot the trend of energy substitution over time for key energy sources.
    
    This function visualizes how the usage of different energy sources (Coal, Oil, Gas, Solar, Wind, Hydropower) has changed 
    from the year 1950 to 2020, with an interval of 10 years. It provides insights into which energy sources have seen growth or decline over time.
    """
    plt.figure(figsize=(14, 8))
    energy_sources = ['Coal (TWh, substituted energy)', 'Oil (TWh, substituted energy)', 'Gas (TWh, substituted energy)',
                      'Solar (TWh, substituted energy)', 'Wind (TWh, substituted energy)', 'Hydropower (TWh, substituted energy)']
    filtered_data = data[(data['Year'] >= 1950) & (data['Year'] <= 2020)]
    for source in energy_sources:
        plt.plot(filtered_data['Year'], filtered_data[source], label=source, linewidth=2)

    plt.title('Global Energy Substitution Trends (1950-2020)', fontsize=18, fontweight='bold')
    plt.xlabel('Year', fontsize=14, fontweight='bold')
    plt.ylabel('Energy Substituted (TWh)', fontsize=14, fontweight='bold')
    plt.legend(title='Energy Sources', fontsize=12, title_fontsize=14)
    plt.xticks(ticks=range(1950, 2021, 10), rotation=45, fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12, fontweight='bold')
    plt.grid(True, linestyle='--', linewidth=0.7)
    plt.tight_layout()
    plt.show()

def plot_energy_2020(data):
    """
    Plot the energy substitution by source in the year 2020.
    
    This function creates a bar plot to compare the energy substitution from different sources in the year 2020. 
    It provides a snapshot of how much energy was generated from each source in that particular year.
    """
    energy_sources = ['Coal (TWh, substituted energy)', 'Oil (TWh, substituted energy)', 'Gas (TWh, substituted energy)',
                      'Solar (TWh, substituted energy)', 'Wind (TWh, substituted energy)', 'Hydropower (TWh, substituted energy)']
    energy_2020 = data[data['Year'] == 2020].iloc[0]
    energy_2020_sources = energy_2020[energy_sources]

    plt.figure(figsize=(12, 6))
    sns.barplot(x=energy_2020_sources.index, y=energy_2020_sources.values, palette='viridis')
    plt.title('Energy Substitution by Source in 2020', fontsize=18, fontweight='bold')
    plt.xlabel('Energy Source', fontsize=14, fontweight='bold')
    plt.ylabel('Energy Substituted (TWh)', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12, fontweight='bold')
    for i, value in enumerate(energy_2020_sources.values):
        plt.text(i, value + 50, f'{int(value)} TWh', ha='center', va='bottom', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()

def plot_energy_correlation_heatmap(data):
    """
    Plot the correlation heatmap of energy sources.
    
    This function generates a heatmap to visualize the correlations between different energy sources. 
    It helps identify which energy sources have a strong positive or negative correlation, indicating relationships between their usages.
    """
    plt.figure(figsize=(10, 8))
    energy_sources = ['Coal (TWh, substituted energy)', 'Oil (TWh, substituted energy)', 'Gas (TWh, substituted energy)',
                      'Solar (TWh, substituted energy)', 'Wind (TWh, substituted energy)', 'Hydropower (TWh, substituted energy)']
    energy_corr = data[energy_sources].corr()
    sns.heatmap(energy_corr, annot=True, cmap='viridis', linewidths=0.5, fmt='.2f', annot_kws={'size': 12, 'weight': 'bold'})
    plt.title('Correlation Heatmap of Energy Sources', fontsize=18, fontweight='bold')
    plt.xticks(fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()

def plot_biomass_vs_renewables(data):
    """
    Plot traditional biomass vs renewable energy substitution over time.
    
    This function compares the use of traditional biomass with the total renewable energy substitution (Solar, Wind, Hydropower, Biofuels) 
    from 1800 to 2023. It shows how renewable energy sources have grown in comparison to traditional biomass over the years.
    """
    plt.figure(figsize=(14, 8))
    plt.plot(data['Year'], data['Traditional biomass (TWh, substituted energy)'], label='Traditional Biomass', color='brown', linewidth=2)
    plt.plot(data['Year'], data['Solar (TWh, substituted energy)'] + data['Wind (TWh, substituted energy)'] +
             data['Hydropower (TWh, substituted energy)'] + data['Biofuels (TWh, substituted energy)'],
             label='Total Renewables', color='green', linewidth=2)
    plt.title('Traditional Biomass vs Renewable Energy Substitution (1800-2023)', fontsize=18, fontweight='bold')
    plt.xlabel('Year', fontsize=14, fontweight='bold')
    plt.ylabel('Energy Substituted (TWh)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=12)
    plt.xticks(rotation=45, fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12, fontweight='bold')
    plt.grid(True, linestyle='--', linewidth=0.7)
    plt.tight_layout()
    plt.show()

# Plotting using the defined functions
plot_energy_trends(energy_data)
plot_energy_2020(energy_data)
plot_energy_correlation_heatmap(energy_data)
plot_biomass_vs_renewables(energy_data)

# Print Summary Statistics, Correlation, Skewness, and Kurtosis
print("Summary Statistics:\n", summary_statistics)
print("\nCorrelation Matrix:\n", correlation_matrix)
print("\nSkewness:\n", skewness)
print("\nKurtosis:\n", kurtosis)