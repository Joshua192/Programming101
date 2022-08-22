// package co1105.exam2022;

import java.util.Objects;

/**
 * Concrete class to represent Rectangles.
 * 
 * @author Gilbert Laycock
 * @version $Id: Rectangle.java 479 2022-05-08 17:17:02Z gtl1 $
 */
class Rectangle extends Shape {
	private final int width;
	private final int height;

	/**
	 * Construct a Rectangle object using its 2 dimensions
	 * <p>
	 * Regardless of the order they are supplied as arguments, identify the smaller
	 * dimension as the "width" and the larger dimension as the "height".
	 * 
	 * @param l1 one dimension of the rectangle
	 * @param l2 second dimension of the rectangle
	 */
	public Rectangle(final int l1, final int l2) {
		width = Math.min(l1, l2);
		height = Math.max(l1, l2);
		// System.out.println(this);
	}

	/**
	 * Calculate the area of the rectangle
	 * <p>
	 * Use the formula<br>
	 * area = height &times; width
	 * <p>
	 * 
	 * @return the area of the rectangle.
	 */
	@Override
	public double getArea() {
		return (double) height * width;
	}

	/**
	 * Calculate the perimeter of the rectangle
	 * <p>
	 * Use the formula<br>
	 * perimeter = 2 &times; (height + width).
	 * 
	 * @return the perimeter of the rectangle.
	 */
	@Override
	public double getPerimeter() {
		return (double) 2 * (height + width);
	}

	/**
	 * Returns a string representation for the Rectangle
	 * <p>
	 * 
	 * Should be of the form: "Rectangle: WxH" where H and W are the height and
	 * width of the rectangle. For example, if the height and width are 10 and 5:
	 * "{@code Rectangle: 5x10}"
	 * 
	 * @return a string representation for the Rectangle.
	 */
	@Override
	public String toString() {
		return String.format("Rectangle: %dx%d", width, height);
	}
}