package fila_b;

public class Pintura extends Obra{
    private String genero;
    
    public Pintura(){
        super();
        this.genero ="";
    }
    public Pintura(String tit, String mat, String gen, String nom1, String ci1, int anios1,String nom2, String ci2, int anios2){
        super(tit, mat, nom1, ci1, anios1, nom2, ci2, anios2);
        this.genero = gen;
    }

    @Override
    public String toString() {
        return "Pintura{" +super.toString()+ "genero=" + genero + '}';
    }
    public void promAnios(Pintura p){
        double prom;
        prom = ((double)(this.a1.getAnios()+this.a2.getAnios()+p.a1.getAnios()+p.a2.getAnios()))/4;
        System.out.println("Promedio de los anios de exp: "+prom);
    }
}
