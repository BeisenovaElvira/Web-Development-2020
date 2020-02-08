let box = document.querySelector('.toDo');
let input = document.querySelector('.input_text');
let btn = document.querySelector('.add');






function addElement() {


¬		alert("Wrong");
}

	else{
	let div = document.createElement("div");
	div.className="one_thing";

	let label = document.createElement("label");
	label.className = "new_text";

	let check = document.createElement("input");
	check.type = "checkbox";
	check.className = "checkbox";
	
	let span = document.createElement("span");
	span.innerHTML = input.value;

    let image = document.createElement("img");
    image.className = "input_img";
    image.src = "https://img.icons8.com/metro/26/000000/trash.png";
    image.addEventListener('click', remove, false);
	

	box.appendChild(div);
	div.appendChild(label);
	label.appendChild(check);
	label.appendChild(span);
	div.appendChild(image);

    input.value = null;
}
}

	function remove(){
    this.parentNode.remove();
};

var divs = document.querySelectorAll('.one_thing');
var button = document.querySelectorAll('.input_img');

for (var i = 0, len = divs.length; i < len; i++) {
    button[i].addEventListener('click', remove, false);
}