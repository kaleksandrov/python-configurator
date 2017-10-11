from manager import  ConfigManager
from arguments_configurator import ArgsConfigurator
from environment_configurator import EnvironmentConfigurator

config_manager = ConfigManager()
config_manager.register(ArgsConfigurator())
config_manager.register(EnvironmentConfigurator())
