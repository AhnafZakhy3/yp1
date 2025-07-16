import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Masukkan nilai: ");
        int nilai = scanner.nextInt();

        if (nilai > 90) {
            System.out.println("Nilai A");
        } else if (nilai > 80) {
            System.out.println("Nilai B");
        } else if (nilai > 70) {
            System.out.println("Nilai C");
        } else {
            System.out.println("Nilai D");
        }
    }
}
