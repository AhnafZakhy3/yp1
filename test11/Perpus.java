import java.util.Scanner;


public class Perpus {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        String[] judul_buku = {
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

        String[] pengarang_buku = {
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
        
        while (true){
        
        System.out.println("===Menu Perpustakaan===");
        System.out.println("1. Tambah Buku");
        System.out.println("2. Lihat Daftar Buku");
        System.out.println("3. Hitung Denda");
        System.out.println("4. Keluar");
        System.out.print("Pilih menu (1-4): ");
        int menu = input.nextInt();
        input.nextLine();

        if (menu == 1) {
            System.out.print("Masukkan judul buku: ");
            String judul = input.nextLine();

            String[] JudulBuku2 = new String[judul_buku.length + 1];
            System.arraycopy(judul_buku, 0, JudulBuku2, 0, judul_buku.length);
            JudulBuku2[judul_buku.length] = judul;
            judul_buku = JudulBuku2;

            System.out.print("Masukkan pengarang buku: ");
            String pengarang = input.nextLine();

            String[] Pengarang2 = new String[pengarang_buku.length + 1];
            System.arraycopy(pengarang_buku, 0, Pengarang2, 0, pengarang_buku.length);
            Pengarang2[pengarang_buku.length] = pengarang;
            pengarang_buku = Pengarang2;

            System.out.println("Buku berhasil ditambahkan!");
            System.out.println("");
        } else if (menu == 2) {
            System.out.println("Daftar Buku:");
            for (int i = 0; i < judul_buku.length; i++) {
                System.out.println((i + 1) + ". " + judul_buku[i] + " - " + pengarang_buku[i]);
            }
            System.out.println("");
        } else if (menu == 3) {
            System.out.print("Masukkan jumlah hari terlambat: ");
            int hariTerlambat = input.nextInt();
            int denda = hariTerlambat * 5000;
            System.out.println("Denda yang harus dibayar: Rp " + denda);
        } else if (menu == 4) {
            System.out.println("Terima kasih telah menggunakan sistem perpustakaan.");
            break;
        } else {
            System.out.println("Menu tidak valid. Silakan coba lagi.");
            
        }
    }
    }

}
