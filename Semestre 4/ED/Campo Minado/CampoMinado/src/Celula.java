import java.util.ArrayList;

public class Celula {
    // --- os estados que a célula pode assumir
    boolean minado;
    boolean clicado;
    boolean revelado;
    boolean marcado;

    // ---

    // --- verifica os vizinhos em busca de bombas
    // --- é mostrado a quantidade de bombas
    ArrayList<Celula> vizinhos;
    // ---

    // --- estado inicial da célula
    public Celula() {
        this.minado = false;
        this.revelado = false;
        this.marcado = false;
        this.clicado = false;

        this.vizinhos = new ArrayList();
    }
    // ---

    // -- adicionar vizinhos
    public void adicionarVizinhos(Celula e) {
        this.vizinhos.add(e);
    }
    // ---

    // --- método que mina a célula
    // --- se a célula já tem uma mina, ele retorna false
    // --- se o espaço não tinha uma mina antes, retorna verdadeiro
    public boolean minar() {
        if (!this.minado) {
            this.minado = true;
            return true;
        } else {
            return false;
        }
    }
    // ---

    // --- ao clicar, retorna o valor atualizado
    public boolean marcar() {
        this.marcado = !this.marcado;
        return this.marcado;
    }
    // ---

    // indices
    // -1 clicou numa mina
    // 0 não possui minas nos vizinhos
    // n possui n minas nos vizinhos
    public int clicar() {
        this.clicado = true;
        if(this.minado) {
            return -1;
        } else {
            return numMinasVizinhos();
        }
    }

    // navegar pelos vizinhos
    public int numMinasVizinhos() {
        int n = 0;
        for (Celula e : this.vizinhos) { // olha todos os vizinhos da celula
            if(e.minado) n++;
        }
        return n;
    }

    public void reiniciar() {
        boolean minado;
        boolean clicado;
        boolean revelado;
        boolean marcado;
    }
}
