# Connections

An open source tool for bringing people together.

## The Idea

Once every `month` create a form that participants can anonymously fill out (this is called the *seed form* because it seeds the rest of the *connections flow*). After `7 days`, close the *seed form* and send out a *nurture form*. The *nurture form* contains all the anonymous submissions from the *seed form*, and a participant may respond to one or more of those *seed requests*. Upon doing so, a message is sent to the anonymous submitter. They can respond to begin a dialog with their responder.

Visualized: https://docs.google.com/drawings/d/1HkrCT4DQliuACuxmSqpGR6taRxDdYVb-wM4-e_g3Pz0/edit?usp=sharing

## Authentication

To participate, users must be authenticated. We propose _passwordless_ login, by providing an email address where a one-time-use token may be sent. Note: In this case of RC Connections (the Connections server that supports members of the Recurse Center), messages will be sent through Zulip. The Connections software has been built s.t. you could easily use email instead of Zulip.
