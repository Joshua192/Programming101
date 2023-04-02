class Person { 
    
    constructor(fullname,mass,height) {// creating a class to instantiate the person's 'John' and 'Mark' as objects
        this._fullname = fullname;
        this._mass = mass;
        this._height = height;
    }
    getFirstName() {
        let name_store = this._fullname.split(' ');
        let first_name = name_store[0]
        console.log(first_name);
        return first_name;
    }
    getBMI(){
        let calcBMI = this._mass / this._height ** 2;
        calcBMI = Math.round(calcBMI*10)/10;
        console.log(calcBMI);
        return calcBMI;

    };
    compareBMI(object1,object2) {
        let markBMI = object1.getBMI();
        let johnBMI = object2.getBMI(); 
        const obj1Higher = markBMI > johnBMI;
if (obj1Higher){
    console.log(`Mark's BMI (${markBMI}) is higher than John's!(${johnBMI})!`);}
     else{
        console.log(`John's BMI (${johnBMI}) is higher than Mark's!(${markBMI})!`);
    }}

};

let johnObject = new Person('John Doe',78.0,1.69);
let markObject = new Person('Mark Miller',92,1.95);

// johnObject.getFirstName();
// johnObject.getBMI();
// johnObject.compareBMI(johnObject,markObject)