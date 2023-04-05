"""Module with model to predict quality of words."""
import time


class SomeModel:
    """Model's class to predict quality of words."""

    def predict(self, message: str) -> float:
        """Predicts probability of quality for word."""
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
    """According to the forecast of the model, it determines the quality class of the word."""
    if message is None or len(message) == 0:
        raise ValueError("That was no valid string!")
    if model is None:
        raise ValueError("Incorrect instanse of model")
    if bad_thresholds is None or good_thresholds is None \
            or bad_thresholds > good_thresholds \
            or bad_thresholds < 0.0 or good_thresholds > 1.0:
        raise ValueError("Incorrect thresholds")

    prediction = model.predict(message)
    if prediction < bad_thresholds:
        return "неуд"
    if prediction > good_thresholds:
        return "отл"
    return "норм"
