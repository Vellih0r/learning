print('__init__package')

#   . - current dir

#   .. -  dir on upper level

from .file1 import *
# can use file1 when import package

from .file2 import a

from .file2 import *  #in * only 'b'

# from . import file1, file2


__all__ = ['file1']
#__all_ works same as in 'file2.py'