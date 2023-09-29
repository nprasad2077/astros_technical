import pandas as pd

def generate_pitcher_stats(csv_file):
    # load csv into pandas data frame
    data_frame = pd.read_csv(csv_file)
    
    # Calculate total pitches by type (AutoPitchtType) and average velocity (RelSpeed) for each type of pitch per player.
    
    grouped_data = data_frame.groupby(['Pitcher', 'AutoPitchType']).agg(
        PitchTypeCount=pd.NamedAgg(column='PitchNo', aggfunc='count'),
        AvgVelo=pd.NamedAgg(column='RelSpeed', aggfunc='mean')
    ).reset_index()
    
    # Calculate total number of overall pitches across all types for each player.  
    
    total_pitches_df = data_frame.groupby('Pitcher').size().reset_index(name='TotalPitches')
    merged_df = pd.merge(grouped_data, total_pitches_df, on='Pitcher', how='left')
    
    # Reorder columns and sort dataframe by pitcher name
    
    result_df = merged_df[['Pitcher', 'TotalPitches', 'AutoPitchType', 'PitchTypeCount', 'AvgVelo']]
    result_df = result_df.sort_values(by=['Pitcher', 'TotalPitches'], ascending=[True, False])
    
    return result_df
    





pitcher_stats = generate_pitcher_stats('./data/data_1.csv')
print(pitcher_stats)

pitcher_stats.to_csv('./data/query_one.csv', index=False)