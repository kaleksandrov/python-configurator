from config import Configurator, Option

def to_env_name(name):
   import re
   s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
   return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).upper()

class EnvironmentConfigurator(Configurator):

   def __init__(self, options):
      super(self.__class__, self).__init__(options)
      self._config = None

   def _load(self):
      import os
      from os import environ as env

      config = {}
      for opt in self._options:
         opt_value = None
         for name in [to_env_name(opt.long_name), opt.long_name]:
            if not opt_value:
               try:
                  opt_value = env[name]
                  break
               except:
                  pass
         else:
            opt_value = opt.default

         config[opt.name] = opt_value

      return config
