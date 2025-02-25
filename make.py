import os

# Define the directory structure
structure = {
    "telegram_sandbox_bot": {
        "bot": {
            "__init__.py": "",
            "core": {
                "__init__.py": "",
                "bot_instance.py": "",
                "config_loader.py": "",
                "error_handler.py": "",
                "logger.py": "",
                "utils": {
                    "__init__.py": "",
                    "helpers.py": ""
                }
            },
            "modules": {
                "__init__.py": "",
                "general_commands": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "start_command.py": "",
                        "help_command.py": ""
                    },
                    "general_commands.py": ""
                },
                "minigames": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "quiz_command.py": "",
                        "number_guess_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "quiz_logic.py": "",
                        "number_guess_logic.py": ""
                    },
                    "minigames.py": ""
                },
                "rpg_elements": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "profile_command.py": "",
                        "inventory_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "profile_logic.py": "",
                        "inventory_logic.py": ""
                    },
                    "data": {
                        "__init__.py": "",
                        "rpg_data.py": ""
                    },
                    "rpg_elements.py": ""
                },
                "pubg_telegram_inspired": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "battle_command.py": "",
                        "loadout_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "pubg_logic.py": ""
                    },
                    "data": {
                        "__init__.py": "",
                        "pubg_data.py": ""
                    },
                    "pubg_telegram.py": ""
                },
                "social_features": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "guild_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "social_logic.py": ""
                    },
import os

# Define the directory structure
structure = {
    "telegram_sandbox_bot": {
        "bot": {
            "__init__.py": "",
            "core": {
                "__init__.py": "",
                "bot_instance.py": "",
                "config_loader.py": "",
                "error_handler.py": "",
                "logger.py": "",
                "utils": {
                    "__init__.py": "",
                    "helpers.py": ""
                }
            },
            "modules": {
                "__init__.py": "",
                "general_commands": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "start_command.py": "",
                        "help_command.py": ""
                    },
                    "general_commands.py": ""
                },
                "minigames": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "quiz_command.py": "",
                        "number_guess_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "quiz_logic.py": "",
                        "number_guess_logic.py": ""
                    },
                    "minigames.py": ""
                },
                "rpg_elements": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "profile_command.py": "",
                        "inventory_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "profile_logic.py": "",
                        "inventory_logic.py": ""
                    },
                    "data": {
                        "__init__.py": "",
                        "rpg_data.py": ""
                    },
                    "rpg_elements.py": ""
                },
                "pubg_telegram_inspired": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "battle_command.py": "",
                        "loadout_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "pubg_logic.py": ""
                    },
                    "data": {
                        "__init__.py": "",
                        "pubg_data.py": ""
                    },
                    "pubg_telegram.py": ""
                },
                "social_features": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "guild_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "social_logic.py": ""
                    },
                    "social_features.py": ""
                },
                "genshin_inspired": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "gacha_command.py": "",
                        "characters_command.py": "",
                        "profile_command.py": "",
                        "explore_command.py": "",
                        "quests_command.py": "",
                        "team_command.py": "",
                        "battle_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "gacha_logic.py": "",
                        "character_logic.py": "",
                        "profile_logic.py": "",
                        "exploration_logic.py": "",
                        "quest_logic.py": "",
                        "team_logic.py": "",
                        "battle_logic.py": ""
                    },
                    "data": {
                        "__init__.py": "",
                        "genshin_data.py": ""
                    },
                    "genshin_telegram.py": ""
                },
                "honkai_inspired": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "warp_command.py": "",
                        "characters_command.py": "",
                        "profile_command.py": "",
                        "explore_command.py": "",
                        "missions_command.py": "",
                        "team_command.py": "",
                        "combat_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "warp_logic.py": "",
                        "character_logic.py": "",
                        "profile_logic.py": "",
                        "exploration_logic.py": "",
                        "mission_logic.py": "",
                        "team_logic.py": "",
                        "combat_logic.py": ""
                    },
                    "data": {
                        "__init__.py": "",
                        "honkai_data.py": ""
                    },
                    "honkai_telegram.py": ""
                }
            },
            "data": {
                "__init__.py": "",
                "databases": {
                    "__init__.py": "",
                    "database_manager.py": "",
                    "models.py": ""
                }
            },
            "config": {
                "__init__.py": "",
                "config.ini": ""
            },
            "logs": {},
            "main.py": "",
            "requirements.txt": "",
            "README.md": ""
        }
    }
}
￼Enter                    "social_features.py": ""
                },
                "genshin_inspired": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "gacha_command.py": "",
                        "characters_command.py": "",
                        "profile_command.py": "",
                        "explore_command.py": "",
                        "quests_command.py": "",
                        "team_command.py": "",
                        "battle_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "gacha_logic.py": "",
                        "character_logic.py": "",
                        "profile_logic.py": "",
                        "exploration_logic.py": "",
                        "quest_logic.py": "",
                        "team_logic.py": "",
                        "battle_logic.py": ""
                    },
                    "data": {
                        "__init__.py": "",
                  "genshin_data.py": ""
                    },
                    "genshin_telegram.py": ""
                },
                "honkai_inspired": {
                    "__init__.py": "",
                    "commands": {
                        "__init__.py": "",
                        "warp_command.py": "",
                        "characters_command.py": "",
                        "profile_command.py": "",
                        "explore_command.py": "",
                        "missions_command.py": "",
                        "team_command.py": "",
                        "combat_command.py": ""
                    },
                    "logic": {
                        "__init__.py": "",
                        "warp_logic.py": "",
                        "character_logic.py": "",
                        "profile_logic.py": "",
                        "exploration_logic.py": "",
                        "mission_logic.py": "",
                        "team_logic.py": "",
                        "combat_logic.py": ""
                    },
