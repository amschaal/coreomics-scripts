import pandas as pd
import matplotlib.pyplot as plt
import math
# Load the TSV file obtained from exporting the submission
file_path = 'submissions.tsv'
df = pd.read_csv(file_path, delimiter="\t")

# Convert Submitted column to datetime
df['Submitted'] = pd.to_datetime(df['Submitted'], errors='coerce').dt.to_period('M')
sample_count = df.sort_values(['Type','Submitted']).groupby(['Type', 'Submitted'], sort=False)[['samples','libraries']].sum()

# Get combined samples and library numbers for each type
sample_count['all'] = sample_count['samples'] + sample_count['libraries']
sample_count.to_csv('samplecount.csv')


# Group the data by type
grouped_df = sample_count.reset_index().groupby('Type')

# Calculate the number of rows and columns for the subplots
num_groups = len(grouped_df)
num_cols = 3
num_rows = math.ceil(num_groups / num_cols)

# Create a figure and subplots
fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 5 * num_rows))

# Iterate over each group and create a bar chart in a subplot
i = 0
for name, group in grouped_df:
  row = i // num_cols
  col = i % num_cols
  axs[row, col].bar(group['Submitted'].dt.strftime('%Y-%m'), group['all'])
  axs[row, col].set_xlabel('Submitted')
  axs[row, col].set_ylabel('All samples and libraries')
  axs[row, col].set_title(f'Type: {name}')
  axs[row, col].tick_params(axis='x', labelrotation=45)
  i += 1

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


# # # Plot sample count for each submission type as individual plot
# for t in sample_count.index.get_level_values('Type').unique():
# #     # Get a temporary dataframe for all monthly values aggregated for this type
#     temp_df = sample_count.loc[[t]].reset_index(level=0, drop=True)
# #     # Resasmple submitted index per month, filling in values of 0 where empty
#     temp_df = temp_df.resample('M').asfreq(fill_value=0).reset_index()
#     fig, ax = plt.subplots()
#     ax.bar(temp_df['Submitted'].dt.strftime('%Y-%m'), temp_df['all'])
#     ax.set_ylabel('All samples and libraries')
#     ax.set_title(t)
#     ax.legend(title=t)
#     plt.show()