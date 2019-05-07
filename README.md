# Mattermost-flask

This repo is based on the code available here https://github.com/sadsfae/mattermost-hotdice. I just made it simpler.


### Mattermost Server Settings

* System Console -> Developer Settings -> Allow untrusted internal connections to: ```localhost```
* System Console -> Custom Integrations -> Enable integrations to override usernames: ```true```
* System Console -> Enable integrations to override profile picture icons: ```true```

### Setup

You only need one of these approaches.  Slash commands are a bit more configurable as they can work in private chat or private channels.

#### Setting up as a Webhook

* Main Menu -> Integrations -> Outgoing Webhook
  - Add Outgoing Webhook
  - Content-type: ```application/json```
  - Trigger Words:   
```
hotdice
Hotdice
```
  - Trigger When: ```First word matches a trigger word exactly```
  - Callback URLs:  ```http://localhost:8090/hotdice```
