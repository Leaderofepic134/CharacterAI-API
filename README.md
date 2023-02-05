# CharacterAI-API
An unofficial API for CharacterAI
## Usage
Run ```bash
npm install node-characterai``` to install.
## Examples
```js
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
```
This is the same code in index.js.
## Other
You can change "Orchid" to anything you like.
## Change the bot
Change the "characterId" to the ID of your character, found in the last part of the URL.
## Use as a user and not a guest
You can also login as a user using ```
authenticateWithToken()```
You will need to provide your token. First, login to Character.AI. Then open the developer controls by pressing CTRL+SHIFT+I.
Go to application, and click on "@@auth0spajs@@::dyD3gE281MqgISG7FuIXYhL2WEknqZzv::https://auth0.character.ai/::openid profile email offline_access"
Open the body, and copy your token. Finally, supply it as a string inside of the function.
