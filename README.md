# ♗ chs

> Play chess against the Stockfish engine in your terminal.

<img src="https://travis-ci.org/nickzuber/chs.svg?branch=master" /> <img src="https://img.shields.io/badge/project-active-brightgreen.svg" /> <img src="https://img.shields.io/badge/status-stable-brightgreen.svg" /> <img src="https://img.shields.io/pypi/dm/chs.svg?color=yellow" /> <img src="https://img.shields.io/pypi/format/chs.svg" /> <img src="https://img.shields.io/badge/state-released-brightgreen.svg" /> <img src="https://img.shields.io/badge/license-MIT%20Licence-blue.svg" />

<img src="https://user-images.githubusercontent.com/10540865/119232802-80c34700-baf4-11eb-9fed-af558575ae4e.png" />

### Table of Contents
 - [Installation](#installation)
    - [Pip](#pip)
    - [Arch Linux](#arch-linux)
 - [Usage](#usage)
    - [How to start playing](#how-to-start-playing)
    - [How to play](#how-to-play)
 - [License](#license)

## Installation

#### Pip

This package is available via PyPi.

```
$ python3 -m pip install chs
```

#### Arch Linux

There is a [chs-git](https://aur.archlinux.org/packages/chs-git/) package in the Arch User Repository, which you can install with an AUR helper:

```
$ yay -S chs-git || paru -S chs-git
```

## Usage

To play against the default level 1 (easiest) version of the Stockfish engine, just run `chs` command.

### How to start playing

```
$ chs
```

You can also specify the level of the engine if you want to tweak the difficulty.

```
$ chs level=8
```

### How to play

There are a few things you can do while playing:

* Make moves using valid algebraic notation (e.g. `Nf3`, `e4`, etc.).
* Take back your last move by playing `back` instead of a valid move.
* Get a hint from the engine by playing `hint` instead of a valid move.

## License

This software is free to use under the MIT License. See [this reference](https://opensource.org/licenses/MIT) for license text and copyright information.
