let shirts = [];

const cardContainer = document.querySelector('#cards');
const button = document.querySelector('button');

button.addEventListener('click', search);

fetch("json/shirts.json") // https://stackoverflow.com/questions/7346563/loading-local-json-file
  .then(response => response.json())
  .then(data => {
    shirts = data.products;
    renderShirts(shirts);
  })

function search() {
  const shirtQuery = document.querySelector('#search').value.toLowerCase();

  const filteredShirts = shirts.filter(shirt => {
    return (
      shirt.name.toLowerCase().includes(shirtQuery) ||
      shirt.description.toLowerCase().includes(shirtQuery) ||
      shirt.tags.some(tag => tag.toLowerCase().includes(shirtQuery)) ||
      shirt.colors.some(tag => tag.toLowerCase().includes(shirtQuery))
    );
  });

  renderShirts(filteredShirts);
}

function renderShirts(shirtArray) {
  cardContainer.innerHTML = ''; // reset html

  shirtArray.forEach(product => {
    const isInStock = product.inStock ? "IN STOCK" : "OUT OF STOCK";

    const itemCard = `
      <div class="card">
        <h6>${product.name}</h6>
        <img src="${product.imageUrl}" alt="${product.name}">
        <div class="item-text-box">
          <p>${product.description}</p>
          <div class="left-right">
            <p>$${product.price}</p>
            <p>${isInStock}</p>
          </div>
        </div>
      </div>
    `;

    cardContainer.innerHTML += itemCard;
  });
}
