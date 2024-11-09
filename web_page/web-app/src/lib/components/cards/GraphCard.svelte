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
        labels: data[name].months, 
        datasets: [
            {
                label: name,            
                data: data[name].y, 
                borderWidth: 2,
                fill: true,                   
                tension: 0.3,                
                segment: {
                    // Custom segment logic based on data point index
                    borderColor: (ctx) => {
                        const index = ctx.p0DataIndex; 
                        const currentMonthIndex = 2; 
                        
                        return index < currentMonthIndex ? 'rgba(54, 162, 235, 1)' : 'rgba(255, 99, 132, 1)';
                    },
                    backgroundColor: (ctx) => {
                        const index = ctx.p0DataIndex;
                        const currentMonthIndex = 2;
                        
                        return index < currentMonthIndex ? 'rgba(54, 162, 235, 0.2)' : 'rgba(255, 99, 132, 0.2)';
                    },
                    borderDash: (ctx) => {
                        const index = ctx.p0DataIndex;
                        const currentMonthIndex = 2;
                        return index < currentMonthIndex ? [] : [6, 6]; 
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
                        xMin: 2,   
                        xMax: 2,
                        borderColor: 'black',    
                        borderWidth: 2,
                        borderDash: [5, 5],    
                        label: {
                            content: 'Now',     
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
