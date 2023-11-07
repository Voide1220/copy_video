import pandas as pd
import ipdb
import numpy as np


import csv

# headers = ['idx','name','series','douban_id','url','status','source','row_id']
# rows = [('1','renxiaren','1','36477357','done','effective','mgtv_movie','788a55c0ca1e9cc86c425300730b37d0'),
# ('2','muoujinghun','1','36477961','done','effective','mgtv_movie','4bbe62f1235b4067ac010cb791ba889c'),
# ('3','xindimingzi','1','36474017','done','effective','mgtv_movie','c94713fd6a7913a02d0b94d73cbd5c61'),
# ('4','xindimingzi','2','36474017','done','effective','mgtv_movie','10d224c02e8d5f2e3017b4724d7b6314'),
# ('5','xindimingzi','3','36474017','done','effective','mgtv_movie','506f91b01e397cd0997a4cd994c5a373'),
# ('6','xindimingzi','4','36474017','done','effective','mgtv_movie','d31cbb92d54d1348dcd7b2a40c91e9b9'),
# ('7','xindimingzi','5','36474017','done','effective','mgtv_movie','da2bc903ee7215f00d29167c7262b3ff'),
# ('8','xindimingzi','6','36474017','done','effective','mgtv_movie','89db312ec3b5429d0e33ac59377c0609')
# ]
# with open('info.csv','w',encoding='utf8',newline='') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(headers)
# 	writer.writerows(rows)



df = pd.read_csv("info.csv", encoding='ISO-8859-1')
df_array = np.array(df) 
df_list = df_array.tolist() 

## 读出来的结果是
# [[1, 'renxiaren', 1, 36477357, 'done', 'effective', 'mgtv_movie', '788a55c0ca1e9cc86c425300730b37d0'], [2, 'muoujinghun', 1, 36477961, 'done', 'effective', 'mgtv_movie', '4bbe62f1235b4067ac010cb791ba889c'], ...]

ipname = []

for i in df_list:
	if i[3] not in ipname:
		ipname.append(i[3])

print('there are %d ips' % len(ipname))

dicts = {}
for u in ipname:
	dicts[u] = []
	for j in df_list:
		if j[3]==u:
			dicts[u].append(j[-1])


ipdb.set_trace()
