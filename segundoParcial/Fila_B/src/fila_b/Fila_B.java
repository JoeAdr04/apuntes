package fila_b;

public class Fila_B {

    public static void main(String[] args) {
        // TODO code application logic here
        //Obra o=new Obra("monaliza", "oleo","picasso", "234",2, "davinci", "456",4);
        //System.out.println(o);
        Pintura p1=new Pintura("monaliza", "oleo","romance","picasso", "234",2, "davinci", "456",4);
        Pintura p2=new Pintura("ultCena", "acuarela","terror","prometeo", "876",4, "pleus", "988",8);
        Anuncio a1 = new Anuncio(1234, 23.4);
        Anuncio a2 = new Anuncio(4567, 44.8);
        System.out.println(p1);
        System.out.println(p2);
        p1.agregarAnuncio(a1);
        p2.agregarAnuncio(a2);
        System.out.println("Despues de agregar los anuncios:");
        System.out.println(p1);
        System.out.println(p2);
        p1.promAnios(p2);
    }
    
}
