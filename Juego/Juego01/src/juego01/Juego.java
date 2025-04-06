/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package juego01;

/**
 *
 * @author Jaeger_04
 */
public class Juego {
    protected int nroVidas;
    protected int record;
    
    public Juego(int vidas){
        this.nroVidas = vidas;
        this.record = vidas;
    }
    public void reiniciarPartida(){
        this.record = this.nroVidas;
    }
    public void actualizaRecord(){
        this.record= this.record-1;
    }
    public boolean quitaVida(){
        //this.nroVidas = this.nroVidas-1;
        if(this.nroVidas == 0 ){
            return false;
        }
        else{
            return true;
        }
    }

    public int getNroVidas() {
        return nroVidas;
    }

    public int getRecord() {
        return record;
    }

    public void setNroVidas(int nroVidas) {
        this.nroVidas = nroVidas;
    }

    public void setRecord(int record) {
        this.record = record;
    }
    
}
