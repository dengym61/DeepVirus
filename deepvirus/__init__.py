"""A tool to fit mechanistic models to deep mutational scanning data"""
# Import classes users will interact with

from deepvirus.project import VirusProject

# Handle versioneer
from deepvirus._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
