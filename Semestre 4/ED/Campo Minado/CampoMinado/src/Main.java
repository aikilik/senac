public class Main {
    public static void main(String[] args) {
        Celula e1 = new Celula();
        Celula e2 = new Celula();
        e1.adicionarVizinhos(e1);
        e2.minar();
        System.out.println(e1.numMinasVizinhos());
    }
}