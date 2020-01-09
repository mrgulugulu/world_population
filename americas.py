import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])#将这些国家放在一组以表突出
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
        'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
'''颜色是按顺序系统自动填充的;传列表的话就是将国家归类'''

wm.render_to_file('americas.svg')
