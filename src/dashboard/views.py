from django.shortcuts import render
import folium
import ee           # earth engine api
from folium import plugins
from requests import request
from dashboard.models import showCal,Feedback
from newsapp.models import News
from django.contrib import messages
from .utils import get_plot


# Create your views here.

#Add custom basemaps to folium

basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    ),
    'Google Satellite': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Google Terrain': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Terrain',
        overlay = True,
        control = True
    ),
    'Google Satellite Hybrid': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Esri Satellite': folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = True,
        control = True
    )
}

def add_ee_layer(self, ee_object, vis_params, name):
    
    try:    
        # display ee.Image()
        if isinstance(ee_object, ee.image.Image):    
            map_id_dict = ee.Image(ee_object).getMapId(vis_params)
            folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = 'Google Earth Engine',
            name = name,
            overlay = True,
            control = True
            ).add_to(self)
        # display ee.ImageCollection()
        elif isinstance(ee_object, ee.imagecollection.ImageCollection):    
            ee_object_new = ee_object.mosaic()
            map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
            folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = 'Google Earth Engine',
            name = name,
            overlay = True,
            control = True
            ).add_to(self)
        # display ee.Geometry()
        elif isinstance(ee_object, ee.geometry.Geometry):    
            folium.GeoJson(
            data = ee_object.getInfo(),
            name = name,
            overlay = True,
            control = True
        ).add_to(self)
        # display ee.FeatureCollection()
        elif isinstance(ee_object, ee.featurecollection.FeatureCollection):  
            ee_object_new = ee.Image().paint(ee_object, 0, 2)
            map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
            folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = 'Google Earth Engine',
            name = name,
            overlay = True,
            control = True
        ).add_to(self)
    
    except:
        print("Could not display {}".format(name))

# Add EE drawing method to folium.
folium.Map.add_ee_layer = add_ee_layer









# Create your views here.
def index(request):
    # Set visualization parameters.
    vis_params = {
    'min': 0,
    'max': 4000,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}
    
    #creating map object
    m= folium.Map(location=[20.5937,78.9629],zoom_start=4)

    # Add custom basemaps
    basemaps['Google Maps'].add_to(m)
    basemaps['Google Terrain'].add_to(m)
    basemaps['Google Satellite Hybrid'].add_to(m)

    #basemaps['Esri Satellite'].add_to(m)

    # Add the elevation model to the map object.
    #dem = ee.Image('USGS/SRTMGL1_003')
    #m.add_ee_layer(dem.updateMask(dem.gt(0)), vis_params, 'DEM')

    # Add a layer control panel to the map.
    m.add_child(folium.LayerControl())

    # Add fullscreen button
    plugins.Fullscreen().add_to(m)
    #conversion in html
    m= m._repr_html_()
    
    #news renders
    first_news=News.objects.first()
    second_news=News.objects.order_by('image')[1]
    third_news=News.objects.order_by('image')[2]
    three_news=News.objects.all()[0:3]

    #AI renders
    #topfive=showCal.objects.all()
    state_id = request.POST.get("district")
    compare_data = showCal.objects.filter(state_no=state_id)
    x = [x.crop_name for x in compare_data]
    y = [y.yieldd for y in compare_data]
    chart =get_plot(x,y)
    
    

    context ={
        'm':m,
        #'topfive': topfive,
        'first_news':first_news,
        'second_news':second_news,
        'third_news' : third_news,
        'three_news':three_news,
        'state_id' : state_id,
        'compare_data' : compare_data,
        'chart' : chart,
        

    }
    return render(request, 'index.html',context)



def contact(request):
    # name = request.POST.get("name")
    # print(name)
    # email = request.POST.get("email")
    # subject = request.POST.get("subject")
    # message = request.POST.get("message")
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        #print(email)
        subject=request.POST['subject']
        message = request.POST['message']

        #print('hi')
        
        contact= Feedback.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request,'Feedback submitted!!!')
    return render(request, 'contact-us.html')









