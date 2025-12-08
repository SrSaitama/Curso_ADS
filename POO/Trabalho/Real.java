package Curso_ADS.POO.Trabalho;

public class Real extends Moeda{

	public Real(double valor) {
		super(valor);
	}

	@Override
	public void info() {
		System.out.println("Real:" + valor);
		
	}

	@Override
	public double converter() {
		return valor;
	}
  @Override
	public double valor() {
		return valor;
	}

}
