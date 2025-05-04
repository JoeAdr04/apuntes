package relaciones;

public class Materia {
    private String nombre;
    private Docente docente; //atributo de tipo docente
    private int nroEst;
    private Estudiante[] estudiantes = new Estudiante[100]; //arreglo de estudiantes
    
    public Materia(){
        this.nombre = "";
        this.docente = new Docente();
        this.nroEst = 0;
    }
    public Materia(String nom, String nomD, String fDoc, int nroItemD){
        this.nombre = nom;
        this.docente = new Docente(nomD, fDoc, nroItemD);
        //this.estudiantes[0]=new Estudiante();
        this.nroEst = 0;
    }
    public void agregarEst(Estudiante est){
        this.estudiantes[this.nroEst] = est;
        this.nroEst = this.nroEst+1;
    }

    @Override
    public String toString() {
        String cad = "\n";
        for (int i=0; i<this.nroEst; i++){
            cad = cad+ estudiantes[i].toString()+"\n";
        }
        return "Materia{" + "nombre=" + this.nombre + ", docente=" + docente + ", nroEst=" + nroEst + ", estudiantes=" + cad + '}';
    }
    public void cambiarMat(int x, String fecha){
        for (int i=0; i<this.nroEst; i++){
            if((this.estudiantes[i]).getNroMat() == x){
                this.estudiantes[i].setFechaNac(fecha);
            }
        }
    }

    public Docente getDocente() {
        return docente;
    }
    public void docenteAntiguo(Materia m){
        int a1;
        int a2;
        String cha1;
        String cha2;
        cha1 = (this.docente).getFechaNac();
        cha2 = (m.docente).getFechaNac();
        //cha1 = (cha1.charAt(6))+cha1.charAt(7)+cha1.charAt(8)+cha1.charAt(9);
        cha1 = cha1.substring(6,10);
        cha2 = cha2.substring(6,10);
        a1 = Integer.parseInt(cha1);//anio en enteros del docente 1
        a2 = Integer.parseInt(cha2);//anio en entero del docente 2
        //System.out.println("anio doc 1: "+ a1+ "anio docente2: "+ a2);
        if(a1<a2){
            System.out.println("El docente mas aintguo es: "+(this.getDocente()).toString());
        }else{
            System.out.println("El docente mas aintguo es: "+(m.getDocente()).toString());
        }
    }   
}
