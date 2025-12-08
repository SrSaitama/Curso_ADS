package Curso_ADS.POO.Trabalho;

import java.util.Scanner;

public class Programa {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Cofrinho c = new Cofrinho();
		boolean menu = true;
		
		
		while(true){
			
			try {
				//MENU PRINCIPAL:
				System.out.println("-----COFRINHO-----\n"
						+ "1 - Adicionar moeda\n"
						+ "2 - Remover moeda\n"
						+ "3 - Listar moedas\n"
						+ "4 - Calcular total convertido para Real\n"
						+ "0 - Sair");
				int opc = sc.nextInt();
				
				switch(opc) {
				
					//ADICIONAR MOEDA:
					case 1:
						System.out.println("Escolha a moeda:\n"
											+ "1 - Dólar\n"
											+ "2 - Euro\n"
											+ "3 - Real");
						int e1 = sc.nextInt();

						if(e1==1) {
							System.out.print("Dólar: ");
							double valor = sc.nextDouble();
							
							if (valor <= 0) { 
								System.out.print("Valor inválido"); }
							else { 
								c.adicionar(new Dolar(valor));
							}
							
							
						}if(e1==2) {
							System.out.print("Euro: ");
							double valor = sc.nextDouble();
							
							if (valor <= 0) { 
								System.out.print("Valor inválido"); }
							else { 
								c.adicionar(new Euro(valor));
							}
							
						}if(e1==3) {
							System.out.print("Real: ");
							double valor = sc.nextDouble();
							
							if (valor <= 0) { 
								System.out.print("Valor inválido"); }
							else { 
								c.adicionar(new Real(valor));
							}
						}else {
							System.out.println("Opção inexistente!");
						}
							
					//REMOVER MOEDA:
					case 2:
						System.out.println("Escolha a moeda para remover:\n"
											+ "1 - Dólar\n"
											+ "2 - Euro\n"
											+ "3 - Real");
						int e2 = sc.nextInt();
						
						
						System.out.println("Digite o valor:");
						double remoValor = sc.nextDouble();

						if(e2==1) {
							c.remover(new Dolar(remoValor));									
						}if(e2==2) {
							c.remover(new Euro(remoValor));			
						}if(e2==3) {
							c.remover(new Real(remoValor));
							
						}else {
							System.out.println("Opção inexistente!");			
						
						break;
						}
						
					//LISTAR AS MOEDAS:
					case 3:
						c.listagemMoedas();
						break;
						
					//CONVERTER AS MOEDAS PARA REAL:
					case 4:
						//System.out.printf("O total em reais: ", c.totalConvertido());
						break;
						
					//SAIR DO SISTEMA:
					case 0:
						menu = false;
						
						break;
				
				}
				
				
				
				
				
				
			}catch(Exception e) {
				
				}
			
		}
		
		
		
		

		
		
		
		
		
		
		
		
		

		
	}

}
