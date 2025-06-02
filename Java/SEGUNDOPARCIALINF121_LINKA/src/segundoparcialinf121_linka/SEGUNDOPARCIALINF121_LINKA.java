
package segundoparcialinf121_linka;
public class SEGUNDOPARCIALINF121_LINKA {
    public static void main(String[] args) {
        Anuncio a1 = new Anuncio(1, 500);
        //inciso a
        Pintura p1 = new Pintura(a1);
        p1.leer();
        Pintura p2 = new Pintura(a1);
        p2.leer();
        //inciso b
        p1.incisoB(p2);
        //inciso c
        p2.incisoC("maria", 50);
    }
}
