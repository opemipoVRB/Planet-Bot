// Get the elements with class="column"
var elements = document.getElementsByClassName("x_column");

// Declare a loop variable
var i;

// List View
function listView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "60%";

  }
}

// Grid View
function gridView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "50%";
  }
}



//init the modal
function openModal1() {
$('.modal').modal();

}
