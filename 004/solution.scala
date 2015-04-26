object Solution {
  val solution = (99 to 999)
      .flatMap( x => (x to 999).map(x*))
      .filter(n => n.toString == n.toString.reverse)
      .max

      def main(args: Array[String]) = println(solution)
}
