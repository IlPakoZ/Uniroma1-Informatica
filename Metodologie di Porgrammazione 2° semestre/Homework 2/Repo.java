import java.util.Arrays;

public class Repo {
    private int[] interi;
    private int curr_length = 0;

    //Crea un array chiamato "interi" di dimensione "dim"
    Repo(int dim){
        interi = new int[dim];
    }

    //Stampa i contenuti dell'array "interi"
    public void stampa(){
        for (int i = 0; i< curr_length; i++) System.out.print(interi[i] + " ");
        System.out.println();
    }

    //Mette "x" nell'array "interi" e ne incrementa la dimensione
    public void input(int x){
        interi[curr_length++] = x;
    }

    //Inverte l'ordine degli elementi nell'array "interi"
    public void gira(){

        //Crea un array temporaneo "new_interi" che conterrà gli elementi al contrario
        int[] new_interi = new int[interi.length];
        int indice = 0;
        for (int i = curr_length -1; i>=0; i--){
            new_interi[indice++] = interi[i];
        }
        //Sostituisce al contenuto di "interi" quello di "new_interi"
        interi = new_interi;
    }

    //Aggiunge agli elementi di "interi" gli elementi dell'array "interi" in rp1.
    public void appendi(Repo rp1){
        if (curr_length + rp1.curr_length <= interi.length) {
            for (int i = 0; i< rp1.curr_length; i++){
                interi[curr_length++] = rp1.interi[i];
            }
        }
    }

    //Restituisce l'array di interi effettivo.
    public int[] toarray(){
        return Arrays.copyOfRange(interi, 0, curr_length);
    }


}

