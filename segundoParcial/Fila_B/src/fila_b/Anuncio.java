/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package fila_b;

/**
 *
 * @author Jaeger_04
 */
public class Anuncio {
    private int numero;
    private double precio;
    
    public Anuncio(){
        this.numero = 0;
        this.precio = 0;
    }
    public Anuncio(int num, double pres){
        this.numero = num;
        this.precio = pres;
    }

    @Override
    public String toString() {
        return "Anuncio{" + "numero=" + numero + ", precio=" + precio + '}';
    }
    
}
