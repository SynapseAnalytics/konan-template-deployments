## **/artifacts** folder
Add your models artifact files needed by your src code at runtime in this directory. This may include the model's weight files or data that the model needs while running.

You can access the path to this folder in your code using the `konan_sdk.konan_service.constants.ARTIFACTS_DIR` constant.
For example, in `python`, it can be accessed by 
```python
from konan_sdk.konan_service import constants as Konan_Constants
models_artifacts_folder_path = Konan_Constants.ARTIFACTS_DIR
```
