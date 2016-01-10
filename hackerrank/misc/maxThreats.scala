package compete.hackerrank.misc

import scala.collection.mutable
import scala.util.control.Breaks

//Example of breakable
object HackerRank {

def main(args: Array[String]) {
    maxThreats(Array(8, 4, 5, 1, 3, 7, 8, 2, 6))
}
  
def maxThreats(a: Array[Int]): Int = {
    val res = Array.fill(a.size)(0)
    for (i <- 1 to a.size - 1){
      val curval = a(i-1)
      var left = false
      var right = false
      val loop = new Breaks
      loop.breakable{
        for (j <- i+1 to a.size){
          val tocompare = a(j-1)
          val diff = j - i
          val p = curval - diff
          val q = curval + diff
          if (!left && p > 0 && tocompare == p){
            //println("Left", i,j,p,tocompare, curval)
            res(i-1) = res(i-1) + 1
            res(j-1) = res(j-1) + 1
            left = true
          } else if (!right && q <= a.size && tocompare == q){
            //println("Right", i,j,q)
            right = true
            res(i-1) = res(i-1) + 1
            res(j-1) = res(j-1) + 1
          }

          if (left && right){
            loop.break
          }

        }
      }

    }
    return res.toList.max
  }
}
