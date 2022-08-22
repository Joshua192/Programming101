public class likePost {
    public static int likePhoto(int currentLikes, String comment, boolean like) {

         n
        System.out.println("Feedback: " + comment);
        if (like) {
            currentLikes += 1;
        }
        System.out.println("Number of likes:" + currentLikes);
        return currentLikes;
    }
}
