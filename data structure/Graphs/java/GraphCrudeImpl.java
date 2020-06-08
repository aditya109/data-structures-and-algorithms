import java.util.LinkedList;

public class GraphCrudeImpl {
    int vertices;
    LinkedList<Integer> adjList[];

    public GraphCrudeImpl(int vertices){
        this.vertices = vertices;
        adjList = new LinkedList[vertices];

        for(int i = 0; i<vertices; i++) {
            adjList[i] = new LinkedList<>();
        }
    }
    void addEdge(int source, int destination) {
        adjList[source].add(destination);
        adjList[destination].add(source);

    }   
    void displayGraph() {
        for(int i=0; i<vertices; i++) {
             if(adjList[i].size()>0) {
                 System.out.println("Vertex "+i+" is connected to:-");
                 for(int j = 0; j<adjList[i].size(); j++) {
                     System.out.print(adjList[i].get(j)+ " ");
                 }
                 System.out.println();
             }
        }
    }
    public static void main(String[] args) {
        GraphCrudeImpl g = new GraphCrudeImpl(3);
        g.addEdge(0, 1);
        g.addEdge(2, 1);
        g.addEdge(2, 0);
        g.displayGraph();
    }
}