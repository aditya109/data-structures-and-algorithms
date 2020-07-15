import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;

class Vertex {
    String label;
    Vertex(String label) {
        this.label = label;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Vertex vertex = (Vertex) o;
        return Objects.equals(label, vertex.label);
    }

    @Override
    public int hashCode() {
        return Objects.hash(label);
    }
}



public class GraphUsingCollections {

    private Map<Vertex, List<Vertex>> adjVertices;

    public GraphUsingCollections(Map<Vertex, List<Vertex>> adjVertices) {
        this.adjVertices = adjVertices;
    }

    public GraphUsingCollections() {

    }

    public Map<Vertex, List<Vertex>> getAdjVertices() {
        return adjVertices;
    }

    public void setAdjVertices(Map<Vertex, List<Vertex>> adjVertices) {
        this.adjVertices = adjVertices;
    }

    void addVertex(String label) {
        adjVertices.putIfAbsent(new Vertex(label), new ArrayList<>());
    }

    void removeVertex(String label) {
        Vertex v = new Vertex(label);
        adjVertices.values().stream().forEach(e->e.remove(v));
        adjVertices.remove(new Vertex((label)));
    }

    void addEdge(String label1, String label2) {
        Vertex v1 = new Vertex(label1);
        Vertex v2 = new Vertex(label2);
        adjVertices.get(v1).add(v2);
        adjVertices.get(v2).add(v1);
    }

    void removeEdge(String label1, String label2) {
        Vertex v1 = new Vertex(label1);
        Vertex v2 = new Vertex(label2);

        List<Vertex> eV1 = adjVertices.get(v1);
        List<Vertex> eV2 = adjVertices.get(v2);

        if (eV1 != null) {
            eV1.remove(v2);
        }

        if (eV2 != null) {
            eV1.remove(v1);
        }
    }

    GraphUsingCollections createGraph() {
        GraphUsingCollections graph = new GraphUsingCollections();
        graph.addVertex("Bob");
        graph.addVertex("Alice");
        graph.addVertex("Mark");
        graph.addVertex("Rob");
        graph.addVertex("Maria");
        graph.addEdge("Bob", "Alice");
        graph.addEdge("Bob", "Rob");
        graph.addEdge("Alice", "Mark");
        graph.addEdge("Rob", "Mark");
        graph.addEdge("Alice", "Maria");
        graph.addEdge("Rob", "Maria");
        return graph;
    }

    List<Vertex> getAdjVertices(String label) {
        return adjVertices.get(new Vertex(label));
    }


}