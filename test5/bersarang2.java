public class bersarang2 {
    public static void main(String[] args) {
        int nilai = 85;
        
        if (nilai >= 80) {
            System.out.println("Nilai Anda: A");
            if (nilai >= 90) {
                System.out.println("Luar biasa!");
            } else {
                System.out.println("Bagus sekali!");
            }
        } else if (nilai >= 60) {
            System.out.println("Nilai Anda: B");
            if (nilai >= 70) {
                System.out.println("Cukup baik!");
            } else {
                System.out.println("Perlu sedikit perbaikan.");
            }
        } else {
            System.out.println("Nilai Anda: C");
            System.out.println("Harus lebih giat belajar!");
        }
    }
}
