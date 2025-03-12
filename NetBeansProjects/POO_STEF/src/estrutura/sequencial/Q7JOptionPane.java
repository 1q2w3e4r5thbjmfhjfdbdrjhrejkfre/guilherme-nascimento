package estrutura.sequencial;
import.javax.swing.JOptionPane;

public class Q7JOptionPane {
    public static void main(String args[]) {
    double p1 = 0, p2 = 0 p3 = 0 , int n1 = 0;
n2 = 0, n3 = 0,int mp = 0;
    String aux;
    aux = JOptionPane.showInputDialog ("qual o valor da primeira n1?");
    n1 = interge.parseInt(aux);
                 
    aux = JOptionPane.showInputDialog ("qual o peso da primeira nota?");
    p1 = interge.parseInt(aux);
                 
    aux = JOptionPane.showInputDialog ("qual o valor da segunta nota?");
    n2 = interge.parseInt(aux);
                 
    aux = JOptionPane.showInputDialog ("qual o peso da segunda nota?");  
    p2 = interge.parseInt(aux);
                 
    aux = JOptionPane.showInputDialog ("qual o valor da terceira nota?");
    n3 = interge.parseInt(aux);
                 
    aux = JOptionPane.showInputDialog ("qual o peso da terceira nota?");
    p3 = interge.parseInt(aux);
    mp= ((n1*p1)+(n2)*p2)+ (n3*p3))/(p1+p2+p3);
                  
    JOptionPane.showMessegeDialog (null, "sua media ponderada é: "+mp);
     }
} 
