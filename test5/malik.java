import java.util.Scanner;
public class malik{
    public static void main(String[] args) {
        int umur;
        Scanner keyboard = new Scanner(System.in);
        
        System.out.println("Masukan umur anda:");
        umur = keyboard.nextInt();
        
        if (umur >= 18) {
        System.out.print("Anda sudah harus mempunyai KTP.");
        }
        else {
        System.out.print("Anda belum harus mempunyai KTP");
        
        }
    }
}