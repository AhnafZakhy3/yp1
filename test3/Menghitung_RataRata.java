import java.util.Scanner;

public class Menghitung_RataRata {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Masukkan nama: ");
        String nama = scanner.nextLine();

        System.out.print("Nilai BIND: ");
        double nilai1 = scanner.nextDouble();

        System.out.print("Nilai MTK: ");
        double nilai2 = scanner.nextDouble();

        System.out.print("Nilai BING: ");
        double nilai3 = scanner.nextDouble();

        double rataRata = (nilai1 + nilai2 + nilai3) / 3;
        System.out.println("Hai " + nama + ", nilai rata-ratamu adalah " + rataRata);
    }
}
