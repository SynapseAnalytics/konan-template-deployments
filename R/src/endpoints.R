# Replace this with your required libraries
library(xgboost)

# Helper functions for your webserver
missing_params <- function(message = "Missing required parameters.") {
  api_error(message = message, status = 400)
}

invalid_range <- function(parameter) {
  message = paste0(parameter, ' is not within the allowed range.')
  api_error(message = message, status = 400)
}

api_error <- function(message, status) {
  err <- structure(
    list(message = message, status = status),
    class = c("api_error", "error", "condition")
  )
  signalCondition(err)
}

between <- function(value, min, max){
  return((value >= min) & (value <= max))
}

# Function that checks if all required parameters are present
check_required_parameters <- function(provided_args, required_parameters){
  if (all(required_parameters %in% provided_args) == FALSE) {
    missing_params("Missing required parameters.")
  }
}

# Function that checks if all parameters are within the allowed range
check_parameter_ranges <- function(input_df){
  # Replace the logic of this function with your actual input validation
  feat_1_int_range <- c(1,5)
  feat_2_int_range <- c(10,15)
  feat_1_char_values <- c('Blue',
                          'Red',
                          'Green')
  feat_2_char_values <- c('Blue',
                          'Red',
                          'Green')
  if(!(input_df$feat_1_int %>% between(feat_1_int_range[1], feat_1_int_range[2]))) invalid_range('feat_1_int')
  if(('feat_2_int' %in% names(input_df)))
    {if(!(input_df$feat_2_int %>% between(feat_2_int_range[1], feat_2_int_range[2]))) invalid_range('feat_2_int')}
  if(!(input_df$feat_1_char %in% feat_1_char_values)) invalid_range('feat_1_char')
  if(('feat_2_char' %in% names(input_df)))
    {if(!(input_df$feat_2_char %in% feat_1_char_values)) invalid_range('feat_2_char')}

}

# Replace these comments with ones applicable to your predict function
#* Return a prediction using two reqired and two optional parameters
#* @param feat_1_int:df Required, numeric argument, must be in [1,5]
#* @param feat_2_int:df Optional, numeric argument, must be in [10,15]
#* @param feat_1_char:df Required categorical variable, must be one of ['Blue', 'Red', 'Green']
#* @param feat_2_char:df Optional categorical variable, must be one of ['Blue', 'Red', 'Green']
#* @post /predict
function(req, feat_1_int, feat_2_int = NULL, feat_1_char, feat_2_char = NULL) {

  required_parameters <- c('feat_1_int', 'feat_1_char')
  body <- jsonlite::fromJSON(req$postBody)
  json_input <- body
  input_df <- json_input %>% as.data.frame

  check_required_parameters(names(input_df), required_parameters)
  check_parameter_ranges(input_df)

  # These lines assume you placed your models in the models/ folder
  if(input_df$feat_1_char == 'Green') model_rds_path <-  paste(Sys.getenv("KONAN_SERVICE_MODELS_DIR"), "green_model.rds", sep="/")
  if(input_df$feat_1_char == 'Red') model_rds_path <-  paste(Sys.getenv("KONAN_SERVICE_MODELS_DIR"), "red_model.rds", sep="/")
  if(input_df$feat_1_char == 'Blue') model_rds_path <-  paste(Sys.getenv("KONAN_SERVICE_MODELS_DIR"), "blue_model.rds", sep="/")

  model <- readRDS(model_rds_path)
  model_input <- input_df %>% select(feat_1_int, feat_2_int) %>% as.matrix()
  prediction <- predict(model, model_input)

  return(list(y = prediction))
}