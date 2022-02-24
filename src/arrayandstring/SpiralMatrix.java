package arrayandstring;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/** Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 */

public class SpiralMatrix {  

    private static void printArray(int[] a) {
        for (int i = 0; i < a.length; ++i) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }

    private static void printArray2(int[][] a) {
        if (a == null || a.length == 0 ) {
            return;
        }
        for (int i = 0; i < a.length; ++i) {
            for (int j = 0; a[i] != null && j < a[i].length; ++j) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }
    }
    public static List<Integer> spiralOrder(int[][] matrix) {

        int M = matrix.length;      //matrix rows
        int N = matrix[0].length;   // matrix collums
        int spiral_length = M*N;    
        List<Integer> spiral = new ArrayList<Integer>();

        //pointer tracking
        int x = 0;
        int y = 0;

        // direction tracking, 0 - rigth, 1 - down, 2 - left, 3 - up
        int direction = 0;

        // dynamic matrix size for borders
        // y_min, y_max, x_min, x_max
        // it will resize after every direction change of spiral moving
        int[] matrix_size = {0, M-1, 0, N-1};

        for (int i=1; i <= spiral_length; i++) {
            spiral.add(matrix[y][x]);
            if (direction == 0) {
                if (x == matrix_size[3]) {  // left border reaching (x_max)
                    matrix_size[0] += 1;    // upper border move down (y_min)
                    direction = 1;          // direction changing 
                    y += 1;                 // move down
                }
                else { x += 1; }
            }
            else if (direction == 1) {
                if (y == matrix_size[1]) {  // bottom border reaching (y_max)
                    matrix_size[3] -= 1;    // rigth border move left (x_max)
                    direction = 2;          // direction changing 
                    x -= 1;                 // move left
                }
                else { y += 1; }
            }
            else if (direction == 2) {
                if (x == matrix_size[2]) {  // left border reaching (x_min)
                    matrix_size[1] -= 1;    // bottom border move up (y_max)
                    direction = 3;          // direction changing 
                    y -= 1;                 // move up
                 }
                else { x -= 1; }
            }
            else if (direction == 3) {
                if (y == matrix_size[0]) {  // top border reaching (y_min)
                    matrix_size[2] += 1;    // left border move rigth (x_min)
                    direction = 0;          // direction changing 
                    x += 1;                 // move left
                }
                else { y -= 1; }
            }
        }

        return spiral;
    }

    public static void main (String[] args) {
        // int[][] nums = null;
        // int[][] nums = { {1,2,3}, {4,5,6}, {7,8,9} };
        // int[][] nums = { {1,2,3,4}, {5,6,7,8}, {9,10,11,12} };
        int[][] nums = { {1,2,3}, {4,5,6}, {7,8,9}, {10,11,12} };

        // the matrix
        printArray2(nums);
        // the answer
        System.out.print("Ans: ");
        // printArray(findDiagonalOrder(nums));
        System.out.println(spiralOrder(nums));
    }
}