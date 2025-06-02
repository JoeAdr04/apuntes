/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package segundoparcialinf121_linka;

/**
 *
 * @author Jaeger_04
 */
public class Anuncio {
    private int numero;
    private double precio;
    public Anuncio(int numero, double precio) {
        this.numero = numero;
        this.precio = precio;
    }
    public double getPrecio() {
        return precio;
    }
    public void setPrecio(double precio) {
        this.precio = precio;
    }    
}
