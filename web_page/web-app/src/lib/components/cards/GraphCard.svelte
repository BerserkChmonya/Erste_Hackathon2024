<script lang="ts">
    import * as Card from "$lib/components/ui/card";
    import Chart from '$lib/components/Chart.svelte';
    // import Combobox from '$lib/components/Combobox.svelte';
    import annotationPlugin from 'chartjs-plugin-annotation';
    import Chartjs from 'chart.js/auto';
    import { createEventDispatcher } from 'svelte';

    // Create dispatcher to emit events
    const dispatch = createEventDispatcher();

    // Handle selection change
    function handleSelectionChange(selectedValue) {
        dispatch('selectionChange', selectedValue);
    }

    export let data;
    let name = Object.keys(data)[0];
    console.log('\n\ndata')
    console.log(data[name].months)

    // Register the annotation plugin
    Chartjs.register(annotationPlugin);

    // Define the data for the chart
    const lineChartData = {
        labels: data[name].months, // X-axis (months)
        datasets: [
            {
                label: name,               // Label for the dataset
                data: data[name].y, // Y-axis (amounts)
                borderWidth: 2,
                fill: true,                     // Fill under the line
                tension: 0.3,                   // Smooth the line
                segment: {
                    // Custom segment logic based on data point index
                    borderColor: (ctx) => {
                        const index = ctx.p0DataIndex; // Get the starting index of the segment
                        const currentMonthIndex = 5; // Example: Current month is June (index 5)
                        
                        return index < currentMonthIndex ? 'rgba(54, 162, 235, 1)' : 'rgba(255, 99, 132, 1)';
                    },
                    backgroundColor: (ctx) => {
                        const index = ctx.p0DataIndex;
                        const currentMonthIndex = 5;
                        
                        return index < currentMonthIndex ? 'rgba(54, 162, 235, 0.2)' : 'rgba(255, 99, 132, 0.2)';
                    },
                    borderDash: (ctx) => {
                        const index = ctx.p0DataIndex;
                        const currentMonthIndex = 5;
                        return index < currentMonthIndex ? [] : [6, 6]; // Solid before current month, dashed after
                    }
                },
            }
        ]
    };

    // Define options for customization
    const lineChartOptions = {
        responsive: true,
        plugins: {
            legend: {
                display: true,
            },
            annotation: {
                annotations: {
                    // Vertical dashed line at the current month
                    line1: {
                        type: 'line',
                        xMin: 5,   // Position the line at the current month (June)
                        xMax: 5,
                        borderColor: 'black',      // Line color
                        borderWidth: 2,
                        borderDash: [5, 5],        // Dashed line pattern
                        label: {
                            content: 'Now',          // Label text for the line
                            enabled: true,
                            position: 'top'
                        }
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Sales'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Months'
                }
            }
        }
    };

    const ComboboxData = [
     {
      value: "mazik",
      label: "Mazik",
     },
     {
      value: "chlieb",
      label: "Chlieb",
     },
     {
      value: "red_bull",
      label: "Red Bull",
     },
     {
      value: "monster",
      label: "Monster",
     },
     {
      value: "bebra",
      label: "Bebra",
     },
    ];
</script>

<Card.Root>
    <Card.Header>
        <Card.Title>Sells Prediction</Card.Title>
    </Card.Header>
    <Card.Content>
        <div class="w-full h-full border-2 rounded-lg">
            <Chart {lineChartData} {lineChartOptions} />
        </div>
        <!-- <div class="mt-4">
            <Combobox {ComboboxData} company={data.company} selectedValue={data.selectedValue}
            on:selectionChange={(e) => handleSelectionChange(e.detail)}/>
        </div> -->
    </Card.Content>
</Card.Root>
