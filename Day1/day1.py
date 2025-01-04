import pandas as pd

input = pd.read_fwf('input.txt', header=None, widths=[7,7])
input.columns = ['list1', 'list2']
input.list1 = sorted(input.list1.astype('int').to_list())
input.list2 = sorted(input.list2.astype('int').to_list())
input['tot_list'] = abs(input.list1 - input.list2)

print(input.tot_list.sum())


