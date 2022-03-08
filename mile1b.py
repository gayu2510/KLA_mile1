import time
import threading
import yaml
from datetime import datetime
import concurrent.futures


def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor, Loader=yaml.FullLoader)
    return data


def yaml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

file_path = "DataSet/Milestone1/Milestone1B.yaml"
data = yaml_loader(file_path)
for key in data:
    workflow_name = key
    break

def conc(workf,dic,path):
    if dic[1]['Type'] == 'Task':
        print(f'{str(datetime.now()) + ";"}{path + "."}{dic[0]} Entry\n')
        time.sleep(int(dic[1]['Inputs']['ExecutionTime']))
        print(
            '{0}{1}{2} Executing {3} ({4}, {5})\n'.format(str(datetime.now()) + ";", path + ".", dic[0], dic[1]['Function'],
                                                        dic[1]['Inputs']['FunctionInput'],
                                                        dic[1]['Inputs']['ExecutionTime']))
        print('{0}{1}{2} Exit\n'.format(str(datetime.now()) + ";", path + ".", dic[0]))
    if dic[1]['Type'] == 'Flow':
        path1 = path + "."
        print(f'{str(datetime.now()) + ";"}{path1}{dic[0]} Entry\n')
        printing(workf, dic[1]['Activities'], dic[1]['Execution'], path1 + dic[0])
        print(f'{str(datetime.now()) + ";"}{path1}{dic[0]} Exit\n')

def printing(workf, dic, execution,path):
    if execution == 'Sequential':
        for ta in dic.items():
            if ta[1]['Type'] == 'Task':
                print(f'{str(datetime.now()) + ";"}{path+"."}{ta[0]} Entry\n')
                time.sleep(int(ta[1]['Inputs']['ExecutionTime']))
                print('{0}{1}{2} Executing {3} ({4}, {5})\n'.format(str(datetime.now()) + ";", path + ".", ta[0], ta[1]['Function'], ta[1]['Inputs']['FunctionInput'],
                                                            ta[1]['Inputs']['ExecutionTime']))
                print('{0}{1}{2} Exit\n'.format(str(datetime.now()) + ";", path+".", ta[0]))
            if ta[1]['Type'] == 'Flow':
                path1 = path + "."
                print(f'{str(datetime.now()) + ";"}{path1}{ta[0]} Entry\n')
                printing(workf, ta[1]['Activities'], ta[1]['Execution'], path1 + ta[0])
                print(f'{str(datetime.now()) + ";"}{path1}{ta[0]} Exit\n')
    elif execution == 'Concurrent':
        l = []
        for k in dic.items():
            t = threading.Thread(target=conc, args=(workf, k, path))
            t.start()
            l.append(t)
        for ele in l:
            ele.join()



print(f'{str(datetime.now()) + ";"}{workflow_name} Entry')
for i in data[workflow_name].items():
    if i[0] == 'Activities':
        printing(workflow_name,data[workflow_name][i[0]], 'Sequential', workflow_name)
        print(f'{str(datetime.now()) + ";"}{workflow_name} Exit')
