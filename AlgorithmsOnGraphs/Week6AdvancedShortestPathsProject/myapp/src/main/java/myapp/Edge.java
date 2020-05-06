package myapp;

public class Edge {
    private int node1;
    private int node2;
    private int weight;
    public Edge(int v1, int v2, int w) {
        node1 = v1;
        node2 = v2; 
        weight = w;
    }
    
    public void printEdge(){
        System.out.println(node1 + " -> " + node2 + " : " + weight);
    }

    public static void main(String[] args){
        Edge e = new Edge(1, 2, -3);
        e.printEdge();
    }
}