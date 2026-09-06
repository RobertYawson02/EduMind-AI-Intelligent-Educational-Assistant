function addMessage(message, sender) {


    let chatBox = document.getElementById("chat-box");


    let div = document.createElement("div");


    div.className = "message " + sender;



    div.innerHTML = `

        <div class="bubble">

            ${message}

        </div>

    `;



    chatBox.appendChild(div);


    chatBox.scrollTop = chatBox.scrollHeight;

}





function askQuestion() {


    let input = document.getElementById("question");


    let question = input.value.trim();



    if (question === "") {

        return;

    }



    addMessage(question, "user");


    input.value = "";



    addMessage(
        "🤔 Thinking...",
        "bot"
    );



    fetch("/ask", {


        method: "POST",


        headers: {


            "Content-Type": "application/json"


        },


        body: JSON.stringify({


            question: question


        })


    })



    .then(response => response.json())


    .then(data => {


        let chatBox = document.getElementById("chat-box");


        chatBox.lastChild.remove();



        addMessage(

            data.answer +

            "<br><br><small>Source: "

            +
            data.source +

            "</small>",

            "bot"

        );


    })


    .catch(error => {


        console.log(error);


        addMessage(

            "Sorry, an error occurred.",

            "bot"

        );


    });



}




function sendSuggestion(text) {


    document.getElementById("question").value = text;


    askQuestion();


}




function handleEnter(event) {


    if (event.key === "Enter") {

        askQuestion();

    }


}