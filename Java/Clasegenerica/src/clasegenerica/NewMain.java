/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package clasegenerica;

/**
 *
 * @author Jaeger_04
 */
public class NewMain {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        PilaGenercica<Integer> pilaEnteros = new PilaGenercica<>();
        pilaEnteros.apilar(10);
        pilaEnteros.apilar(20);
        pilaEnteros.apilar(30);
        pilaEnteros.mostrarElementos();
        pilaEnteros.desapilar();

        // Pila de cadenas
        PilaGenercica<String> pilaCadenas = new PilaGenercica<>();
        pilaCadenas.apilar("uno");
        pilaCadenas.apilar("dos");
        pilaCadenas.mostrarElementos();
    }
}
