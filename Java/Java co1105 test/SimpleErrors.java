import java.util.InputMismatchException;
import java.util.Scanner; // Imported Scanner

public class SimpleErrors {
    public static void main(String[] args) { //Appended void to main, it's not returning anything
        Scanner stdin = new Scanner(System.in); //Appended a missing semi colon 
        System.out.print("Enter two numbers: ");
        try {
        int input1 = stdin.nextInt();//Appended braces to the nextint method.
        int input2 = stdin.nextInt();//Appended braces to the nextint method.
        int num1 = input1;
        int num2 = input2; //Changed a misspelled word "intpu2"
        while (num1 % num2 != 0) { //Appended a missing curly brace, completing the while loop.
        int oldn1 = num1; //oldn1 hadn't been declared as a variable.
        int oldn2 = num2; //Same as previous error for oldn2
        num1 = oldn2;
        num2 = oldn1 % oldn2;
        num2 = Math.abs(num2);
    } 
    System.out.println("The GCD of "+ input1 +" and "+ input2 + " is "+ num2);// Corrected the improper concatenation of variables to the strings
                            //Moved the print statement so that it is in the scope of the variables. 
        } //Missing brace to close out try clause 
            //num 2 integer was misplaced into the string.
        catch (Exception InputMismatchException) { //Type declaration was missing
        System.err.println("Error: input must be two numbers.");
        System.exit(1);
        }
        stdin.close();//Closed scanner 

}
}
