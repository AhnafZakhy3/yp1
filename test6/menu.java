import java.util.Scanner;
public class menu {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Selamat Datang di Toko MBOON");
        System.out.println("Pilih Menu:");
        System.out.println("1. Nasi Goreng");
        System.out.println("2. Mie Goreng");
        System.out.println("3. Ayam Goreng");
        System.out.println("4. Nasi Bungkus");
        
        System.out.println("Pilih Menu anda:");
        int pilihan = scanner.nextInt();
        
        if (pilihan == 1) {
            System.out.println("Anda memilih Nasi Goreng");
            System.out.println("Harganya Rp14000");
        }else if (pilihan == 2) {
            System.out.println("Anda memilih Mie Goreng");
            System.out.println("Harganya Rp12000");
        }else if (pilihan == 3){
            System.out.println("Anda memilih Ayam Goreng");
            System.out.println("Harganya Rp18000");
        }else if (pilihan == 4){
            System.out.println("Anda memilih Nasi Bungkus");
            System.out.println("Harganya Rp10000");
        }else {
            System.out.println("Menu tidak tersedia");
        }
    }
}
