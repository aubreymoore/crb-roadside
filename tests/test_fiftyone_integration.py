import crb_roadside as crb

# detect trees in an image
image_path = "20251129_152106.jpg"
model = crb.initialize_model()
results = crb.find_trees(
    model=model, 
    image_path=image_path)
print(f'{len(results[0].boxes)} coconut palm trees detected')

# create a persistent FiftyOne dataset
dataset_name = 'test_dataset'
datasets = crb.list_51_datasets()
if dataset_name in datasets:
    crb.delete_51_dataset(dataset_name)
dataset = crb.create_51_dataset(dataset_name)

# add instances to the dataset
crb.add_instances_to_51_dataset(results[0], dataset)
print(dataset)

# visualize the dataset in the FiftyOne app
session = crb.visualize_51_dataset(dataset_name)