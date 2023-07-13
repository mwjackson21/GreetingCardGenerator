from contextlib import contextmanager

@contextmanager
def generic(card_type, sender_name, recipient):
  generic_card = open(card_type, 'r')
  new_card = open(f'{sender_name}_generic.txt', 'w')
  try:
    new_card.write(f'Dear {recipient}\n')
    new_card.write(generic_card.read())
    new_card.write(f'Sincerely, {sender_name}\n')
    yield new_card

  finally:
    generic_card.close()
    new_card.close()


with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as card:
  print('Card Generated')
with open(card.name, 'r') as test:
  print(test.read())

class Personalized:
  def __init__(self, sender_name, recipient, file):
    self.sender_name = sender_name
    self.recipient = recipient
    self.file = open(f'{sender_name}_personalized.txt', 'w')

  def __enter__(self):
    self.file.write(f'Dear, {self.recipient}')
    return self.file

  def __exit__(self, *exc):
    self.file.write(f'\nSincerely {self.sender_name}')
    self.file.close()


with Personalized('John', 'Michael', 'john_card.txt') as card:
  card.write('I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.')

with Personalized('Josiah', 'Remy', 'remy_card.txt') as first_card:
  with Personalized('Josiah', 'Remy', 'esther_card.txt') as second_card:
    first_card.write('happy_bday.txt')
    second_card.write('Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can\'t live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!')