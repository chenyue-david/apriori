import sys

def init():
  '''This function opens the flow of file containing data, 
  assign arguments to support and confidence'''
  datasets=[]  #dataset is a list of lists
  support = sys.argv[1]
  confidence = sys.argv[2]
  f = open(sys.argv[3],'r')
  lines = f.readlines()
  for line in lines:
    datasets.append(line.split())
  return datasets, support, confidence

def find_elements(datasets):
  elements = set() #elements is a set of strings
  for record in datasets:
    for element in record:
      elements.add(element)
  return elements

def gen_frepsets(freqsets):
  '''this function takes a list of freqsets whose length = k,
  returns a list of joint candidate sets whose length = k + 1'''
  k = len(freqsets)
  cand_sets = []
  for freqset in freqsets:
    for item in freqset:
      


