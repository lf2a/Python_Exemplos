from logging import basicConfig, INFO, captureWarnings
from warnings import warn

basicConfig(level=INFO)

warn('warning 1')
captureWarnings(True)

warn('warning 2')