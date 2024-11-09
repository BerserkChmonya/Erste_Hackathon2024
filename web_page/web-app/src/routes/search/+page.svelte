<script>
    import { Image } from "@unpic/svelte";
  </script>
  
  <div class="h-screen flex flex-col justify-center items-center px-4 md:px-0 space-y-12">
    <!-- Header Section -->
        <!-- Circle centered above the header -->
        
        
    


    <div class="text-center space-y-6">
        <div class="flex flex-col items-center mt-6">
            <div class="w-20 h-20  bg-gray-300 rounded-full flex flex-col items-center justify-center ">
                <h1 class="text-4xl">L
                </h1>
            </div>
          </div>
      <h1 class="text-7xl md:text-9xl">Find your company</h1>
      <h3 class="text-xl font-light">You're just a step away from your personalised improving instructions</h3>
    </div>
  
    <!-- Search Input Section -->
    <form method="POST" class="relative w-full max-w-lg">
      <input
        type="text"
        name="query"
        class="h-12 w-full pl-4 pr-12 rounded-lg border border-gray-300"
        placeholder="Search..."
      />
      <button
        type="submit"
        class="absolute top-1/2 right-3 transform -translate-y-1/2 rounded-full text-gray-600"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
          <path
            fill="currentColor"
            d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5l-1.5 1.5l-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16A6.5 6.5 0 0 1 3 9.5A6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14S14 12 14 9.5S12 5 9.5 5"
          />
        </svg>
      </button>
    </form>
  
    <!-- Shops Section -->
    <h3 class="text-xl font-light">Popular Searches:</h3>
    <div class="flex flex-wrap justify-center gap-6 mt-12">

      {#each ['Lidl', 'Billa', 'Tesco', 'DM'] as shop}
        <form method="POST" class="flex flex-col items-center space-y-2">
          <input type="hidden" name="query" value={shop} />
          <button type="submit" class="flex flex-col items-center">
            <Image src={`/src/lib/images/${shop.toLowerCase()}.png`} class="w-24 h-24 object-contain rounded-3xl border-2 border-black" alt={shop} />
            <h2 class="text-lg text-center">{shop}</h2>
          </button>
        </form>
      {/each}
    </div>
  </div>
  