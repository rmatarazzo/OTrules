import tkinter as tk
from tkinter import messagebox

# Mock Database (Example Data)
RULES_DATABASE = {
    'football': {
        'college': {
            'fbs': {
                'preseason': 'FBS college football preseason OT rules: Each team gets one possession...',
                'regular_season': 'FBS college football regular season OT rules: Each team gets one possession...',
                'playoffs': 'FBS college football playoff OT rules: Each team gets one possession...'
            },
            'fcs': {
                'preseason': 'FCS college football preseason OT rules: Each team gets one possession...',
                'regular_season': 'FCS college football regular season OT rules: Each team gets one possession...',
                'playoffs': 'FCS college football playoff OT rules: Each team gets one possession...'
            }
        },
        'professional': {
            'nfl': {
                'preseason': 'NFL preseason OT rules: First team to score wins...',
                'regular_season': 'NFL regular season OT rules: Each team gets one possession unless first team scores a touchdown...',
                'playoffs': 'NFL playoff OT rules: Each team gets one possession unless first team scores a touchdown...'
            }
        }
    },
    'basketball': {
        'college': {
            'ncaa': {
                'preseason': 'NCAA college basketball preseason OT rules: 5-minute overtime period...',
                'regular_season': 'NCAA college basketball regular season OT rules: 5-minute overtime period...',
                'playoffs': 'NCAA college basketball playoff OT rules: 5-minute overtime period...'
            }
        },
        'professional': {
            'nba': {
                'preseason': 'NBA preseason OT rules: 5-minute overtime period...',
                'regular_season': 'NBA regular season OT rules: 5-minute overtime period...',
                'playoffs': 'NBA playoff OT rules: 5-minute overtime period...'
            },
            'wnba': {
                'preseason': 'WNBA preseason OT rules: 5-minute overtime period...',
                'regular_season': 'WNBA regular season OT rules: 5-minute overtime period...',
                'playoffs': 'WNBA playoff OT rules: 5-minute overtime period...'
            }
        }
    },
    'hockey': {
        'college': {
            'ncaa': {
                'preseason': 'NCAA college hockey preseason OT rules: 5-minute sudden death...',
                'regular_season': 'NCAA college hockey regular season OT rules: 5-minute sudden death...',
                'playoffs': 'NCAA college hockey playoff OT rules: 20-minute sudden death periods...'
            }
        },
        'professional': {
            'nhl': {
                'preseason': 'NHL preseason OT rules: 5-minute sudden death...',
                'regular_season': 'NHL regular season OT rules: 5-minute sudden death...',
                'playoffs': 'NHL playoff OT rules: 20-minute sudden death periods...'
            },
            'pwhl': {
                'preseason': 'PWHL preseason OT rules: 5-minute sudden death...',
                'regular_season': 'PWHL regular season OT rules: 5-minute sudden death...',
                'playoffs': 'PWHL playoff OT rules: 20-minute sudden death periods...'
            }
        }
    },
    'baseball': {
        'college': {
            'ncaa': {
                'preseason': 'NCAA college baseball preseason OT rules: Extra innings...',
                'regular_season': 'NCAA college baseball regular season OT rules: Extra innings...',
                'playoffs': 'NCAA college baseball playoff OT rules: Extra innings...'
            }
        },
        'professional': {
            'mlb': {
                'preseason': 'MLB preseason OT rules: Extra innings...',
                'regular_season': 'MLB regular season OT rules: Extra innings...',
                'playoffs': 'MLB playoff OT rules: Extra innings...'
            }
        }
    }
}

def get_user_input():
    """
    Collect user preferences for the sport, level, and league.
    """
    sport = sport_var.get().lower()
    level = level_var.get().lower()
    league = league_var.get().lower()
    game_type = game_type_var.get().lower()
    
    if not all([sport, level, league, game_type]):
        messagebox.showerror("Input Error", "Please select all fields.")
        return None
    
    return sport, level, league, game_type

def query_overtime_rules(sport, level, league, game_type):
    """
    Retrieve overtime rules from the database based on user input.
    """
    return RULES_DATABASE.get(sport, {}).get(level, {}).get(league, {}).get(game_type, 'Rules not found')

