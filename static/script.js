document.addEventListener("DOMContentLoaded", () => {
    const text = "My father studied Chinese language and literature in college and was part of the first generation to attend college after 1976. Writing poetry has been his lifelong passion, and he has created countless poems over the years. This website is my way of bringing his words to life—using AI to recreate the imagery in his poems and share the beauty of my hometown, Yueyang, Hunan, with the world.";
    const typingEffect = document.getElementById("typing-effect");
    const mainContent = document.getElementById("main-content");
    const seasonRow = document.getElementById("season-row");
    const audio = document.getElementById('bgm');
    const toggleBtn = document.getElementById('music-toggle');
    

    let typingInProgress = true;

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

    let isPlaying = false;

    audio.play().then(() => {
        isPlaying = true;
    }).catch(err => {
        console.log("自动播放被阻止，需要用户交互来启动音乐。");
    });

    toggleBtn.addEventListener('click', () => {
        if (isPlaying) {
            audio.pause();
            isPlaying = false;
            musicIcon.src = "{{ url_for('static', filename='images/music_off.png') }}";
        } else {
            audio.play().then(() => {
                isPlaying = true;
                musicIcon.src = "{{ url_for('static', filename='images/music_on.png') }}";
            }).catch(err => {
                console.error("无法播放音乐：", err);
            });
        }
    });
});
