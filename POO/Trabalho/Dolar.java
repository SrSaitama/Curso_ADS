package Curso_ADS.POO.Trabalho;

public class Dolar extends Moeda{

	public Dolar(double valor) {
		super(valor);
	}

	@Override
	public void info() {
		System.out.println("Dolar:" + valor);

	}

	@Override
	public double converter() {
		double total = valor * 5.31;
		return total;
	}

  @Override
	public double valor() {
		return valor;
	}

}
