import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Graph {
    static class Edge {
        int src, dest;

        Edge(int src, int dest) {
            this.src = src;
            this.dest = dest;
        }
    };

    List<List<Integer>> adj = new ArrayList<>();

    public Graph(List<Edge> edges) {
        for (int i = 0; i < edges.size(); i++) {
            adj.add(i, new ArrayList<>());
        }

        for (Edge current : edges) {
            adj.get(current.src).add(current.dest);
            adj.get(current.dest).add(current.src);
        }
    }

    private static void printGraph(Graph graph) {
        int src = 0;
        int n = graph.adj.size();

        while (src < n) {
            for (int dest: graph.adj.get(src))
                System.out.println("("+src+"-->"+dest+")\t");            
            System.out.println();
            src++;            
        }
    }
    public static void main(String[] args) {
        List<Edge> edges = Arrays.asList(new Edge(0, 1))
    }



}