"""
Módulo compartilhado para os projetos de automação.
"""

from .browser_config import create_edge_driver, create_safari_driver, create_firefox_driver, create_driver, create_wait

__all__ = ['create_edge_driver', 'create_safari_driver', 'create_firefox_driver', 'create_driver', 'create_wait']

