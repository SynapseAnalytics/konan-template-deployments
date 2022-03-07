## **/models** folder
Add your model files needed by your src code at runtime in this directory.

You can access the path to this folder in your code using the environment variable `KONAN_SERVICE_MODELS_DIR`.
For example, in `R`, it can be accessed by 
```R
models_folder_path <- Sys.getenv("KONAN_SERVICE_MODELS_DIR")
```