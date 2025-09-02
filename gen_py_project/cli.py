
import argparse
from .base import BaseArch

def main():
    parser = argparse.ArgumentParser(description="Генератор структуры проекта на Python")

    parser.add_argument('-n','--name',help='Имя проекта', required=True)
    parser.add_argument('-a','--arch',help='Тип архитектуры',required=True)
    parser.add_argument('-d','--dir',help='Расположение папки проекта',required=True)
    
    
    args = parser.parse_args()
    
    if args.arch:
        BaseArch(name=args.name, base_dir=args.dir)
    