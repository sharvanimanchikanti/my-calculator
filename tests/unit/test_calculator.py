"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract,multiply

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2,-3) == -5
        assert add(-10,-15) == -25
    def test_subtract_negative_numbers(self):
        assert subtract(-5,-3) ==-2
        assert subtract(-10,-4) == -6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

class TestMultiplyDivide:
    """Test multiplication and division operations"""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(2, 3) == 6
        assert multiply(10, 5) == 50
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(6, 3) == 2
        assert divide(10, 2) == 5
    def test_multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(0, 5) == 0
        assert multiply(10, 0) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-2, -3) == 6
        assert multiply(-10, -5) == 50
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        assert divide(-6, -3) == 2
        assert divide(-10, -2) == 5
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide -10 by zero - division by zero is undefined"):
            divide(-10, 0)
        with pytest.raises(ValueError, match="Cannot divide 10 by zero - division by zero is undefined"):
            divide(10, 0)
        
class TestPowerSqrt:
    """Test power and square root operations"""
    
    def test_power(self):
        """Test exponentiation"""
        from src.calculator import power
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(4, 0.5) == 2
    
    def test_sqrt(self):
        """Test square root"""
        from src.calculator import sqrt
        assert sqrt(9) == 3
        assert sqrt(16) == 4
        with pytest.raises(ValueError, match="Cannot compute square root of negative number"):
            sqrt(-4)