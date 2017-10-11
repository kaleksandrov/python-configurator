from config import Option
from environment_configurator import EnvironmentConfigurator

opts = []
opts.append(Option('Virgo Directory', 'virgoDir', 'h', False, 'localhost', 'help...'))
opts.append(Option('Virgo Dir 1', 'virgoDir1', 'h', False, 'localhost', 'help...'))
opts.append(Option('NVM bin', 'NVM_BIN', 'h', False, 'localhost', 'help...'))
config_manager = EnvironmentConfigurator(opts)
res = config_manager.config
print '====='
print res
