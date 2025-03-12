package estrutura.sequencial;

import javax.swing.JOptionPane;

public class Q2_JOptionPane {

    public static void main(String[] args) {
        int qtdPao = 0, qtdBroa = 0;
        float arrecadou = 0, guardar = 0;

        String aux = "";
        
        aux = JOptionPane.showInputDialog("Digite a quantidade de pães ");
        qtdPao = Integer.parseInt(aux);
     
        aux = JOptionPane.showInputDialog("Digite a quantidade de broas");
        qtdBroa = Integer.parseInt(aux);
        arrecadou = (float)((qtdPao * 1.2) + (qtdBroa * 1,5 ));
        guardar =arrecadou * (10/100);
        
        JOptionPane.showMessageDialog(null,"total arrecado r$"+ arrecadou);
        JOptionPane.showMessageDialog(null, "poupança r$" + guardar);
    }

}
