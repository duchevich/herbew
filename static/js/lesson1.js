les1.classList.add('active');
 	
 function compareRandom(a, b) { //перемішування масиву
  return Math.random() - 0.5;
}

var arr = ['Алеф', 'Бэт / Вэт', 'Гимель', 'Далет', 'Хе', 'Вав', 'Заин', 'Хет', 'Тет', 'Йуд', 'Каф / Хаф', 'Ламед', 'Мем', 'Нун', 'Самех', 'Аин', 'Пэ / Фэ', 'Цади', 'Коф', 'Рейш', 'Шин / Син', 'Тав'];
var count = 0;
arr.sort(compareRandom);
//alert(arr);


game.onclick = function(){
	stop = document.getElementById('stop');
	stop.classList.remove('hidden');
	
	$( "#modal_del" ).empty();
	
	if (count === 22){ alert('Win!!!'); location.reload(); return false;}
	
	var game = document.getElementById("game");
	var txt = document.createTextNode('Дальше');
	
	y=game.childNodes[0];
	game.removeChild(y);
	game.appendChild(txt);
	
	
	
	var cell = document.querySelectorAll(".t_img");	//створення коллекцыъ
   // alert(cell);
	var cell_array = Array.prototype.slice.call(cell); //перетворення колекції в масив
	//alert(cell_array);
	var neww = document.getElementById('table_cont');
	
	
	cell_array.sort(compareRandom);


	var l = cell.length;		//видалення масиву літер з таблиці
	for (var i = 0; i < l; i++) {
		
		cell[i].parentNode.removeChild(cell[i]);
	}
	for (var i = 0; i < l; i++) { 	//запис масиву в таблицю
	
		neww.appendChild(cell_array[i]);
	}

	var letter = arr[count];

	
	var title = document.getElementById("tytle");
	var text = document.createTextNode('Найдите букву: ' + letter);
	
	x=title.childNodes[0];
	title.removeChild(x);
	title.appendChild(text);
	title.style.textAlign='left';
	title.style.paddingLeft='20px';
	
	document.getElementById(letter).addEventListener("click", function(){ count += 1; 
	
	
	var correct = document.getElementById("tytle");
	var text_correct = document.createTextNode('Правильно!');
	
	node=correct.childNodes[0];
	correct.removeChild(node);
	correct.appendChild(text_correct);
	});
	document.getElementById('stop').addEventListener("click", function(){
		//alert('Game over! Your count= ' + count + ' !');
		location.reload();
		
	});
};
