import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }
        // Integer[] sorted = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(nums);
        System.out.println(nums[k]);
    }
}