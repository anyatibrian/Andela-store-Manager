

var add_pdt_modal = document.getElementById('add-product-modal');
var edit_add_product_modal =document.getElementById('edit-add-product-modal');
var edit_attend_modal = document.getElementById('edit-attend-modal');
var add_attend_modal  = document.getElementById('add-attend-modal');
var cart_modal = document.getElementById('by-product');
/* displaying the edit food modal*/
function displayAddPdtModal(){
    add_pdt_modal.style.display = 'block';

}
/* function display edit product modal boxes */
function displayEditPdtModals() {
    edit_add_product_modal.style.display ='block';
}
/* display the add attend model*/
function displayEditAttendantModals() {
    edit_attend_modal.style.display ='block';
}
/* display the add attend model*/
function displayAddAttendantModals() {
    add_attend_modal.style.display ='block';
}
function displayCartModals() {
    cart_modal.style.display ='block';
}
/* the close modal function */
function closeModal(){
    add_pdt_modal.style.display = 'none';
    edit_add_product_modal.style.display = 'none';

}
function close_attendant_model() {
     edit_attend_modal.style.display ='none';
     add_attend_modal.style.display ='none';
}
function close_cart_modal() {
    cart_modal.style.display ='none';
}