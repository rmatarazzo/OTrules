import json
import tkinter as tk
from tkinter import ttk, messagebox

# RULES_DATABASE with the clarified structure and sample data
RULES_DATABASE = {
    'football': {
        'professional': {
            'nfl': {
                'preseason': {
                    'overview': 'NFL preseason overtime rules...',
                    'duration': 15,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 3,
                    'challenges': 2
                },
                'regular_season': {
                    'overview': 'NFL regular season overtime rules...',
                    'duration': 10,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 2,
                    'challenges': 2
                },
                'playoffs': {
                    'overview': 'NFL playoff overtime rules...',
                    'duration': 15,
                    'scoring_rules': 'Play continues until a winner is decided',
                    'sudden_death': 'no',
                    'timeouts': 3,
                    'challenges': 2
                }
            },
            'wfa': {
                'preseason': {
                    'overview': 'WFA preseason overtime rules...',
                    'duration': 10,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 2,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'WFA regular season overtime rules...',
                    'duration': 10,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 2,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'WFA playoff overtime rules...',
                    'duration': 15,
                    'scoring_rules': 'Play continues until a winner is decided',
                    'sudden_death': 'no',
                    'timeouts': 3,
                    'challenges': 2
                }
            }
        },
        'college': {
            'ncaa_mens_d1': {
                'preseason': {
                    'overview': 'NCAA Mens D1 preseason overtime rules...',
                    'duration': 15,
                    'scoring_rules': 'Teams alternate possessions from the 25-yard line',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'NCAA Mens D1 regular season overtime rules...',
                    'duration': 15,
                    'scoring_rules': 'Teams alternate possessions from the 25-yard line',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'NCAA Mens D1 playoff overtime rules...',
                    'duration': 15,
                    'scoring_rules': 'Teams alternate possessions from the 25-yard line',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                }
            },
            'ncaa_womens_d1': {
                'preseason': {
                    'overview': 'NCAA Womens D1 preseason overtime rules...',
                    'duration': 15,
                    'scoring_rules': 'Teams alternate possessions from the 25-yard line',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'NCAA Womens D1 regular season overtime rules...',
                    'duration': 15,
                    'scoring_rules': 'Teams alternate possessions from the 25-yard line',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'NCAA Womens D1 playoff overtime rules...',
                    'duration': 15,
                    'scoring_rules': 'Teams alternate possessions from the 25-yard line',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                }
            }
        }
    },
    'basketball': {
        'professional': {
            'nba': {
                'preseason': {
                    'overview': 'NBA preseason overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 1,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'NBA regular season overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'NBA playoff overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                }
            },
            'wnba': {
                'preseason': {
                    'overview': 'WNBA preseason overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 1,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'WNBA regular season overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'WNBA playoff overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                }
            }
        },
        'college': {
            'ncaa_mens_d1': {
                'preseason': {
                    'overview': 'NCAA Mens D1 preseason overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 1,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'NCAA Mens D1 regular season overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'NCAA Mens D1 playoff overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                }
            },
            'ncaa_womens_d1': {
                'preseason': {
                    'overview': 'NCAA Womens D1 preseason overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 1,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'NCAA Womens D1 regular season overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'NCAA Womens D1 playoff overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'Team with the most points wins',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                }
            }
        }
    },
    'baseball': {
        'professional': {
            'mlb': {
                'preseason': {
                    'overview': 'MLB preseason overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Each team gets a turn to bat and field',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 2
                },
                'regular_season': {
                    'overview': 'MLB regular season overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Each team gets a turn to bat and field',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 2
                },
                'playoffs': {
                    'overview': 'MLB playoff overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Each team gets a turn to bat and field',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 2
                }
            }
        },
        'college': {
            'ncaa_mens_d1': {
                'preseason': {
                    'overview': 'NCAA Mens D1 preseason overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Each team gets a turn to bat and field',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'NCAA Mens D1 regular season overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Each team gets a turn to bat and field',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'NCAA Mens D1 playoff overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Each team gets a turn to bat and field',
                    'sudden_death': 'no',
                    'timeouts': 2,
                    'challenges': 1
                }
            }
        }
    },
    'hockey': {
        'professional': {
            'nhl': {
                'preseason': {
                    'overview': 'NHL preseason overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'NHL regular season overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'NHL playoff overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Play continues until a winner is decided',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                }
            },
            'pwhl': {
                'preseason': {
                    'overview': 'PWHL preseason overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'PWHL regular season overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'PWHL playoff overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Play continues until a winner is decided',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                }
            }
        },
        'college': {
            'ncaa_mens_d1': {
                'preseason': {
                    'overview': 'NCAA Mens D1 preseason overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'NCAA Mens D1 regular season overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'NCAA Mens D1 playoff overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Play continues until a winner is decided',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                }
            },
            'ncaa_womens_d1': {
                'preseason': {
                    'overview': 'NCAA Womens D1 preseason overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                },
                'regular_season': {
                    'overview': 'NCAA Womens D1 regular season overtime rules...',
                    'duration': 5,
                    'scoring_rules': 'First team to score wins',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                },
                'playoffs': {
                    'overview': 'NCAA Womens D1 playoff overtime rules...',
                    'duration': 20,
                    'scoring_rules': 'Play continues until a winner is decided',
                    'sudden_death': 'yes',
                    'timeouts': 1,
                    'challenges': 1
                }
            }
        }
    }
}

class OvertimeRulesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Overtime Rules Database")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.sport_label = tk.Label(self, text="Sport:")
        self.sport_label.pack()
        self.sport_combobox = ttk.Combobox(self, values=list(RULES_DATABASE.keys()))
        self.sport_combobox.pack()
        self.sport_combobox.bind("<<ComboboxSelected>>", self.update_levels)

        self.level_label = tk.Label(self, text="Level:")
        self.level_label.pack()
        self.level_combobox = ttk.Combobox(self)
        self.level_combobox.pack()
        self.level_combobox.bind("<<ComboboxSelected>>", self.update_leagues)

        self.league_label = tk.Label(self, text="League:")
        self.league_label.pack()
        self.league_combobox = ttk.Combobox(self)
        self.league_combobox.pack()
        self.league_combobox.bind("<<ComboboxSelected>>", self.update_game_types)

        self.game_type_label = tk.Label(self, text="Game Type:")
        self.game_type_label.pack()
        self.game_type_combobox = ttk.Combobox(self)
        self.game_type_combobox.pack()
        self.game_type_combobox.bind("<<ComboboxSelected>>", self.display_rules)

        self.rules_text = tk.Text(self, wrap=tk.WORD, height=20, width=80)
        self.rules_text.pack()

    def update_levels(self, event):
        sport = self.sport_combobox.get()
        levels = list(RULES_DATABASE[sport].keys())
        self.level_combobox.config(values=levels)
        self.level_combobox.set('')
        self.league_combobox.set('')
        self.game_type_combobox.set('')
        self.rules_text.delete(1.0, tk.END)

    def update_leagues(self, event):
        sport = self.sport_combobox.get()
        level = self.level_combobox.get()
        leagues = list(RULES_DATABASE[sport][level].keys())
        self.league_combobox.config(values=leagues)
        self.league_combobox.set('')
        self.game_type_combobox.set('')
        self.rules_text.delete(1.0, tk.END)

    def update_game_types(self, event):
        sport = self.sport_combobox.get()
        level = self.level_combobox.get()
        league = self.league_combobox.get()
        game_types = list(RULES_DATABASE[sport][level][league].keys())
        self.game_type_combobox.config(values=game_types)
        self.game_type_combobox.set('')
        self.rules_text.delete(1.0, tk.END)

    def display_rules(self, event):
        sport = self.sport_combobox.get()
        level = self.level_combobox.get()
        league = self.league_combobox.get()
        game_type = self.game_type_combobox.get()

        rules = RULES_DATABASE[sport][level][league][game_type]
        rules_display = (
            f"Overview: {rules['overview']}\n"
            f"Duration: {rules['duration']} minutes\n"
            f"Scoring Rules: {rules['scoring_rules']}\n"
            f"Sudden Death: {rules['sudden_death']}\n"
            f"Timeouts: {rules['timeouts']}\n"
            f"Challenges: {rules['challenges']}\n"
        )

        self.rules_text.delete(1.0, tk.END)
        self.rules_text.insert(tk.END, rules_display)

if __name__ == "__main__":
    app = OvertimeRulesApp()
    app.mainloop()
