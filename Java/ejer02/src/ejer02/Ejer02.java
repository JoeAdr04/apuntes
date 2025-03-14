
package ejer02;


public class Ejer02 {

    /**
Crea una clase Empleado con nombre y sueldo
a)
Agrega un método para calcular el sueldo anual
b)
Agrega un método para aplicar un aumento del 10%
c)
Crea dos empleados y muestra sus sueldos antes y después del aumento
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        Empleado e2=new Empleado("maria", 3467.4);
        Empleado e3=new Empleado("Marturian", 40.4);
        System.out.println(e2.getSueldo());
        System.out.println(e3.getSueldo());
        System.out.println("despues del aumento");
        e2.aplicarAumento();
        e3.aplicarAumento();
        System.out.println(e2.getSueldo());
        System.out.println(e3.getSueldo());
        
        
        System.out.println(e2.toString());
        e2.aplicarAumento(); //llamamos a la funcion para aplicar aumento
        System.out.println(e2.toString());
        
        //double sueldoAnual = e1.sueldoAnual();
        //System.out.println("El salario anual del empleado es:" );
        //System.out.println(sueldoAnual);
    }
    
}
