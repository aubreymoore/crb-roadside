import exif
import pandas as pd
import sqlite3

def update_images_table(image_path, db_path):
    """ 
    Gets image data from embedded EXIF metadata and saves it in a SQLite database.
    """

    with open(image_path, 'rb') as f:
        imgx = exif.Image(f)
        
    if imgx.has_exif:
                
        # to see all available exif_data  use imgx.get_all()
        
        exif_data = {
            'image_path': image_path,
            'image_width': imgx.image_width,
            'image_height': imgx.image_height,
            'timestamp': imgx.datetime
        }

        d, m, s = imgx.gps_latitude
        latitude = d + m/60 + s/3600   
        if imgx.gps_latitude_ref == 'S':
            latitude = -latitude  
        exif_data['latitude']  = latitude   

        d, m, s = imgx.gps_longitude
        longitude = d + m/60 + s/3600   
        if imgx.gps_longitude_ref == 'W':
            longitude = -longitude
        exif_data['longitude'] = longitude
    else:
        exif_data = {
            'image_path': image_path,
            'image_width': null,
            'image_height': null,
            'timestamp': null,
            'latitude': null,
            'longitude': null
        }
    df_image = pd.DataFrame([exif_data])
    
    # Connect to the SQLite database (creates if it doesn't exist)
    conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()
    df_image.to_sql(name='images', con=conn, if_exists='append', index=False)
    conn.close()


def update_detections_table(results, image_path, db_path):
    
    # Process detection results (assuming one image for simplicity: results[0])
    result = results[0]

    # --- Extract Bounding Box Data into a DataFrame ---
    # The .boxes.data attribute is a tensor containing [x_min, y_min, x_max, y_max, confidence, class]
    boxes_data = result.boxes.data.tolist()
    df_boxes = pd.DataFrame(boxes_data, columns=['x_min', 'y_min', 'x_max', 'y_max', 'confidence', 'class_id'])

    # Add class names for readability
    # class_names = model.names
    # df_boxes['class_name'] = df_boxes['class_id'].apply(lambda x: class_names[int(x)])

    # --- Extract Segmentation Mask Data ---
    # Masks are more complex as they represent pixel-wise information or polygon points.
    # To put this into a DataFrame, you could store the polygon points list for each object.
    masks_data = []
    # Iterate over each detected object's mask
    for i, mask in enumerate(result.masks.xy):
        # mask.xy contains the polygon points as a list of [x, y] coordinates
        # You can associate this with the corresponding entry in the bounding box DataFrame
        polygon_points = mask.tolist()
        polygon_points_str = ','.join(str(x) for x in polygon_points)
        masks_data.append({
            'image_path': image_path,
            'object_index': i, 
            'class_id': df_boxes.iloc[i]['class_id'], 
            'polygon_points_str': polygon_points_str})
        df_masks = pd.DataFrame(masks_data)  
        
    # merge df_masks and df_detections  
    df_detections = pd.merge(df_masks, df_boxes, how="outer", left_index=True, right_index=True)
    
    # Connect to the SQLite database (creates if it doesn't exist)
    conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()
    df_detections.to_sql(name='detections', con=conn, if_exists='append', index=False)
    conn.close()


        
    

