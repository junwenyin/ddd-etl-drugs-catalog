etl-drugs-catalog
==============================

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── staging        <- Intermediate data that has been transformed.
    │   ├── output         <- The final, canonical data sets for modeling.
    │   └── input          <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        ├── main.py        <- Any external connection (via API for example) should be written here    
        │
        └── application    <- Core of the business logic.
        └── domain         <- Entity of the process.
        └── infrastructure <- All the config and connections to the outside.
--------

#### Running the pipeline locally:
* Install the requirements:

```
pip install -r requirements.txt
```

* Run the pipeline:

```
python src/main.py -d 2021-01-01 -s all
```
### Run pytest locally:

We use `pytest`. command line:
pip install -e .
`python -m pytest tests`

### Build and push image:
chmod +x build_image.sh
./build_image.sh
