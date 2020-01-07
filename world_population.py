import json

from country_codes import get_country_code

#将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)#读取内容并存在pop_data中

#打印每个国家2010年的人口数量
for i in pop_data:
    if i['Year'] == '2010':
        country_name = i['Country Name']#类似字典的引用
        population = int(float(i['Value']))
        code = get_country_code(country_name)
        if code :
            print(code + ': ' + str(population))
        else:
            print('ERROR - ' + country_name)
