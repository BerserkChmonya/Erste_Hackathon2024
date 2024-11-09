<script>
    import * as Card from "$lib/components/ui/card";

    export let data;
    let pairsSum = data.counts.reduce((accumulator, currentValue) => accumulator + currentValue, 0);;
    
</script>

<Card.Root>
    <Card.Header>
        <Card.Title>Best Product Pairs</Card.Title>
    </Card.Header>
    <Card.Content>
       <div class="w-full h-full ">
            {#each data.counts as pair, i}
                <h1 class="ml-4">{data.items[i]}</h1>
                <div class="relative w-full h-[2rem] bg-[#ADE8F4] m-3 rounded-xl">
                    
                    <div class="absolute inset-0 h-full bg-[#0077B6] opacity-50 rounded-xl" 
                        style="width: calc(100% * {data.counts[i] / pairsSum});">
                        
                    </div>
                </div>

            {/each}
       </div>
    </Card.Content>
</Card.Root>