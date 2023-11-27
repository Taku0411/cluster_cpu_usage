// ホストごとのCPU使用率を取得して動的にグラフを生成
fetch('/cpu_usage')
  .then(response => response.json())
  .then(cpuData => {
    const cpuChartsContainer = document.getElementById('cpuChartsContainer');

    // 各ホストごとにグラフを生成
    Object.keys(cpuData).forEach(host_str => {
      const host = JSON.parse(host_str)
      alert(host)
      const chartContainer = document.createElement('div');
      chartContainer.classList.add('col');

      const chartTitle = document.createElement('div');
      chartTitle.textContent = `${host.hostname}`;
      chartTitle.textAlign = "center";
      chartContainer.appendChild(chartTitle);

      const canvas = document.createElement('canvas');
      chartContainer.appendChild(canvas);

      cpuChartsContainer.appendChild(chartContainer);

      // ホストごとのCPU使用率のグラフを生成
      new Chart(canvas.getContext('2d'), {
        type: 'bar',
        data: {
          labels: Array.from({length: host.cpu_percent_per_core.length}, (_, i) => `Core ${i + 1}`),
          datasets: [{
            data: host.cpu_percent_per_core,
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
    });
  });

