import pandas as pd
import matplotlib.pyplot as plt
# Load the TSV file obtained from exporting the submission
file_path = 'submissions.tsv'
df = pd.read_csv(file_path, delimiter="\t")

# Convert Submitted column to datetime
df['Submitted'] = pd.to_datetime(df['Submitted'], errors='coerce').dt.to_period('M')
sample_count = df.sort_values(['Type','Submitted']).groupby(['Type', 'Submitted'], sort=False)[['samples','libraries']].sum()

# Get combined samples and library numbers for each type
sample_count['all'] = sample_count['samples'] + sample_count['libraries']
sample_count.to_csv('samplecount.csv')

# # Plot sample count for each submission type as individual plot
for t in sample_count.index.get_level_values('Type').unique():
#     # Get a temporary dataframe for all monthly values aggregated for this type
    temp_df = sample_count.loc[[t]].reset_index(level=0, drop=True)
#     # Resasmple submitted index per month, filling in values of 0 where empty
    temp_df = temp_df.resample('M').asfreq(fill_value=0).reset_index()
    fig, ax = plt.subplots()
    ax.bar(temp_df['Submitted'].dt.strftime('%Y-%m'), temp_df['all'])
    ax.set_ylabel('All samples and libraries')
    ax.set_title(t)
    ax.legend(title=t)
    plt.show()