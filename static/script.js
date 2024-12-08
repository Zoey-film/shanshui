document.addEventListener("DOMContentLoaded", () => {
    const text = "My father studied Chinese language and literature in college and was part of the first generation to attend college after 1976. Writing poetry has been his lifelong passion, and he has created countless poems over the years. This website is my way of bringing his words to life—using AI to recreate the imagery in his poems and share the beauty of my hometown, Yueyang, Hunan, with the world.";
    const typingEffect = document.getElementById("typing-effect");
    const mainContent = document.getElementById("main-content");
    const seasonRow = document.getElementById("season-row");

    function typeWriter(str, element, delay = 50) {
        let i = 0;
        function typing() {
            if (i < str.length) {
                element.innerHTML += str.charAt(i);
                i++;
                setTimeout(typing, delay);
            } else {
                // 打字完成后
                setTimeout(() => {
                    typingEffect.style.display = "none";
                    mainContent.style.display = "block";
                    setTimeout(() => {
                        seasonRow.style.display = "flex";
                    }, 500);
                }, 500);
            }
        }
        typing();
    }

    typeWriter(text, typingEffect);
});
