<script>
  const text = "My father studied Chinese language and literature in college and was part of the first 
            generation to attend college after 1976. 
            Writing poetry has been his lifelong passion, and he has created countless poems over the years. 
            This website is my way of bringing his words to life—using AI to recreate the imagery in his poems and share the beauty of my hometown, Yueyang, Hunan, with the world.";
  const typingEffect = document.getElementById("typing-effect");
  const mainContent = document.getElementById("main-content");

  function typeWriter(text, element, delay = 10) {
    let i = 0;
    function typing() {
      if (i < text.length) {
        element.innerHTML += text.charAt(i);
        i++;
        setTimeout(typing, delay);
      } else {
        setTimeout(() => {
          typingEffect.style.display = "none"; 
          mainContent.style.display = "block"; 
        }, 100); 
      }
    }
    typing();
  }

  document.addEventListener("DOMContentLoaded", () => {
    typeWriter(text, typingEffect);
  });
</script>
