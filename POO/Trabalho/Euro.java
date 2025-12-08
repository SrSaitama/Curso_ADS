package Curso_ADS.POO.Trabalho;

public class Euro extends Moeda{

	public Euro(double valor) {
		super(valor);
	}

	@Override
	public void info() {
		System.out.println("Euro:" + valor);

	}

	@Override
	public double converter() {
		double total = valor * 6.19;
		return total;
	}

  @Override
	public double valor() {
		return valor;
	}
}
