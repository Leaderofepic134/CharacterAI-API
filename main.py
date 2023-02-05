const CharacterAI = require('node_characterai');
const uuid = require('uuid')
const characterAI = new CharacterAI();
const prompt = require('prompt-sync')();


(async() => {
    await characterAI.authenticateAsGuest();

    const characterId = "lryij6Pg95hRvpU7y4SLrRzwWvVyCugTF4lpciiJyY8" // Orchid

    const chat = await characterAI.createOrContinueChat(characterId);
    while (true) {
      const message = prompt('You: ');
      const response = await chat.sendAndAwaitResponse(message, true)
      
      console.log("Orchid: " + response);
    }
})();
