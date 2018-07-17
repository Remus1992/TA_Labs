// class Human {
//   constructor() {
//     this.gender = 'male';
//   }
//
//   printGender(){
//     console.log(this.gender);
//   }
// }
//
// class Person extends Human {
//   constructor() {
//     super();
//     this.name = 'max';
//     this.gender = 'female';
//   }
//
//   printMyName() {
//     console.log(this.name);
//   }
// }
//
// const person = new Person();
// person.printMyName();
// person.printGender();

//ES6/ Babel
class Human {
  gender = 'male';

  printGender = () => {
    console.log(this.gender);
  }
}

class Person extends Human {
  name = 'max';
  gender = 'female';

  printMyName = () => {
    console.log(this.name);
  }
}

const person = new Person();
person.printMyName();
person.printGender();