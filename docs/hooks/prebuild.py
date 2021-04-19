#
# Mkdocs Hook:  prebuild
#

import os
import re
from pathlib import Path
import shutil


def prebuild(*args, **kwargs):
  '''
  Restructures the docs folder before building the site
  '''
  print("Prebuild:  organize_folders\n")
  organize_folders()

  print("Prebuild:  create_main_index_page\n")
  create_main_index_page()

  # DEBUG
  # f = open("docs/test.txt", "a")
  # f.write("args: " + str(args) + "\n")
  # f.write("kwargs: " + str(kwargs) + "\n")
  # f.close()



def organize_folders():
  '''
  Make sure necessary subfolders exist for each main class folder
  Expecting 2-levels for each Model:
    Model Name:
      classes:
      mixins:
      slots:    
      types:    ## types is auto-generated.
  If the subdirs do not exist, create them
  '''

  dir_list = [ f.path for f in os.scandir('docs') if f.is_dir() and os.path.basename(f) not in ['hooks'] ]
  print(f"Dir List: {dir_list}\n")


  slot_pattern = r"\((?P<md_file>[a-zA-Z0-9]+__[a-zA-Z0-9_]+\.md)\)"
  id_pattern = r"\((?P<md_file>(?:[a-zA-Z0-9]+_)?id\.md)\)"
  class_pattern = r"\((?P<md_file>(?!id|_)[a-zA-Z0-9]+\.md)\)"
  type_pattern = r"\((?P<md_file>types\/[a-zA-Z0-9]+\.md)\)"

  # Visit each model directory
  for dir in dir_list:

    print(f"Organizing: {dir}\n")

    # Create Model subdirectories if they do not exist
    # Types already exist in their own subdir
    for mdir in ['classes', 'slots']:
      if not os.path.exists(f"{dir}/{mdir}"):
        os.makedirs(f"{dir}/{mdir}")
        

    # Visit each *.md file in the model directory
    # Correct link paths as we go
    
    # md_files = [ f.path for f in os.scandir(dir) if f.is_file() ]
    for md_file in Path(dir).rglob('*.md'):    

      md_basename = os.path.basename(md_file)
      bChanged = False
      
      with open(md_file, 'r') as file:
        lines = file.readlines()
      # file.close()

      # print(f"md_file: {md_file}; line_count: {len(lines)}\n")
      # print(f"Range: {range(len(lines))}")
        
      for n in range(len(lines)):
        line = lines[n];

        if '](' in line:
          if 'index.md' == md_basename:
            line = re.sub(slot_pattern, "(slots/\g<md_file>)", line)
            line = re.sub(id_pattern, "(slots/\g<md_file>)", line)
            line = re.sub(class_pattern, "(classes/\g<md_file>)", line)
          else:
            line = re.sub(slot_pattern, "(../slots/\g<md_file>)", line)
            line = re.sub(id_pattern, "(../slots/\g<md_file>)", line)
            line = re.sub(class_pattern, "(../classes/\g<md_file>)", line)
            line = re.sub(type_pattern, "(../\g<md_file>)", line)
            # if lines[n] == line:
            #   print(f"NOT MATCHED - {md_file}; line: {line}\n")
          lines[n] = line

        with open(md_file, 'w') as file:
          file.writelines( lines )
        # file.close()
        

      # Sort/Move the model's files into appropriate subdirectories
      
      if md_basename not in ['index.md']:
        if ('__' in md_basename) or ('_id.md' in md_basename) or ('id.md' == md_basename):
          # Is this a slot file?
          if 'slots' not in str(md_file):
            os.rename(md_file, f"{dir}/slots/{md_basename}")
        else:
          # Is this a class or a types file?
          if '/classes/' not in str(md_file) and '/types/' not in str(md_file):
            os.rename(md_file, f"{dir}/classes/{md_basename}")
          # else:
          #   print(f"NOT MOVED:  {md_file}\n")


def create_main_index_page():
  '''
  create the main docs/index.md based on the model docs generated.
  '''
  lines = []
  main_index_template = "templates/markdown/main_index.md"
  main_index_md = "docs/index.md"

  # delete the old file, if it exists
  if os.path.exists(main_index_md):
    os.remove(main_index_md)
  shutil.copyfile(main_index_template, main_index_md)

  # Get the list of models from docs/*, skip the hooks dir
  dir_list = [ f.path for f in os.scandir('docs') if f.is_dir() and os.path.basename(f) not in ['hooks'] ]

  for dir in dir_list:
    dir_basename = os.path.basename(dir)
    lines.append(f"* [{dir_basename}]({dir_basename}/index.md)\n")

  with open(main_index_md, 'a') as file:
    file.writelines(lines)
     
