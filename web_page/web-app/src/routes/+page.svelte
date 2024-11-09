<script>
    import { onMount } from 'svelte';
    import anime from 'animejs';
    let textWrapper;
    let phoneElement;

    import { Button } from "$lib/components/ui/button/index.js";
    import * as Carousel from "$lib/components/ui/carousel/index.js";
    import Autoscroll from "embla-carousel-auto-scroll";

  
    onMount(() => {
      // Split the text into individual words wrapped in span elements, preserving spaces
      textWrapper.innerHTML = textWrapper.textContent.replace(/(\S+)(\s*)/g, "<span class='my-text inline-block text-white'>$1</span>$2");
  
      // Create the animation timeline
      anime.timeline()
        .add({
          targets: '.my-text', // Target each word individually
          translateY: [100, 0], // Animate from 100px below to its original position
          easing: 'easeOutExpo',
          duration: 800, // Faster animation for each word
          delay: (el, i) => i * 200, // Delay between words (200ms)
        });

        const animation = anime({
      targets: phoneElement,
      translateY: ['50%', '0%'],
      duration: 1000,
      easing: 'easeOutQuad',
      autoplay: false
    });

    const handleScroll = () => {
      const scrollPercentage = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight);
      animation.seek(animation.duration * scrollPercentage);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
    });









    import { Image } from "@unpic/svelte";
  
  import * as Card from "$lib/components/ui/card";
  </script>

<style>


  :root {
    --cards: 3;
    --cardHeight: 87vh;
    --cardTopPadding: 2.1em;
    --cardMargin: 4vw;
  }
  
  .container {
    width: 90%;
    margin: 0 auto;
  }
  
  #cards {
    list-style: none;
    padding-left: 0;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(var(--cards), var(--cardHeight));
    gap: var(--cardMargin);
    padding-bottom: calc(var(--cards) * var(--cardTopPadding));
    margin-bottom: var(--cardMargin);
  }
  
  #card1 {
    --index: 1;
  }
  #card2 {
    --index: 3;
  }
  #card3 {
    --index: 5;
  }
 

