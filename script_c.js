document.addEventListener('DOMContentLoaded', function () {
    // Example script to render a chart using Chart.js
    const ctx = document.getElementById('performanceChart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'bar', // Specify the type of chart
        data: {
            labels: ['NICHOLAS POORAN', 'UNMUKT CHAND', 'FINN ALLEN','MATTHEW SHORT','SHAKIB AL HASAN'],
            datasets: [{
                label: 'Runs',
                data: [106,68,63,58,53],
                backgroundColor: ['red', 'blue', 'green','pink','purple'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(75, 192, 192, 1)','rgba(78, 40, 145, 8)','rgba(201, 255, 6, 1)'],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
