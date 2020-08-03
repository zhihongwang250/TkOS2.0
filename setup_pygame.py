import os
import sys

executable = sys.executable
command = f'{executable} -m pip install '
package = 'pygame==1.9.6'
command += f'--no-cache-dir --force-reinstall {package}'

if __name__ == "__main__":
    os.system(command)
