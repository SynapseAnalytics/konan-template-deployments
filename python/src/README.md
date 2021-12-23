## **/src** folder
Add your src code in this directory.

In particular, your main file that includes your webserver should be created here.

You can access the path to this folder in your code using the `konan_sdk.konan_service.constants.SRC_DIR` constant.
For example, in `python`, it can be accessed by 
```python
from konan_sdk.konan_service import constants as Konan_Constants
src_folder_path = Konan_Constants.SRC_DIR
```
