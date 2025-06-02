package fila_b;

public class Obra {
    protected String titulo;
    protected String material;
    protected Artista a1, a2;
    protected Anuncio b;
    
    public Obra(){
        this.titulo = "";
        this.material = "";
        this.a1 = new Artista();
        this.a2 = new Artista();
    }
    public Obra(String tit, String mat, String nom1, String ci1, int anios1,String nom2, String ci2, int anios2){
        this.titulo = tit;
        this.material = mat;
        this.a1 = new Artista(nom1, ci1, anios1);
        this.a2 = new Artista(nom2, ci2, anios2);
    }
    public void agregarAnuncio(Anuncio a){
        this.b = a;
    }

    @Override
    public String toString() {
        return "Obra{" + "titulo=" + titulo + ", material=" + material + ", a1=" + a1 + ", a2=" + a2 + ", b=" + b + '}';
    }
    
}
