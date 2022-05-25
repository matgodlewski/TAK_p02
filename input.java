public class MyClass {

    public void printThree() {

           int i = 3;
           System.out.println(i);
    }

    void printFirstTenSquares() {

         int i = 0;
         while (i <= 10) {
             int y = 3;
             printNumber(i * i, 0);
             i = i + 1;
         }
    }

     void printNumber(int x, int y) {

         System.out.println(x);
     }
}