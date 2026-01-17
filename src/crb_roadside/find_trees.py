from ultralytics import YOLOE

def initialize_model():
    """ Initializes and returns the YOLOE model for coconut palm tree detection. """
    model = YOLOE("yoloe-11l-seg.pt") 
    names = ["coconut palm tree"] 
    model.set_classes(names, model.get_text_pe(names))
    return model

def find_trees(model, image_path:str):
    """ 
    Detects coconut palm trees in an image using YOLOE model.
    Annotated images and cropped detections in the automatically created 'annotated_images' directory.

    IMPORTANT NOTES: 
    
    Requires a GPU with at least 8GB of VRAM to run successfully.
    If you attempt to run it on a machine without a suitable GPU, it will likely fail with an out-of-memory error.
    
    When first executed, this script will download the YOLOE-11L-Seg model weights (~90MB) and mobileclip_blt.ts (~300MB)
    These files are too large for pushing to GitHub so they should be added to .gitignore
    
    Usage:
        import crb_roadside as crb
        
        model = crb.initialize_model()
        image_path = "/home/aubrey/Desktop/Efate2025/original_images/20251129_152106.jpg"        
        results = crb.find_trees(image_path)
    """

    results = model.predict(
        source=image_path, 
        imgsz=1920,
        conf=0.01, 
        save=True, 
        project='annotated_images', 
        name='', 
        exist_ok=True, 
        verbose=False, 
        stream=False,
        save_crop=True
    )
    return results
