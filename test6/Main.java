import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int angka1, angka2;
        int hasil;
        String pilihan;

        System.out.print("Pilih operasi: \n1. Penambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n");
        pilihan = scanner.next();
        
        System.out.print("Masukkan angka pertama: ");
        angka1 = scanner.nextInt();
        System.out.print("Masukkan angka kedua: ");
        angka2 = scanner.nextInt();

        if (pilihan.equals("1")) {
            hasil = angka1 + angka2;
            System.out.println("hasil Penambahan:" + hasil);
        }else if (pilihan.equals("2")) {
            hasil = angka1 - angka2;
            System.out.println("hasil Pengurangan:" + hasil);
        }else if (pilihan.equals("3")) {
            hasil = angka1 * angka2;
            System.out.println("hasil Perkalian:" + hasil);
        }else if (pilihan.equals("4")) {
            if (angka2 == 0){
                System.out.println("Error! tidak Bisa Dibagi 0");
            }else {
            hasil = angka1 / angka2;
            System.out.println("hasil Perkalian:" + hasil);
            }
        }else{
            System.out.println("Error! Pilihan tidak ada");
        }
    }
}
