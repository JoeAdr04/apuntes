/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ejer02;

/**
 *
 * @author Jaeger_04
 */
public class Empleado {
    public String nombre;
    public double sueldo;
    
    public Empleado(){
        this.nombre = "";
        this.sueldo = 0.0;
    }  
    public Empleado(String nombre, double sueldo){
        this.nombre = nombre;
        this.sueldo = sueldo;
    }
    public Empleado(double sueldo){
        this.nombre = "";
        this.sueldo = sueldo;
    }

    public String getNombre() {
        return nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
    @Override
    public String toString() {
        return "Empleado{" + "nombre=" + nombre + ", sueldo=" + sueldo + '}';
    }
    
    public double sueldoAnual(){
        return this.sueldo*12;
    }
    
    public void aplicarAumento(){//metodo para aplicar aumento del 10%
        double nuevoSalario;
        nuevoSalario = this.sueldo*(1.10);
        this.sueldo = nuevoSalario;
    }
    
}
