import java.util.Scanner;
public class MenghitungDiskon {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("==Selamat datang di toko Oren==");
        System.out.print("Total belanja:RP ");
        double harga = scanner.nextDouble();
        System.out.print("Kamu dapat Diskon sebesar: %");
        double diskon = scanner.nextDouble();
        double totalHarga = harga - (harga * diskon / 100);
        System.out.println("Total harga setelah diskon: RP " + totalHarga);
    }
}