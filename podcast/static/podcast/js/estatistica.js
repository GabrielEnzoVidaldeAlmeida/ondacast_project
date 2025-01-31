document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('grafico-barra').getContext('2d');
    const graficoBarra = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            datasets: [{
                label: 'Visualizações Mensais (em milhões)',
                data: [120, 150, 180, 200, 170, 140, 190, 220, 240, 210, 230, 250],
                backgroundColor: '#a078ff',
                borderColor: '#a078ff',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: '#fff'
                    }
                },
                x: {
                    ticks: {
                        color: '#fff'
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#fff'
                    }
                }
            }
        }
    });
});