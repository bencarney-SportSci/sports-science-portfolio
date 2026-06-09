import pandas as pd 
import numpy as np 

# 1 Load the static athlete roster from Excel 
roster = pd.read_excel("Football_Master_Roster.xlsx") 

# 2 Initialize the master list to capture all the data 
all_camp_data = []

# 3 Simulate the 4-Day Training Camp Microcycle 
for day in [1, 2, 3, 4]: 

    #Loop through every individual athlete on the roster 
    for index, player in roster.iterrows(): 

        #Pull baseline attributes from the roster DataFrame 
        p_id = player['player_ID'] 
        last_name = player['last_name'] 
        pos = player['position'] 
        group = player['position_group'] 
        base_weight = player['baseline_bodyweight_lbs'] 
        max_vel = player['max_velocity_mph'] 

        # --- SPORTS SCIENCE SIMULATION LOGIC --- 
        # Category A: Lineman Group 
        if group == 'Lineman': 
            player_load = np.random.uniform(450, 550) 
            top_speed = np.random.uniform(12, 15) 
            h_srd = np.random.uniform(0, 20) 
            pct_weight_loss = np.random.uniform(1.5, 2.5) 

        # Category B: Skill Group 
        elif group == 'Skill': 
            player_load = np.random.uniform(350, 450) 
            speed_percentage = np.random.uniform(0.85, 0.95) 
            top_speed = max_vel * speed_percentage 
            h_srd = np.random.uniform(300, 500) 
            pct_weight_loss = np.random.uniform(0.5, 1.5) 

        # Category C: Hybrid Group 
        else: 
            player_load = np.random.uniform(400, 500) 
            speed_percentage = np.random.uniform(0.85, 0.95) 
            top_speed = max_vel * speed_percentage 
            h_srd = np.random.uniform(100, 250) 
            pct_weight_loss = np.random.uniform(1.0, 2.0) 

        # Calculate actual post-practice body weight 
        post_weight = base_weight * (1 - (pct_weight_loss / 100)) 

        # Pack all data for every player into packet
        player_daily_packet = { 
            'day': day,
            'player_ID': p_id,
            'last_name': last_name,
            'position': pos,
            'position_group': group,
            'baseline_weight_lbs': base_weight,
            'max_velocity_mph': max_vel,
            'player_load': player_load,
            'top_speed_mph': top_speed,
            'high_speed_running_yards': h_srd,
            'fluid_loss_percentage': pct_weight_loss,
            'post_practice_weight_lbs': post_weight
        }

        # Save the data packet to the master list
        all_camp_data.append(player_daily_packet) 

# 4 Export to Excel
final_table = pd.DataFrame(all_camp_data)
final_table.to_excel("Camp_Performance_Dasboard_Dataset.xlsx", index=False) 