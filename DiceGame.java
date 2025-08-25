import java.util.Random;
import java.util.Scanner;

public class DiceGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
    
        System.out.print("Kuinka monta kierrosta pelataan?");
        int kierrokset = scanner.nextInt();
        scanner.nextLine();

        int p1Voitot = 0;
        int p2Voitot = 0;

        for (int i = 1; i <= kierrokset; i++) {
            System.out.println(("\nKierros"+i));

            // 1. pelaaja
            System.out.print("Pelaaja 1, paina Enter heittääksesi noppaa...");
            scanner.nextLine();
            int p1 = random.nextInt(6) + 1;
            System.out.println("Pelaaja 1 heitti: " + p1);

            // 2. pelaaja
            System.out.print("Pelaaja 2, paina Enter heittääksesi noppaa...");
            scanner.nextLine();
            int p2 = random.nextInt(6) + 1;
            System.out.println("Pelaaja 2 heitti: " + p2);

            // Voittaja
            if (p1 > p2) {
                System.out.println("Kierroksen voitti pelaaja 1!");
                p1Voitot++;
            } else if (p2 > p1) {
                System.out.println("Kierroksen voitti pelaaja 2!");
                p2Voitot++;
            } else {
                System.out.println("Tasapeli.");
            }
        }


        System.out.println("\n*** PELI PÄÄTTYI ***");
        System.out.println("Pelaaja 1 voitti" + p1Voitot + "kierrosta");
        System.out.println("Pelaaja 2 voitti" + p2Voitot + "kierrosta");

        if (p1Voitot > p2Voitot) {
            System.out.println("--- Voittaja on PELAAJA 1! ---");
        } else if (p2Voitot > p1Voitot) {
            System.out.println("--- Voittaja on PELAAJA 1! ---");
        } else {
            System.out.println("--- TASAPELI! ---");
        }

        scanner.close();
    }
}
        
    

    


