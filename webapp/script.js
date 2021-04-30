window.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button");
    const iframe = document.getElementById("iframe");
    const result = document.getElementById("result");
    const main = document.getElementsByTagName("main")[0];
    let listening = false;
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    if (typeof SpeechRecognition !== "undefined") {
      const recognition = new SpeechRecognition();

      
      const stop = () => {
        main.classList.remove("speaking");
        recognition.stop();
        button.innerHTML = "Click to speak";
        
      };

      const start = () => {
        main.classList.add("speaking");
        recognition.start();
        button.innerHTML = "I'm listening...";
       
      };
      
      const onResult = event => {
        result.innerHTML = "";
        for (const res of event.results) {
          const text = document.createTextNode(res[0].transcript);
          const p = document.createElement("p");

          // condition to check the speech recognition has finished and passes text to API
          if (res.isFinal) {
            p.classList.add("final"); 
            callAPI(res[0].transcript);
          }
          p.appendChild(text);
          result.appendChild(p);
        }
      };

      const finished = event => {
            listening = false;
            stop();
      };

      function callAPI(text) {
        var ip = location.host;
        axios.get(ip + '/api/v1/process', {
            params: {
              speech: text
            }
        })
        .then(response => {
          const words = response.data;
          console.log(words);
          // takes an action I.E. Play video if there is an action
          if (words['action'] !== 'Y') {
            iframe.style.display = 'block';
            iframe.src = words['action'];
          } else {
            iframe.style.display = 'none';
            iframe.src = null;

            
          }

        })
        .catch(error => console.error(error));
      };

      recognition.continuous = false;
      recognition.interimResults = true;
      recognition.addEventListener("result", onResult);
      recognition.addEventListener("audioend", finished);
      button.addEventListener("click", event => {
        start();
        listening = true;
      });
    } else {
      button.remove();
      const message = document.getElementById("message");
      message.removeAttribute("hidden");
      message.setAttribute("aria-hidden", "false");
    }
  });