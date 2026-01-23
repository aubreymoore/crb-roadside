import fiftyone as fo
import fiftyone.utils.ultralytics as fou

def list_51_datasets():
    """
    Docstring for list_51_datasets
    """
    try:
        datasets = fo.list_datasets()
    except:
        datasets = fo.list_datasets()
    return datasets
    
    
def create_51_dataset(result, dataset_name):
    """
    Docstring for create_51_dataset

    :param result: Description
    """
    datasets = list_51_datasets()
    if dataset_name in datasets:
        dataset = fo.delete_dataset(dataset_name)
                      
    dataset = fo.Dataset(dataset_name)

    # detections (boxes only)
    # sample["detections"] = fou.to_detections(result)
    # dataset.add_sample(sample)

    # instances (boxes + masks)
    sample = fo.Sample(filepath=result["path"])    
    sample["instances"] = fou.to_instances(result)
    dataset.add_sample(sample)
    