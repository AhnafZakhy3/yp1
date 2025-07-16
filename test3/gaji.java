import java.util.Scanner;

public class gaji {
    public static void main(String[] args) {
        
        String nama, alamat ;
        int usia, gaji;

        Scanner keyboard = new Scanner(System.in);

        System.out.print("Nama kamu: ");
        nama = keyboard.nextLine();

        System.out.print("Alamat: ");
        alamat = keyboard.nextLine();

        System.out.print("Usia: ");
        usia = keyboard.nextInt();

        System.out.print("Gaji: ");
        gaji = keyboard.nextInt();
        
        System.out.println("\nInformasi yang dimasukkan:");
        System.out.println("Nama: " + nama);
        System.out.println("Alamat: " + alamat);
        System.out.println("Usia: " + usia);
        System.out.println("Gaji: Rp" + gaji);

        keyboard.close();
    }
}