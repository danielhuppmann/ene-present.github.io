# Generate IIASA Energy Program Presentation

## Requirements

- `nbconvert`

## After cloning

We use a submodule for `reveal.js` so make sure to

```
git submodule update --init --recursive
```

## Make Your Presentation

- make a new folder
- add the presentation Jupyter Notebook
- type `python make_pres.py ./path/to/notebook`
- add a line in the top-level `index.md`
- add, commit, push
