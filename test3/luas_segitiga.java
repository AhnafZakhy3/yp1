import java.util.Scanner;
public class luas_segitiga {
        public static void main(String[] args) {
            int alas;
            int tinggi;
            double luas;
            Scanner keyboard = new Scanner(System.in);
            System.out.println("Masukkan nilai alas : ");
            alas = keyboard.nextInt();
            System.out.println("Masukkan nilai tinggi : ");
            tinggi = keyboard.nextInt();
            luas = 0.5 * alas * tinggi;
            System.out.println("Luas Segitiga : " + luas);
         }

}
