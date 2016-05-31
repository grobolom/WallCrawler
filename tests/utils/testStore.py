import unittest

from app.utils import Store

class MockReducer:
    def reduce(self, state, action):
        return []

class TestStore(unittest.TestCase):
    def test_it_should_get_an_initial_state(self):
        initialState = { 'something': 'else' }
        s = Store([], initialState)
        assert s.getState() == initialState

    def test_it_should_dispatch_actions(self):
        reducers = [ MockReducer() ]
        s = Store(reducers, { 'something': 'else' })
        s.dispatch({})
        assert s.getState() == []

    def test_it_should_not_shallow_copy_state(self):
        reducers = [ MockReducer() ]
        state = { 'something': ['deeper'] }
        s = Store(reducers, state)
        s.dispatch({})
        assert s.getState() != state
