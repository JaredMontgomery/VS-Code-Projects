// Gets an object of every word.
import {words} from "./words.js"

// Gets a list of every word.
let keys = Object.keys(words);
// Randomly selects one of those words.
let chosen_word = keys[Math.round(Math.random() * keys.length)];

// Creates underscores for each char from the word.
let underscored_word = new Array(...("_".repeat(chosen_word.length)));

// A list of every drawing of a man being hung. Pretty odd. What are even the
// origins of this game?
let drawing_list = [
    `      ___<br />
     |/  |<br />
     |<br />
     |<br />
     |<br />
     |<br />`,

     `     ___<br />
     |/  |<br />
     |   O<br />
     |<br />
     |<br />
     |<br />`,

     `     ___<br />
     |/  |<br />
     |   O<br />
     |   |<br />
     |<br />
     |<br />`,

     `     ___<br />
     |/  |<br />
     |   O<br />
     |  /|<br />
     |<br />
     |<br />`,

     `     ___<br />
     |/  |<br />
     |   O<br />
     |  /|\\<br />
     |<br />
     |<br />`,

     `     ___<br />
     |/  |<br />
     |   O<br />
     |  /|\\<br />
     |  /<br />
     |<br />`,

     `     ___<br />
     |/  |<br />
     |   O<br />
     |  /|\\<br />
     |  / \\<br />
     |<br />`,
];

let drawing_index = 0;
let drawing = drawing_list[drawing_index];

// A list of every wrong guess you have made (so far).
let wrong_guesses = [];

function game_loop()
{
    document.querySelector("#underscored_word").innerHTML = `Word: ${underscored_word.join(" ")}\n`;
    document.querySelector("#drawing").innerHTML = `${drawing}\n`;
    document.querySelector("#wrong_guesses").innerHTML = `Wrong: ${wrong_guesses.join(" ")}\n`;

    let guess = prompt("Enter some letter(s): ");

    for (let char of guess.toLowerCase())
    {
        let index = chosen_word.indexOf(char);

        // If the guessed char is in the word, then the correct underscore is
        // replaced.
        if (index !== -1)
        {
            underscored_word[index] = char;

            // If all underscores were replaced, then you have won the game.
            if (underscored_word.indexOf("_") === -1)
            {
                alert(`You win.`);

                return;
            }

            continue;
        }

        wrong_guesses.push(char);

        drawing_index++;

        // If we exhausted the drawings, then the man has been hung, so you
        // lose.
        if (drawing_index >= drawing_list.length)
        {
            alert(`You lose. The chosen word was: ${chosen_word}.`);

            return;
        }

        drawing = drawing_list[drawing_index];
    }

    setTimeout(game_loop, 100);
}

game_loop();