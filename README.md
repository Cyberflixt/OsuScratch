# osu-Scratch
*osu! made on scratch (optimised)*

⚠️ This is an old project and not up to my scratch overengineering standards

<h1>Links</h1>

- 🪶 [osu! Scratch Light](https://scratch.mit.edu/projects/560772811/) (~3Go of ram, 10 songs)
- 💾 [osu! Scratch Full](https://scratch.mit.edu/projects/538618292) (∞ of ram, more songs, might crash laptops)

<h1></h1>

![OsuScratchGameplay2](https://github.com/Cyberflixt/OsuScratch/assets/54700008/6c1b96be-4ef6-476a-909b-f8030c2bf81a)

> please ignore skill issues

<h1>System</h1>

### Osz Extractor

⚠️ Only supports circles

![Extractor demo](https://github.com/Cyberflixt/OsuScratch/assets/54700008/e8071126-092c-4e88-943a-11085ebfa8b7)

Result can easily be unpacked by string splitting with the used separators

### defaults separators:

> since we want to optimise the splitting process, we're praying to not find these characters in our song's name

> defaults can be changed in the extractor script

- map = "§" (same song, different difficulties)
  - datatype = "µ" ([0] metadata, [1] map elements)
    - metadata keys/values = "¨" ([0] key, [1] value)
    - elements = ";" (all circles)
      - values = "," (circle data: [0] X, [1] Y, [2] Time, [3], Type)

![Tb](https://github.com/Cyberflixt/OsuScratch/assets/54700008/a186aeac-a4a6-415a-8e96-94aeef144f4d)

> In Osu!Scratch **full** (Light version is stripped from features such as developpement tools)

Copy paste the data produced by the python file (yes it's supposed to be huge)<br>
You can then add the thumbnail and music by giving them the same name as the filename.
Moreover, a preview of the music can be added with the name "0{song name}"

Once you are done, go in "Publish" sprite and use the resetting block.<br>
This will clear any map compilation cache

![image](https://github.com/Cyberflixt/OsuScratch/assets/54700008/6fa8a396-03f6-49f8-9716-69f3f42c624d)

