
import os
from keyword import iskeyword


class BaseArch:
    
    
    COMMON_DIRS = [
        "tests",
        "docs",
        "scripts"
    ]
    
    COMMON_FILES = [
        "README.md",
        "requirements.txt",
        ".env",
        "config.py"
    ]
    
    
    def __init__(self, name: str, base_dir: str):
        self.name = name
        self.base_dir = base_dir
        
        if not self._check_valid_proj_name():
            raise TypeError
        self._create_proj_dir()
        
        
    def _check_valid_proj_name(self):
        return self.name and self.name.isidentifier() and not iskeyword(self.name)

    def _create_proj_dir(self):
        os.makedirs(os.path.join(self.base_dir, self.name))
    
    def create_env(self):
        pass
    
    