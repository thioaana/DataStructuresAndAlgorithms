
package myapp;

import java.util.ArrayList;
import java.util.Scanner;

public class Graph {
    private int numOfVertices;
    private static ArrayList<Integer>[] graph;
    private static ArrayList<Integer>[] weights;
      
    public Graph(int n){
        numOfVertices = n;
        graph = new ArrayList[n];
        weights = new ArrayList[n];
    }
    
    // Import an Edge e from Vertex v to Vertex e
    public static void importEdge(int u, int v, int w){
       graph[u].add(v);
       weights[u].add(w);
    }
    
    public static void main(String[] args){
        Integer[] m = new Integer[5];
        for ()
    }
}
