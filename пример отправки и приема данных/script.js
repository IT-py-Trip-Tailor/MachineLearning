document.getElementById('recommendation-form').addEventListener('submit', function(e) {
    e.preventDefault();

    let from = document.getElementById('from').value;
    let to = document.getElementById('to').value;
    let budget = document.getElementById('budget').value;
    // собрать все остальные данные формы

    let data = {
        'from': from,
        'to': to,
        'budget': budget,
        // остальные данные
    };

    fetch('http://localhost:5000/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // вывод рекомендаций
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
