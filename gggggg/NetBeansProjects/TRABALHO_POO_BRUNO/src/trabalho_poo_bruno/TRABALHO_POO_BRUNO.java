
package trabalho_poo_bruno;

import java.util.Scanner;

public class TRABALHO_POO_BRUNO {

    public static void main(String[] args) {
        float lata = 0, garrafa = 0, garrafa2 = 0;
        double  litros =0;
        Scanner bruh = new Scanner(System.in);
        
        System.out.println("qual a quantidade de latas?");
        lata = bruh.nextFloat();
        
        System.out.println("quantas garrafas de 600ml vocce comprou?");
        garrafa = bruh.nextFloat();
        
        System.out.println("quantas garrafas de 2L vocce comprou?");
        garrafa2 = bruh.nextFloat();
        
        litros = lata*0.350 + garrafa*0.600 + garrafa2*2;
        System.out.println("quantidade de litros comprados"+ litros);
        
        
    }
    
}
