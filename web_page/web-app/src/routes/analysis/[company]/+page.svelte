<script>
    import GraphCard from '$lib/components/cards/GraphCard.svelte';
    import * as Card from "$lib/components/ui/card";

    export let data;

    let selectedValue = data.selectedValue;

    // Handle the selection change event from GraphCard
    function handleSelectionChange(event) {
        selectedValue = event.detail;
    }
</script>

<div class="h-full w-screen">
    <div class="w-full h-full p-8">
        <h1 class="text-[#1E1E1E] text-4xl">{data?.company}</h1>
        <div class="w-full h-[2rem] bg-purple-200 mt-4 rounded-xl"> </div>
        <div class="mt-4">
            <GraphCard data={data} on:selectionChange={handleSelectionChange}/>
        </div>
        <div class="w-full mt-4">
            <Card.Root>
                <Card.Header>
                    
                </Card.Header>
                <Card.Content>
                    
                </Card.Content>
            </Card.Root>
        </div>
    </div>
</div>
