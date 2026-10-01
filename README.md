# Microtonal Init Presets For Reason

This repo contains presets for multiple Reason Rack devices, grouped by tuning.

To get started,
[download here](https://github.com/xerydian/Microtonal-Init-Presets/archive/refs/heads/main.zip)
and extract it in ~/Music/Reason Studios/User Library

This repo also contains the scripts to generate the presets.
<br>You can tweak the list of tunings, and other settings in `config.py`

```bash
git clone https://github.com/xerydian/Microtonal-Init-Presets
cd Microtonal-Init-Presets
uv run generate-presets
```


### Contents

This pack contains presets in:
- 14edo, 15edo, 16edo, 17edo, 19edo, 22edo, 24edo, 27edo, 29edo,
<br>31edo, 34edo, 36edo, 41edo, 43edo, 53edo
- 44ed6 (~17edo), 49ed6 (~19edo), 57ed6 (~22edo), 70ed6 (~27edo), 88ed6 (~34edo),
- 26edt (double BP), 39edt (triple BP), 27edt (~~17edo), 30edt (~~19edo), 
<br>43edt (~~27edo), 54edt (~~34edo)
- Wendy Carlos' Alpha, Beta & Gamma

For the following Rack instruments:
- **Reason Studio**: Complex-1, Europa, Grain, Parsec, Polytone
- **Third party**: Antidote, Arkana, Autosub, Blackpole Station, BitSynthzr, 
DyingStar, MonoPoly, Nostromo, Obsession, Spectra, The Legend HZ, Torsion, VK-2 Synthesizer


### Helpers

Universally microtune (almost) any Rack instrument.
<br>Requires: CV out, CV splitter, x2 Tinker instances, an instrument with Pitch Bend support.
<br>Example setup: 
```
Blamsoft Distributor
  |--> Voice 1 --> CV splitter 
  |                   |--> (In A) Tinker: Note (Result) --> (Note CV) Instrument #1
  |                   |--> (In A) Tinker: Bend (Result) --> (Pitch Bend)
  |--> Voice 2 (Optional) (Same setup)
  |--> ...

(Tweak the 'Number of Voices' parameter accordingly)
```

Note: Some devices don't expose a Pitch Bend CV jack but do accept Pitch Bend input, 
<br>Place the  Combinator to achieve this
- **One voice**: 
  <br>CV Connections (Rear view)
  <br>- Tinker: Bend (Result) --> Combinator (Wheel CV In) Pitch Bend
- **Multiple voices**:
  <br>CV Connections (Rear view)
  <br>- Tinker: Bend (Result) --> Combinator CV1, or CV2, ..., CV8
  <br>Editor mapping (Front view)
  <br>- Source: CV In 1, or CV In 2, ..., CV In 8
  <br>- Target: Pitch Bend
