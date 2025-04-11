
package herencisprob02;


public class HerencisProb02 {

    
    public static void main(String[] args) {
        // TODO code application logic here
        Electrodomestico eP = new Electrodomestico(12.0, "rojo", "B", 22);
        System.out.println("Precio del electrodomestico= "+eP.precioFinal());
        Lavadora L = new Lavadora(12.0, "rojo", "B", 22,31);
        System.out.println("Precio de la lavadora= "+L.precioFinal());
        Television T = new Television(12.0, "rojo", "B", 22, 60, true);
        System.out.println("Precio de la Television= "+T.precioFinal());
    }
    
}
