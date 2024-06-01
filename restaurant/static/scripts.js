// Function to fetch and display menu items
function fetchMenu() {
    fetch('/menu')
        .then(response => response.json())
        .then(menu => {
            const menuTable = document.getElementById('menu-table');
            menuTable.innerHTML = '';
            menu.forEach(item => {
                const row = document.createElement('tr');
                row.id = item._id; // Set the id attribute to the dish ID
                row.innerHTML = `
                <td contenteditable="true">${item.name}</td>
                <td contenteditable="true">$${item.price}</td>
                <td>
                    <button onclick="saveChanges('${item._id}', '${item.name}', ${item.price})">Save Changes</button>
                    <button onclick="deleteDish('${item._id}')">Delete</button>
                </td>
            `;
                menuTable.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching menu:', error));
}

// Function to add a new dish
function addDish(event) {
    event.preventDefault();
    const dishName = document.getElementById('dish-name').value;
    const dishPrice = document.getElementById('dish-price').value;
    fetch('/menu', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: dishName,
            price: parseFloat(dishPrice)
        })
    })
        .then(response => response.json())
        .then(response => {
            console.log(response); // Log response from the server
            fetchMenu(); // Fetch updated menu after adding the dish
        })
        .catch(error => console.error('Error adding dish:', error));
}

// Function to save changes to the name and price of a dish
function saveChanges(dishId, currentName, currentPrice) {
    const row = document.getElementById(dishId);
    const cells = row.querySelectorAll('td');
    const newName = cells[0].textContent.trim(); // Get the name from the first cell
    const newPrice = parseFloat(cells[1].textContent.replace('$', '').trim()); // Get the price from the second cell

    if (newName !== currentName) {
        fetch('/menu/change_name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                _id: dishId,
                name: newName,
                price: newPrice
            })
        })
            .then(response => response.json())
            .then(response => {
                console.log(response); // Log response from the server
                fetchMenu(); // Fetch updated menu after saving changes
            })
            .catch(error => console.error('Error saving changes:', error));
    }
    if (newPrice !== currentPrice) {
        fetch('/menu/change_price', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                _id: dishId,
                price: newPrice
            })
        })
            .then(response => response.json())
            .then(response => {
                console.log(response); // Log response from the server
                fetchMenu(); // Fetch updated menu after saving changes
            })
            .catch(error => console.error('Error saving changes:', error));
    }
}

// Function to delete a dish
function deleteDish(dishId) {
    fetch(`/menu/${dishId}`, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(response => {
            console.log(response); // Log response from the server
            fetchMenu(); // Fetch updated menu after deleting the dish
        })
        .catch(error => console.error('Error deleting dish:', error));

}

// Add event listener to the add dish form
document.getElementById('add-dish-form').addEventListener('submit', addDish);

// Fetch menu when the page loads
fetchMenu();
