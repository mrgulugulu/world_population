import json
import pygal_maps_world.maps
from pygal.style import RotateStyle

from country_codes import get_country_code

#将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)#读取内容并存在pop_data中

#创建一个包含人口数量的字典
cc_populations = {}#字典用来表示人口，列表就是分类
for i in pop_data:
    if i['Year'] == '2010':
        country_name = i['Country Name']#类似字典的引用
        population = int(float(i['Value']))
        code = get_country_code(country_name)
        if code :
            cc_populations[code] = population

#根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():#遍历整个字典，将国家分类
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#446699')#返回了一个样式
wm = pygal_maps_world.maps.World(style=wm_style)

#看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
