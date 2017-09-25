
# coding: utf-8

# In[1]:


import folium
import MySQLdb
db = MySQLdb.connect("localhost","root","","folium" )
from folium.plugins import Draw, Fullscreen
cursor = db.cursor()
m = folium.Map(location=[-27.228989, -48.36525], zoom_start=12)

draw = Draw(export=True)

draw.add_to(m)

m


# In[1]:


import os
import geopandas


gpd = geopandas.read_file(
    os.path.join(os.path.expanduser('~'), 'data.geojson')
)

gpd['geometry'][0]
 try:
    cursor.execute("""INSERT INTO draw_data VALUES (%s)""",('geometry'][0]))
    db.commit()
 except:     
     db.rollback()
 

# In[2]:


gpd.__geo_interface__