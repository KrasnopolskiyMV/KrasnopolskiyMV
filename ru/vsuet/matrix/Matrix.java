package vsuet.matrix;

import java.util.Arrays;
import java.util.Random;
import java.util.function.BiFunction;

public class Matrix {
   private int[][] matrix;

   public Matrix(int size) {
      this.matrix = new int[size][size];
      this.fillRandom();
   }

   public int calculate(BiFunction<Integer, Integer, Boolean> condition, BiFunction<Integer, Integer, Integer> expression, Integer accumulator) {
      int result = accumulator;

      for(int i = 0; i < this.matrix.length; ++i) {
         for(int j = 0; j < this.matrix[i].length; ++j) {
            if ((Boolean)condition.apply(i, j)) {
               result = (Integer)expression.apply(result, this.matrix[i][j]);
            }
         }
      }

      return result;
   }

   public String toString() {
      StringBuilder sb = new StringBuilder();
      int[][] var2 = this.matrix;
      int var3 = var2.length;

      for(int var4 = 0; var4 < var3; ++var4) {
         int[] row = var2[var4];
         sb.append(Arrays.toString(row)).append("\n");
      }

      return sb.toString().replace("[[", "[").replace("]]", "]");
   }

   private void fillRandom() {
      Random random = new Random();

      for(int i = 0; i < this.matrix.length; ++i) {
         for(int j = 0; j < this.matrix[i].length; ++j) {
            this.matrix[i][j] = random.nextInt(10);
         }
      }

   }

   private void printMatrix() {
      for(int i = 0; i < this.matrix.length; ++i) {
         for(int j = 0; j < this.matrix[i].length; ++j) {
            System.out.print(this.matrix[i][j] + " ");
         }

         System.out.println();
      }

   }

   public void performOperations(Calculator calculator) {
      int sumAboveDiagonal = 0;
      int differenceBelowDiagonal = 0;
      int productOnDiagonal = 1;

      for(int i = 0; i < this.matrix.length; ++i) {
         for(int j = 0; j < this.matrix[i].length; ++j) {
            if (i < j) {
               sumAboveDiagonal = calculator.calculateSum(sumAboveDiagonal, this.matrix[i][j]);
            } else if (i > j) {
               differenceBelowDiagonal = calculator.calculateDifference(differenceBelowDiagonal, this.matrix[i][j]);
            } else {
               productOnDiagonal = calculator.calculateProduct(productOnDiagonal, this.matrix[i][j]);
            }
         }
      }

      System.out.println("\u0421\u0443\u043c\u043c\u0430 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u0432\u044b\u0448\u0435 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0438: " + sumAboveDiagonal);
      System.out.println("\u0420\u0430\u0437\u043d\u043e\u0441\u0442\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043d\u0438\u0436\u0435 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0438: " + differenceBelowDiagonal);
      System.out.println("\u041f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0438: " + productOnDiagonal);
   }
}