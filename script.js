window.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("button");
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
          if (res.isFinal) {
            p.classList.add("final");
          }
          p.appendChild(text);
          result.appendChild(p);
        }
      };

      const finished = event => {
            listening = false;
            stop();
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