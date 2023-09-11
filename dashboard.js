// Simulated data for the table
const data = [
    { id: 1, name: 'Item 1', value: 'Value 1' },
    { id: 2, name: 'Item 2', value: 'Value 2' },
    { id: 3, name: 'Item 3', value: 'Value 3' }
];

// Function to display data in the table
function displayData() {
    const filterValue = document.getElementById('filter').value;
    const searchValue = document.getElementById('search').value.toLowerCase();
    const tableBody = document.getElementById('data');
    tableBody.innerHTML = '';

    data.forEach(item => {
        if (filterValue === 'all' || filterValue === item.value) {
            if (item.name.toLowerCase().includes(searchValue)) {
                const row = document.createElement('tr');
                row.innerHTML = `<td>${item.id}</td><td>${item.name}</td><td>${item.value}</td>`;
                tableBody.appendChild(row);
            }
        }
    });
}

// Event listeners for filter and search
document.getElementById('filter').addEventListener('change', displayData);
document.getElementById('search').addEventListener('input', displayData);

// Initial data display
displayData();
