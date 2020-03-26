package com.company;

import java.util.ArrayList;

public class quarantadue {

    public static void main(String[] args) {
        
        System.out.println("42 è la risposta alla vita, all'universo, tutto quanto!");

        //Creo un array dinamico che conterrà i numeri primi
        ArrayList<Integer> primes = new ArrayList<Integer>();
        int count = 2;
        //Aggiungo 3 come primo numero primo
        primes.add(3);
        int number = 5;
        //Finché non raggiungi 41 numeri...
        while (count < 42){
            boolean prime = true;
            //Per ogni elemento 'el' nella lista dei numeri primi...
            for (Integer el:primes){
                //...se el è minore o uguale alla radice del numero...
                if (el <= Math.ceil(Math.sqrt(number))){
                    //...se number è divisibile per el, allora non è primo e puoi uscire dal ciclo.
                    if (number % el == 0){
                        prime = false;
                        break;
                    }
                }
            }
            //Se il numero è primo allora aggiungilo alla lista dei primi.
            if (prime){
                primes.add(number);
                count+=1;
            }
            //Aggiungi 2 al numero (un numero pari non può essere primo).
            number+=2;
        }
        //Aggiungi 2 come primo elemento della lista dei numeri primi (per evitare di confrontare inutilmente i numeri con 2 essendo dispari.
        primes.add(0, 2);
        //Stampa la lista dei primi.
        System.out.print(primes);
    }
}
