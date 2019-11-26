// script.js
function promptUser() {  // line 2
  var num = prompt("Please enter number of squares...");
  if (num != null) {
    document.getElementById("demo").innerHTML =
    "You want " + num + " number of squares...";
  }
} // line 8
Array.prototype.memory_card_shuffle = function(){ // line 9
    var i = this.length, j, temp;
    while(--i > 0){
        j = Math.floor(Math.random() * (i+1));
        temp = this[j];
        this[j] = this[i];
        this[i] = temp;
    }
} // line 17
