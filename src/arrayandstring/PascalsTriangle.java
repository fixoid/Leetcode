package arrayandstring;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/** 118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    1       |
   1 1      |
  1 2 1     |
 1 3 3 1   \ /
1 4 6 4 1   |
*/

public class PascalsTriangle { 

    public static List<List<Integer>> generate(int numRows) {
        // List of list for store Triangle levels from top to bottom
        List<List<Integer>> p_triangle = new ArrayList<List<Integer>>();

        // First (top) line of trianle - always contains only one item: 1
        p_triangle.add(new ArrayList<Integer>(Arrays.asList(1)));
        
        if (numRows > 1) {
            // generate lines from 2 to numRows
            for (int i = 1; i < numRows; i++) {
                // list for generated lines
                List<Integer> pt_line = new ArrayList<>();
                // first item of line always is 1
                pt_line.add(1);
                int j = 1;
                //generate items from 2nd to second to last
                while (j < i) {
                    // item[j] = prev line item[j-1] + prev line item[j]
                    pt_line.add(p_triangle.get(i-1).get(j-1)+p_triangle.get(i-1).get(j));
                    // System.out.println(pt_line);
                    j++;
                }
                // last item of line always is 1
                pt_line.add(1);
                //adds line to triange
                p_triangle.add(pt_line);
            }
        }
        return p_triangle;
    }

    public static void main (String[] args) {
        // the answer
        System.out.println("Ans: ");
        System.out.println(generate(7));
    }
}