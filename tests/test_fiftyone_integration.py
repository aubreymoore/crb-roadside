import crb_roadside as crb

def test_fiftyone_integration():
    """
    Test the FiftyOne integration functions in crb_roadside.
    This test will initialize the model, detect trees in a test image,
    create a FiftyOne dataset, add instances to it, and visualize it.
    """
    
    # detect trees in an image
    print("Testing tree detection and FiftyOne integration...")
    image_path = 'data/20251129_152106.jpg'
    model = crb.initialize_model()
    results = crb.find_trees(model, image_path)
    assert len(results) == 1
    assert len(results[0].boxes) > 0
    
    # create a persistent FiftyOne dataset
    
    dataset_name = 'test_dataset'
    datasets = crb.list_51_datasets()
    if dataset_name in datasets:
        print(f"Deleting existing dataset: {dataset_name}")
        crb.delete_51_dataset(dataset_name)
    print(f"Creating new dataset: {dataset_name}")
    dataset = crb.create_51_dataset(dataset_name)
    print(dataset)
    assert dataset.name == dataset_name
    
    # add instances to the dataset
    print("Adding instances to the FiftyOne dataset...")
    crb.add_instances_to_51_dataset(results[0], dataset)
    assert len(dataset) > 0
    
    # visualize the dataset in the FiftyOne app
    print("Visualizing the FiftyOne dataset...")
    session = crb.visualize_51_dataset(dataset_name)
    assert session is not None
    print("FiftyOne integration test completed successfully.")