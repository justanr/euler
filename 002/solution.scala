object Solution {
  val fib: Stream[Long] = {
    def tail(h: Long, n: Long): Stream[Long] = h #:: tail(n, h+n)
    tail(0, 1)
  }
  def main(args: Array[String]) = {
    val solution = fib.takeWhile(_ < 4000000).toList.filter( _ % 2 == 0).sum
    println(solution)
  }
}
