# AoU EHR Submission Validator

Validate submissions for the FTD omop data 

## Local Development 

### Requirements 

 * Python >=3.9 (download from [here](https://www.python.org/downloads/) and install)
 * pip (download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and run `python get-pip.py`)

### Installation / Configuration

 * Install requirements by running
 
        pip install -r requirements.txt
 
### Running
 * Update `_settings.py` and rename it to `settings.py`
 * Create a folder and place all the EHR submission files to be validated into it
 * Set the "csv_dir" parameter in `settings.py` to the full path of the folder created above
 * Ensure the resources folder is also downloaded and is located in the same place as `omop_file_validator.py`
 * Execute the following at the command line:

```bash
python omop_file_validator.py [-h] [-r RESTRICT] [-c CSV_DIR]

Evaluate OMOP files for formatting issues before AoU submission.

optional arguments:
  -h, --help            show this help message and exit
  -r RESTRICT, --restrict RESTRICT
                        Number of rows to restrict for validation per file. e.g. --restrict 1000 for only validating
                        the first 1000 lines
  -c CSV_DIR, --restrict CSV_DIR
                        Relative filepath to the stored data to be validated e.g. --csv_dir uploads/omop_test
                        Relative to the root dir e.g. If your data is in this dir `ftd-omop-validator/src/ftd_omop_validator/data/input`. -c would be `src/ftd_omop_validator/data/input'.
```
## Validation logic
 * File names must follow naming convention `{table}.csv`
     * `table` an OMOP CDM table listed in [resources/omop](resources/omop)
 * Files must be in CSV format (comma-delimited) as specified by [rfc4180](https://tools.ietf.org/html/rfc4180)
 * Column names and types must follow the conventions in [resources/omop](resources/omop)


## Terra Development
 1. Use the most recent custom environment when creating the Terra env.
  -  [DockerHub link](https://hub.docker.com/repository/docker/gutman16/ftd_terra_python/tags)
  -  A longer creation time may be needed. Expectation <20 minutes.
 2. Use the pre-built notebook in `resources/omop_validation.ipynb`