package relaciones;

public class Relaciones {

    public static void main(String[] args) {
        // TODO code application logic here
        //System.out.println("asdf");
        //Docente d = new Docente("juan", "perez", 23);
        //System.out.println(d);
        Materia m1 = new Materia("matematica", "jose", "05/04/1920", 123);
        System.out.println(m1);
        Estudiante e1 = new Estudiante("123456", "05/04/1993", 456);
        Estudiante e2 = new Estudiante("76543", "15/04/1994", 789);
        Estudiante e3 = new Estudiante("asdf", "15/04/1994", 1234);
        Estudiante e4 = new Estudiante("345", "15/04/1994", 768);
        Estudiante e5 = new Estudiante("4256", "15/04/1994", 345678);
        m1.agregarEst(e1);
        m1.agregarEst(e2);
        m1.agregarEst(e3);
        m1.agregarEst(e4);
        m1.agregarEst(e5);
        System.out.println(m1);
        //cammbiar la fecha de nacimiento del estudiante con matricula x
        m1.cambiarMat(789, "11/09/2001");
        System.out.println("--------cambiar est por matricula----------");
        System.out.println(m1);
        //creamos otra materia
        Materia m2  = new Materia("fisica","pablito", "12/12/1930", 12);
        m2.agregarEst(e3);
        m2.agregarEst(e3);
        m2.agregarEst(e3);
        //Buscar a la materia con el docente mas antiguo
        m1.docenteAntiguo(m2);
        
        
    }
    
}
