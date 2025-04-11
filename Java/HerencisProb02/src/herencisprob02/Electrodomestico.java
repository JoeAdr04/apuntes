
package herencisprob02;


public class Electrodomestico {
    private double precioBase;
    private String color;
    private String consumoE;
    private double peso;
    
    public Electrodomestico(){
        this.precioBase=0.0;
        this.color = "";
        this.consumoE = "";
        this.peso = 0.0;
    }
    public Electrodomestico(double p, String c, String cE, double pes){
        this.precioBase=p;
        this.color = c;
        this.consumoE =cE;
        this.peso = pes;
    }
    
    public double precioFinal(){
        double fin = this.precioBase;
        String c = this.consumoE;
        if(c == "A"){
            fin = fin+100;
        }
        else if(c == "B"){
            fin = fin +80;
        }
        else if (c == "C"){
            fin = fin +60;
        }
        else if(c == "D"){
            fin = fin +50;
        }
        else if(c == "E"){
            fin = fin +30;
        }
        else if(c == "F"){
            fin = fin +10;
        }
        double pes = this.peso;
        if(pes >0 && pes<=19){
            fin  = fin+10;
        }
        else if(pes >=20 && pes<=49){
            fin  = fin+50;
        }
        else if(pes >=50 && pes<=79){
            fin  = fin+80;
        }
        else if(pes >=80){
            fin  = fin+100;
        }
        
        return fin;
    }

    public double getPrecioBase() {
        return precioBase;
    }

    public String getColor() {
        return color;
    }

    public String getConsumoE() {
        return consumoE;
    }

    public double getPeso() {
        return peso;
    }

    public void setPrecioBase(double precioBase) {
        this.precioBase = precioBase;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setConsumoE(String consumoE) {
        this.consumoE = consumoE;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }
    
    
    
}
