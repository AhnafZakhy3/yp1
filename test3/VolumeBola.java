import java.util.Scanner;

public class VolumeBola {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan r: ");
        double r = scanner.nextDouble();

        double volume = (4/3.0) * Math.PI * Math.pow(r, 3);

        System.out.println("Volume bola adalah: " + volume );
    }

    
}
