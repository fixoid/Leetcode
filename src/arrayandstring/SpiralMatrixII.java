package arrayandstring;

/** 59. Spiral Matrix II (Medium)
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Input: n = 1
Output: [[1]]
 */

public class SpiralMatrixII {  

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

    // generate the matrix with elements in spiral order
    public static int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];

        //pointer tracking
        int x = 0;
        int y = 0;

        // direction tracking, 0 - rigth, 1 - down, 2 - left, 3 - up
        int direction = 0;

        // dynamic matrix size for borders
        // y_min, y_max, x_min, x_max
        // it will resize after every direction change of spiral moving
        int[] matrix_size = {0, n-1, 0, n-1};

        for (int i=1; i <= n*n; i++) {
            matrix[y][x] = i;
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

        return matrix;
    }

    public static void main (String[] args) {

        // the matrix
        int[][] matrix = generateMatrix(7);
        
        // the answer
        System.out.println("Ans: ");
        printArray2(matrix);
    }
}