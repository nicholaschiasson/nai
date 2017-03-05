import abc

class AISearchProblem:
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def __eq__(self, other):
        return
    @abc.abstractmethod
    def __hash__(self):
        return
    @abc.abstractmethod
    def __ne__(self, other):
        return
    @abc.abstractmethod
    def get_adjacent_states(self):
        return
    @abc.abstractmethod
    def get_goal(self):
        return
    @abc.abstractmethod
    def get_transition_cost(self, other):
        return
