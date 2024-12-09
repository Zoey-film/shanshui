console.log("JavaScript is running on season_template.html");
document.addEventListener("DOMContentLoaded", () => {
    const text = "My father studied Chinese language and literature in college and was part of the first generation to attend college after 1976. Writing poetry has been his lifelong passion, and he has created countless poems over the years. This website is my way of bringing his words to life—using AI to recreate the imagery in his poems and share the beauty of my hometown, Yueyang, Hunan, with the world.";
    const typingEffect = document.getElementById("typing-effect");
    const mainContent = document.getElementById("main-content");
    const seasonRow = document.getElementById("season-row");
    const audio = document.getElementById('bgm');
    const toggleBtn = document.getElementById('music-toggle');

    if (!audio || !toggleBtn) {
        console.error("Audio or toggle button not found");
        return;
    }

    // Extracting paths from data attributes
    const musicOnImage = toggleBtn.getAttribute('data-music-on');
    const musicOffImage = toggleBtn.getAttribute('data-music-off');

    let typingInProgress = true;
    let isPlaying = false; 

    function finishTyping() { 
        typingInProgress = false;
        setTimeout(() => {
            if (seasonRow) {
                seasonRow.style.display = "flex";
            }
        }, 500);
    }

    function skipTyping() {
        if (typingInProgress) {
            typingInProgress = false;
            if (typingEffect) {
                typingEffect.innerHTML = text;
            }
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

    if (typingEffect) {
        typingEffect.addEventListener("click", skipTyping);
        typeWriter(text, typingEffect);
    }

    // Try to play the audio immediately
    audio.play().then(() => {
        isPlaying = true;
        toggleBtn.src = musicOnImage;
    }).catch(err => {
        console.log("Autoplay blocked. User interaction needed.");
        isPlaying = false;
        toggleBtn.src = musicOffImage; 
    });

    toggleBtn.addEventListener('click', () => {
        if (isPlaying) {
            audio.pause();
            isPlaying = false;
            toggleBtn.src = musicOffImage;
        } else {
            audio.play().then(() => {
                isPlaying = true;
                toggleBtn.src = musicOnImage;
            }).catch(err => {
                console.error("Unable to play music:", err);
            });
        }
    });

    const bgm = document.getElementById('bgm');
    bgm.play().then(() => {
        console.log("Audio is playing");
    }).catch(err => {
        console.error("Error playing audio:", err);
    });
});
