# Post Documentation Process

In order to support backward compatibility of the documentation generation process, this additional step is needed to add refresh HTMLs for older released docs.
The issue persists across helm, provider, and regular airflow docs.

To generate these back referencing (refresh HTMLs), run the script in the following manner:
```commandline
python add-back-reference.py [airflow | providers | helm]
```

Before running the script, make sure to install requirements from `requirements.txt` file into
your virtual environment. For example by `pip install -r requirements.txt`.
