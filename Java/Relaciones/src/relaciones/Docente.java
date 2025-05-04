/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package relaciones;

/**
 *
 * @author Jaeger_04
 */
public class Docente {
    private String nombre;
    private String fechaNac;
    private int nroItem;
    
    public Docente(){
        this.nombre = "";
        this.fechaNac = "";
        this.nroItem = 0;
    }
    public Docente(String n, String f, int nro){
        this.nombre = n;
        this.fechaNac = f;
        this.nroItem = nro;
    }
    @Override
    public String toString() {
        return "Docente{" + "nombre=" + nombre + ", fechaNac=" + fechaNac + ", nroItem=" + nroItem + '}';
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public void setFechaNac(String fechaNac) {
        this.fechaNac = fechaNac;
    }
    public void setNroItem(int nroItem) {
        this.nroItem = nroItem;
    }
    public String getNombre() {
        return nombre;
    }
    public String getFechaNac() {
        return fechaNac;
    }
    public int getNroItem() {
        return nroItem;
    } 
}
