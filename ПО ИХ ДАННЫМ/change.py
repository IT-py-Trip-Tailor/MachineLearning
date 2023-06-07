import pandas as pd

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

json_data = []

# Преобразование каждого JSON объекта в плоский словарь и преобразование списка словарей в DataFrame
flat_json = [flatten_json(item) for item in json_data]
df = pd.DataFrame(flat_json)

# Сохранение DataFrame в CSV файл
df.to_csv('tour_data.csv', index=False)
