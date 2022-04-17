## **/src** folder
Add your src code in this directory.

In particular, these files should include:
1. the webserver file
2. the retraining file

You can access the path to this folder in your code using the environment variable `KONAN_SERVICE_SRC_DIR`.
For example, in `R`, it can be accessed by 
```R
src_folder_path <- Sys.getenv("KONAN_SERVICE_SRC_DIR")
```