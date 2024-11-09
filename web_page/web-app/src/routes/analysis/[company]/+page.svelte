<script>
    import GraphCard from '$lib/components/cards/GraphCard.svelte';
    import * as Card from "$lib/components/ui/card";
    import PairsCard from '$lib/components/cards/PairsCard.svelte';
    import ArrangementCard from '$lib/components/cards/ArrangementCard.svelte';
    import {Button} from '$lib/components/ui/button/index.js';

    export let data;

    let popularProductsData = data.popularProductsData;
    let popularCategoriesData = data.popularCategoriesData;
    let pairsData = data.pairsData;
    let predictionsData = data.predictionsData;
    let isLoading = data.isLoading;

    let selectedValue = data.selectedValue;
    let bestToSellData = data.bestToSellData;

    $: product_index = 2;

    function increment() {
        if (product_index >= predictionsData.length - 1) {
            product_index = 0;
        }
        else {
            product_index += 1;
        }
    }

    function decrement() {
        if (product_index <= 0) {
            product_index = predictionsData.length - 1;
        }
        else {
            product_index -= 1;
        }
    }


    // Handle the selection change event from GraphCard
    function handleSelectionChange(event) {
        selectedValue = event.detail;
    }
    import * as Tabs from "$lib/components/ui/tabs/index.js";
</script>


{#if isLoading}
    <h1>Please Wait. Analyzing...</h1>
{:else}
<div class="h-full w-screen">
    <div class="w-full h-full p-8">
        <h1 class="text-[#1E1E1E] text-4xl">{data?.company}</h1>
        <div class="flex flex-col justify-center items-center mt-10">
            <Tabs.Root value="forecast" class="w-full">
                <Tabs.List>
                  <Tabs.Trigger value="forecast">Demand Forecast</Tabs.Trigger>
                  <Tabs.Trigger value="pairs">Product Pairs</Tabs.Trigger>
                  <Tabs.Trigger value="arrange">Arrangement System</Tabs.Trigger>
                </Tabs.List>
                <Tabs.Content value="forecast">
                    <div class="mt-4">
                        {#key product_index}
                        <GraphCard data={predictionsData[product_index]} on:selectionChange={handleSelectionChange}/>
                        {/key}
                        <div class="w-full flex flex-row  justify-between mt-3">
                            <Button variant="outline" on:click={decrement}>Previous</Button>
                            <Button variant="outline" on:click={increment}>Next</Button>
                        </div>
                        
                    </div>
                </Tabs.Content>
                <Tabs.Content value="pairs">
                    <PairsCard data={pairsData} />
                </Tabs.Content>
                <Tabs.Content value="arrange">
                    <ArrangementCard data={bestToSellData} items={popularProductsData}/>
                    <div class="">

                    </div>
                </Tabs.Content>
              </Tabs.Root>
            </div>
        

        <div class="w-full mt-4">
            <Card.Root>
                <Card.Header>
                    <div class="w-full flex items-center justify-center text-5xl">
                        Recomendations
                    </div>
                </Card.Header>
                <Card.Content>
                    
                </Card.Content>
            </Card.Root>
        </div>
    </div>
</div>
{/if}
