package fila_b;


public class Artista {
    private String nombre;
    private String ci;
    private int aniosExp;
    
    public Artista(){
        this.nombre = "";
        this.ci = "";
        this.aniosExp = 0;
    }
    public Artista(String nom, String ci, int anios){
        this.nombre = nom;
        this.ci = ci;
        this.aniosExp = anios;
    }

    @Override
    public String toString() {
        return "Artista{" + "nombre=" + nombre + ", ci=" + ci + ", aniosExp=" + aniosExp + '}';
    }
    public int getAnios(){
        return this.aniosExp;
    }
}
