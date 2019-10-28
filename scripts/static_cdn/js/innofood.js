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
    })
});

let fillOrderList = () => {
    orderList.forEach((order, index) => {
        let li = document.createElement('li');
        total += parseInt(order[1]);
        li.innerHTML = `${order[0]} | ${order[1]} <i onclick="deleteDish(${index})" class="fas fa-trash" style="float: right"></i>`;
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

document.querySelector('.cartSubmit').addEventListener('click', () => {
    document.querySelector('.dish-main').style.display = 'none';
    document.querySelector('.my-order').style.display = 'block';

    fillOrderList();

});

