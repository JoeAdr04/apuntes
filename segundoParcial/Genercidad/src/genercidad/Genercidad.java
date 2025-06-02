
package genercidad;


public class Genercidad {

    public static void main(String[] args) {
        // TODO code application logic here
        Persona p1=new Persona("jose", 12,true);
        Persona p2=new Persona("maria", 16,false);
        Persona p3=new Persona("luis", 21,true);
        int numero = 12345678;
        
        Registro<Persona> r=new Registro();
        r.agregar(p1);
        r.agregar(p2);
        //r.agregar(numero);
        r.listar();
        
        Registro r2 = new Registro();
        
    }
    
}
