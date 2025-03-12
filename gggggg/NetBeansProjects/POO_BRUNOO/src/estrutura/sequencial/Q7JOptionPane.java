package estrutura.sequencial;

import javax.swing.JOptionPane;

public class Q7JOptionPane {


    
    public static void main(String[] args){
    String aux;
    double n1, n2, n3,mp;
    
   aux= JOptionPane.showInputDialog("digite a n1");
   n1 = Double.parseDouble(aux);
   aux= JOptionPane.showInputDialog("digite a n2");
   n2 = Double.parseDouble(aux);
   aux= JOptionPane.showInputDialog("digite a n3");
   n3 = Double.parseDouble(aux);
  
   mp = (n1*1+n2*2+n3*3)/6;
  
  JOptionPane.showMessageDialog(null, "sua media é"+ mp);
    
    
    
    
    
    
    
    
    }

   
}
