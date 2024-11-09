<script>
    import { createEventDispatcher } from 'svelte';
    import Check from "lucide-svelte/icons/check";
    import ChevronsUpDown from "lucide-svelte/icons/chevrons-up-down";
    import * as Command from "$lib/components/ui/command/index.js";
    import * as Popover from "$lib/components/ui/popover/index.js";
    import { Button } from "$lib/components/ui/button/index.js";
    import { cn } from "$lib/utils.js";
    import { tick } from "svelte";

    export let ComboboxData;
    export let company;
    export let selectedValue = ''; // receives selected value from parent

    console.log(company);

    let open = false;
    let value = '';

    const dispatch = createEventDispatcher();

    $: displayedValue = ComboboxData.find((f) => f.value === value)?.label ?? "Select a product...";

    function closeAndFocusTrigger(triggerId) {
        open = false;
        tick().then(() => {
            document.getElementById(triggerId)?.focus();
        });
    }

    function handleSelect(selected) {
        value = selected;
        dispatch('selectionChange', value); // Emit selected value

        // Submit the form to update the selected value on the server
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = `/analysis/${company}/selectProduct`;
        console.log('bebra');

        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'selectedValue';
        input.value = value;

        form.appendChild(input);
        document.body.appendChild(form);
        form.submit();
    }
</script>

<Popover.Root bind:open let:ids>
    <Popover.Trigger asChild let:builder>
        <Button
            builders={[builder]}
            variant="outline"
            role="combobox"
            aria-expanded={open}
            class="w-[200px] justify-between"
        >
            {displayedValue}
            <ChevronsUpDown class="ml-2 h-4 w-4 shrink-0 opacity-50" />
        </Button>
    </Popover.Trigger>
    <Popover.Content class="w-[200px] p-0">
        <Command.Root>
            <Command.Input placeholder="Search product..." />
            <Command.Empty>No product found.</Command.Empty>
            <Command.Group>
                {#each ComboboxData as data}
                    <Command.Item
                        value={data.value}
                        onSelect={() => {
                            handleSelect(data.value);
                            closeAndFocusTrigger(ids.trigger);
                        }}
                    >
                        <Check
                            class={cn(
                                "mr-2 h-4 w-4",
                                value !== data.value && "text-transparent"
                            )}
                        />
                        {data.label}
                    </Command.Item>
                {/each}
            </Command.Group>
        </Command.Root>
    </Popover.Content>
</Popover.Root>
