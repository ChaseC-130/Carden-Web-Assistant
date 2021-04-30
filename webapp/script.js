window.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button");
    const iframe = document.getElementById("iframe");
    const result = document.getElementById("result");
    const main = document.getElementsByTagName("main")[0];
    const carden = document.getElementById("carden");
    const commands = document.getElementById("commands");
    const overlay = document.getElementById("overlay-content");
    commandsShown = false;
    axios.defaults.baseURL = 'https://www.chasecargill.com:8000'
    let listening = false;

    commandList = ["Weather in {City, State}", "Play {Song/Video}"];
    commandList.forEach((word) => {
        overlay.innerHTML += "<li>" + word + "</li>";
    });
    overlay.innerHTML += "</ol>";

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
        axios.get('/api/v1/process', {
            params: {
              speech: text
            }
        })
        .then(response => {
          const words = response.data;
          // takes an action I.E. Play video if there is an action
          if (words['action'] !== 'Y') {
            iframe.style.display = 'block';
            iframe.src = words['action'];
          } else {
            iframe.style.display = 'none';
            iframe.src = null;
          }
          readText(words['response']);
          carden.innerHTML = (words['response']);
        })
        .catch(error => console.error(error));
      };

      function readText(text) {
        var msg = new SpeechSynthesisUtterance();
        msg.text = text;
        window.speechSynthesis.speak(msg);
      };

      commands.addEventListener("click", 
      function toggleCommands() {
        commandsShown = !commandsShown;
        if (!commandsShown) {
          commands.innerHTML = "Show Commands"
          document.getElementById("overlay").style.width = "0%";
        } else {
          commands.innerHTML = "Hide Commands"
            document.getElementById("overlay").style.width = "100%";
        }
      });

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