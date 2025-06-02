/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package segundoparcialinf121_linka;

/**
 *
 * @author Jaeger_04
 */
public class Pintura extends Obra {
    private String genero;
    public Pintura(Anuncio be){
        super(be);
    }
    public void leer(){
        //read(genero);
        super.leer();
    }

    public Artista getA1() {
        return a1;
    }

    public Artista getA2() {
        return a2;
    }
    //inciso b
    public void incisoB(Pintura p2){
        double promedio = (this.getA1().getaExp()+this.getA2().getaExp()+p2.getA1().getaExp()+p2.getA2().getaExp())/4;
        //print (promedio)
    }
    //inciso c
    public void incisoC(String x, double y){
        if(this.getA1().getNombre().equals(x) || this.getA2().getNombre().equals(x))
            this.b.setPrecio(this.b.getPrecio()+y);
    }
}