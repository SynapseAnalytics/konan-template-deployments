## **/src** folder
Add your src code in this directory.

In particular, these files should include:
1. the webserver file
2. the retraining file

You can access the path to this folder in your code using the `konan_sdk.konan_service.constants.SRC_DIR` constant.
For example, in `python`, it can be accessed by 
```python
from konan_sdk.konan_service import constants as Konan_Constants
src_folder_path = Konan_Constants.SRC_DIR
```
