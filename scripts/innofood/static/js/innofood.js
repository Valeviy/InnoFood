let buttons = document.querySelectorAll('.addToCart');
let orderList = [];
let total = 0;
let orderListing = document.querySelector('.orderListing');


buttons.forEach((button) => {
    button.addEventListener('click' , (e) => {
        let id = e.target.closest('.row').children[0].innerHTML;
        let dish = e.target.closest('.row').children[1].innerHTML;
        let price = e.target.closest('.row').children[2].innerHTML;
        orderList.push([id,dish,price]);
        fillOrderList();
    })
});

let fillOrderList = () => {
    total = 0;
    orderListing.innerHTML = '';
    orderList.forEach((order, index) => {
        let li = document.createElement('li');
        li.className = 'order_item';
        total += parseInt(order[2]);
        li.innerHTML = `${order[1]} <i onclick="deleteDish(${index})" class="fas fa-trash" style="float: right; font-size: 15px!important;"></i>`;
        orderListing.appendChild(li);
    });

    document.querySelector('.total').innerHTML = `Total: ${total} rub`;
};

let deleteDish = (index) => {
    orderList.splice(index,1);
    orderListing.innerHTML = "";
    total = 0;
    fillOrderList();
};

fillOrderList();
