# TeamSilly
## Description
Library for Messaging a MS Teams' Chat using simple text or rich card text through a Inbound Webhook.

## Usage Example
  
```python
from teamsnotifier import TeamsNotifier, TeamsCard
from datetime import datetime

teams = TeamsNotifier(
    webhook_url="https://outlook.office.com/webhook/..."
)

card = TeamsCard(summary='Test Card', subtitle='Subtitle test card', text='Test of text data')
card.add_fact('Destination:', 'The Moon')
card.add_fact('Traveler:', 'David Bowie')
card.add_fact('ETA:', str(datetime.now()))
print(teams.notify_advanced(card.get_card()))
```

## Requirements
### Interpreter
Python >= 3.6
### Libraries
requests >= 2.0
