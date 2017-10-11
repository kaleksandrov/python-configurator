from configurator import config_manager
from configurator.config import Option

opts = []
opts.append(Option('host', 'host', 'h', False, 'localhost', 'help...'))
opts.append(Option('vcip', 'vcip', 'v', True, True, 'help...'))
opts.append(Option('Virgo Directory', 'virgoDir', 'h', False, 'localhost', 'help...'))
opts.append(Option('Virgo Dir 1', 'virgoDir1', 'h', False, 'localhost', 'help...'))
opts.append(Option('NVM bin', 'NVM_BIN', 'h', False, 'localhost', 'help...'))

config_manager.setup(opts)

res = config_manager.config
print '====='
print res
