# FUNCTIONS FOR FIFTYONE DATASET MANAGEMENT AND VISUALIZATION

import fiftyone as fo
import fiftyone.utils.ultralytics as fou
from fiftyone import ViewField as F

def list_51_datasets():
    """
    Returns a list of all FiftyOne datasets, with a retry on failure."""
    try:
        datasets = fo.list_datasets()
    except:
        print('First attempt to list datasets failed, trying again...')
        datasets = fo.list_datasets()
    return datasets


def create_51_dataset(dataset_name: str):
    """
    Creates and returns a new, persistent FiftyOne dataset with the provided dataset_name. 
    """
    return fo.Dataset(name=dataset_name, persistent=True, overwrite=True)


def delete_51_dataset(dataset_name):
    """
    Deletes a FiftyOne dataset which is identified by dataset_name.
    """
    fo.delete_dataset(dataset_name)
    
    
def add_instances_to_51_dataset(result, dataset):
    """
    Adds instances (boxes and masks) to a FiftyOne dataset

    :param result: a single result from results returned by crb.find_trees
    :param dataset_name: the name of the FiftyOne dataset to which to add the instances
    """
    # add instances (boxes + masks) to the dataset
    sample = fo.Sample(filepath=result.path)    
    sample["instances"] = fou.to_instances(result)
    dataset.add_sample(sample)
    return dataset


def create_instance_patches_view(dataset, min_conf=0.0):
    """
    Creates a view of patches for all prediction instances in a FiftyOne dataset, filtered and sorted sorted by confidence.
    """
    patches_view = (
        dataset
        .filter_labels(
            "instances",
            (F("confidence") > min_conf)  # adjust threshold as desired
        )
        .to_patches("instances")
        .sort_by("instances.confidence")
        )
    dataset.save_view("instance-patches-by-conf", patches_view)
    return patches_view

  
def visualize_51_dataset(dataset_name):
    """
    Launches the FiftyOne app to visualize the dataset identified by dataset_name.
    """
    dataset = fo.load_dataset(dataset_name)
    session = fo.launch_app(dataset)
    return session

# # Usage example:

# # detect trees in an image
# import find_trees
# image_path = "20251129_152106.jpg"
# model = find_trees.initialize_model()
# results = find_trees.find_trees(
#     model=model, 
#     image_path=image_path)
# print(f'{len(results[0].boxes)} coconut palm trees detected')

# # create a persistent FiftyOne dataset
# dataset_name = 'test_dataset'
# datasets = list_51_datasets()
# if dataset_name in datasets:
#     delete_51_dataset(dataset_name)
# dataset = create_51_dataset(dataset_name)

# # add instances to the dataset
# add_instances_to_51_dataset(results[0], dataset)
# print(dataset)

# # # visualize the dataset in the FiftyOne app
# # session = visualize_51_dataset(dataset_name)