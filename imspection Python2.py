import platform
import sys
if platform.python_version_tuple()[0] == 2:
    print('不对Python2进行支持')
    sys.exit(-1)
else:
    print('请使用')