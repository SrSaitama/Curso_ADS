package Curso_ADS.POO.Trabalho;

import java.util.ArrayList;

public class Cofrinho {
	
	private ArrayList<Moeda> listaMoedas = new ArrayList<>();
	
	
	public void adicionar(Moeda m) {
		listaMoedas.add(m);
		
	}	
	public void remover(Moeda m) {
		listaMoedas.remove(m);
	}	
	
	public void listagemMoedas() {
		for(Moeda m : listaMoedas) {
			m.info();
		}
	}	
	
	public void totalConvertido() {
		double total=0;
		for(Moeda m : listaMoedas) {
			total += m.converter();
		}
		System.out.println("O total convertido para real: " + total);
	}
}
