from config import Option
from arguments_configurator import ArgsConfigurator

opts = []
opts.append(Option('host', 'host', 'h', False, 'localhost', 'help...'))
config_manager = ArgsConfigurator(opts)
res = config_manager.config
print '====='
print res
