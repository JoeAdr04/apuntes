/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package herencisprob02;

/**
 *
 * @author Jaeger_04
 */
public class Television extends Electrodomestico{
    private double resolucion;
    private boolean sintonizadorTDT;
    
    public Television(){
        super();
        this.resolucion = 0.0;
        this.sintonizadorTDT = false;
    }
    public Television(double precioBase, String color, String consumo, double peso, double res, boolean sint){
        super(precioBase, color, consumo, peso);
        this.resolucion = res;
        this.sintonizadorTDT = sint;
    }
    
    public double precioFinal(){
        if(this.resolucion > 50){
            return (((super.precioFinal()*1.3)+50));
        }
        else if(this.resolucion>50){
            return ((super.precioFinal()*1.30));
        }
        else if(this.sintonizadorTDT == true){
            
            return (super.precioFinal()+50);
        }
        else{
            //System.out.println("entro");
            return super.precioFinal();
        } 
    }
    
}
