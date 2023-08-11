import json

from django.shortcuts import render

from Roads.models import *


def index(request):
    azs = TblAzs
    data = 'some data'
    return render(request, 'template.html', {'data': data})


def coordinates_view(request):
    azs_list = TblAzs.objects.all()
    azs_coordinates_data = []
    for azs in azs_list:
        inp_str = azs.coordinates[1:-1]
        x_str, y_str = inp_str.split(',')
        azs_coordinates_data.append({'id': azs.id, 'x': float(x_str), 'y': float(y_str), 'road_code': azs.road_code})
    roads_list = TblRoads.objects.all()
    road_coordinates_data = []
    road_id_data, road_code_data, road_length_data, road_data = [], [], [], []
    for road in roads_list:
        coordinate_str = road.coordinates
        coordinates_list = json.loads(coordinate_str)
        coordinate_dict_list = [{'x': coord[0], 'y': coord[1]} for coord in coordinates_list]
        road_coordinates_data.append(coordinate_dict_list)
        road_dict_list = {'id': road.id, 'road_code': road.road_code,
                          'road_length': float(road.length_km)}
        road_data.append(road_dict_list)

    context = {
        'azs_coordinates_data': azs_coordinates_data,
        'road_coordinates_data': road_coordinates_data,
        'road_data': road_data,
    }

    return render(request, 'coordinates_template.html', context)
