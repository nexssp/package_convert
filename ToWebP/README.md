# Convert/toWebP - Nexss PROGRAMMER 2.x

Convert Image files to WebP

## Examples

```sh
nexss Convert/ToWebP myfile.jpg myfile2.jpg

nexss Convert/ToWebP/Images myfolder # will convert all images in the specified folder


```

Example of Nexss Programmer script which convert images to webp by one command.

```nexss
FS/Files .  --_inFileTypes=.png --_inFileTypes=.jpg --_inFileTypes=.gif
Convert/ToWebp
```

## TODO

- [ ] Add Video Conversion
- [ ] Add directory crawl (subfolders)
