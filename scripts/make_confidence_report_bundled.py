"""
make_confidence_report_bundled.py
Usage:
  python make_confidence_report_bundled.py model.joblib

  where model.joblib is a file created by cleverhans.serial.save containing
  a picklable cleverhans.model.Model instance.

This script will run the model on clean data and bundled adversarial examples
( https://openreview.net/forum?id=H1g0piA9tQ ) for a max norm threat model
on the dataset the model was trained on.
It will save a report to to model_bundled_report.joblib.
The report can be later loaded by another
script using cleverhans.serial.load.

See cleverhans.confidence_report for more description of the report format.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
import tensorflow as tf
from tensorflow.python.platform import flags
import six

from cleverhans.confidence_report import make_confidence_report_bundled
from cleverhans.confidence_report import TRAIN_START, TRAIN_END
from cleverhans.confidence_report import TEST_START, TEST_END
from cleverhans.confidence_report import WHICH_SET


FLAGS = flags.FLAGS

def main(argv=None):
  """
  Make a confidence report and save it to disk.
  """
  try:
    name_of_script, filepath = argv
  except ValueError:
    raise ValueError(argv)
  print(filepath)
  make_confidence_report_bundled(filepath=filepath,
                                 test_start=FLAGS.test_start,
                                 test_end=FLAGS.test_end,
                                 which_set=FLAGS.which_set)


if __name__ == '__main__':
  flags.DEFINE_integer('train_start', TRAIN_START, 'Starting point (inclusive)'
                       'of range of train examples to use')
  flags.DEFINE_integer('train_end', TRAIN_END, 'Ending point (non-inclusive) '
                       'of range of train examples to use')
  flags.DEFINE_integer('test_start', TEST_START, 'Starting point (inclusive) of range'
                       ' of test examples to use')
  flags.DEFINE_integer('test_end', TEST_END, 'End point (non-inclusive) of range'
                       ' of test examples to use')
  flags.DEFINE_string('which_set', WHICH_SET, '"train" or "test"')
  tf.app.run()