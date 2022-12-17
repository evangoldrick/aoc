import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;
import java.util.Vector;

public class Both {
    static final int FILE_SYSTEM_SIZE = 70000000;
    static final int FILE_SYSTEM_SPACE_NEEDED = 30000000;
    public static Vector<String> readFile(String fileName) {
        Vector<String> fileContents = new Vector<>();
        try {
            File myObj = new File(fileName);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                fileContents.add(myReader.nextLine());
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            throw new RuntimeException(e.toString());
        }
        return fileContents;
    }

    public static Vector<NodeDirectory> findDirsLessThanSize(NodeDirectory dir, int maxSize) {
        Vector<NodeDirectory> ret = new Vector<>();
        if (dir.getSize() < maxSize) {
            ret.add(dir);
        }
        for (Node child : dir.getChildMap().values()) {
            if (child.getType().equals("Directory")) {
                ret.addAll(findDirsLessThanSize((NodeDirectory) child, maxSize));
            }
        }
        return ret;
    }

    public static Vector<NodeDirectory> getAllDirsSorted(NodeDirectory root) {
        Vector<NodeDirectory> ret = new Vector<>();
        Stack<NodeDirectory> nextDirs = new Stack<>();
        
        nextDirs.add(root);
        binaryInsert(ret, (NodeDirectory)root);
        NodeDirectory currentDirectory = null;

        while (nextDirs.size() > 0) {
            currentDirectory = nextDirs.pop();
            for (Node i : currentDirectory.getChildMap().values()) {
                if (i.getType().equals("Directory")) {
                    nextDirs.add((NodeDirectory)i);
                    binaryInsert(ret, (NodeDirectory)i);
                }
            }
        }

        return ret;
    }

    public static void binaryInsert(Vector<NodeDirectory> list, NodeDirectory newVal) {
        int start = 0;
        int end = list.size();
        while (start < end) {
            int mid = ((end - start) / 2) + start;
            if (newVal.getSize() > list.get(mid).getSize()) {
                start = mid + 1;
            } else if (newVal.getSize() < list.get(mid).getSize()) {
                end = mid - 1;
            } else {
                start = mid;
                end = mid;
            }
        }
        int insertionIndex = start;
        if (list.size() > start) {
            if (list.get(start).getSize() < newVal.getSize()) {
                ++insertionIndex;
            }
        }

        list.insertElementAt(newVal, insertionIndex);
    }

    public static void processLsLine(Vector<String> commandOutput, NodeDirectory currentDirectory) {
        if (currentDirectory.getChildMap().size() != 0) {
            System.out.printf("Skipping non empty dir: %s\n", currentDirectory.getName());
        } else {
            for (String line : commandOutput) {
                String[] s = line.split(" ");

                if (s[0].equals("dir")) {
                    currentDirectory.getChildMap().put(s[1], new NodeDirectory(s[1], currentDirectory));
                } else {
                    currentDirectory.getChildMap().put(s[1], new NodeFile(s[1], currentDirectory, Integer.parseInt(s[0])));
                }
            }
        }
    }

    public static NodeDirectory processCdLine(String command, NodeDirectory currentDirectory) {
        String dirName = command.split(" ")[2];
        return currentDirectory.traverse(dirName);
    }


    public static NodeDirectory createTreeStructure(Vector<String> lines) {
        NodeDirectory root = new NodeDirectory("/", null);
        NodeDirectory currentDirectory = root;

        Vector<String> cdOutput = new Vector<>();
        boolean captureOutput = false;

        for (String line : lines) {
            if (line.startsWith("$ cd")) {
                if (captureOutput) {
                    processLsLine(cdOutput, currentDirectory);
                }
                currentDirectory = processCdLine(line, currentDirectory);
                captureOutput = false;
                cdOutput.clear();
            } else if (line.startsWith("$ ls")) {
                if (captureOutput) {
                    processLsLine(cdOutput, currentDirectory);
                }
                captureOutput = true;
                cdOutput.clear();
            } else {
                captureOutput = true;
                cdOutput.add(line);
            }
        }
        if (captureOutput) {
            processLsLine(cdOutput, currentDirectory);
        }
        root.calculateSize();
        return root;
    }

    public static int part1TotalSizeOfFolders(NodeDirectory root) {
        
        //System.out.println(root.toTree());
        int totalSize = 0;
        Vector<NodeDirectory> dirs = findDirsLessThanSize(root, 100000);
        for (NodeDirectory i : dirs) {
            totalSize += i.getSize();
        }

        return totalSize;
    }

    public static NodeDirectory part2SmallestBigDir(NodeDirectory root) {
        Vector<NodeDirectory> allDirs = getAllDirsSorted(root);
        NodeDirectory smallestBigDir = null;
        for (NodeDirectory i : allDirs) {
            int freeSpace = FILE_SYSTEM_SIZE + i.getSize() - root.getSize();
            if (freeSpace >= FILE_SYSTEM_SPACE_NEEDED) {
                smallestBigDir = i;
                break;
            }
        }
        if (smallestBigDir == null) {
            return null;
        }
        return smallestBigDir;
        

    }

    public static void main(String args[]) {
        if (args.length != 1) {
            throw new RuntimeException("Incorrect number of arguments");
        }
        Vector<String> text = readFile(args[0]);

        NodeDirectory rootOfDirectory = createTreeStructure(text);

        int totalSize = part1TotalSizeOfFolders(rootOfDirectory);
        NodeDirectory bestDir = part2SmallestBigDir(rootOfDirectory);
        System.out.printf("Part 1: %d\nPart 2: %s\n", totalSize, bestDir.getSize());
    }
}