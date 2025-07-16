import java.util.Scanner;

public class bilgenap {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Menghitung jumlah bilangan genap dari n bilangan");
        System.out.println("--------------------------------------------------");
        System.out.print("Masukan range bilangan: ");
        int range = scanner.nextInt();
        int jumlahGenap = 0;

        int genap = 0;
        for (int i = 1; i <= range; i++) {
            if (i % 2 == 0) {
                genap += i;
                System.out.println("Bilangan genap ke-" + (i / 2) + " adalah " + i);
                jumlahGenap++;
            }
        }
        double ratarata = (double) genap / jumlahGenap;
        System.out.println("Jumlah semua bilangan genap dari 1 sampai " + range + " : " + genap);
        System.out.println("Rata-rata bilangan genap dari 1 sampai " + range + " : " + ratarata);
                
        System.out.println("nama anggota: ahnafzakhy, raditya syaputra, elang alamsyah, krisna ferdiramsyah");
    
    }
            
}