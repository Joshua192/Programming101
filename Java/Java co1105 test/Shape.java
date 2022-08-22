// package co1105.exam2022;

/**
 * Abstract class to represent shapes.
 * 
 * @author Gilbert Laycock
 * @version $Id: Shape.java 479 2022-05-08 17:17:02Z gtl1 $
 */
abstract public class Shape {
	private static int shapeCounter = 0;
	protected final int shapeID;
	
	public Shape() {
		shapeID = ++shapeCounter;
	}
	
	/**
	 * Return the ID number of the shape
	 * @return the ID number of the shape
	 */
	public int getID() {
		return shapeID;
	}
	
	/**
	 * Return the area of the shape
	 * 
	 * @return the area of the shape
	 */
	abstract public double getArea();

	/**
	 * Return the perimeter of the shape
	 * <p>
	 * The perimeter is the total length of all the edges of the shape.
	 * 
	 * @return the perimeter of the shape
	 */
	abstract public double getPerimeter();

	/**
	 * Returns a string representation for the shape.
	 * 
	 * @return a string representation for the shape.
	 */
	@Override
	abstract public String toString();
}