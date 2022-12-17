

public abstract class Node {
    protected String name;
    protected NodeDirectory parent = null;
    protected int size = 0;

    public Node(String name, NodeDirectory parent) {
        this.name = name;
        this.parent = parent;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public NodeDirectory getParent() {
        return (NodeDirectory) this.parent;
    }

    public void setParent(NodeDirectory parent) {
        this.parent = parent;
    }

    @Override
    public String toString() {
        return String.format("NodeDirectory: name=%s, size=%d", this.name, this.size);
    }

    public String toTree() {
        return toTree(0);
    }
    public abstract String toTree(int depth);
    public abstract String getType();
    public abstract int calculateSize();
    public abstract int getSize();
}
