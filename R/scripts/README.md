## **/scripts** folder
Add any extra scripts needed by your src code at runtime in this directory.

You can access the path to this folder in your code using the environment variable `KONAN_SERVICE_SCRIPTS_DIR`.
For example, in `R`, it can be accessed by 
```R
scripts_folder_path <- Sys.getenv("KONAN_SERVICE_SCRIPTS_DIR")
```