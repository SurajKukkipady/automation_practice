//declarative function

function helloOne(){
    console.log("Hello One");
}

helloOne();

// Anonymous function

const helloTwo = function(){
    console.log("Hello Two");
}

helloTwo();

// Difference between declarative and anonymous function is that in declarative function 
// we can call the function before its declaration but in anonymous function we cannot 
// call the function before its declaration.

// ES6 Arrow function

var helloThree = () => {
    console.log("Hello Three");
}

helloThree();

//Function with arguments

function printName(name){
    console.log("Hello " + name);
}

printName("John");

// Function with return

function multiplyByTwo(num){
    var result = num * 2;
    return result;
}

var myResult = multiplyByTwo(5);
console.log(myResult);