@screen lg {
  #card1 {
    --index: 1;
  }
  #card2 {
    --index: 4;
  }
  #card3 {
    --index: 7;
  }
}
.shrink-on-hover {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s;
  -webkit-transition-property: transform;
  transition-property: transform;
}
.shrink-on-hover:hover, .shrink-on-hover:focus, .shrink-on-hover:active {
  -webkit-transform: scale(0.9);
  transform: scale(0.9);
}
  
  .card {
    position: sticky;
    top: 0;
    padding-top: calc(var(--index) * var(--cardTopPadding));
  }
  
  
  
  .card-body {
    box-sizing: border-box;
  
    border-radius: 50px;
  
  
    display: flex;
    justify-content: center;
    align-items: center;
    transition: all 0.5s;
  }


    </style>
    
    <div class="w-screen flex justify-center items-center">
        <div class="relative flex items-center justify-center min-h-screen ">
            <!-- Circles -->
            <div class="absolute top-0 right-0 w-32 h-32 mr-8 mt-20 bg-[#028661] rounded-full opacity-40 flex items-center justify-center">
                
                <svg   xmlns="http://www.w3.org/2000/svg" width="5em" height="5em" viewBox="0 0 24 24">
                    <path fill="currentColor" d="m16 11.78l4.24-7.33l1.73 1l-5.23 9.05l-6.51-3.75L5.46 19H22v2H2V3h2v14.54L9.5 8z" />
                  </svg>
                
              </div>
              
              <div class="absolute bottom-0 left-0 w-32 h-32 mb-20 ml-8 lg:w-64 lg:h-64 bg-[#E1015B] rounded-full opacity-40 flex items-center justify-center">
                <svg  class="lg:w-40 lg:h-40 " xmlns="http://www.w3.org/2000/svg" width="6em" height="6em" viewBox="0 0 24 24">
                    <path fill="currentColor" d="M19 7h-3V6a4 4 0 0 0-8 0v1H5a1 1 0 0 0-1 1v11a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V8a1 1 0 0 0-1-1m-9-1a2 2 0 0 1 4 0v1h-4Zm8 13a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V9h2v1a1 1 0 0 0 2 0V9h4v1a1 1 0 0 0 2 0V9h2Z" />
                  </svg>
              </div>
              
            
            <!-- Content -->
            <div class="text-center space-y-6 relative z-10 md:mx-8">
              <h1 class="text-7xl md:text-9xl">Revolutionize Your Store's Performance</h1>
              <h3 class="text-xl font-light">Optimize aisles, predict sales, and uncover popular product pairs—all with data-driven insights.</h3>
              <div class="mt-24"></div>
              <a href="/search">
                <button class="h-20 text-xl bg-[#157FF7] mt-5 rounded-full mb-3 border-[3px] border-black shrink-on-hover px-3 text-white">
                  Start Improving Your Store Today
                </button>
              </a>
              
            </div>
          </div>
          
          
          
        
    </div> 

      <div class="container flex justify-center items-center">



          <ul id="cards">
              <li class="card " id="card1">
                  <div class="card-body w-full">
                      <div class="w-screen flex justify-center items-center">
                          <Card.Root class=" w-full h-full rounded-3xl min-w-[270px] mx-10">
                              <Card.Header>
                                  <div class="flex justify-between items-center flex-row w-full">
                                  <div class="flex justify-between items-center flex-row w-full">
                                  <h1 class="self-start text-2xl lg:text-7xl">(01) Demand Forecast</h1>
                                  
                              </div>
                              <svg class="ml-24" xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 24 24" {...$$props}>
                                <path fill="currentColor" d="M20 13.75a.75.75 0 0 0-.75-.75h-3a.75.75 0 0 0-.75.75v6.75H14V4.25c0-.728-.002-1.2-.048-1.546c-.044-.325-.115-.427-.172-.484s-.159-.128-.484-.172C12.949 2.002 12.478 2 11.75 2s-1.2.002-1.546.048c-.325.044-.427.115-.484.172s-.128.159-.172.484c-.046.347-.048.818-.048 1.546V20.5H8V8.75A.75.75 0 0 0 7.25 8h-3a.75.75 0 0 0-.75.75V20.5H1.75a.75.75 0 0 0 0 1.5h20a.75.75 0 0 0 0-1.5H20z" />
                            </svg>
                          </div>
                              </Card.Header>
                              <Card.Content class="w-full h-full">
                                 
                                  <div class="h-full w-full grid grid-cols-1  md:grid-rows-1 md:grid-cols-[40%_60%]">
                                    <div class="aspect-w-12 aspect-h-9 ">
                                        <Image src="/src/lib/images/image.png" class="w-full h-full object-contain rounded-3xl border-2 border-black" alt="test" />
                                    </div>
                                    
                                      <div class="w-full flex flex-col justify-center items-start text-4xl font-light p-6 ">
                                          <h1 class="text-xl font-bold mb-3 lg:text-4xl">Predict Item Sales</h1>
                                          <p class="text-base mb-3 lg:text-xl lg:mb-6">Determine amount of sales in upcoming monthes for products based on previous experience.</p>
                                          <h1 class="text-xl font-bold mb-3 lg:text-4xl ">Control Your Stocks</h1>
                                          <p class="text-base lg:text-xl">Minimise waste when planning your store restocking.</p>
                                         
                                        </div>
                                      
                                      
                                      
                                      </div>
                           
                              </Card.Content>
                          </Card.Root>
                        </div>
                  </div>
  
              </li>
              <li class="card " id="card2">
                <div class="card-body w-full">
                    <div class="w-screen flex justify-center items-center">
                        <Card.Root class=" w-full h-full rounded-3xl min-w-[270px] mx-10">
                            <Card.Header>
                                <div class="flex justify-between items-center flex-row w-full">
                                <div class="flex justify-between items-center flex-row w-full">
                                <h1 class="self-start text-2xl lg:text-7xl">(02) Product Pairs</h1>
                                
                            </div>
                            <svg class="ml-24" xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 20 20" {...$$props}>
                                <path fill="currentColor" d="M2 3.5a1.5 1.5 0 0 0 .75 1.3v6.4a1.5 1.5 0 1 0 2.05 2.05h1.95v1.95a1.5 1.5 0 1 0 2.05 2.05h6.4a1.5 1.5 0 1 0 2.05-2.05V8.8a1.5 1.5 0 1 0-2.05-2.05h-1.95V4.8a1.5 1.5 0 1 0-2.05-2.05H4.8A1.5 1.5 0 0 0 2 3.5m6.8 12.25a1.5 1.5 0 0 0-.55-.55v-1.95h2.95a1.5 1.5 0 1 0 2.05-2.05V8.25h1.95c.132.228.322.418.55.55v6.4a1.5 1.5 0 0 0-.55.55zM4.25 11.2V4.8a1.5 1.5 0 0 0 .55-.55h6.4c.132.228.322.418.55.55v1.95H8.8A1.5 1.5 0 1 0 6.75 8.8v2.95H4.8a1.5 1.5 0 0 0-.55-.55m7.5 0a1.5 1.5 0 0 0-.55.55H8.25V8.8a1.5 1.5 0 0 0 .55-.55h2.95z" />
                            </svg>
                        </div>
                            </Card.Header>
                            <Card.Content class="w-full h-full">
                               
                                <div class="h-full w-full grid grid-cols-1  md:grid-rows-1 md:grid-cols-[40%_60%]">
                                  <div class="aspect-w-12 aspect-h-9 ">
                                      <Image src="/src/lib/images/image2.png" class="w-full h-full object-contain rounded-3xl border-2 border-black" alt="test" />
                                  </div>
                                  
                                    <div class="w-full flex flex-col justify-center items-start text-4xl font-light p-6 ">
                                        <h1 class="text-xl font-bold mb-3 lg:text-4xl">Find Product Pairs</h1>
                                        <p class="text-base mb-3 lg:text-xl lg:mb-6">Target specific product pairs to include in promotion to increase sales.</p>
                    
                                      </div>
                                    
                                    
                                    
                                    </div>
                         
                            </Card.Content>
                        </Card.Root>
                      </div>
                </div>

            </li>
            <li class="card " id="card3">
                <div class="card-body w-full">
                    <div class="w-screen flex justify-center items-center">
                        <Card.Root class=" w-full h-full rounded-3xl min-w-[270px] mx-10">
                            <Card.Header>
                                <div class="flex justify-between items-center flex-row w-full">
                                <div class="flex justify-between items-center flex-row w-full">
                                <h1 class="self-start text-2xl lg:text-7xl">(03) Arrangement System</h1>
                                
                            </div>
                            <svg class="ml-24" xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 24 24" {...$$props}>
                                <path fill="currentColor" d="M17 18a2 2 0 0 1 2 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2c0-1.11.89-2 2-2M1 2h3.27l.94 2H20a1 1 0 0 1 1 1c0 .17-.05.34-.12.5l-3.58 6.47c-.34.61-1 1.03-1.75 1.03H8.1l-.9 1.63l-.03.12a.25.25 0 0 0 .25.25H19v2H7a2 2 0 0 1-2-2c0-.35.09-.68.24-.96l1.36-2.45L3 4H1zm6 16a2 2 0 0 1 2 2a2 2 0 0 1-2 2a2 2 0 0 1-2-2c0-1.11.89-2 2-2m9-7l2.78-5H6.14l2.36 5z" />
                            </svg>
                        </div>
                            </Card.Header>
                            <Card.Content class="w-full h-full">
                               
                                <div class="h-full w-full grid grid-cols-1  md:grid-rows-1 md:grid-cols-[40%_60%]">
                                  <div class="aspect-w-12 aspect-h-9 ">
                                      <Image src="/src/lib/images/image3.png" class="w-full h-full object-contain rounded-3xl border-2 border-black" alt="test" />
                                  </div>
                                  
                                    <div class="w-full flex flex-col justify-center items-start text-4xl font-light p-6 ">
                                        <h1 class="text-xl font-bold mb-3 lg:text-4xl">No Need to think were to place your products!</h1>
                                        <p class="text-base mb-3 lg:text-xl lg:mb-6">Our system will analyze info from previous clients purchases and will provide your with comprehensive guide on product placment, save yourself time and money on team of proffesionals!</p>
                    
                                      </div>
                                    
                                    
                                    
                                    </div>
                         
                            </Card.Content>
                        </Card.Root>
                      </div>
                </div>

            </li>
            
          </ul>
      </div>

      <footer class="h-full text-zinc-600 rounded-3xl mt-40 mx-4 bg-[#D9D9D9] py-10 px-8">
        <div class="max-w-screen-xl mx-auto flex flex-col lg:flex-row justify-between items-start lg:items-center space-y-8 lg:space-y-0">
          
          <!-- Branding Section -->
          <div class="flex flex-col space-y-2">
            <h1 class="text-4xl font-bold text-zinc-800">Your Company</h1>
            <p class="text-md text-zinc-700">Bringing you the best solutions for your needs.</p>
          </div>

          
      
          <!-- Navigation Links -->
          <div class="flex flex-col lg:flex-row space-y-4 lg:space-y-0 lg:space-x-10 text-lg text-zinc-700">
            <a href="#about" class="hover:text-zinc-900 transition-colors">About Us</a>
            <a href="#services" class="hover:text-zinc-900 transition-colors">Services</a>
            <a href="#careers" class="hover:text-zinc-900 transition-colors">Careers</a>
            <a href="#contact" class="hover:text-zinc-900 transition-colors">Contact</a>
          </div>
      
          <!-- Contact Information -->
          <div class="text-zinc-700 text-md">
            <p><strong>Email:</strong> support@yourcompany.com</p>
            <p><strong>Phone:</strong> +1 (123) 456-7890</p>
            <p><strong>Address:</strong> 123 Business Rd, Business City, BC 12345</p>
          </div>
      
          <!-- Social Media Icons (use your preferred icon library here) -->
          <div class="flex space-x-4">
            <a href="#" class="hover:text-zinc-900 transition-colors" aria-label="Facebook">
              <i class="fab fa-facebook text-2xl"></i>
            </a>
            <a href="#" class="hover:text-zinc-900 transition-colors" aria-label="Twitter">
              <i class="fab fa-twitter text-2xl"></i>
            </a>
            <a href="#" class="hover:text-zinc-900 transition-colors" aria-label="Instagram">
              <i class="fab fa-instagram text-2xl"></i>
            </a>
            <a href="#" class="hover:text-zinc-900 transition-colors" aria-label="LinkedIn">
              <i class="fab fa-linkedin text-2xl"></i>
            </a>
          </div>
        </div>
      
        <!-- Footer Bottom Section -->
        <div class="mt-10 border-t border-zinc-300 pt-6 text-center text-zinc-600 text-sm">
          <p>&copy; 2024 Your Company. All rights reserved.</p>
        </div>
      </footer>
      


     




      

      
       
