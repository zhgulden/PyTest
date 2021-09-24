import pytest

@pytest.mark.parametrize("test_input, expected", [({1, 2, 3}, 3), ({4, 3, 2}, 4), ({5, 5, 0}, 5)])
def test_max_in_set(test_input, expected):
	assert max(test_input) == expected

def test_set_subset():
	a_set = {'Gulden', 'Zhanmukanbetova'}
	b_set = {'Zhanmukanbetova', 'Gulden', 'Maratovna'}
	assert a_set.issubset(b_set)

def test_set_remove():
	a_set, element = set(), 1
	try:
		assert a_set.remove(element)
	except KeyError:
		pass

@pytest.mark.parametrize("test_input, expected", [(4, 1), (-3, 0), (43, 1)])
def test_int_positive(test_input, expected):
	assert (test_input > 0) == expected

def test_int_power():
	num, arg = 0, 0
	try:
		assert pow(num, arg)
	except ZeroPowerError:
		pass

def test_int_xor():
	num_1, num_2 = 5, 7
	assert num_1 ^ num_2 == 2