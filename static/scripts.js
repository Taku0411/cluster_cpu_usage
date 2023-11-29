async function fetchHosts()
{
  const response = await fetch(`/hosts`);
  const data = await response.json();
  console.log(data)
  return data;
}


async function fetchHostData(host) {
  const response = await fetch(`/cpu_usage?host=${host}`);
  const data = await response.json();
  console.log(data);
  return data;
};

async function createCharts(hosts) {
  const chartsContainer = document.getElementById("chartContainer");

  hosts.forEach(async (host) => {
    const chartCanvas = document.createElement("canvas");
    chartCanvas.width = 400;
    chartCanvas.height = 200;
    chartsContainer.appendChild(chartCanvas);

    //drawEmptyChart(chartCanvas);
    await fetchAndDrawChart(host, chartCanvas);
  });
}

async function fetchAndDrawChart(host, canvas) {
  const response = await fetch(`/cpu_usage?host=${host}`);
  const host_data = await JSON.parse(response.json());
  drawChart(host_data, canvas);
}

async function drawEmptyChart(canvas)
{
  drawChart([], canvas);
}

function drawChart(host_data, canvas) {
  new Chart(canvas,
    {
      type: "bar",
      data:
      {
        labels: Array.from({length: host_data.cpu_percent_per_core.length}, (_, i) => `Core ${i + 1}`),
        datasets: [
          {
            data: host_data.cpu_percent_per_core || [],
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
            fill: false
          }]
      },
      options: {
        legend: {
          display: false
        },
        responsive: true,
        maintainAspectRatio: true,
        scales: {
          y: {
            min: 0,
            max: 100
          }
        }
      }
    });
}

async function initialize()
{
  const hosts = await fetchHosts();
  await createCharts(hosts);
}

initialize();
