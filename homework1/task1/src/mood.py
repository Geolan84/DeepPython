import time


class SomeModel:
    def predict(self, message: str) -> float:
        # Very long expensive operation.
        time.sleep(25)
        # The shorter - the better.
        return 1.0/len(message) if len(message) != 0 else 1.0


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    if message is None or len(message) == 0:
        raise ValueError("That was no valid string!")
    if model is None:
        raise ValueError("Incorrect instanse of model")
    if bad_thresholds == None or good_thresholds == None \
            or bad_thresholds > good_thresholds \
            or bad_thresholds < 0.0 or good_thresholds > 1.0:
        raise ValueError("Incorrect thresholds")

    prediction = model.predict(message)
    if prediction < bad_thresholds:
        return "неуд"
    elif prediction > good_thresholds:
        return "отл"
    else:
        return "норм"
