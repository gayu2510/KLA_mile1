import time
import threading
import yaml
from datetime import datetime


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


def printing(workf, dic, execution):
    for ta in dic.items():
        if ta[1]['Type'] == 'Task':
            print(f'{str(datetime.now()) + ";"}{str(workf) + "."}{ta[0]} Entry')
            time.sleep(int(ta[1]['Inputs']['ExecutionTime']))
            print('{0}{1}{2} Executing {3} ({4}, {5})'.format(str(datetime.now()) + ";", str(workf) + ".", ta[0], ta[1]['Function'], ta[1]['Inputs']['FunctionInput'],
                                                        ta[1]['Inputs']['ExecutionTime']))
            print('{0}{1}{2} Exit'.format(str(datetime.now()) + ";", str(workf) + ".", ta[0]))
        if ta[1]['Type'] == 'Flow':
            print(f'{str(datetime.now()) + ";"}{str(workf) + "."}{ta[0]} Entry')
            printing(workf, ta[1]['Activities'], ta[1]['Execution'])
            print(f'{str(datetime.now()) + ";"}{str(workf) + "."}{ta[0]} Exit')
    # elif execution == 'Concurrent':
    #     for ta in dic.items():


print(f'{str(datetime.now()) + ";"}{workflow_name} Entry')
for i in data[workflow_name].items():
    if i[0] == 'Activities':
        printing(workflow_name,data[workflow_name][i[0]], 'Sequential')
        print(f'{str(datetime.now()) + ";"}{workflow_name} Exit')






