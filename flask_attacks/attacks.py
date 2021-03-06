import json
import pickle
import copy
import base64
import random
import cv2, base64
import PIL
import numpy 
import os

from filters import _to_cv_image, _cv_to_array, _cv_to_base64
from agv_model_loader import ModelLoader
from agv_optimizer import Individual 

def attack(in_img, model_path):

    # load the model and apply
    model = ModelLoader().load(model_path)
    in_img = _cv_to_array(in_img)
    mod_img_np = model.apply(in_img)

    # return modified np image and its base64 encoding
    return (mod_img_np, _cv_to_base64(_to_cv_image(mod_img_np)))

def custom_attack(in_img, model):
    jdata = {
        "filters": [],
        "params": [],
        "fitness": [
            0.32999999999999996,
            0.5519230678677559
        ],
        "Attack rate": 0.65,
        "norm inf": 0.5525378511846065,
        "norm 2": 9.954765423892086,
        "norm 1": 429.4292598032579,
        "norm 0": 1.0,
        "feature squeezing": 0.01,
        "feature squeezing on success attacks": 0.01,
        "feature squeezing with rispet to success attack": 0.015384615384615385,
        "neural_network_model": "densenet",
        "in_params": {
            "dataset": "CIFAR-10-SUBSET-200-DENSENET",
            "logs": "instagram_Tournament_pareto_norminf_cifar_200_densenet.txt",
            "input": "None",
            "test": "True",
            "save_adv_ex": "300",
            "show_info": "True",
            "number_of_filters": "5",
            "population_size": "10",
            "batch_size": "100",
            "epochs": "3",
            "params_optimizer": "random",
            "params_strategy": "tournament",
            "params_pool": "offsprings|parents",
            "selection": "pareto",
            "elitims": "True",
            "distance_function": "norm_inf",
            "gen_population": "None",
            "output": "instagram_Tournament_pareto_norminf_cifar_200_densenet.json"
        },
        "filters_data": "gANdcQAoY2Fndl9maWx0ZXJzCkltYWdlRmlsdGVyCnEBKYFxAn1xAyhYBAAAAG5hbWVxBFgJAAAAY2xhcmVuZG9ucQVYBwAAAGRvbWFpbnNxBl1xByhjYWd2X2ZpbHRlcnMKUGFyYW1ldGVyRG9tYWluCnEIKYFxCX1xCihoBFgJAAAAaW50ZW5zaXR5cQtYBQAAAHB0eXBlcQxjYWd2X2ZpbHRlcnMKUGFyYW1ldGVyVHlwZQpxDSmBcQ59cQ8oaAxjYnVpbHRpbnMKZmxvYXQKcRBYDQAAAGlzX2NsYXNzX3R5cGVxEYl1YlgGAAAAZG9tYWlucRJdcRMoRz+5mZmZmZmaRz/wAAAAAAAAZVgFAAAAdmFsdWVxFEc/8AAAAAAAAHViaAgpgXEVfXEWKGgEWAUAAABhbHBoYXEXaAxoDSmBcRh9cRkoaAxoEGgRiXViaBJdcRooRz/pmZmZmZmaRz/0zMzMzMzNZWgURz/wAAAAAAAAdWJlWAMAAABmdW5xG2NmaWx0ZXJzCmNsYXJlbmRvbgpxHHViaAEpgXEdfXEeKGgEWAcAAABnaW5naGFtcR9oBl1xIChoCCmBcSF9cSIoaARoC2gMaA0pgXEjfXEkKGgMaBBoEYl1YmgSXXElKEc/uZmZmZmZmkc/8AAAAAAAAGVoFEc/8AAAAAAAAHViaAgpgXEmfXEnKGgEaBdoDGgNKYFxKH1xKShoDGgQaBGJdWJoEl1xKihHP+mZmZmZmZpHP/TMzMzMzM1laBRHP/AAAAAAAAB1YmVoG2NmaWx0ZXJzCmdpbmdoYW0KcSt1YmgBKYFxLH1xLShoBFgEAAAAanVub3EuaAZdcS8oaAgpgXEwfXExKGgEaAtoDGgNKYFxMn1xMyhoDGgQaBGJdWJoEl1xNChHP7mZmZmZmZpHP/AAAAAAAABlaBRHP/AAAAAAAAB1YmgIKYFxNX1xNihoBGgXaAxoDSmBcTd9cTgoaAxoEGgRiXViaBJdcTkoRz/gAAAAAAAARz/4AAAAAAAAZWgURz/wAAAAAAAAdWJlaBtjZmlsdGVycwpqdW5vCnE6dWJoASmBcTt9cTwoaARYBQAAAHJleWVzcT1oBl1xPihoCCmBcT99cUAoaARoC2gMaA0pgXFBfXFCKGgMaBBoEYl1YmgSXXFDKEc/uZmZmZmZmkc/8AAAAAAAAGVoFEc/8AAAAAAAAHViaAgpgXFEfXFFKGgEaBdoDGgNKYFxRn1xRyhoDGgQaBGJdWJoEl1xSChHP+mZmZmZmZpHP/GZmZmZmZplaBRHP/AAAAAAAAB1YmVoG2NmaWx0ZXJzCnJleWVzCnFJdWJoASmBcUp9cUsoaARYBAAAAGxhcmtxTGgGXXFNKGgIKYFxTn1xTyhoBGgLaAxoDSmBcVB9cVEoaAxoEGgRiXViaBJdcVIoRz+5mZmZmZmaRz/wAAAAAAAAZWgURz/wAAAAAAAAdWJoCCmBcVN9cVQoaARoF2gMaA0pgXFVfXFWKGgMaBBoEYl1YmgSXXFXKEc/7MzMzMzMzUc/8ZmZmZmZmmVoFEc/8AAAAAAAAHViZWgbY2ZpbHRlcnMKbGFya19oc3YKcVh1YmUu"
    }

    for i in range(len(model['filters'])):
        jdata['filters'].append(int(model['filters'][i]['type']))
        jdata['params'].append(float(model['filters'][i]['intensity']))
        jdata['params'].append(float(model['filters'][i]['alpha']))

    model = ModelLoader().load(jdata)
    in_img = _cv_to_array(in_img)
    mod_img_np = model.apply(in_img)

    # return modified np image and its base64 encoding
    return (mod_img_np, _cv_to_base64(_to_cv_image(mod_img_np)))

    
if __name__ == "__main__":
    pass