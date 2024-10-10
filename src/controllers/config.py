import os
import configparser

# Define the config controller class
class ConfigController:
    def __init__(self, repo_path=".kinto", global_config=False):
        # Local repository config or global config based on the flag
        self.config_file = (
            os.path.expanduser("~/.kinto/config") if global_config else f"{repo_path}/config"
        )
        self.config = configparser.ConfigParser()
        
        # Load config if the file exists
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
        else:
            # Create the config file if it doesn't exist
            self.create_config()

    def create_config(self):
        """Initialize the config file with default sections."""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, "w") as f:
            self.config.write(f)

    def get(self, section, option):
        """Get a configuration value."""
        try:
            return self.config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return None

    def set(self, section, option, value):
        """Set a configuration value and save it."""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, value)
        self.save()

    def save(self):
        """Save the configuration to the file."""
        with open(self.config_file, "w") as f:
            self.config.write(f)

    def list_all(self):
        """List all configurations."""
        return {section: dict(self.config.items(section)) for section in self.config.sections()}
