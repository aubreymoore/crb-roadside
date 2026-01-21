# crb-roadside

This repository contains a python package for analysing images from roadside surveys of coconut rhinoceros beetle damage.

[documentation](https://aubreymoore.github.io/crb-roadside/docs/build/html/crb_roadside.html#module-crb_roadside.html)

## Installation

If you are using `uv` for your Python project, you can add this package directly from GitHub:

```bash
uv add git+https://github.com/aubreymoore/crb-roadside.git
```

To update the package to the latest version on the main branch:
```bash
uv add --upgrade git+https://github.com/aubreymoore/crb-roadside.git
```

If you are using `pip`:

```bash
pip install git+https://github.com/aubreymoore/crb-roadside.git
```

## Usage example
```python
import crb_roadside as crb

# initialize model if it does not already exist
try:
    model
except NameError:
    model = crb.initialize_model()

# detect coconut palm trees in a specified image
image_path = “/home/aubrey/Desktop/Efate2025/original_images/20251129_152106.jpg” 
results = crb.find_trees(image_path)
```

