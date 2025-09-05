# from .base import BaseArch
from pathlib import Path

from .base import GitHubUtils

COMMON_DIRS = []
COMMON_FILES = []

class LayeredArch(BaseArch):
    
    COMPONENT_DIRS = {
            "presentation": ["domain", "ports"],
            "application": ["use_cases"],
            "adapters": ["primary", "secondary"]
        }
    
    def _create_сomponent_dirs(self):

        if isinstance(self.COMPONENT_DIRS, dict):

            for comp, subcomps in self.COMPONENT_DIRS.items():
                comp_dir = self.src_dir / comp
                self._create_directory(comp_dir)
                self._create_file(comp_dir / "__init__.py")

                for subcomp in subcomps:
                    subcomp_dir  = comp_dir / subcomp
                    self._create_directory(subcomp_dir)
                    self._create_file(subcomp_dir / "__init__.py")

        elif isinstance(self.COMPONENT_DIRS, (str|list)):

            if isinstance(self.COMPONENT_DIRS, (str)):
                self.COMPONENT_DIRS = [self.COMPONENT_DIRS]

            for comp in self.COMPONENT_DIRS:
                comp_dir  = self.src_dir / comp
                self._create_directory(comp_dir)
                self._create_file(comp_dir / "__init__.py")


class GexArch(BaseArch):

    COMPONENT_DIRS = {
            "core": ["domain", "ports"],
            "application": ["use_cases"],
            "adapters": ["primary", "secondary"]
        }
    
    def _create_сomponent_dirs(self):

        for comp, subcomps in self.COMPONENT_DIRS.items():
            comp_dir = self.src_dir / comp
            self._create_directory(comp_dir)
            self._create_file(comp_dir / "__init__.py")

            for subcomp in subcomps:
                subcomp_dir  = comp_dir / subcomp
                self._create_directory(subcomp_dir)
                self._create_file(subcomp_dir / "__init__.py")


    def _create_domain_layer(self):
        pass


class CastomArch:
  pass

class PypiArch(BaseArch):
    pass
