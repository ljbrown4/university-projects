public class ArrayRecursion {
    public static boolean search(Object item, Object[] arr, int start) {
        if (arr == null ||arr.length == 0 || start > arr.length - 1) {
            return false;
        } else if (arr.length == 1 && arr[0].equals(item)) {
            return false;
        } else {
            boolean rest = search(item, arr, start + 1);
            if (arr[start].equals(item)) {
                return true;
            } else {
                return rest;
            }
        }
    }
    public static String reverseArrayToString(Object [] arr, int index ) {
        if (arr == null || arr.length == 0 || index < 0 || index > arr.length ) {
            return "";
        } else if (index == arr.length - 1) {
            return "[" + arr[index];
        } else {
           String rest = reverseArrayToString(arr, index+ 1);
           if (index == 0) {
                return rest + ", " + arr[index] + "]";
           } else {
            return rest + ", " + arr[index];
           }
        }
    }
    public static void main(String[] args) {
        /*String a[] = { "abc", "def", "ghi", "klm", "nop", "qrs" };
        System.out.println();
        System.out.println(reverseArrayToString(a, 0));
        System.out.println();
        System.out.println();
        /* */
        String[] b={"abc","def","ghi","klm","nop","qrs"};
        System.out.println(search("def",b, 0));
    }
}
