import os
from flask_wtf import FlaskForm
from wtforms import SelectField, FileField

# add newtork keys and values here
networks = [
    ('', "Select a Network"),
    ("VGG19","VGG19"),
    ("MobileNetV2","MobileNet"),
    ("DenseNet201","DenseNet201"),
    ("InceptionV3","InceptionV3"),
    ("ResNet50", "ResNet50")
]

images = [
    ('', "ImageNet Photos"),
    ('1', "1"),
    ('2', "2"),
    ('3', "3"),
]

class ModelForm(FlaskForm):
    custom_image = FileField( id='custom_image')
    imagenet_image = SelectField(id = 'image-select')
    network = SelectField(id = 'network', choices = networks)
    model = SelectField(id = 'model', choices = images)

