package Curso_ADS.POO.Trabalho;

import java.util.Scanner;

public class Programa {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Cofrinho c = new Cofrinho();
		boolean menu = true;

		while (true) {

			try {
				// MENU PRINCIPAL:
				System.out.println("-----COFRINHO-----\n" 
									+ "1 - Adicionar moeda\n" 
									+ "2 - Remover moeda\n"
									+ "3 - Listar moedas\n" 
									+ "4 - Calcular total convertido para Real\n" 
									+ "0 - Sair");
				int opc = sc.nextInt();

				switch (opc) {

				// ADICIONAR MOEDA:
				case 1:
					System.out.println("Escolha a moeda:\n" 
										+ "1 - Dólar\n" 
										+ "2 - Euro\n" 
										+ "3 - Real");
					int e1 = sc.nextInt();

					if (e1 == 1) {
						System.out.print("Dólar: ");
						double valor = sc.nextDouble();

						if (valor <= 0) {
							System.out.print("Valor inválido");
							continue;
						} else {
							c.adicionar(new Dolar(valor));
							continue;
						}

					}
					if (e1 == 2) {
						System.out.print("Euro: ");
						double valor = sc.nextDouble();

						if (valor <= 0) {
							System.out.print("Valor inválido");
							continue;
						} else {
							c.adicionar(new Euro(valor));
							continue;
						}

					}
					if (e1 == 3) {
						System.out.print("Real: ");
						double valor = sc.nextDouble();

						if (valor <= 0) {
							System.out.print("Valor inválido");
							continue;
						} else {
							c.adicionar(new Real(valor));
							continue;
						}
					} else {
						System.out.println("Opção inexistente!");
						continue;
					}

					// REMOVER MOEDA:
				case 2:
					System.out.println("Escolha a moeda para remover:\n" 
										+ "1 - Dólar\n" 
										+ "2 - Euro\n" 
										+ "3 - Real");
					int e2 = sc.nextInt();

					System.out.println("Digite o valor:");
					double remoValor = sc.nextDouble();

					if (e2 == 1) {
						c.remover(new Dolar(remoValor));
						continue;
					}
					if (e2 == 2) {
						c.remover(new Euro(remoValor));
						continue;
					}
					if (e2 == 3) {
						c.remover(new Real(remoValor));
						continue;
					} else {
						System.out.println("Opção inexistente!");
						continue;
					}

					// LISTAR AS MOEDAS:
				case 3:
					c.listagemMoedas();
					continue;

				// CONVERTER AS MOEDAS PARA REAL:
				case 4:
					c.totalConvertido();
					break;

				// SAIR DO SISTEMA:
				case 0:
					System.out.println("Saindo..");
					menu = false;
					break;
					
				default:
					throw new Exception("Opção invalida!");
				}
			} catch (Exception e) {
				//System.out.printf("Erro: " + e.getMessage());
				System.out.printf("Algo deu errado!");
				return;
			}
		}

	}

}
