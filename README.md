# Snake AI

## But made with Python

If you have seen my [`other version of a Snake AI that was written in Java`](https://github.com/SCRIPTERBLOX/SelfBeatingSnake) Then you know the jist of what this is.

For those who haven't seen it, its about as straightforward as it can be.
Its a bot that plays snake and reaches the maximum length.

## What is different in this version

As the title says this version of the `Snake Ai`  was written in `Python` making it allot `faster` and more people understand it.

### Additionally

In the past version the AI would only loop over the `entire` map before returning to the start and repeating the entire cycle and had basically not even anything close to self awareness.

### However

In this version of the `Snake AI` I implemented logic so that if food spawned that was behind the snake then it would turn around and return to the start before having finished the round.

### There is more

In the previous version of the `Snake AI` I had already tried to implement code so that the snake would be rendered rainbow but had failed after a multitude of attempts.

In this version of the `Snake AI` I however had managed to implement code making the snake be rendered `rainbow colored`.

## What can you do

### Support my work

If you want to support my work including this `Snake AI` then there are a few things you can do:

 1. You can subscribe to `my YouTube channel`

You can find `my YouTube channel` under the name of SCRIPTERBLOX or at the following link: https://www.youtube.com/@scriptoblox. On this channel I create videos about how I create projects like this.

 2. You can visit `my website`

I have a website which you can find under scripterblox.github.io and i would greatly appreciate it allot if you would take the time to check it out.

### Download this just for looking at

[![Download](https://img.shields.io/badge/Download-File-darkblue?style=plastic&label=Download&labelColor=darkred&color=darkblue)](./dist/main.exe)

Just click this button and click the `Download raw file` button.

If you download the `.exe` file and double click it windows will flag it as a virus.
It is not a virus.
I know that I would say that if it was a virus.
But the reason it is being flagged as a virus is that I did not sign the file and because usually viruses also are not signed windows thinks that that could be a virus.

I guarantee you that to the day I get hacked that `.exe`  is not going to be a virus.

### Use this for your own stuff

If you want to embed my `Snake AI` into your own projects, develop on it yourself or anything else (as long as it is not monetary distribution without any own additions) then you can follow the following instructions for a detailed guide on how to use this yourself.

### Follow the steps you are sure you have not done yet

#### Install Python

1. Got to python.org
2. Go to the downloads section
3. Bellow the tabs you should see 

>Download the latest version for Windows

and bellow you should see something like:
`Download Python 3.13.1`
Although the version will probably differ.

If you are on windows you can simply proceed by clicking that button and following on to step 4

If you are on any other operating system then bellow that button should be listed other operating systems with links to their respective download pages.

As I do not use any other operating systems than windows I am not familiar with how the downloading procedures for other operating systems work I am not able to explain how to follow for installing but you should be able to download a form of installer and if you run it then you should be fine.

4. For windows users in the installer they should be able to select an option like `Add to path` enable this option and proceed through the installer.
5. When the installer is finished Python should be installed and you are able to proceed

#### Downloading an IDE

6. Not strictly necessary but very helpful `Downloading an IDE`:

- If you wish to use an IDE and do not have one installed yet then please follow the following steps
- Select an IDE of your choosing
- As I use IntelliJ for Python development I am only familiar with other setup processes but they should be fairly straightforward and similar to setup
- For IntelliJ go to https://www.jetbrains.com/idea/download/
- ### Important DO NOT SELECT THE TOP OPTION
- Instead scroll down to the community edition and select which for of installer you wish to use and download it.
- Open the installer and follow through the installation process. If you wish you can tick the `Add program ascociation` boxes.
- When you finished the installer then open IntelliJ or your IDE of choosing and continue

#### Create a new project

- Select the `New project` button
- In IntelliJ at the bottom left select the `More via plugins...` option. For other IDEs the plugins button might be somewhere else.
- In IntelliJ there should be an option for Python. For other IDEs you might have to search for it,
- In IntelliJ there is a free Community edition Python plugin. Just download it and you might need to restart your IDE.
- When your IDE has loaded again then you will need to again select the `New Project` Button.
- Now you should be able to select the Python programming language for the template.

- In IntelliJ you should be able to follow these instructions without issues. For other IDEs there might be similar procedures but I would not know.

	1. For the `Name`  you can choose whatever you want.
	2. `Location` is mostly fine as whatever it is. If you plan to create more projects then you might want to setup a organisation structure and select it accordingly
	3. You can leave the `Create Git repository` as is or deselect it.
	4. For `Environment` you should probably select `New`
	5. For `Environment type` I use `Virtualenv` but others could also work.
	6. You can leave the `Location` section that comes after that as is.
	7. If `Base interpreter` is not already set you can just set it for the one the Python installer had created.
	8. The `Inherit global site-packages` and `Make availible to all projects` buttons can be ignored.
	9. Finally you can click the `Create` button
	10. IntelliJ will now create the virtual environment and some other project files.

#### Import my code

7. On the GitHub page you are reading this on scroll to the top and select the `Code` option
8. Click on `Download Zip`
9. When the zip file has downloaded extract its contents and open the file
10. If there is another subfolder then just open that one
 11. In this folder there should be a directory named `src`
 12. Hold down on the folder and go into IntelliJ and whilst holding `Ctrl` (or on Mac `Cmd`) and release the left mouse button whilst holding down on the top directory displayed in IntelliJ.
 13. It will probably ask you something along the lines of

> Do you want to copy the specified files into this directory?
14. Select the `Yes` option.
15.  If everything worked then you should see a directory named `src` under the top directory
16. If you want right click the `src` directory and go to the bottom to `Mark Directory as` and then select `Sources root`

#### Import the Python packages

17. Finally you only need to install the Python packages
18. In IntelliJ at the bottom left select the terminal button.
19. In there paste and execute the following commands:

    pip install pygame;
    pip install numpy

20. Now if you expand the `src` directory and double click on the main.py file then at the top you should be able to click on the run button.
21. If everything worked to plan then you should now see a green line dash over the screen at hardware depending speeds.
