
public class NodeFile extends Node {

    public NodeFile(String name, NodeDirectory parent, int size) {
        super(name, parent);
        this.size = size;
    }


    public int calculateSize() {
        return this.size;
    }

    public int getSize() {
        return this.size;
    }

    public String toTree(int depth) {
        return String.format("%d %s", this.size, this.name);
    }

    @Override
    public String getType() {
        return new String("File");
    }
}
