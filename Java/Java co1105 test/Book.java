public class Book {
    private final String title;
    private final String author;
    private final int year;
    public Book (String t, String a, int y) {
      title = t;
      author = a;
      year = y;
    }
    public String getTitle() {
      return title;
    }
    public String getAuthor() {
      return author;
    }
    public int getYear() {
      return year;
    }
    public String toString() {
      return String.format("%s (%d) by %s", title, year, author);
    }
  } 