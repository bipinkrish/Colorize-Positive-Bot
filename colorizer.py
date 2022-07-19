import torch
import warnings

from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import get_image_colorizer

def colorize(filename,output):
    torch.hub.set_dir('models')
    warnings.filterwarnings('ignore')
    torch.backends.cudnn.benchmark = True
    device.set(device=DeviceId.CPU) # GPU0
    colorizer = get_image_colorizer(artistic=False)
    colorizer.get_transformed_image(filename, render_factor=35, watermarked=False).save(output)
    
   