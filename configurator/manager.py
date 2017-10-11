#!/usr/bin/env python
from config import Configurator

def extend_configs(c1, c2):
   for k,v in c2.items():
      if not c1.has_key(k):
         c1[k] = v

class ConfigManager(Configurator):
   """
   Configuration option model
   """

   def __init__(self):
      self._configurators = []

   def register(self, configurator):
      if not configurator:
         raise ValueError('The configurator must not be None')

      if not isinstance(configurator, Configurator):
         raise ValueError('The configurator must of type Configurator')

      self._configurators.append(configurator)

   def setup(self, options):
      super(self.__class__, self).setup(options)
      for configurator in self._configurators:
         print 'Setup configurator : ' + str(configurator)
         configurator.setup(options)

   def _load(self):
      config = {}
      for configurator in self._configurators:
         tmp_config = configurator._load()
         print tmp_config
         extend_configs(config, tmp_config)

      return config
