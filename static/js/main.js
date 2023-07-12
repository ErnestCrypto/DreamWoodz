if(document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
} else{
    ready()
}

function ready(){
    var removeBtn = document.getElementsByClassName('rm')
    for (var i = 0; i < removeBtn.length; i++ ){
        var button = removeBtn[i]
        button.addEventListener('click', function(event){
          var buttonClicked = event.target
          buttonClicked.parentElement.parentElement.remove()
          updateCartTotal()
        })
    }


    var quantityInputs = document.getElementsByClassName('cart-quantity-input')
        for (var i = 0; i < quantityInputs.length; i++ ){
            var input = quantityInputs[i]
            input.addEventListener('change', quantityChanged)
    }

    var addToCartBtn = document.getElementsByClassName('add')
        for (var i = 0; i < addToCartBtn.length; i++ ){
            var button = addToCartBtn[i]
            button.addEventListener('click', addToCartClicked)
    }


    document.getElementsByClassName('purchase')[0].addEventListener('click', purchaseClicked)

}

    function purchaseClicked(){
        alert('Thank you for your purchase')
        cartItems = document.getElementsByClassName('cart-items')[0]
        while(cartItems.hasChildNodes()){
            cartItems.removeChild(cartItems.firstChild)
        }
        updateCartTotal()
    }

// modal
var icon = document.querySelector(".cart-img");
var modal = document.querySelector(".container2");
var closeModal = document.querySelector("#close");


icon.addEventListener("click", () => {
    modal.classList.add("show");
  });
  closeModal.addEventListener("click", () => {
    modal.classList.remove("show");
  });


// modal






function addToCartClicked(event){
 var button = event.target
 var shopItem  = button.parentElement
 var title = document.getElementsByClassName('item-title')[0].innerText
 var price = shopItem.getElementsByClassName('shop-item-price')[0].innerText
 var imageSrc = shopItem.getElementsByClassName('image')[0].src
 console.log(title, price, imageSrc) 
 addItemTocart(title, price, imageSrc)
}

function addItemTocart(title, price, imageSrc){
var cartRow = document.createElement('div')
cartRow.classList.add('hori-1')
var cartItems = document.getElementsByClassName('cart-items')[0]
var cartItemNames = cartItems.getElementsByClassName('cart-item-title')
for (var i = 0; i < cartItemNames.length; i++){
 if (cartItemNames[i].innerText == title){
     alert('this item is already in the cart')
     return
 }
}
var cartRowContents = `
                <div class="hori-1">
                    <div class="items">
                        <img src="${imageSrc}" alt="">
                        <p>${title}</p>
                    </div>

                    <div class="price">
                        <p>GH₵<span class="cart-price">${price}</span></p>
                    </div>

                    <div class="quantity">
                        <input type="number" class="cart-quantity-input" name="" id="numb" value='1'>
                        <button class="rm" id="remove">Remove</button>
                    </div>
                </div>
`
cartRow.innerHTML=cartRowContents
cartItems.append(cartRow)
cartRow.getElementsByClassName('rm')[0].addEventListener('click',removeCartItem)
cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', quantityChanged)
}




function removeCartItem(event){
    var buttonClicked = event.target
    buttonClicked.parentElement.parentElement.remove()
    updateCartTotal()
}


function quantityChanged(event){
    var input = event.target
    if(isNaN(input.value) || input.value <= 0 ){
        input.value = 1
    }

    updateCartTotal()
}


function updateCartTotal(){
var cartItemContainer = document.getElementsByClassName('cart-items')[0]
var cartRows = cartItemContainer.getElementsByClassName('hori-1')
var total = 0
for (var i = 0; i < cartRows.length; i++ ){
    var cartRow = cartRows[i]
    var priceElement = cartRow.getElementsByClassName('cart-price')[0]
    var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
    var price = parseFloat(priceElement.innerText)
    var quantity = quantityElement.value
    total = total + (price * quantity)
}
document.getElementsByClassName('sum')[0].innerText = total

}




// forms



