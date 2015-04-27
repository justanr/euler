import math.pow

object Solution {
  def series_sum(n: Int) = (n * (n+1))/2
  def squared_sum(n: Int) = pow(series_sum(n), 2)
  def sum_of_squares(n: Int) = (n * (n+1) * (2*n+1))/6
  def main(args: Array[String]) = println(squared_sum(100) - sum_of_squares(100))
}
