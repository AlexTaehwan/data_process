import pandas as pd
import json
import numpy as np

def processid():
    dic = {}
    with open("entity_list.txt", "r") as f:
        for line in f:
            arr = line.strip().split()
            dic[''.join(arr[:-1])] = int(arr[-1])
    with open('ent2id.txt','w') as file:
        file.write(json.dumps(dic))

def processrel():
    data = pd.read_csv("relation_list.txt", sep=" ", header=None)
    data = data[1:]
    data = data.rename(columns={0:'X', 1: 'Y'})
    data['Y'] = data['Y'].astype(int)
    dic = dict(zip(data.X, data.Y))
    with open('rel2id.txt', 'w') as file:
        file.write(json.dumps(dic))

def processkg():
    data = pd.read_csv("kg_final.txt", sep=" ", header=None)
    cols = [1,0,2]
    data = data[cols]
    np.savetxt('kg_final_mod.txt', data.values, fmt='%d')

def processtrain():
    print("start processing train")
    columns = ["id_num", "source", "relation"]
    pd_train = pd.DataFrame(columns=columns)
    with open("train.txt", "r") as f:
        for line in f:
            arr = line.strip().split()
            for i in range(1, len(arr)):
                new_row = {'id_num' : 39, 'source' : arr[0], 'relation': arr[i]}
                pd_train = pd_train.append(new_row, ignore_index=True)
    np.savetxt('train_mod.txt', pd_train.values, fmt='%d')
    print("fininsh processing train")
def processtest():
    print("start processing test")
    columns = ["id_num", "source", "relation", "edge"]
    pd_test = pd.DataFrame(columns=columns)
    with open("test.txt", "r") as f:
        for line in f:
            arr = line.strip().split()
            for i in range(1, len(arr)):
                new_row = {'id_num' : 39, 'source' : arr[0], 'relation': arr[i], 'edge': 1}
                pd_test = pd_test.append(new_row, ignore_index=True)
    np.savetxt('test_mod.txt', pd_test.values, fmt="%d")
    print("finish processing test")

if __name__ == '__main__':
    # processid()
    # processrel()
    # processkg()
    processtrain()
    processtest()