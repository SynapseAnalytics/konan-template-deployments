## **/scripts** folder
Add your scripts needed by your src code at runtime in this directory.

You can access the path to this folder in your code using the `konan_sdk.konan_service.constants.SCRIPTS_DIR` constant.
For example, in `python`, it can be accessed by 
```python
from konan_sdk.konan_service import constants as Konan_Constants
scripts_folder_path = Konan_Constants.SCRIPTS_DIR
```
