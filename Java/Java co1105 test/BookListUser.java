public class BookListUser {
    public static Book findNewest(ReadingList rl) {
      Book newest = null;
      // add code here
      return newest;
    }
    public static void main(String[] args) {
      Book b1 = new Book("Java in a Nutshell, 7th edition","Evans and Flanagan", 2018);
      Book b2 = new Book("Program Development in Java", "Liskov and Guttag", 2000);
      Book b3 = new Book("Using UML, 2nd edition","Stevens and Pooley", 2006);
      
      ReadingList rlist1 = new ReadingList("CO1003",new Book[] {b1,b2,b3});
      System.out.println(rlist1);
      Book newest = findNewest(rlist1);
      System.out.printf("The newest book is %s%n",newest);
    }
  }