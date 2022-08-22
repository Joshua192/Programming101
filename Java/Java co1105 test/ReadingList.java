// Q3(a)
public class ReadingList {
	private String moduleCode;
	private Book[] books;
	
	public ReadingList(String n, Book[] bks) {
		moduleCode = n;
		books = bks;
	}
	
	public String getModCode() {
		return moduleCode;
	}
	
	public Book getBook(int n) {
		return books[n];
	}
	
	public Book[] getAllBooks() {
		return books;
	}
	
	public String toString() {
		String aList = "";
		for (int x = 0; x < books.length; x++) {
			aList = aList + books[x].toString() + "\n";
		}
		return String.format("%s: %n%s", moduleCode, aList);
	}
}

// Q3(b)
public static Book findNewest(ReadingList rl) {
	Book newest = null;
	int solutionYear = 0;
	Book[] rList = rl.getAllBooks();
	
	for (int x = 0; x < rList.length; x++) {
		if (rList[x].getYear() > solutionYear) {
			solutionYear = rList[x].getYear();
			newest = rList[x];
		}
	}

	return newest;
}