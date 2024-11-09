<script>
    import * as Card from "$lib/components/ui/card";

    export let data;
    console.log(data);
    let pairsSum = data.counts.reduce((accumulator, currentValue) => accumulator + currentValue, 0);;
    
</script>

<Card.Root>
    <Card.Header>
        <Card.Title>Best Product Pairs</Card.Title>
    </Card.Header>
    <Card.Content>
       <div class="w-full h-full ">
            {#each data.counts as pair, i}
                <div class="w-full h-[2rem] bg-black m-3"></div>
            {/each}
       </div>
    </Card.Content>
</Card.Root>