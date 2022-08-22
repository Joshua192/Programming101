public class Car {
        private final String registration;
        private final double efficiency; // fuel efficiency in litres/km
        private final double capacity; // fuel capacity in litres
        private double fuel; // current fuel level in litres
        public Car(String reg, double eff, double cap) { registration = reg;
            efficiency = eff; // in litres/km
            capacity = cap; // in litres
            fuel = 0.0;
        }
        public String getRegistration() {
            return registration;
        }
        public double getFuel() {
            return fuel;
        }
        public double getRange() {
// calculate current range based on the efficiency and
// current fuel level
            return fuel / efficiency;
        }
        public void addFuel(double moreFuel) throws FuelFillException {
            if (moreFuel<=0) {
                throw new FuelFillException("Fuel cannot be zero.");
            } else if (moreFuel+this.fuel>capacity) {
                throw new FuelFillException("Fuel cannot be above the maximum capacity.");
            } else {
// Add more fuel
                this.fuel += moreFuel;
            }
            }
        public void drive(double distance) {
// drive (and use some fuel)
            double usedFuel = efficiency * distance;
            fuel -= usedFuel;
        }
        public String toString() {
            return String.format("%s range: %6.2f km", registration, getRange());
        }
    }


