# Rowser (Python)

This is a prototype implementation of a Text-based browser inspired by Firefox + Vimium controls.

Full-scale implementation will target faster languages like Rust, Go, C, or Zig.

## Theme

Web Browsing with native Vim controls

## Motivation

Firefox + Vimium has been my preferred web browsing setup for several months now. However, the Vimium plugin requires a running javascript instance for it to work. So, there would be a delay between opening a webpage and being able to use the Vimium Controls (because the javascript instance runs inside the webpage). Also, I do not yet have a good project to attempt a lower-level language in. Finally, PDF's suffer from the same problem as the javascript delay, since no javascript is running when the PDF file is open.

In Summary, Firefox + Vimium has:
1. Delayed controls when opening a new website
2. Vimium Controls do not work with PDF files
3. A great case to experiment with lower-level programming languages

While the terminal-based implementation does not solve point #2, a future GUI-based implementation using Firefox's Gecko engine would be an interesting future project.

## Notes

This the currently considered procedure for rendering a website using the terminal.
1. Loop through the tags of a website until the terminal is filled
2. If tag is recognized (e.g. form, title, header, paragraph, etc.)
3. Rowser will choose an appropriate render object for the tag.
4. Renders the object to the terminal
5. Ends Loop
6. If user makes an action
7. Rowser will identify the change and re-render the appropriate objects. For example, scrolling down will delete the upper object and renders the object below.

## Milestone

- [x] Achieved a text parser that prints to terminal - 2025-06-18
- [x] Began making a terminal user interface using Rich - 2025-06-19
