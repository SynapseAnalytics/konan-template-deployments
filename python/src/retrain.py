# This retraining code will be invoked by the command in the `retrain.sh` file

import json

RETRAINING_DIR_PATH = "/retraining"
METRICS_FILE_PATH = f"{RETRAINING_DIR_PATH}/metrics.json"
ARTIFACTS_DIR_PATH = f"{RETRAINING_DIR_PATH}/artifacts"
DATA_DIR_PATH = f"{RETRAINING_DIR_PATH}/data"
TRAINING_DATA_FILE_PATH = f"{DATA_DIR_PATH}/training.csv"
SERVING_DATA_FILE_PATH = f"{DATA_DIR_PATH}/serving.csv"

# TODO: [1] retrain your model and generate the new weights
new_weights = "Amazing new weights"  # replace this with your newly retrained weights
weights_file_name = "weights.txt"  # This must EXACTLY match the name of the current weights file
with open(f"{ARTIFACTS_DIR_PATH}/{weights_file_name}", "w") as file:
    file.write(new_weights)

# NOTE: you can repeat step [1] as many times as you want, particularly if you have multiple weights files
# NOTE: obviously, you will need to supply different weights_file_name(s)

# TODO: [2] write your retraining metrics dictionary
retraining_metrics = {
    'split': {
        'train': 0.8,
        'test': 0.2,
    },
    'evaluation': {
        'train': [
            {
                'metric_name': 'accuracy',
                'metric_value': 0.93,
            },
        ],
        'test': [
            {
                'metric_name': 'accuracy',
                'metric_value': 0.89,
            },
        ],
    },
}
with open(METRICS_FILE_PATH, 'w') as file:
    json.dump(retraining_metrics, file)
