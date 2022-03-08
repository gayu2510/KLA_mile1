import yaml

def yaml_loader(filepath):
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor, Loader=yaml.FullLoader)
    return data


def yaml_dump(filepath, data):
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)


file_path = "DataSet/Milestone1/Milestone1A.yaml"
data = yaml_loader(file_path)
print(data['M1A_Workflow'].items())
for i in data['M1A_Workflow'].items():
    if i[0] == 'Activities':
        for ta in data['M1A_Workflow'][i[0]].items():
            if ta[1]['Type'] == 'Task':
                print(ta[0],end=" ")
                print('entered')
