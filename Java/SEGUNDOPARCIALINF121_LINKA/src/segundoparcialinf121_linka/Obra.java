/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package segundoparcialinf121_linka;

/**
 *
 * @author Jaeger_04
 */
public class Obra {
    protected String titulo, material;
    protected Artista a1 = new Artista();
    protected Artista a2 = new Artista();
    protected Anuncio b;

    public Obra(Anuncio b) {
        this.b = b;
    }
    public Obra(){}
    public void leer(){
        //read(titulo);
        //read(material);
        a1.leer();
        a2.leer();
    }
}
