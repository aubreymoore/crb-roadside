import crb_roadside as crb
from pathlib import Path
import os

def test_find_trees(tmp_path, monkeypatch):
    """
    Docstring for test_change_cwd_to_tmp
    
    :param tmp_path: Description
    :type tmp_path: Path
    :param monkeypatch: Description
    :type monkeypatch: MonkeyPatch
    
    To see the print statements and other messages run pytest with the -s option.
    for example: "uv run pytest -s"
    
    This test will be run using a temporary working directory in /tmp which will be permanently
    deleted on the next system reboot. You can find the temporary directory in /tmp and inspect it
    to see results of this test.
    
    After the test completes, monkeypatch automatically 
    restores the original CWD
    """
    
    # get the absolute path of the test image
    image_path = os.path.abspath('data/20251129_152106.jpg')
    print(image_path)
    assert os.path.exists(image_path)
    
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
    results = crb.find_trees(model, image_path)
    assert len(results) == 1
    
    # test update_images_table()
    db_path = 'test.sqlite3'
    crb.update_images_table(image_path, db_path)
    assert (tmp_path / db_path).exists()
    
    # test update_detections_table()
    crb.update_detections_table(results, image_path, db_path)
 