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
    --index: 4;
  }
  #card3 {
    --index: 7;
  }
  #card4 {
    --index: 10;
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
    

      <div class="container flex justify-center items-center">
          <ul id="cards">
              <li class="card " id="card1">
                  <div class="card-body w-full">
                      <div class="w-screen flex justify-center items-center">
                          <Card.Root class=" w-full h-full rounded-3xl min-w-[270px] mx-10">
                              <Card.Header>
                                  <div class="flex justify-between items-center flex-row w-full">
                                  <div class="flex justify-between items-center flex-row w-full">
                                  <h1 class="self-start text-4xl lg:text-7xl">(01) Heading</h1>
                                  
                              </div>
                              <svg class="ml-24" xmlns="http://www.w3.org/2000/svg" width="3em" height="3em" viewBox="0 0 24 24" {...$$props}>
                                <path fill="currentColor" d="M20 13.75a.75.75 0 0 0-.75-.75h-3a.75.75 0 0 0-.75.75v6.75H14V4.25c0-.728-.002-1.2-.048-1.546c-.044-.325-.115-.427-.172-.484s-.159-.128-.484-.172C12.949 2.002 12.478 2 11.75 2s-1.2.002-1.546.048c-.325.044-.427.115-.484.172s-.128.159-.172.484c-.046.347-.048.818-.048 1.546V20.5H8V8.75A.75.75 0 0 0 7.25 8h-3a.75.75 0 0 0-.75.75V20.5H1.75a.75.75 0 0 0 0 1.5h20a.75.75 0 0 0 0-1.5H20z" />
                            </svg>
                          </div>
                              </Card.Header>
                              <Card.Content class="w-full h-full">
                                 
                                  <div class="h-full w-full grid grid-cols-1  md:grid-rows-1 md:grid-cols-[40%_60%]">
                                    <div class="aspect-w-12 aspect-h-9">
                                        <Image src="https://picsum.photos/435/335" class="w-full h-full object-contain rounded-3xl" alt="test" />
                                    </div>
                                    
                                      <div class="w-full flex flex-col justify-center items-center text-4xl font-light p-6 ">
  
                                          <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Consequuntur, corrupti! Reprehenderit enim tenetur unde expedita beatae aliquid obcaecati veritatis perspiciatis.</p>
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
                                <h1 class="self-start text-6xl">(01)</h1>
                                <h1 class="self-end text-7xl">Heading</h1>
                                
                            </div>
                            <svg class="ml-24" xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24" {...$$props}>
                                <path fill="currentColor" d="M12 1.67a2.91 2.91 0 0 0-2.492 1.403L1.398 16.61a2.914 2.914 0 0 0 2.484 4.385h16.225a2.914 2.914 0 0 0 2.503-4.371L14.494 3.078A2.92 2.92 0 0 0 12 1.67" />
                            </svg>
                        </div>
                            </Card.Header>
                            <Card.Content class="w-full h-full">
                               
                                <div class="h-full w-full grid grid-cols-1  md:grid-rows-1 md:grid-cols-[40%_60%]">
                                  <div class="aspect-w-12 aspect-h-9">
                                      <Image src="https://picsum.photos/435/335" class="w-full h-full object-contain rounded-3xl" alt="test" />
                                  </div>
                                  
                                    <div class="w-full flex flex-col justify-center items-center text-4xl font-light p-6 ">

                                        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Consequuntur, corrupti! Reprehenderit enim tenetur unde expedita beatae aliquid obcaecati veritatis perspiciatis.</p>
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
                                <h1 class="self-start text-6xl">(01)</h1>
                                <h1 class="self-end text-7xl">Heading</h1>
                                
                            </div>

                        </div>
                            </Card.Header>
                            <Card.Content class="w-full h-full">
                               
                                <div class="h-full w-full grid grid-cols-1  md:grid-rows-1 md:grid-cols-[40%_60%]">
                                  <div class="aspect-w-12 aspect-h-9">
                                      <Image src="https://picsum.photos/435/335" class="w-full h-full object-contain rounded-3xl" alt="test" />
                                  </div>
                                  
                                    <div class="w-full flex flex-col justify-center items-center text-4xl font-light p-6 ">

                                        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Consequuntur, corrupti! Reprehenderit enim tenetur unde expedita beatae aliquid obcaecati veritatis perspiciatis.</p>
                                    </div>
                                    
                                    
                                    
                                    </div>
                         
                            </Card.Content>
                        </Card.Root>
                      </div>
                </div>

            </li>
             
          </ul>
      </div>




      

      
       
