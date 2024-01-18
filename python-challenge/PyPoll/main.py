import pandas as pd

file_path = "resources/election_data.csv"
df = pd.read_csv(file_path)

total_votes = len(df)

candidate_data = df['Candidate'].value_counts().reset_index()
candidate_data.columns = ['Candidate','Votes']
candidate_data['Percentage'] = (candidate_data['Votes']/total_votes) * 100

winner = candidate_data.loc[candidate_data['Votes'].idxmax()]['Candidate']

print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")
for index, row in candidate_data.iterrows():
    print(f"{row['Candidate']}:{row['Percentage']:.3f}%({row['Votes']})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")