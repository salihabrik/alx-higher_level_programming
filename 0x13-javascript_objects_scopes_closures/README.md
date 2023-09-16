# JavaScript object basics

# Object basics
An object is a collection of related data and/or functionality. These usually consist of several variables and functions (which are called properties and methods when they are inside objects). Let's work through an example to understand what they look like.

To begin with, make a local copy of our oojs.html file. This contains very little — a <script> element for us to write our source code into. We'll use this as a basis for exploring basic object syntax. While working with this example you should have your developer tools JavaScript console open and ready to type in some commands.

|JS               |
|------------|
|const person = {};|

Now open your browser's JavaScript console, enter person into it, and press Enter/Return. You should get a result similar to one of the below lines:
```
[object Object]
Object { }
{ }
```

Congratulations, you've just created your first object. Job done! But this is an empty object, so we can't really do much with it. Let's update the JavaScript object in our file to look like this:

|   JS |
|--|
```
const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf: function () {
    console.log(`Hi! I'm ${this.name[0]}.`);
  },
};
```
After saving and refreshing, try entering some of the following into the JavaScript console on your browser devtools:

|JS|
|--------------------|
```
person.name;
person.name[0];
person.age;
person.bio();
// "Bob Smith is 32 years old."
person.introduceSelf();
// "Hi! I'm Bob."
```
You have now got some data and functionality inside your object, and are now able to access them with some nice simple syntax!

