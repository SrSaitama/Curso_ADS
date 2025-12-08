package Curso_ADS.POO.Trabalho;

public abstract class Moeda {
	
	protected double valor;
	
  @Override
  public boolean equals(Object o) {
      if (this == o) return true;
      if (o == null || getClass() != o.getClass()) return false;

      Moeda moeda = (Moeda) o;
      return Double.compare(moeda.valor, valor) == 0;
  }

  @Override
  public int hashCode() {
      return Double.hashCode(valor);
  }

	public Moeda(double valor) {
		this.valor = valor;
	}

	public abstract void info();
		
	public abstract double converter();

  public abstract double valor();
	
}
