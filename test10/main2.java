public class main2 {
    public static void main(String[] args) {
    int prima = 1000; // limit deret bilangan
    int deret; // Inisiasi penghitung untuk pembagian

    // Ulangi dari 1 hingga 'prima' untuk mengidentifikasi bilangan prima
    for (int i = 1; i <= prima; i++) {
        deret = 0; // Reset penghitung untuk setiap 'i

// Periksa pembagian dari 2 hingga i/2
        for (int j = 2; j <= i / 2; j++) {
        if (i % j == 0) {
            deret++; // Tambah jika 'i' habis dibagi 'j'
            break; // Keluar dari loop jika pembagi ditemukan
        }
    }
    // Jika hitungannya 0, 'i' adalah bilangan prima
        if (deret == 0) {
        System.out.println(i);// Output
        }
    }
    
    }
}