package july.twentyFirst;

public class HideAndSeek {
    public static int seek(int start, int end){
        // 1칸 앞으로, 1칸 뒤로, 현재 위치 두배
        boolean[] visited = new boolean[100];
        int level = 0;
        if(start == end)
            return level;
        else {
            level++;
        }
        // level 0, up/down/jump
        // level 1, up/down/jump...
        System.out.println("check");

        start = up(start, visited);
        System.out.println(visited[5]);
        System.out.println(visited[6]);
        System.out.println(visited[10]);
        start = down(start, visited);
        System.out.println(start);
        System.out.println(visited[5]);
        System.out.println(visited[6]);
        System.out.println(visited[10]);
        start = jump(start, visited);
        System.out.println(start);
        System.out.println(visited[5]);
        System.out.println(visited[6]);
        System.out.println(visited[10]);

        return start;
    }

    public static int up(int start, boolean[] visited){
        start = start+1;
        visited[start] = true;
        return start;
    }

    public static int down(int start, boolean[] visited){
        start = start-1;
        visited[start] = true;
        return start;
    }

    public static int jump(int start, boolean[] visited){
        start = start*2;
        visited[start] = true;
        return start;
    }

}
