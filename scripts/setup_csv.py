
import csv
import os 

filename = "data/player_transfers.csv"

if not os.path.exists(filename):
  with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerow([
       # --- Core Transfer Info ---
    "player_name", "age_at_transfer", "position", "preferred_foot", "nationality",
    "from_team", "to_team", "from_league", "to_league", "from_league_rank", "to_league_rank",
    "transfer_fee", "injury_history_games_missed",
    
    # --- Team Context ---
    "from_team_playstyle", "to_team_playstyle", 
    "from_team_avg_possession", "to_team_avg_possession",
    "manager", "manager_playstyle",
    
    # --- Universal Metrics ---
    "minutes_before", "minutes_after",
    "yellow_cards_before", "red_cards_before", 
    "yellow_cards_after", "red_cards_after",
    
    # --- Attacker/Winger Metrics (FW, LW, RW, ST) ---
    "goals_before", "goals_after", "assists_before", "assists_after",
    "shots_per90_before", "shots_per90_after", "xG_before", "xG_after",
    "xA_before", "xA_after", "dribbles_completed_before", "dribbles_completed_after",
    "shot_conversion_before", "shot_conversion_after",
    
    # --- Midfielder Metrics (CM, CAM, CDM) ---
    "key_passes_before", "key_passes_after",
    "through_balls_before", "through_balls_after",
    "progressive_passes_before", "progressive_passes_after",
    "ball_recoveries_before", "ball_recoveries_after",
    
    # --- Defender Metrics (CB, LB, RB, DM) ---
    "tackles_before", "tackles_after", "interceptions_before", "interceptions_after",
    "clearances_before", "clearances_after", "blocks_before", "blocks_after",
    "aerials_won_before", "aerials_won_after", "defensive_duels_won_before", "defensive_duels_won_after",
    "pressures_per90_before", "pressures_per90_after",
    
    # --- Goalkeeper Metrics (GK) ---
    "saves_before", "saves_after", "goals_conceded_before", "goals_conceded_after",
    "clean_sheets_before", "clean_sheets_after", "penalty_saves_before", "penalty_saves_after",
    "crosses_stopped_before", "crosses_stopped_after", 
    "pass_accuracy_long_before", "pass_accuracy_long_after",
    
    # --- Position-Aware Success Metrics (Target Variables) ---
    "attacking_success_score",  # For attackers: (goals+assists per90 change)
    "defensive_success_score",  # For defenders: (tackles+interceptions per90 change)
    "gk_success_score",        # For GKs: (saves% - goals conceded per90 change)
    "overall_success_rating"   # 1-5 scale (human-adjusted)
    ])
    print(f"✅ Created CSV with headers at {filename}")
else:
    print(f"📁 CSV already exists at {filename}")