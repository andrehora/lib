# Library refactoring example

This repository contains a refactoring example (+ unit tests) adapted from the Refactoring book by Martin Fowler and Kent Beck.

The code has three classes: `Client`, `Rental`, and `Book`.
The key idea is to refactor method `statement` in `Client`.

First version of `statement`:

https://github.com/andrehora/lib/blob/9d7191dd8d639599ecae409b1ccdeaca4f04e851/model.py#L45-L78

Final version of `statement` after multiple refactorings:

https://github.com/andrehora/lib/blob/025fb9bb9cd6beb51adc1a7c2eca7afe54bbce98/model.py#L69-L77