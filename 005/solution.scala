import math.abs

object Solution {
  def gcd(a: Int, b: Int): Int = {
    b match {
      case 0 => a
      case _ => gcd(b, a % b)
    }
  }

  def lcm(a: Int, b: Int): Int = abs(a * b)/gcd(a, b)

  def main(args: Array[String]) = {
    println((11 to 20).toList.foldRight(1)(lcm))
  }
}