def differentiate_rules(rules):
    """
    Differentiate and format rules for preseason, regular season, and playoffs.
    """
    return rules

def get_timeouts_and_challenges(rules):
    """
    Extract information about timeouts and challenges from the rules.
    """
    # Example mock extraction logic (this can be adapted to actual rules data)
    timeouts = "Each team gets 3 timeouts per overtime period."
    challenges = "Each team gets 2 challenges per game."
    return timeouts, challenges

def setup_countdown_clock(overtime_duration):
    """
    Initialize a countdown clock for the overtime period.
    """
    countdown_clock = f"{overtime_duration} minutes countdown clock"
    return countdown_clock

def display_on_web_page(rules, timeouts, challenges, countdown_clock):
    """
    Display the retrieved and formatted information on a web page.
    """
    output_text.set(f"=== Overtime Rules ===\n{rules}\n\n=== Timeouts ===\n{timeouts}\n\n=== Challenges ===\n{challenges}\n\n=== Countdown Clock ===\n{countdown_clock}")

def submit():
    user_input = get_user_input()
    if user_input:
        sport, level, league, game_type = user_input
        rules = query_overtime_rules(sport, level, league, game_type)
        differentiated_rules = differentiate_rules(rules)
        timeouts, challenges = get_timeouts_and_challenges(differentiated_rules)
        countdown_clock = setup_countdown_clock(overtime_duration=10)  # Assume 10 minutes for example
        display_on_web_page(differentiated_rules, timeouts, challenges, countdown_clock)

# GUI Setup
root = tk.Tk()
root.title("Overtime Rules Query")

# Input Variables
sport_var = tk.StringVar()
level_var = tk.StringVar()
league_var = tk.StringVar()
game_type_var = tk.StringVar()
output_text = tk.StringVar()

# Sport Dropdown
tk.Label(root, text="Select Sport:").grid(row=0, column=0, padx=10, pady=5)
sport_options = ["Football", "Basketball", "Hockey", "Baseball"]
sport_menu = tk.OptionMenu(root, sport_var, *sport_options)
sport_menu.grid(row=0, column=1, padx=10, pady=5)

# Level Dropdown
tk.Label(root, text="Select Level:").grid(row=1, column=0, padx=10, pady=5)
level_options = ["College", "Professional"]
level_menu = tk.OptionMenu(root, level_var, *level_options)
level_menu.grid(row=1, column=1, padx=10, pady=5)

# League Dropdown
tk.Label(root, text="Select League:").grid(row=2, column=0, padx=10, pady=5)
league_menu = tk.OptionMenu(root, league_var, "")
league_menu.grid(row=2, column=1, padx=10, pady=5)

def update_league_options(*args):
    sport = sport_var.get().lower()
    level = level_var.get().lower()
    
    if sport == "football" and level == "college":
        league_options = ["FBS", "FCS"]
    elif sport == "football" and level == "professional":
        league_options = ["NFL"]
    elif sport == "basketball" and level == "college":
        league_options = ["NCAA"]
    elif sport == "basketball" and level == "professional":
        league_options = ["NBA", "WNBA"]
    elif sport == "hockey" and level == "college":
        league_options = ["NCAA"]
    elif sport == "hockey" and level == "professional":
        league_options = ["NHL", "PWHL"]
    elif sport == "baseball" and level == "college":
        league_options = ["NCAA"]
    elif sport == "baseball" and level == "professional":
        league_options = ["MLB"]
    else:
        league_options = []
    
    league_var.set('')
    menu = league_menu["menu"]
    menu.delete(0, "end")
    for league in league_options:
        menu.add_command(label=league, command=lambda value=league: league_var.set(value))

sport_var.trace("w", update_league_options)
level_var.trace("w", update_league_options)

# Game Type Dropdown
tk.Label(root, text="Select Game Type:").grid(row=3, column=0, padx=10, pady=5)
game_type_options = ["Preseason", "Regular Season", "Playoffs"]
game_type_menu = tk.OptionMenu(root, game_type_var, *game_type_options)
game_type_menu.grid(row=3, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Output Display
output_label = tk.Label(root, textvariable=output_text, justify=tk.LEFT)
output_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
