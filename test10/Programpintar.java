import java.util.Scanner;
public class Programpintar {

    public static void main(String[] args) {
      int a,t,s;
      int luas_persegi;
      int Luas_segitiga;
      int pilihan;
      Scanner scanner = new Scanner(System.in);
      System.out.println("masukan pilihan : ");
      pilihan = scanner.nextInt();
      
      if (pilihan == 1){
        System.out.println("masukan alas:");
        a = scanner.nextInt();
        System.out.println("masukan tinggi:");
        t = scanner.nextInt();
        Luas_segitiga =  (a*t)/2;
        System.out.println("jadi luas segitiga = "+ Luas_segitiga);
      }else if(pilihan == 2){
        System.out.println("masukan sisi :");
        s = scanner.nextInt();
        luas_persegi = s*s;
        System.out.println("luas perseginya adalah = "+ luas_persegi);
      }else if (pilihan == 3){
        System.out.println("masukan total belanja:");
        double diskon = 0.3;
        int total = scanner.nextInt();
        double bayar = total - (total*diskon);
        System.out.println("harga setelah diskon = "+ bayar);
          
      }else{
        System.out.println("maaf pilihan kamu tidak ada");  
      }    
    }
}
