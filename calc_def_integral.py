import numpy as np
import scipy.integrate as spi


# Monte-Carlo method
def monte_carlo_method(func, a, b, N=10000):
    """
    Calculates the approximate value of the integral of a given function on the interval [a, b] using the Monte Carlo method.

    Parameters:
    func (callable): A function of a single variable whose integral is to be calculated. It takes one argument (float) and returns float.
    a (float): Start of the integration interval.
    b (float): End of the integration interval.
    N (int, optional): The number of random points used to calculate the integral. The default value is 10000.

    Returns:
    float: The approximate value of the integral of a function over a given interval.

    Example:
    >>> def my_func(x):
    ...     return x**2
    >>> monte_carlo_method(my_func, 0, 1)
    0.333...  # the approximate value of the integral x^2 on the interval [0, 1]
    """

    # Generate N random points in the given interval (a, b)
    random_points = np.random.uniform(a, b, N)

    # Calculate the value of the function at each point
    function_values = func(random_points)

    # Calculate the average value of the function
    mean_value = np.mean(function_values)

    # Calculate the approximate value of the integral
    integral_value = mean_value * (b - a)

    return integral_value

# Test function
def check_calc_def_integral(func, a, b):
    result, error = spi.quad(func, a, b)
    return result, error


# Main function
def main():
    # Let's define the function whose integral we want to calculate
    # As an example, let's take f(x) = (x^2)/2 + (x^3)/3 + x^4 - sqrt(x^5)
    def f(x):
        return (x**2 / 2) + (x**3 / 3) + x**4 - np.sqrt(x**5)

    a = 0
    b = 1

    result = monte_carlo_method(f, a, b)

    print(f"Homework 10 - Task 2 | Calculating the value of the integral of a function using the Monte-Carlo method")
    print(f"Homework 10 - Task 2 | Function: f(x) = (x^2)/2 + (x^3)/3 + x^4 - sqrt(x^5)")
    print(f"Homework 10 - Task 2 | Result: {result}")

    test_result, error = check_calc_def_integral(f, a, b)

    print(f"Homework 10 - Task 2 | Checking the calculation of a defined integral using the library scipy.integrate.quad")
    print(f"Homework 10 - Task 2 | Function: f(x) = (x^2)/2 + (x^3)/3 + x^4 - sqrt(x^5)")
    print(f"Homework 10 - Task 2 | Test result: {test_result}")
    print(f"Homework 10 - Task 2 | Estimation of the absolute error: {error}")

    return result, test_result


if __name__ == "__main__":
    main()
