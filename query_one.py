import pandas as pd

def generate_pitcher_stats(csv_file):
    # load csv into pandas data frame
    data_frame = pd.read_csv(csv_file)
    
    # Calculate total pitches and average velocity (RelSpeed) for each player.
    
    grouped_data = data_frame.groupby(['Pitcher', 'AutoPitchType']).agg(
        TotalPitches=pd.NamedAgg(column='PitchNo', aggfunc='count'),
        AvgVelo=pd.NamedAgg(column='RelSpeed', aggfunc='mean')
    ).reset_index()
    
    total_pitches_df = data_frame.groupby('Pitcher').size().reset_index(name='TotalPitches')
    
    merged_df = pd.merge(grouped_data, total_pitches_df, on='Pitcher', how='left')
    
    return merged_df



stats = generate_pitcher_stats('./data/data_1.csv')
print(stats)