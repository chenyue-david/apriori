import sys
import file

def init():
  '''This function opens the flow of file containing data, 
  assign arguments to support and confidence'''
  datasets=()  #dataset is a tuple of tuples
  pass
  support = sys.argv[1]
  cofidence = sys.argv[2]
  return datasets, support, confidence

def find_elements(datasets):
  elements = set()
  for record in dataset:
    for element in record:
      elements.add(element)
  return elements

def gen_
