## **/src** folder
Add your src code in this directory.

In particular, your main file that includes your webserver should be created here.

You can access the path to this folder in your code using the environment variable `KONAN_SERVICE_SRC_DIR`.
For example, in `R`, it can be accessed by 
```R
src_folder_path <- Sys.getenv("KONAN_SERVICE_SRC_DIR")
```