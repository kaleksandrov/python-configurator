#!/usr/bin/env python

class Option(object):
   """
   Configuration option model
   """

   def __init__(self, name, long_name, short_name, is_flag, default, help_msg):
      self._name = name
      self._long_name = long_name
      self._short_name = short_name
      self._is_flag = is_flag
      self._default = default
      self._help_msg = help_msg

   @property
   def name(self):
      return self._name

   @property
   def long_name(self):
      return self._long_name

   @property
   def short_name(self):
      return self._short_name

   @property
   def is_flag(self):
      return self._is_flag

   @property
   def default(self):
         return self._default

   @property
   def help_msg(self):
         return self._help_msg

   def opt_set(self):
      optSet = set()
      optSet.add(self._short_opt(False, True))
      optSet.add(self._long_opt(False, True))
      return optSet

   def _short_opt(self, isComplex=True, hasPrefix=False):
      pattern = '-'*int(hasPrefix)+'%s'+':'*int(isComplex)
      return pattern % self.short_name


   def _long_opt(self, isComplex=True, hasPrefix=False):
      pattern = '--'*int(hasPrefix)+'%s'+'='*int(isComplex)
      return pattern % self.long_name


class Configurator(object):
   """
   Abstract configurator class
   """

   def __init__(self, options):
      self._options = options


   @property
   def config(self):
      if not self._config:
         self._config = self._load()

      return self._config

   def _load(self):
      pass

   def print_help(self, scriptName):
      msg =  "Usage: {} [OPTION=<value>]..."
      args = [scriptName]

      def line(line):
         import os
         return os.linesep + line

      for opt in self._options:
         msg += line("{}, {} : {}")
         args.append(opt._short_opt(False, True))
         args.append(opt._long_opt(False, True))
         args.append(opt._help_msg)

      print msg.format(*args)
