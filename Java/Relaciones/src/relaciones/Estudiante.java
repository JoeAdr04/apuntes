/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package relaciones;

/**
 *
 * @author Jaeger_04
 */
public class Estudiante {
    private String ci;
    private String fechaNac;
    private int nroMat;
    
    public Estudiante(){
        this.ci = "";
        this.fechaNac = "";
        this.nroMat = 0;
    }
    public Estudiante(String ci, String f, int nro){
        this.ci = ci;
        this.fechaNac = f;
        this.nroMat = nro;
    }

    @Override
    public String toString() {
        return "Estudiante{" + "ci=" + ci + ", fechaNac=" + fechaNac + ", nroMat=" + nroMat + '}';
    }

    public String getCi() {
        return ci;
    }

    public String getFechaNac() {
        return fechaNac;
    }

    public int getNroMat() {
        return nroMat;
    }

    public void setCi(String ci) {
        this.ci = ci;
    }

    public void setFechaNac(String fechaNac) {
        this.fechaNac = fechaNac;
    }

    public void setNroMat(int nroMat) {
        this.nroMat = nroMat;
    }
    
}
