<!-- LineChart.svelte -->
<script>
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';
  
    export let lineChartData;       // Data for the chart
    export let lineChartOptions = {};  // Additional chart options

    console.log(lineChartData);
    console.log(lineChartOptions);
  
    let canvas;            // Canvas element reference
    let chart;             // Chart instance reference
  
    onMount(() => {
      // Initialize the chart
      chart = new Chart(canvas, {
        type: 'line',
        data: lineChartData,
        options: lineChartOptions
      });
  
      // Destroy the chart when component unmounts
      return () => chart.destroy();
    });
  </script>
  
  <canvas bind:this={canvas} class="w-full h-full"></canvas>
  