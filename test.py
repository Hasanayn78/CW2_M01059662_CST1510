from APP.datasets import get_all_datasets_metadata
from APP.db import conn



print(get_all_datasets_metadata(conn))
