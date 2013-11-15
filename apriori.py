#encoding = utf-8
import sys

#what do i need: a dict containing the support for each dataset,
#a list of frozenset(dataset)

def init():
  '''opens the flow of file containing data, 
  assigns arguments to support and confidence'''
  datasets=[]  #dataset is a list of lists
 # support = sys.argv[1]
 # confidence = sys.argv[2]
  f = open(sys.argv[3],'r')
  lines = f.readlines()
  for line in lines:
    datasets.append(map(str,line.split()))
  return datasets

def find_elements(datasets, supports_dict):
  elements = [] #elements is a list of all item strings
  for record in datasets:
    for element in record:
      if element not in elements:
        elements.append(element)
        supports_dict[frozenset(list(element))] = 0
  return elements, supports_dict

def gen_joint(kfreqsets, supports_dict):
  '''takes a list of freqsets whose length = k,
  returns a list of joint candidate sets whose length = k + 1'''
  k = len(kfreqsets[0])
  n = len(kfreqsets)
  cand_sets = []
  for i in range(0, n):
    for j in range(i + 1, n):
      kfreqsets[i].sort()
      kfreqsets[j].sort()
      if kfreqsets[i][:k - 1] == kfreqsets[j][:k - 1]:
        s1 = set(kfreqsets[i])
        s2 = set(kfreqsets[j])
        new_cand = list(s1.union(s2))
        cand_sets.append(new_cand)
        supports_dict[frozenset(new_cand)] = 0
  return cand_sets, supports_dict

def prune(cand_sets, supports_dict, datasets, support):
  '''takes cand_sets, returns pruned sets
  and updates the dict for every dataset'''
  pruned = []
  total_rows = float(len(datasets))
  for candidate in cand_sets:
    count = 0
    for item in datasets:
      if set(candidate).issubset(set(item)):
        count += 1
    cand_sup = float(count) / total_rows
    supports_dict[frozenset(candidate)] = cand_sup
    if cand_sup >= support:
      pruned.append(candidate)
  return pruned, supports_dict

def apriori():
  '''calls gen_joint, prune until finished, returns all
  frequent sets and support dict'''
  datasets = init()
  support = sys.argv[1]
  supports_dict = {}
  elements, supports_dict = find_elements(datasets, supports_dict)  #create 1freqsets
  all_freqsets = []
  pruned, supports_dict = prune(map(list,elements), supports_dict, datasets, support)
  all_freqsets.append(pruned)
  pruned = [1, 2]
  while(len(pruned) > 0):
  #  print all_freqsets
    cand_sets, supports_dict = gen_joint(all_freqsets[-1], supports_dict)
    pruned, supports_dict = prune(cand_sets, supports_dict, datasets, support)
    all_freqsets.append(pruned)
  print all_freqsets, supports_dict
  return all_freqsets, supports_dict

#apriori()
