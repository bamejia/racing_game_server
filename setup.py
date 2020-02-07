""" For using cx-freeze to turn python main.py into an executable """

from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages=["sys", 'pygame'],
    include_files=["controller", "model", "global_variables.py", 'online_multiplayer'],
    build_exe=".\\build\\server-v0.4",
    excludes=[]
)

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('server.py', icon='red_car_horizontal.ico', targetName='Racing Game Server.exe')  # base=base
]

setup(name='racing game',
      version='0.4',
      description='racing game',
      options=dict(build_exe=buildOptions),
      executables=executables, requires=['pygame'])
