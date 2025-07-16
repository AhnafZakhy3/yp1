import java.util.Scanner;

public class BERSARANG {
    public static void main(String[] args) {
        String juara1dkv, juara2dkv, juara3dkv, juara1pplg, juara2pplg, juara3pplg, input;
        int juara;
        Scanner keyboard = new Scanner(System.in);

        juara1dkv = "7 juta";
        juara2dkv = "5 juta";
        juara3dkv = "3 juta";
        juara1pplg = "Laptop";
        juara2pplg = "HP";
        juara3pplg = "Sepeda";

        System.out.println("Mata Lomba Desain:");
        System.out.println("Juara 1");

        System.out.println("Mata lomba apa [desain] [program]");
        input = keyboard.nextLine();

        if (input.equalsIgnoreCase("desain")) {
            System.out.println("Juara berapa");
            juara = keyboard.nextInt();
            keyboard.nextLine();
            if (juara == 1) {
                System.out.println("Juara 1 mendapatkan hadiah " + juara1dkv);
            } else if (juara == 2) {
                System.out.println("Juara 2 mendapatkan hadiah " + juara2dkv);
            } else if (juara == 3) {
                System.out.println("Juara 3 mendapatkan hadiah " + juara3dkv);
            } else {
                System.out.println("Maaf, Anda tidak mendapatkan hadiah");
                }

        } else if (input.equalsIgnoreCase("program")) {
            System.out.println("Juara berapa");
            juara = keyboard.nextInt();
            keyboard.nextLine();
            if (juara == 1) {
                System.out.println("Juara 1 mendapatkan hadiah " + juara1pplg);
            } else if (juara == 2) {
                System.out.println("Juara 2 mendapatkan hadiah " + juara2pplg);
            } else if (juara == 3) {
                System.out.println("Juara 3 mendapatkan hadiah " + juara3pplg);
            } else{
                System.out.println("Maaf, Anda tidak mendapatkan hadiah");
            }
        } else{
            System.out.println("Mata lomba tidak ada");
        }
    }
}