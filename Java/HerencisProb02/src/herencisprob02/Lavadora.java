/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencisprob02;


public class Lavadora extends Electrodomestico {
    private double carga;
    
    public Lavadora(double precioBase, String color, String consumo, double peso, double carga){
        //super();
        super(precioBase, color, consumo, peso);
        this.carga = carga;
    }
    
    public Lavadora(){
        super();
        this.carga = 0.0;
    }
    //double aux;
    public double precioFinal(){
        if (this.carga >30){
            return (super.precioFinal()+50);
            //aux = super.precioFinal();
            //aux = aux+50;
        }
        return super.precioFinal();
    }
    
}
