## **/models** folder
Add your model files needed by your src code at runtime in this directory.

You can access the path to this folder in your code using the `konan_sdk.konan_service.constants.MODELS_DIR` constant.
For example, in `python`, it can be accessed by 
```python
from konan_sdk.konan_service import constants as Konan_Constants
models_folder_path = Konan_Constants.MODELS_DIR
```
