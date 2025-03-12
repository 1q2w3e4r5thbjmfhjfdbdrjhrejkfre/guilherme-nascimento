package estrutura.sequencial;

import javax.swing.JOptionPane;

public class Q2JOptionPane {

    public static void main(String args[]) {
        int qtdPao = 0, qtdBroa = 0;
        float arrecadou = 0, guardar = 0;
        String aux = "";

        aux = JOptionPane.showInputDialog("Digite a quantidade de paẽs: ");
        qtdPao = Integer.parseInt(aux);

        aux = JOptionPane.showInputDialog("Digite a quantidade de Broas: ");
        qtdBroa = Integer.parseInt(aux);

        arrecadou = (float) ((qtdPao * 0.12) + (qtdBroa * 1.5));
        guardar = arrecadou * (10 / 100);

        JOptionPane.showInputDialog(null, "Total arrecadado R$" + arrecadou);
        JOptionPane.showInputDialog(null, "Poupança R$" + guardar);

    }
}
 