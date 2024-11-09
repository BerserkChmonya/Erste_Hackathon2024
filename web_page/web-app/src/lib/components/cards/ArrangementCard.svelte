<script>
    import * as Card from "$lib/components/ui/card";

    export let data;
</script>

<Card.Root>
    <Card.Header>
        <Card.Title>Products Arrangement</Card.Title>
    </Card.Header>
    <Card.Content>
        <div class="w-full h-full">
            <Card.Root>
                <Card.Header>
                    <Card.Title>Low Cost Best Sell</Card.Title>
                </Card.Header>
                <Card.Content>
                    <div class="w-full h-full">
                        <h1 class="underline">Place these products near checkouts:</h1>
                        <div class=" w-2/3 overflow-x-auto h-[15rem] mt-3 ">
                            {#each data as product}
                                <div class="w-full flex flex-row justify-between">
                                    <h1 class="">
                                        {product.name}
                                    </h1>
                                    <h1 class="">
                                        Category: {product.category}
                                    </h1>
                                    
                                </div>
                            {/each}
                        </div>
                    </div>
                </Card.Content>
            </Card.Root>
        </div>
        <div class="w-full h-full mt-4">
            <Card.Root>
                <Card.Header>
                    <Card.Title>Arrangament Recommendations</Card.Title>
                </Card.Header>
                <Card.Content>
                    <div class="w-full h-full">
                    
                    </div>
                </Card.Content>
            </Card.Root>
        </div>
    </Card.Content>
</Card.Root>