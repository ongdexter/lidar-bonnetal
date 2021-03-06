#!/usr/bin/env python3
# Created by Dexter

import argparse
import subprocess
import datetime
import yaml
from shutil import copyfile
import os
import shutil
import __init__ as booger

from tasks.semantic.modules.user import ExportUser
from tasks.semantic.modules.segmentator import *

if __name__ == '__main__':
  parser = argparse.ArgumentParser("./infer.py")
  parser.add_argument(
      '--model', '-m',
      type=str,
      required=True,
      default=None,
      help='Directory to get the trained model.'
  )
  FLAGS, unparsed = parser.parse_known_args()

  # print summary of what we will do
  print("----------")
  print("INTERFACE:")
  print("model", FLAGS.model)
  print("----------\n")
  print("Commit hash (training version): ", str(
      subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()))
  print("----------\n")

  # open arch config file
  try:
    print("Opening arch config file from %s" % FLAGS.model)
    ARCH = yaml.safe_load(open(FLAGS.model + "/arch_cfg.yaml", 'r'))
  except Exception as e:
    print(e)
    print("Error opening arch yaml file.")
    quit()

  # open data config file
  try:
    print("Opening data config file from %s" % FLAGS.model)
    DATA = yaml.safe_load(open(FLAGS.model + "/data_cfg.yaml", 'r'))
  except Exception as e:
    print(e)
    print("Error opening data yaml file.")
    quit()

  # does model folder exist?
  if os.path.isdir(FLAGS.model):
    print("model folder exists! Using model from %s" % (FLAGS.model))
  else:
    print("model folder doesnt exist! Can't infer...")
    quit()

  # create user and infer dataset
  user = ExportUser(ARCH, DATA, FLAGS.model)
  user.convert_to_onnx()