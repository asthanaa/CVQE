"""This is an efficient python code to run  pulse level molecular simulation algorithm: ctrl-VQE."""

# Add imports here
from .src import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
