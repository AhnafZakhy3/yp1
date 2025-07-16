import java.util.Scanner;

public class luas_persegi {
    public static void main(String[] args) {
        int sisi;
        int Luas;
        Scanner keyboard = new Scanner (System.in);
        System.out.println("Masukkan sisi : ");
        sisi = keyboard.nextInt();
        Luas = sisi * sisi;
        System.out.println("Luas Persegi adalah : " + Luas);
    }

}
