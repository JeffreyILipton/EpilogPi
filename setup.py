from distutils.core import setup
import py2exe 
setup(
    console=['httpinterface.py'],
    options={"py2exe": {
                        "bundle_files":1,
                        }
              }
    )