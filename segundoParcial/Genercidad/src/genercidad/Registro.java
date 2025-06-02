
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package genercidad;

/**
 *
 * @author Jaeger_04
 */
public class Registro <Na>{
    private Na[] v;
    private int nroElem;
    
    public Registro(){
        v= (Na[])new Object[100];
    }
    
    public void agregar(Na valor){
        this.v[this.nroElem]=valor;
        this.nroElem=this.nroElem+1;
    }
    
    public void listar(){
        for(int i=0; i<this.nroElem;i++){
            System.out.print(v[i]+" ");
        }
    }
}
