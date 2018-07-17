var nums = [];

function getSum(total, num) {
   return total + num;
}

var x = true;
while(x) {
   var user_input = prompt('Enter a number, or "done": ');
   if (user_input !== 'done') {
       var number = parseInt(user_input);
       nums.push(number);
   } else if (user_input === 'done')  {
       var i;
       for (i = 0; i < nums.length; i++) {
           var total = nums.reduce(getSum);
           x = false
       }
   }  else {
       console.log("not a valid option.")
   }
}

var average = total / nums.length;
console.log(average);
