public class ShapeQuestion {

	public static void main(String[] args) {
	    Circle c1 = new Circle(2);
	    Circle c2 = new Circle(3);
	    Rectangle r1 = new Rectangle(2,3);
	    Rectangle r2 = new Rectangle(3,1);
		
	    System.out.printf("%s%n%s%n%s%n%s%n",c1,c2,r1,r2);
	    
	    Object[] shapes = {c1,c2,r1,r2};
	    for (Object o: shapes) {
	      System.out.println(o);
	    }
	    
	    double totalArea=0.0;
	    for (Object o: shapes) {
	      totalArea += o.getArea();
	    }
	    System.out.printf("Total area of the shapes is: %4.2f%n",totalArea);
	    
	}

}