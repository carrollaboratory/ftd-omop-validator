import inspect
import os

base_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
resource_path = os.path.join(base_path, 'resources')
html_boilerplate = os.path.join(resource_path, 'html_boilerplate.txt')
test_path = os.path.join(base_path, 'tests')
test_resource_path = os.path.join(test_path, 'resources')
example_path = os.path.join(test_resource_path, 'examples_erroneous')
cdm_metadata_path_53 = os.path.join(resource_path, 'omop_53')
data_path = os.path.join(base_path, 'data')

