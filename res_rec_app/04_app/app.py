from flask import Flask, Response, request, jsonify, render_template

from flask_pymongo import PyMongo

import numpy as np
#MPLD3 lets us make an html of a matplotlib plot:
import matplotlib.pyplot as plt, mpld3
import seaborn as sns
import pandas as pd
#Mapping Specific imports:
# import json 
# import requests
# from shapely.geometry import shape, Point
# import folium


#This is supposed to help with crashing
import matplotlib
matplotlib.use('Agg')

#initialize the flask app

port = 27017
db_name = "myDatabase"

app = Flask('reporting_app')
app.config["MONGO_URI"] = f"mongodb://localhost:{port}/{db_name}"
mongo = PyMongo(app)



  


#### END MAPPING SETUP ####



### ROUTES / WEBPAGES ###

#First route: Hello world
#Returns a simple string
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("/index.html")


# #Route 4: show user a form
# @app.route("/form")
# def form():
#     return render_template("form.html")

# #route 5: accept form submission and handle it
# @app.route("/submit")
# def make_graph():
#     #load in form data from incoming request
#     user_input = request.args

#     x = user_input['x_var']
#     y = user_input['y_var']
#     #plot_hue = user_input['hue']
#     #plot_yr =user_input['year']


#     f = plt.figure()
#     sns.scatterplot(df[x].values, df[y].values) #hue=plot_hue
#     plt.xlabel(x)
#     plt.ylabel(y)
#     plt.title(x + ' vs '+ y)
#     #plt.show()

#     return render_template('results.html', graph=(mpld3.fig_to_html(f)))

# @app.route("/test")
# def test():
#     return render_template('test.html')

# @app.route("/graph")
# def graph():
#     #https://stackoverflow.com/questions/25728442/how-to-place-a-matplotlib-plot-into-an-html-container-using-mpld3-and-flask
#     #load in form data from incoming request
#     user_input = request.args

#     x = user_input['x_var']
#     y = user_input['y_var']
#     #plot_hue = user_input['hue']
#     #plot_yr =user_input['year']

#     x2 = user_input['x_var2']
#     y2 = user_input['y_var2']
#     #plot_hue2 = user_input['hue2']
#     #plot_yr2 =user_input['year2']

#     chorop_n = user_input['chorop_n']
#     #choro_w = user_input['chorop_w']

#     #First Graph:
#     f2 = plt.figure()
#     sns.scatterplot(df[x].values, df[y].values) #hue=plot_hue
#     plt.xlabel(x)
#     plt.ylabel(y)
#     plt.title(x + ' vs '+ y)
    
#     #Second Graph:
#     f3 = plt.figure()
#     sns.scatterplot(df[x2].values, df[y2].values) #hue=plot_hue
#     plt.xlabel(x2)
#     plt.ylabel(y2)
#     plt.title(x2 + ' vs '+ y2)

#     #Choropleth:
#     m = folium.Map(width = 750, height=750, location = [38.9, -77], zoom_start=10.0)
#     #Adding a neighborhood layer:
#     neighborhood_layer = folium.FeatureGroup(name='Neighborhoods', show=False, )
#     folium.GeoJson(neighbs_data).add_to(neighborhood_layer)
#     neighborhood_layer.add_to(m)
#     #Adding a ward layer:
#     ward_layer = folium.FeatureGroup(name='Wards', show=False)
#     folium.GeoJson(ward_data).add_to(ward_layer)
#     ward_layer.add_to(m)
#     school_layer = folium.FeatureGroup(name='Schools', show=False)
#     #Iterate through the schoo
#     for row in range(len(school_df)):
#         lat = school_df.iloc[row]['school_latitude']
#         long = school_df.iloc[row]['school_longitude']
#         label = school_df.iloc[row]['school_name']
#         folium.Marker(location = [lat, long], popup = label, tooltip=f'''
#         School Name: {label}  \n  
#         Neighborhood: {school_df.iloc[row]['neighborhood']} 
#         ''').add_to(school_layer)
#     school_layer.add_to(m)
#     folium.LayerControl().add_to(m)
#     #Display the map:
#     m.save('templates/map.html') 

#     #second Map:
#     #Defining our Map:
    
#     m2 = folium.Map(width = 750, height=750, location = [38.9, -77], zoom_start=10.5)
#     #Adding a neighborhood layer:
#     neighborhood_layer = folium.FeatureGroup(name='Neighborhoods', show=False, )
    
   
#     choro = folium.Choropleth(
#         geo_data = neighbs_url,
#         data = df,
#         columns = ['Neighborhood Cluster', chorop_n],
#         key_on='feature.properties.NAME',
#         fill_color='BuPu',
#         fill_opacity = .6,
#         legend_name = chorop_n,
#         name = chorop_n
#     )
#     choro.add_to(m2)
    

#     #Placeholder for ward choropleth
#     # folium.Choropleth(
#     #     geo_data = neighbs_url,
#     #     data = df,
#     #     columns = ['Neighborhood Cluster',var_2],
#     #     key_on='feature.properties.NAME',
#     #     fill_color='YlGnBu',
#     #     fill_opacity = .6,
#     #     name = var_2
#     # ).add_to(m2)
#     #school_layer = folium.FeatureGroup(name='Schools', show=False)
#     school_layer = folium.FeatureGroup(name='Schools', show=False)
#     for row in range(len(school_df)):
#         lat = school_df.iloc[row]['school_latitude']
#         long = school_df.iloc[row]['school_longitude']
#         label = school_df.iloc[row]['school_name']
#         folium.Marker(location = [lat, long], popup = label, tooltip=f'''
#         School Name: {label}  \n  
#         Neighborhood: {school_df.iloc[row]['neighborhood']} 
#         ''').add_to(school_layer)
#     school_layer.add_to(m2)
#     folium.LayerControl().add_to(m2)
#     #Save the map:
#     m2.save('templates/map2.html')

#     return render_template('test.html', graph=(mpld3.fig_to_html(f2)), graph2=(mpld3.fig_to_html(f3)), graph_title=chorop_n)


if __name__=="__main__":
    app.run(debug=True)
