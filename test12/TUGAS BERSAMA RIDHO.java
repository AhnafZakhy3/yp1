import java.util.Scanner;
import java.util.Arrays;

public class Perpustakaan {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String[] judul = {
        	"Clean Code",
        	"The Pragmatic Programmer",
        	"Introduction to Algorithms",
        	"Python Crash Course",
        	"Head First Java",
        	"You Don't Know JS",
        	"Eloquent JavaScript",
        	"Structure and Interpretation of Computer Programs",
        	"Design Patterns",
        	"Artificial Intelligence: A Modern Approach"
        };

        String[] pengarang = {
            "Robert C. Martin",
            "Andrew Hunt dan David Thomas",
            "Thomas H. Cormen",
            "Eric Matthes",
            "Kathy Sierra dan Bert Bates",
            "Kyle Simpson",
            "Marijn Haverbeke",
            "Harold Abelson dan Gerald Jay Sussman",
            "Erich Gamma et al.",
            "Stuart Russell dan Peter Norvig"
        };
        System.out.println("==================================================");
            System.out.println("<<<Tugas Proyek Aplikasi Perpustakaan Sederhana>>>");
            System.out.println("==================================================");

        while (true) {
            System.out.println("\n===MENU PERPUSTAKAAN===");
            System.out.println("1. Tambah Buku");
            System.out.println("2. Lihat Buku");
            System.out.println("3. Hitung Denda");
            System.out.println("4. Keluar");
            System.out.println("==================================================");
            System.out.print("Masukan pilihan anda: ");
            int pilih = input.nextInt();
            input.nextLine();

            if (pilih == 1) {
                System.out.println("\n===TAMBAH BUKU===");
                System.out.print("Masukan judul buku: ");
                String j = input.nextLine();
                System.out.print("Masukan pengarang buku: ");
                String p = input.nextLine();
                
                String[] JudulBaru= Arrays.copyOf(judul, judul.length + 1);
                JudulBaru [JudulBaru.length - 1]= j;
                judul= JudulBaru;
                
                String[] PengarangBaru = Arrays.copyOf(pengarang, pengarang.length + 1);
                PengarangBaru [PengarangBaru.length - 1] = p;
                pengarang= PengarangBaru;

                System.out.println("Buku "+j+ " dengan pengarang " +p+ " berhasil ditambahkan\n");

            } else if (pilih == 2) {
                System.out.println("\n===DAFTAR BUKU===");
                for (int i = 0; i < judul.length; i++) {
                    System.out.println((i + 1) + ". " + judul[i] + " - " + pengarang[i]);
                }

            } else if (pilih == 3) {
                System.out.println("\n===HITUNG DENDA===");
                System.out.print("Hari telat pengembalian: ");
                int hari = input.nextInt();
                if (hari > 0) {
                    int denda = hari * 5000;
                    System.out.println("Denda yang harus anda bayar: Rp" + denda + "\n");
                } else {
                    System.out.println("Hari tidak boleh 0 atau minus!\n");
                }

            } else if (pilih == 4) {
                System.out.println("Terima kasih!! Silahkan datang kembali");
                
                break;
            } else {
                System.out.println("Pilihan anda tidak valid, silahkan pilih nomor yang tertera!\n");
            }
        }
    }
}