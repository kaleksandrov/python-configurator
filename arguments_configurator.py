from config import Configurator, Option

class ArgsConfigurator(Configurator):

   def __init__(self, options):
      super(self.__class__, self).__init__(options)
      self._config = None

   def _load(self):
      import sys
      import getopt

      scriptName = sys.argv[0]
      clops = sys.argv[1:]

      shortOpts = ''
      longOpts = []
      config = {}
      for opt in self._options:
         shortOpts += opt.short_name
         longOpts.append(opt.long_name + int(not opt.is_flag)*'=')

      try:
         opts, args = getopt.getopt(clops, shortOpts, longOpts)
      except getopt.GetoptError, e:
         print e
         self.print_help(scriptName)
         sys.exit(2)

      for opt, arg in opts:
         print opt, arg
         for option in self._options:
            if opt in option.opt_set():
               config[option.name] = arg
               break
         else:
            sys.exit(3)
            print "Unknown property %s" % opt

         for option in self._options:
            if option.name not in config:
                config[option.name] = option.default

      return config
