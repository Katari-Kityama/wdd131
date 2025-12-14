fetch("json/shirts.json") // https://stackoverflow.com/questions/7346563/loading-local-json-file
  .then(response => response.json())
  .then(data => {
    data.products.forEach(product => {

      let isInStock;

      if (product.inStock === false) {
        isInStock = "OUT OF STOCK";
      } else if (product.inStock === true) {
        isInStock = "IN STOCK";
      }

      const itemCards = `
        <div class="card">
          <h6>${product.name}</h6>
          <img src="${product.imageUrl}">
          <div class="item-text-box">
            <p>${product.description}</p>
            <div class="left-right">
              <p>$${product.price}</p>
              <p>${isInStock}</p>
            </div>
          </div>
        </div>
      `;

      document.getElementById("cards").innerHTML += itemCards;
    });
  })

