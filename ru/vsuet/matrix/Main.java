package vsuet.matrix;

import java.util.Objects;

public class Main {
   public Main() {
   }

   public static void main(String[] args) {
      Matrix matrix = new Matrix(5);
      System.out.println(matrix);
      System.out.println(matrix.calculate((i, j) -> {
         return i > j;
      }, Integer::sum, 0));
      System.out.println(matrix.calculate((i, j) -> {
         return i < j;
      }, (acc, item) -> {
         return acc - item;
      }, 0));
      System.out.println(matrix.calculate(Objects::equals, (acc, item) -> {
         return acc * item;
      }, 1));
   }
}