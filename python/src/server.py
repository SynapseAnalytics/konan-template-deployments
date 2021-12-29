from konan_sdk.konan_service.services import KonanService
from konan_sdk.konan_service.models import KonanServiceBaseModel
from konan_sdk.konan_service.serializers import (
    KonanServiceBasePredictionRequest, KonanServiceBasePredictionResponse,
    KonanServiceBaseEvaluateRequest, KonanServiceEvaluateResponse,
    )


class MyPredictionRequest(KonanServiceBasePredictionRequest):
    """Defines the schema of a prediction request

    Follow the convention of <field_name>: <type_hint>
    Check https://pydantic-docs.helpmanual.io/usage/models/ for more info

    Optionally add validators for your features
    Follow the pydantic convention
    Check https://pydantic-docs.helpmanual.io/usage/validators/ for more info
    """
    # TODO: [1] Define your request schema
    pass


class MyPredictionResponse(KonanServiceBasePredictionResponse):
    """Defines the schema of a prediction response

    Follow the convention of <field_name>: <type_hint>
    Check https://pydantic-docs.helpmanual.io/usage/models/ for more info

    Optionally add validators for your features
    Follow the pydantic convention
    Check https://pydantic-docs.helpmanual.io/usage/validators/ for more info
    """
    # TODO: [2] Define your response schema
    pass


class MyModel(KonanServiceBaseModel):
    def __init__(self):
        """Add logic to initialize your actual model here

        Maybe load weights, connect to a database, etc ..
        For example, the following code will load a model saved as a model.pickle file in the models/ directory
        import pickle
        from konan_sdk.konan_service import constants as Konan_Constants
        self.loaded_model = pickle.load(open(f"{Konan_Constants.MODELS_DIR}/model.pickle", 'rb'))
        """
        super().__init__()
        # TODO: [3] Initialize your model

    def predict(self, req: MyPredictionRequest) -> MyPredictionResponse:
        """Makes an intelligent prediction

        Args:
            req (MyPredictionRequest): raw request from API 

        Returns:
            MyPredictionResponse: this will be the response returned by the API
        """
        # TODO: [4] Implement your prediction logic
        # Optionally preprocess the request here
        prediction = "" # Use your logic to make a prediction
        # Optionally postprocess the prediction here
        return prediction

    def evaluate(self, req: KonanServiceBaseEvaluateRequest) -> KonanServiceEvaluateResponse:
        """Evaluates the model based on passed predictions and their ground truths

        Args:
            req (KonanServiceBaseEvaluateRequest): includes passed predictions and their ground truths

        Returns:
            KonanServiceEvaluateResponse: the evaluation(s) of the model based on some metrics
        """
        # TODO: [5] Implement your evaluation logic
        evaluation = "" # Use your logic to make an evaluation
        return evaluation


app = KonanService(MyPredictionRequest, MyPredictionResponse, MyModel)
