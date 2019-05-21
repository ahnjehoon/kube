// Set new default font family and font color to mimic Bootstrap's default styling
//Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
//Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var myPieChart = new Chart(document.getElementById("myPieChart"), {
	type: 'doughnut',
	data: {
		labels: ["유튜브", "트위터"],
		datasets: [{
			data: [20000, 5000],
			backgroundColor: ['#ff0000', '#1da1f2'],
		}],
	},
    options: {
        maintainAspectRatio: false,
		tooltips: {
			backgroundColor: "rgb(255,255,255)",
			bodyFontColor: "#858796",
			borderColor: '#dddfeb',
			borderWidth: 2,
			xPadding: 15,
			yPadding: 15,
			displayColors: true,
			caretPadding: 10,
		},
		legend: {
		},
		cutoutPercentage: 60,
	},
});
