import java.util.Random;

public class pasteBin {
        public static void main(String[] args) {
            //Assume this can have any value from 1 to 7:
            Random rand = new Random();
            int dayOfWeek = rand.nextInt(8-1) + 1;
            String schedule = "";
            switch (dayOfWeek) {
                case 1: schedule = "Gym in the morning.";
                    break;
                case 2: schedule = "Class after work.";
                    break;
                case 3: schedule = "Meetings all day.";
                    break;
                case 4: schedule = "Work from home.";
                    break;
                case 5: schedule = "Game night after work";
                    break;
                case 6: case 7: schedule = "Free!";
                    break;
                default: schedule = "Free!";
                    break;
            }
            System.out.println(dayOfWeek);
            System.out.println(schedule);
        }
}
