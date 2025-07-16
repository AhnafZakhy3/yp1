import java.util.Scanner;

public class pengulangan {
    public static void main(String[] args) {

        int i = 1;
        int ulang;
        Scanner scanner = new Scanner(System.in);
        System.out.println("berapa kali perulangan: ");
        ulang = Integer.parseInt(scanner.nextLine());
        
        //for (i = 0; i < ulang; i++) {
        //    System.out.println("Halo Dunia");
        //}

        //while (i<=ulang){
        //    System.out.println("Halo Dunia 2");
        //    i++;
        //}

        do {
            System.out.println("Halo Dunia 2");
            i++;
        } while (i <= ulang);
    }
}