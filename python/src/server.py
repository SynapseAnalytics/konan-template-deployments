from typing import (
    Any,
    Dict,
    List,
)
import pydantic

from konan_sdk.konan_service.models import KonanServiceBaseModel
from konan_sdk.konan_service.services import KonanService
from konan_sdk.konan_service.serializers import (
    KonanServiceBasePredictionRequest, KonanServiceBasePredictionResponse,
    KonanServiceBaseEvaluateRequest, KonanServiceBaseEvaluateResponse,
    KonanServiceEvaluation,
    KonanServicePredefinedMetricName,
)


class MyPredictionRequest(KonanServiceBasePredictionRequest):
    """Defines the schema of a prediction request
    Follow the convention of <field_name>: <type_hint>
    Check https://pydantic-docs.helpmanual.io/usage/models/ for more info
    """
    # TODO: [1] Define your request schema
    # Uncomment what you need and adjust their names and types
    # Check https://pydantic-docs.helpmanual.io/usage/models/ for more data types
    # sample_str: str
    # sample_int: int
    pass


class MyPredictionResponse(KonanServiceBasePredictionResponse):
    """Defines the schema of a prediction response
    Follow the convention of <field_name>: <type_hint>
    Check https://pydantic-docs.helpmanual.io/usage/models/ for more info
    """
    # TODO: [2] Define your response schema
    # Uncomment what you need and adjust their names and types
    # Check https://pydantic-docs.helpmanual.io/usage/models/ for more data types

    # sample_int: int
    # sample_bool: bool
    # sample_float: float
    # sample_str: str
    # sample_list_of_ints: List[int]
    # sample_dict: Dict[str, Any]

    # If you want your fields to be nested objects themselves
    # class SampleObject(pydantic.BaseModel):
    #     sample_field_1: int
    #     sample_field_2: str
    # sample_object: SampleObject
    pass


class MyModel(KonanServiceBaseModel):
    def __init__(self):
        """Add logic to initialize your actual model here

        Maybe load weights, connect to a database, etc ..
        """
        super().__init__()
        # TODO: [3] Initialize your model
        # # For example, the following code will load a model saved as a model.pickle file in the models/ directory
        # import pickle
        # from konan_sdk.konan_service import constants as Konan_Constants
        # self.loaded_model = pickle.load(open(f"{Konan_Constants.MODELS_DIR}/model.pickle", 'rb'))

    def predict(self, req: MyPredictionRequest) -> MyPredictionResponse:
        """Makes an intelligent prediction

        Args:
            req (MyPredictionRequest): raw request from API

        Returns:
            MyPredictionResponse: this will be the response returned by the API
        """
        # TODO: [4] Implement your prediction logic
        # Optionally preprocess the request here

        # Use your logic to make a prediction
        # Create a MyPredictionResponse object using kwargs
        sample_prediction = MyPredictionResponse(
            # sample_int=42,
            # sample_bool=False,
            # sample_float=0.68,
            # sample_str="hello world",
            # sample_list_of_ints=[10, 2, 3],
            # sample_dict={
            #     'key_1': 'value_1',
            #     'key_2': 2,
            # },

            # sample_object=MyPredictionResponse.SampleObject(
            #     sample_field_1=1,
            #     sample_field_2='field_2',
            # ),
        )

        # Optionally postprocess the prediction here

        return sample_prediction

    def evaluate(self, req: KonanServiceBaseEvaluateRequest) -> KonanServiceBaseEvaluateResponse:
        """Evaluates the model based on passed predictions and their ground truths

        Args:
            req (KonanServiceBaseEvaluateRequest): includes passed predictions and their ground truths

        Returns:
            KonanServiceEvaluateResponse: the evaluation(s) of the model based on some metrics
        """
        # TODO: [5] Implement your evaluation logic
        # Use your logic to make an evaluation
        # Create a KonanServiceBaseEvaluateResponse object using kwargs
        sample_evaluation = KonanServiceBaseEvaluateResponse(
            # results should be a list of KonanServiceEvaluation objects
            # define each KonanServiceEvaluation object using kwargs
            results=[
                # KonanServiceEvaluation(
                #     metric_name=KonanServicePredefinedMetricName.precision,
                #     metric_value=0.95,
                # ),
                # KonanServiceEvaluation(
                #     metric_name="custom-metric",
                #     metric_value=0.7,
                # ),
            ],
        )
        return sample_evaluation


app = KonanService(MyPredictionRequest, MyPredictionResponse, MyModel)
