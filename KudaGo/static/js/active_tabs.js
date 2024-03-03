// $(document).ready(function() {
// 	$('#tabs .btn').on('click', function() {
// 		$('.container .block').removeClass('active');
//     $(this).addClass('active');
// 	});
// });
// Получаем контейнерный элемент
const btnContainer = document.getElementById("myDIV");

// Получаем все кнопки с классом "btn" внутри контейнера
const btns = btnContainer.getElementsByClassName("btn");

// Проходим по кнопкам и добавляем активный класс к текущей/нажатой кнопке
for (let i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    const current = document.getElementsByClassName("active");

    // Если активного класса нет
    if (current.length > 0) {
      current[0].className = current[0].className.replace(" active", "");
    }

    // Добавляем активный класс к текущей/нажатой кнопке
    this.className += " active";
  });
}
