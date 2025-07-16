public class Kalkulator {
    private double bil1;
    private double bil2;
    private double hasil;

    public void setBil1(double bil1) {
        this.bil1 = bil1;
    }

    public void setBil2(double bil2) {
        this.bil2 = bil2;
    }

    public double tambah() {
        hasil = bil1 + bil2;
        return hasil;
    }

    public double kurang() {
        hasil = bil1 - bil2;
        return hasil;
    }

    public double kali() {
        hasil = bil1 * bil2;
        return hasil;
    }

    public double bagi() {
        if (bil2 != 0) {
            hasil = bil1 / bil2;
            return hasil;
        } else {
            System.out.println("Pembagian dengan nol tidak diperbolehkan");
            return 0;
        }
    }

    public static void main(String[] args) {
        Kalkulator kalkulator = new Kalkulator();
        kalkulator.setBil1(10);
        kalkulator.setBil2(5);
        System.out.println("Hasil penjumlahan: " + kalkulator.tambah());
        System.out.println("Hasil pengurangan: " + kalkulator.kurang());
        System.out.println("Hasil perkalian: " + kalkulator.kali());
        System.out.println("Hasil pembagian: " + kalkulator.bagi());
    }
}