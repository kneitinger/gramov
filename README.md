# gramov
A Telegram bot that uses Markov chains to learn to speak from a chat.

---

## Installation

Manual method:

```
$ git clone https://github.com/kneitinger/gramov.git
$ cd gramov
$ sudo python setup.py install
```

 Automatic method with 'pip':

```
$ sudo pip install gramov
```

## Usage

First, acquire a Telegram Bot API token by messaging the @BotFather bot and
following the instructions. Store the API token in a
file such as `~/.gramov_token` and launch gramov with the command:

```
$ gramov -t "$(cat ~/.gramov_token)"
```

Additionally, you may specify a file where received messages are stored and/or
loaded from, with the -f flag.  The -v flag enables verbose output to stdout,
printing all received and sent messages.

```
$ gramov -t "$(cat ~/.gramov_token)" -f ~/.gramov_words -v
```

As expected, the -h flag prints the program usage.

