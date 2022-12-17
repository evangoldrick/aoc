import java.util.HashMap;

public class NodeDirectory extends Node {
    private HashMap<String, Node> children = new HashMap<>();

    public NodeDirectory(String name, NodeDirectory parent) {
        super(name, parent);
    }

    public HashMap<String, Node> getChildMap() {
        return this.children;
    }

    public NodeDirectory traverse(String dir) {
        if (dir.equals("/")) {
            NodeDirectory current = this;
            while (current.getParent() != null) {
                current = current.getParent();
            }
            return current;
        } else if (dir.equals("..")) {
            return this.parent;
        } else {
            return (NodeDirectory) children.get(dir);
        }
    }

    public int calculateSize() {
        this.size = 0;
        for (Node child : this.children.values()) {
            this.size += child.calculateSize();
        }
        return this.size;
    }

    public int getSize() {
        return this.size;
    }

    public String toTree(int depth) {
        String ret = name + " (dir)\n";
        for (Node n : children.values()) {
            for (int i = 0; i < depth + 1; ++i) {
                ret += "    ";
            }
            ret += n.toTree(depth + 1) + "\n";
        }
        return ret;
    }

    @Override
    public String toString() {
        return String.format("NodeDirectory(name=%s, size=%d)", this.name, this.size);
    }

    @Override
    public String getType() {
        return new String("Directory");
    }
}
