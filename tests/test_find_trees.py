import crb_roadside as crb
from pathlib import Path

def test_find_trees(tmp_path, monkeypatch):
    """
    Docstring for test_change_cwd_to_tmp
    
    :param tmp_path: Description
    :type tmp_path: Path
    :param monkeypatch: Description
    :type monkeypatch: MonkeyPatch
    
    To see the print statements and other messages run pytest with the -s option.
    for example: "uv run pytest -s"
    
    This test will be run using a temporary wotking directory which will be permanently
    delete on the next system reboot. After the test completes, monkeypatch automatically 
    restores the original CWD
    """
    
    # Change the current working directory to the tmp_path provided by pytest
    print(f'tmp_path is {tmp_path} which will be permanently deleted on the next system boot.')
    monkeypatch.chdir(tmp_path)
    current_dir = Path.cwd()
    assert current_dir == tmp_path
    
    # Now, any operations that rely on the current working directory will use tmp_path

    # test initialize_model()
    print('testing initialize_model(). This will take several minutes to complete.')
    model = crb.initialize_model()
    assert (tmp_path / "yoloe-11l-seg.pt").exists()
    assert (tmp_path / "mobileclip_blt.ts").exists()
    
    # test find_trees()
    # results = crb.find_trees(image_path='')
   

# def test_initialize_model(tmp_path):
#     with chdir(tmp_path):
#         crb.initialize_model()
        
    
    


# def test_find_trees(
#    import crb_roadside as crb
        
#         model = crb.initialize_model()
#         image_path = "/home/aubrey/Desktop/Efate2025/original_images/20251129_152106.jpg"        
#         results = crb.find_trees(image_path)
    