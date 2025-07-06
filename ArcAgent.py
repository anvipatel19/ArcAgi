import numpy as np

from ArcProblem import ArcProblem
from ArcData import ArcData
from ArcSet import ArcSet


class ArcAgent:
    def __init__(self):
        """
        You may add additional variables to this init. Be aware that it gets called only once
        and then the solve method will get called several times.
        """
        pass

    def make_predictions(self, arc_problem: ArcProblem) -> list[np.ndarray]:
        """
        Write the code in this method
        to solve the incoming ArcProblem.

        You can add up to THREE (3) the predictions to the
        predictions list provided below that you need to
        return at the end of this method.

        In the Autograder, the test data output in the arc problem will be set to None
        so your agent cannot peek at the answer.

        Also, you shouldn't add more than 3 predictions to the list as
        that is considered an ERROR and the test will be automatically
        marked as incorrect.
        """

        predictions: list[np.ndarray] = list()

        '''
        The next 2 lines are only an example of how to populate the predictions list.
        This will just be an empty answer the size of the input data;
        delete it before you start adding your own predictions.
        '''
        output = np.zeros_like(arc_problem.test_set().get_input_data().data())
        predictions.append(output)

        return predictions
