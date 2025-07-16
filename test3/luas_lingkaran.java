import java.util.Scanner;

public class luas_lingkaran {
    public static void main(String[] args) {
        int ruas;
        double luas;

        Scanner keyboard = new Scanner(System.in);
        System.out.println("Masukkan nilai ruas : ");
        ruas = keyboard.nextInt();
        luas = Math.PI * ruas * ruas;
        // luas = 22/7 * ruas * ruas;
        // luas = 3.14 * ruas * ruas;
        
        System.out.println("jadi luas lingkarannya:" + luas);

    }

}