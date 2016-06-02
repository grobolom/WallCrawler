from app.utils import VectorHandler

class TestVectorHandler:
    def test_it_should_swap_a_positive_and_negative_vector_to_positive(self):
        v1 = [5, 5]
        v2 = [-3, -3]

        first, second = VectorHandler().getPositiveVectors(v1, v2)

        assert first == [2, 2]
        assert second == [3, 3]
