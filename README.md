# GreetingCardGenerator.github.io
This Python code provides two context managers for generating personalized and generic greeting cards. This code makes use of the contextlib module to create context managers, which allow for cleaner and more readable code when dealing with resources like file handling.

How to Use:
Generic Cards
To create a generic card, you can use the generic context manager as follows:

with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as card:
  print('Card Generated')
This code generates a generic thank-you card with the sender's name "Mwenda" and recipient "Amanda." The card content is read from the 'thankyou_card.txt' file, and the resulting card is written to 'Mwenda_generic.txt'.

Personalized Cards
To create personalized cards, you can use the Personalized class as follows:

with Personalized('John', 'Michael', 'john_card.txt') as card:
  card.write('I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.')
This code generates a personalized card from "John" to "Michael" and writes the provided message to 'John_personalized.txt'. You can create multiple personalized cards in a nested manner, as demonstrated in the code example.

File Management
The code takes care of opening and closing files properly, ensuring that resources are managed efficiently and without resource leaks.

The generic context manager reads the content of a generic card file and writes it into a new file with a personalized greeting. It automatically closes both the input and output files when done.

The Personalized context manager opens a personalized card file for writing, writes the greeting message, and closes the file when done. Multiple instances of Personalized can be used in a nested manner to create multiple personalized cards.
