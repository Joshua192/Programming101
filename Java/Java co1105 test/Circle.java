// package co1105.exam2022;

import java.util.Objects;

/**
 * Concrete class to represent circles.
 * 
 * @author Gilbert Laycock
 * @version $Id: Circle.java 479 2022-05-08 17:17:02Z gtl1 $
 */
public class Circle extends Shape {
	private final int radius;

	/**
	 * Construct a circle object using its radius
	 * 
	 * @param r the radius of the new circle
	 */
	public Circle(final int r) {
		super();
		radius = r;
		// System.out.println(this);
	}

	/**
	 * Calculate the area of the circle
	 * <p>
	 * Use the formula<br>
	 * area = &pi; &times; radius&sup2;
	 * <p>
	 * You can use {@code Math.PI} to get the value of &pi;.
	 * 
	 * @return the area of the circle.
	 */
	@Override
	public double getArea() {
		return Math.PI * radius * radius;
	}

	/**
	 * Calculate the perimeter (circumference) of the circle
	 * <p>
	 * Use the formula<br>
	 * perimeter = 2 &times; &pi; &times; radius.
	 * 
	 * @return the perimeter of the circle.
	 */
	@Override
	public double getPerimeter() {
		return 2 * Math.PI * radius;
	}

	/**
	 * Returns a string representation for the Circle.
	 * <p>
	 * Should be of the form: "Circle: r=RR" where RR is the radius of the circle.
	 * For example, if the radius is 5, return "{@code Circle: r=5}"
	 * 
	 * @return a string representation for the Circle.
	 */
	@Override
	public String toString() {
		return String.format("Circle: r=%d", radius);
	}
}