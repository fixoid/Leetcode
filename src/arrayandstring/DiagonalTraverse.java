package arrayandstring;

/** 498. Diagonal Traverse
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
 */

public class DiagonalTraverse {  

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

    public static int[] findDiagonalOrder(int[][] mat) {

        // empry matrix check
        if (mat == null || mat.length == 0 ) {
            return new int[0];
        }

        int M = mat.length;     //matrix rows
        int N = mat[0].length;  // matrix collums
        int[] diag_arr = new int[M*N]; // array for answer

        //pointer tracking
        int x = 0;
        int y = 0;

        int direction = 1; // 1 - move top-rigth, -1 move - bottom-left
        for (int indx = 0; indx < diag_arr.length; indx++) {
            // assignment answer element from pointer
            diag_arr[indx] = mat[y][x];

            // need to change direction if reaching border of matrix
            // top or bottom border
            if ( (y +1*-direction < 0)  || (y +1*-direction > M-1) ) {
                // top-rigth corner
                if (x +1*direction > N-1) {
                    direction *= -1; 
                    y +=1;  // cant move rigth and move down
                }
                else {
                    direction *= -1;
                    x +=1;  // move rigth
                }
            }
            // left or rigth border
            else if ( (x +1*direction < 0)  || (x +1*direction > N-1) ) {
                direction *= -1;
                y +=1;
            }
            // pointer inside the matrix
            else {
                x += 1*direction;
                y += -1*direction;
            }

        }
        return diag_arr;
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
        printArray(findDiagonalOrder(nums));
    }
}