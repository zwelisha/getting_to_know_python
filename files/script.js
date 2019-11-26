var memory_array = ['A', 'A','B','B','C','C','D','D','E','E','F','F','G','G','H','H','I','I','J','J','K','K','L','L'];   //content hiding uder each card
var memory_values = [];
var memory_card_ids = [];
var correctGuess;
var card = 0; //cards flipped

function promptUser() {
  var num = prompt("Please enter number of squares...");
  if (num != null) {
    document.getElementById("demo").innerHTML =
    "You want " + num + " number of squares...";
  }
}

Array.prototype.memory_card_shuffle = function(){ // shuffling method / putting array to a shuffle method
    var i = this.length, j, temp;
    while(--i > 0){
        j = Math.floor(Math.random() * (i+1));
        temp = this[j];
        this[j] = this[i];
        this[i] = temp;
    }
}

function newBoard(){ // generate a new board
  cards_flipped = 0;
	var output = '';
  memory_array.memory_card_shuffle(); // run memroy card shuffle method on memory array

	for(var i = 0; i < memory_array.length; i++){ // loop over all the cards
		output += '<div id="card_'+i+'" onclick="memoryFlipCard(this,\''+memory_array[i]+'\')"></div>'; //add to output all child divs representing cards - memory flip card fucntion responsible for fliping the cards over
		//boxes += "<div id='box-" + i + "' class='box-picture'><img src='img/" + (parseInt(boxIndexes[i-1]) + 1) + ".png'/></div>";
  }
	document.getElementById('memory_board').innerHTML = output; // put output into memory board
}

function memoryFlipCard(card,val){

	if(card.innerHTML == "" && memory_values.length < 2){  //check if innerHTML is empty && memory values arraay is less than 2
		card.style.background = '#FFF';
		card.innerHTML = val; //addd value into innerHTML of card

		if(memory_values.length == 0){
			memory_values.push(val); // push value of clicked card into memory value array
			memory_card_ids.push(card.id);   //push id of the card clicked
		} else if(memory_values.length == 1){   //if there is already one card flipped over
			memory_values.push(val);
			memory_card_ids.push(card.id);

			if(memory_values[0] == memory_values[1]){    //check if both cards are a match

				cards_flipped += 2;    //if cards are a match, accumulate card flipped
				// Clear both arrays
				memory_values = [];
        memory_card_ids = [];
				// Check to see if the whole board is cleared

				if(cards_flipped == memory_array.length){    //check if cards flipped is = to the memory board array length
					alert("Board cleared... generating new board");
					document.getElementById('memory_board').innerHTML = "";
					newBoard();    //generate new board
				}
			} else {
				function flip2Back(){
				    // Flip the 2 card back over
				    var card_1 = document.getElementById(memory_card_ids[0]);
				    var card_2 = document.getElementById(memory_card_ids[1]);
				    card_1.style.background = 'url() no-repeat';
            	    card_1.innerHTML = "";
				    card_2.style.background = 'url() no-repeat';
            	    card_2.innerHTML = "";
				    // Clear both arrays
				    memory_values = [];
            memory_card_ids = [];
				}
				setTimeout(flip2Back, 700);   //cards flip back time over half a second
			}
		}
	}
}
