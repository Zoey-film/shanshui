document.addEventListener("DOMContentLoaded", () => {
    const text = "My father studied Chinese language and literature in college and was part of the first generation to attend college after 1976. Writing poetry has been his lifelong passion, and he has created countless poems over the years. This website is my way of bringing his words to life—using AI to recreate the imagery in his poems and share the beauty of my hometown, Yueyang, Hunan, with the world.";
    const typingEffect = document.getElementById("typing-effect");
    const mainContent = document.getElementById("main-content");
    const seasonRow = document.getElementById("season-row");
    const audio = document.getElementById('bgm');
    const toggleBtn = document.getElementById('music-toggle');

    // Extracting paths from data attributes
    const musicOnImage = toggleBtn.getAttribute('data-music-on');
    const musicOffImage = toggleBtn.getAttribute('data-music-off');

    let typingInProgress = true;
    let isPlaying = false; // we'll try to play immediately

    function finishTyping() { 
        typingInProgress = false;
        setTimeout(() => {
            seasonRow.style.display = "flex";
        }, 500);
    }

    function skipTyping() {
        if (typingInProgress) {
            typingInProgress = false;
            typingEffect.innerHTML = text;
            finishTyping();
        }
    }

    function typeWriter(str, element, delay = 50) {
        let i = 0;
        
        function typing() {
            if (!typingInProgress) {
                return;
            }

            if (i < str.length) {
                element.innerHTML += str.charAt(i);
                i++;
                setTimeout(typing, delay);
            } else {
                finishTyping();
            }
        }
        typing();
    }

    typingEffect.addEventListener("click", skipTyping);
    typeWriter(text, typingEffect);

    // Try to play the audio immediately
    audio.play().then(() => {
        // If autoplay is allowed, show music_on icon and set isPlaying = true
        isPlaying = true;
        toggleBtn.src = musicOnImage;
    }).catch(err => {
        console.log("Autoplay blocked. User interaction needed.");
        // If autoplay is blocked, we start with isPlaying=false and show music_on icon (since we want default as playing)
        // But since we can't play, we should still show the icon as on since that's the intended default.
        // The first toggle click will attempt to start playing.
        isPlaying = false;
        toggleBtn.src = music_on; // keep music_on to indicate default "wants to be playing"
    });

    toggleBtn.addEventListener('click', () => {
        // If currently playing, toggle off
        if (isPlaying) {
            audio.pause();
            isPlaying = false;
            toggleBtn.src = musicOffImage;
        } else {
            // Try to play again
            audio.play().then(() => {
                isPlaying = true;
                toggleBtn.src = musicOnImage;
            }).catch(err => {
                console.error("Unable to play music:", err);
            });
        }
    });
});
