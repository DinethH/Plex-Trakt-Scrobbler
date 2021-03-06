import sys

# submodules for Plex plugins "hack"

import plugin
sys.modules['core.plugin'] = plugin

import logger
sys.modules['core.logger'] = logger

import localization
sys.modules['core.localization'] = localization

import logging_handler
sys.modules['core.logging_handler'] = logging_handler

import header
sys.modules['core.header'] = header


import model
sys.modules['core.model'] = model

import helpers
sys.modules['core.helpers'] = helpers

import configuration
sys.modules['core.configuration'] = configuration

import numeric
sys.modules['core.numeric'] = numeric

import eventing
sys.modules['core.eventing'] = eventing

import cache
sys.modules['core.cache'] = cache

import network
sys.modules['core.network'] = network

import method_manager
sys.modules['core.method_manager'] = method_manager

import update_checker
sys.modules['core.update_checker'] = update_checker

import migrator
sys.modules['core.migrator'] = migrator

import task
sys.modules['core.task'] = task
