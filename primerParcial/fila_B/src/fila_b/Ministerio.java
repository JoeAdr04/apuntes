package fila_b;


public class Ministerio {
    private String nombre;
    private String direccion;
    private int nroEmpleados;
    private String[][] empleados = new String[3][100];
    private int[] edades= new int[100];
    private double[] sueldos= new double[100];
    
    public Ministerio(){//este constructor nos sirve asi vacio nada mas
        this.nombre = "";
        this.direccion = "";
        this.nroEmpleados = 0;
        
    }
    public Ministerio(String nombre, String direccion){//en este caso asignaremos solo al que reciba argumentos con los datos que nos dieron
        this.nombre = nombre;
        this.direccion = direccion;
        this.empleados[0][0] = "pedro";
        this.empleados[1][0] = "rojas";
        this.empleados[2][0] = "luna";
        this.empleados[0][1] = "lucy";
        this.empleados[1][1] = "sosa";
        this.empleados[2][1] = "rios";
        this.empleados[0][2] = "ana";
        this.empleados[1][2] = "perez";
        this.empleados[2][2] = "rojas";
        this.empleados[0][3] = "saul";
        this.empleados[1][3] = "arce";
        this.empleados[2][3] = "calle";
        this.edades[0] = 35;
        this.edades[1] = 43;
        this.edades[2] = 26;
        this.edades[3] = 29;
        this.sueldos[0] = 2500;
        this.sueldos[1] = 3250;
        this.sueldos[2] = 2700;
        this.sueldos[3] = 2500;
        this.nroEmpleados = (this.empleados).length+1;
    }

    @Override
    public String toString() {
        String salida = "";
        for (int i=0; i<this.nroEmpleados;i++){
            salida=salida+("Nombre: "+this.empleados[0][i]+" Paterno: "+this.empleados[1][i]+" Materno: "+this.empleados[2][i]
                    +" Edad: "+this.edades[i]+" Sueldo: "+this.sueldos[i])+"\n";
        }
        return "Ministerio{" + "nombre=" + nombre + ", direccion=" + direccion + ", nroEmpleados=" + nroEmpleados
                +"\n"+salida + '}';
    }
    //esta aprte la hice por demas, lei que era igual que la fila a eliminar al de apellido paterno o materno
    //la opcion correcta era buscar la edad
    /*public void eliminarEmpleado(String x){
        for (int i=0; i<this.nroEmpleados;i++){
            if(this.empleados[1][i].equals(x) || this.empleados[2][i].equals(x)){
                for (int j =i; j<this.nroEmpleados;j++){
                    this.empleados[0][j]=this.empleados[0][j+1];
                    this.empleados[1][j]=this.empleados[1][j+1];
                    this.empleados[2][j]=this.empleados[2][j+1];
                    this.edades[j] = this.edades[j+1];
                    this.sueldos[j] = this.sueldos[j+1];
                }
                this.nroEmpleados --;
            }
        }
    }*/
    
    public void eliminarEmpleado(int x){
        for (int i=0; i<this.nroEmpleados;i++){
            if(this.edades[i] == x){//busca la deda que corresponda
                for (int j =i; j<this.nroEmpleados;j++){//recorremos el vector una posicon para eliminar ese dato
                    this.empleados[0][j]=this.empleados[0][j+1];
                    this.empleados[1][j]=this.empleados[1][j+1];
                    this.empleados[2][j]=this.empleados[2][j+1];
                    this.edades[j] = this.edades[j+1];
                    this.sueldos[j] = this.sueldos[j+1];
                }
                this.nroEmpleados --;
            }
        }
    }
    public void operador(Ministerio m, String x){
        int pos = 0; 
        for(int i = 0; i<m.nroEmpleados;i++){
            if(m.empleados[0][i].equals(x)){//busca la posicion de el empleado de nombre x
                //System.out.println("find!"); (esto lo use solo para ver que encontrar correctamente).
                pos = i;
                break;
            }
        }//aqui se agrega al primer objeto todos los datos corrspondientes
        this.empleados[0][this.nroEmpleados] = m.empleados[0][pos];
        this.empleados[1][this.nroEmpleados] = m.empleados[1][pos];
        this.empleados[2][this.nroEmpleados] = m.empleados[2][pos];
        this.edades[this.nroEmpleados] = m.edades[pos];
        this.sueldos[this.nroEmpleados] = m.sueldos[pos];
        this.nroEmpleados ++;//se debe subir el numeor de empleados debido a el cambio
        //aqui se elimina al empleado de el segundo objeto :
        for (int j =pos; j<m.nroEmpleados;j++){
            m.empleados[0][j]=m.empleados[0][j+1];
            m.empleados[1][j]=m.empleados[1][j+1];
            m.empleados[2][j]=m.empleados[2][j+1];
            m.edades[j] = m.edades[j+1];
            m.sueldos[j] = m.sueldos[j+1];
        }
        m.nroEmpleados --; //tambien se recude su cantidad
    }
    
    public int menorEdad(){//funcion aucilair para hallar la menor edad
        int menor = 9999999;
        for(int i = 0; i<this.nroEmpleados;i++){
            if(this.edades[i] < menor){
                menor = this.edades[i];
            }
        }
        return menor;
    }
    public double menorSueldo(){ // funcion auxiliar para hallar el menor sueldo
        double menor = 9999999;
        for(int i = 0; i<this.nroEmpleados;i++){
            if(this.sueldos[i] < menor){
                menor = this.sueldos[i];
            }
        }
        return menor;
    }
    
    public void mostrar(int x){//primera asignacion que recibe un entero
        for(int i = 0; i<this.nroEmpleados;i++){
            if(this.edades[i] == x){
                System.out.println(("Nombre: "+this.empleados[0][i]+" Paterno: "+this.empleados[1][i]+" Materno: "+this.empleados[2][i]
                    +" Edad: "+this.edades[i]+" Sueldo: "+this.sueldos[i])+"\n");
            }
        }
    }
    public void mostrar(double x){//segunda asignacion(sobrecarga) que recibe un double
        for(int i = 0; i<this.nroEmpleados;i++){
            if(this.sueldos[i] == x){
                System.out.println(("Nombre: "+this.empleados[0][i]+" Paterno: "+this.empleados[1][i]+" Materno: "+this.empleados[2][i]
                    +" Edad: "+this.edades[i]+" Sueldo: "+this.sueldos[i])+"\n");
            }
        }
    }
}
