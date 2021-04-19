
#
# Mkdocs Hook:  postbuild
#

import shutil

def postbuild(*args, **kwargs):
  '''
  Postbuild
  '''
  print("Postbuild:  Cleanup\n")
  
  shutil.rmtree('site/hooks')

  # DEBUG
  # f = open("docs/test.txt", "a")
  # f.write("args: " + str(args) + "\n")
  # f.write("kwargs: " + str(kwargs) + "\n")
  # f.close()

