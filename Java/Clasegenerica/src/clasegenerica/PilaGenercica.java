/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package clasegenerica;

import java.util.Stack;

/**
 *
 * @author Jaeger_04
 */
public class PilaGenercica<T>{
    private Stack<T> pila;

    public PilaGenercica(){
        pila = new Stack<T>();
    }

    public void apilar(T elemento) {
        pila.push(elemento);
        System.out.println("Elemento apilado: " + elemento);
    }

    public T desapilar() {
        if (!pila.isEmpty()) {
            T elemento = pila.pop();
            System.out.println("Elemento desapilado: " + elemento);
            return elemento;
        } else {
            System.out.println("La pila está vacía");
            return null;
        }
    }

    public T cima() {
        if (!pila.isEmpty()) {
            return pila.peek();
        } else {
            System.out.println("La pila está vacía");
            return null;
        }
    }

    public boolean estaVacia() {
        return pila.isEmpty();
    }

    public int tamanio() {
        return pila.size();
    }

    public void mostrarElementos() {
        System.out.println("Elementos en la pila: " + pila);
    }
    
}
