from config import Option
from arguments_configurator import ArgsConfigurator

opts = []
opts.append(Option('host', 'host', 'h', False, 'localhost', 'help...'))
opts.append(Option('vcip', 'vcip', 'v', True, True, 'help...'))
config_manager = ArgsConfigurator(opts)
res = config_manager.config
print '====='
print res
