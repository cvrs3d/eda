import pytest
from mean_var_std import calculate

# Test that ValueError is raised for invalid input
@pytest.mark.parametrize("bad_input", [
    [], [1,2,3], list(range(8)), list(range(10))
])
def test_invalid_input_raises(bad_input):
    with pytest.raises(ValueError) as exc:
        calculate(bad_input)
    assert str(exc.value) == "List must contain nine numbers."

# Test for correct outputs with a known 3×3 input
def test_calculations_on_0_to_8():
    data = list(range(9))
    result = calculate(data)

    expected = {
      'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
      'variance': [[6.0, 6.0, 6.0],
                   [0.6666666666666666]*3,
                   6.666666666666667],
      'standard deviation': [
           [2.449489742783178]*3,
           [0.816496580927726]*3,
           2.581988897471611
      ],
      'max': [[6,7,8],[2,5,8],8],
      'min': [[0,1,2],[0,3,6],0],
      'sum': [[9,12,15],[3,12,21],36]
    }

    # Ensure all expected keys are present
    assert set(result.keys()) == set(expected.keys())

    # Compare numerical lists with tolerance
    for key in expected:
        for axis_idx in range(3):
            assert pytest.approx(result[key][axis_idx]) == expected[key][axis_idx]

# test_calculations_on_0_to_8()
# test_invalid_input_raises([123])
