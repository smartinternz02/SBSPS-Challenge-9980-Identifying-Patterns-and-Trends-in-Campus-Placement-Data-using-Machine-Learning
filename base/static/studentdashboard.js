/*EXCHANGE RATES*/
var data = {
    labels: ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"],
    datasets: [{
        backgroundColor: "rgba(0,0,0,0)",
        borderColor: "rgba(91,37,245, 1)",
        borderWidth: 4.5,
        data: [10.2, 10, 13, 12, 15, 13, 14.5, 11, 13.5, 13, 11],
    }]
};

var options = {
    maintainAspectRatio: false,
    legend: {
        display: false
    },
    scales: {
        yAxes: [{
            stacked: true,
            gridLines: {
                display: true,
                color: "rgba(91,37,245, 0.03)"
            },
            ticks: {
                maxTicksLimit: 5,
                min: 9,
                max: 16
            }
        }],
        xAxes: [{
            gridLines: {
                display: false
            }
        }]
    },
    elements: {
        point: {
            radius: 0
        }
    }
};


var ctx = document.getElementById('exchangeRates').getContext('2d');
var myLineChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: options
});

/*CHECK STAND*/
var data = {
    labels: ["SSC", "HSC", "Aptitude Test", "MBA"],
    datasets: [{
        label: 'Class Average',
        backgroundColor: "rgba(91,37,245, 0.2)",
        data: [100, 30, 80, 15, 20, 15],
    }, {
        label: 'Your Score',
        backgroundColor: "rgba(91,37,245, 1)",
        data: [100, 80, 18, 10, 100],
    }, ]
};

var options = {
    cornerRadius: 0,
    maintainAspectRatio: false,
    legend: {
        position: 'bottom',
        labels: {
            fontColor: "rgba(0,0,0, 0.5)",
            boxWidth: 20,
            padding: 10
        }
    },
    scales: {
        yAxes: [{
            gridLines: {
                display: true,
                color: "rgba(91,37,245, 0.03)"
            },
            ticks: {
                maxTicksLimit: 5,
            }
        }],
        xAxes: [{}]
    }
};


var ctx = document.getElementById('ckeck_stand').getContext('2d');
var myLineChart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: options
});

/*EFFICIENCY CHART*/

var data = {
    labels: ["Placed", "Not Placed", "Avg"],
    datasets: [{
        label: "Population (millions)",
        backgroundColor: ["f10f", "#dad7e9", "#f9f9f9"],
        data: [50, 45, 5]
    }]
};

var options = {
    maintainAspectRatio: false,
    legend: {
        position: 'bottom',
        labels: {
            fontColor: "rgba(0,0,0, 0.5)",
            boxWidth: 20,
            padding: 10
        }
    },
};


var ctx = document.getElementById('efficiency').getContext('2d');
var myLineChart = new Chart(ctx, {
    type: 'doughnut',
    data: data,
    options: options
});