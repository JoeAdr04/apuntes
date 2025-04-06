

package juego01;
import java.util.Scanner;
/**
 *
 * @author Jaeger_04
 */
public class juegoAdivinaNumero extends Juego{
    Scanner te = new Scanner(System.in);
    private int nroAdivinar;
    
    public juegoAdivinaNumero(int nroVidas){
        super(nroVidas);
        this.nroAdivinar = (int)(Math.random() * 11);
    }
    public void juega(){
        super.reiniciarPartida();
        
        while(this.quitaVida()){
            //System.out.print(this.nroAdivinar);
            System.out.print("Ingresa un numeor del 0 al 10: ");
            int numero = te.nextInt();
            if(this.nroAdivinar == numero){
                System.out.println("Acertaste! (Record = "+this.record+")");
                //this.nroAdivinar = (int)(Math.random() * 11);
            }
            else{
                if(numero >this.nroAdivinar){
                    System.out.println("el numero a adivinar es menor, vidas restantes: "+this.nroVidas);
                }
                else{
                    System.out.println("el numero a adivinar es mayor, vidas restantes: "+this.nroVidas);
                }
                this.nroVidas = this.nroVidas-1;
                this.record = this.record-1;
                      
                //System.out.println("Intentalo de nuevo \n te quedan: "+this.nroVidas+" vidas");
            }
        }
        System.out.println("---------------------------");
        System.out.println("Juego Terminado \n record: "+this.record);
    }
    public int getNroAdivinar() {
        return nroAdivinar;
    }
    public void setNro(int x){
        this.nroAdivinar =x;
    } 
}
