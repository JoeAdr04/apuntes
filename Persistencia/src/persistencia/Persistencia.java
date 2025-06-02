/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package persistencia;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

/**
 *
 * @author Jaeger_04
 */
public class Persistencia {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        Scanner te =new Scanner(System.in);
        int opt = 0;
        ArchEmpleado arch=new ArchEmpleado("C:\\Users\\Jaeger_04\\Desktop\\archi.dat");
        arch.crear();
        while(opt!=5){
            System.out.println("Elije una opcion :");
            System.out.println("opcion 1:(adicionar empleado)");
            System.out.println("opcion 2(listar todos):");
            System.out.println("opcion 3(eliminar empelado):");
            System.out.println("opcion 4(editar empelado):");
            System.out.println("opcion 5(salir):");
            opt = te.nextInt();
            if(opt== 1){
                Empleado e1=new Empleado(3245,"rtyu","rtyu","cbfg");
            }
            else if(opt ==2){
                for (int i=0;i<(arch.listar().length);i++ ){
                    System.out.print(arch.listar()[i][0]);
                    System.out.print(arch.listar()[i][1]);
                    System.out.print(arch.listar()[i][2]);
                    System.out.print(arch.listar()[i][3]);
                }
            }
            else if(opt ==3){
                arch.eliminar(3245);
            }
            else if(opt ==4){
                Empleado e2=new Empleado(123,"123","123","123");
                arch.editar(3245, e2);
            }
            
        }

        
    }
    
}
