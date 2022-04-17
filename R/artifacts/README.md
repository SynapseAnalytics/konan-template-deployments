## **/artifacts** folder
Add your models artifact files needed by your src code at runtime in this directory. This may include the model's weight files or data that the model needs while running.

You can access the path to this folder in your code using the environment variable `KONAN_SERVICE_ARTIFACTS_DIR`.
For example, in `R`, it can be accessed by 
```R
models_artifacts_folder_path <- Sys.getenv("KONAN_SERVICE_ARTIFACTS_DIR")
```