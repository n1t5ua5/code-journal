# Friday, 01/12/2024
https://bit.ly/3HjLxde

I spent the morning doing some debugging of my own code in a private repo. I kept incurring an error in the console of my browser that stated how the "Number of translated a elements does not match. applyTranslations @ main.js:66 toggleTranslation @ main.js:34 onclick @ (index):81. From that I could tell that the source of the problem originated with my applyTranslate function & how it accepted a elements. It was accepting a elements from the entire program (there are eleven pairs in total), except I only needed the a elements within the nav element that had a class of "green-button" to be translated because the program names generally don't change from english to spanish, just how they're pronounced, so I only wanted the text in the translateButton to toggle along with the h1 & h4 elements to change. I altered the right variables inside of main.js to reflect their proper order & then altered the applyTranslate function so it only accepted those specific a elements. It took awhile to reconfigure it correctly + I had to alter the toggleTranslation function & the onClick event in a similar fashion.

On top of that, I re-familiarized myself with domain mapping when I purchased a new domain to be used for a basic tic-tac-toe project I built. In this case, with Pair as the host which runs on an Apache server, I had to edit the Apache VirtualHost configuration file to associate my new domain with the directory that my project is hosted in. This involved specifying the DocumentRoot & ServerName for the domain within the VirtualHost block. Now that I'm done with this other vanilla JavaScript coding challenge I had been working on, I needed to find something else to practice with in my spare time so I found a tiny course about the basics of Redux on Codecademy to brush up on state management! 


# Thursday, 01/11/24
https://github.com/nitsua5/js30practice/commits/master

Fixing up a countdown clock today. I got it to work in the console first by declaring a global variable of let dountdown & then writing a function named timer that expects a parameter of seconds & another beneath it named displayTimeLeft which also expects a parameter of seconds. I utilized the Date.now() method to get the current time in milliseconds. It then calculates the end time of the countdown by adding the input seconds to the current time. Then displayTimeLeft runs to initially show the time left. It logs the remaining seconds to the console & bam. timer(10) works in the console & stops at 1, next I input timer(100) & it returned 100 numbers in the console.

Now the code now interacts with HTML elements using DOM manipulation, document.querySelector, allowing for dynamic updates to the displayed time & end time. The addition of the displayEndTime function formats the end time for a more user-friendly presentation, while the startTimer function responds to button clicks, initiating the countdown with the specified duration. Moreover, the displayTimeLeft function has been improved to set the document title dynamically, enabling users to track the countdown even when the tab is inactive. I am definitely going to use this in a new project I'm going to start working on regarding music. Next I'm going to finish the last challenge once & for all! This one's about making an interactive game.

The HTML file contains mole holes with the class 'hole', a scoring display with the class 'score' & moles with the class 'mole'. Inside the <script></script? tags I declared the variables holes, scoreBoard, moles, lastHole, timeUp & score. Then I defined functions for generating a random time interval (randomTime), selecting a random mole hole (randomHole), making a mole appear & disappear (peep), starting the game (startGame) & handling clicks on moles (bonk). In the startGame function, the score is set to zero & the peep function is called to make a mole appear. The game runs for 10 seconds (setTimeout(() => timeUp = true, 10000)), during which players can click on moles to increase their score. The bonk function increments the score upon a legitimate click & updates the score display. Overall, the code creates a responsive & interactive whack-a-mole game with a 10-second time limit, where players aim to click as many moles as possible to score points.

This project is really useful & reinforces tactics like DOM manipulation & event handling - I'm going to remodel this into one that's called something like 'Whack-A-Cactus' & make it a little more in depth. I'm really proud to go through this whole crash-course. My coding reflexes are a lot more keen then they used to be. From here I'm going to start a course on redux, re-make this game into something better & keep on reading my Python book & download an e-book on JavaScript!


# Wednesday, 01/10/24
https://github.com/nitsua5/js30practice/commits/master

Later today I'll create another private repo for a tic-tac-toe game I made awhile back because I wanted to center it on all devices instead of residing on the left side like it currently does. It'll include to a second one I made as well! I also went back to that php project to fix some naming conventions one more time, I think I can finally put it to rest now. Update: the private repo has been created & I applied the d-n-r style.

I've got two days left of this vanilla JavaScript challenge my friend sent to me, my reflexes are a lot more keen now. Today I'm working on a video speed controller. The .mp4 wasn't working so I'll post a message in Slack if it isn't working by tomorrow. I tried using different browsers & inputting different .mp4 files but that didn't seem to do it either.

I followed along firdt by adding a new addEventListerner which waited for the object of mousemouve. This should show an event in the console but the only thing I get is an error about that ol' .mp4 (I tried simply adding an s to http but I still recieved an error in the console). The code's ready now for double checking tomorrow, considering there were also no notes about this error in the GitHub notes.


# Tuesday, 01/09/24
https://github.com/nitsua5/js30practice/commits/master

Tinkered with an old project that uses php earlier today. I didn't mess around with the logic too much, I mostly altered some naming conventions & that added the files to a new private repo I made for it. Now I'm heading back to finish some more of that vanilla JavaScript challenge I've been working on. 

Scrolling was the theme of today's lesson. I used the offsetLeft method once more to by subtracting slider.offsetLeft from e.pageX. This calculates the horizontal distance between the mouse click & the left edge of the .items element. Three more days left! Then I'll start a new course on Redux.


# Monday, 01/08/24
https://github.com/nitsua5/js30practice/commits/master

Fixed some icon resolution in my portfolio again 'cuz it just wasn't good enough. Now I'm working on a little mini-project about styling navs. After adding writing some addEventListeners & functions (handleEnter & handleLeave), the coordinates on the page are being consoled correctly because the console.log(dropdownCoords) statement inside the handleEnter function is successfully logging the coordinates of the dropdown menu to the console when the mouse enters the navigation element.

After I updated the width & height of the background element based on the dimensions of the dropdown menu (coords) & then the background element finally became responsive to the size of each specific dropdown menu when hovered over. A few more changes & now the code now accurately calculates the dropdown menu's position relative to the .top element & adjusts the background size & position accordingly. 


# Sunday, 01/07/24

Couldn't help but pick up the portfolio project one more time because the resolution on the mobile versions backdrop wasn't clear enough. Finally found one that works for it well. Thought about going back to that vanilla JavaScript course again but I think it's better to let the batteries recharge some more. 

# Saturday, 01/06/24

I've been getting carried away with my making my little portfolio site more responsive & now it really is. I had done almost everything planned for it before, but it was still kind of staticky. It's pretty late now so I'm gunna go back to reading tonight & solve some puzzles on Codecademy again.

# Friday, 01/05/24
https://github.com/nitsua5/js30practice/commits/master

I started another private repo, this time for all the random logical problems I find from places like Leetcode & such. It'll be good to have it as a reference to go back to & upload all the past one's into one spot. I want to create a new Leetcode problem, it'll be about human verification. 

Working with addEventListenders today. I was just introduced to the capture object which according to Wes is a boolean value that specifies whether an event should be handled during the event capturing phase (true) or during the event bubbling phase (false). 

Now we are using the stopPropagation method to stop triggering events from happening. Next the once property will be set to true underneath the capture property to unbind itself from the event. He explains that this sort of function could be used in store checkouts online where you do not want someone to be able to click something more then once. This was a mouthfull but definitely insightful.

Later on in the day I implemented a day / night mode toggle button on my portfolio along with some other minor styling updates. I went back to Codecademy & practiced some more random JavaScript & Python questions + I finally made my own 'Leetcode'-like logicical question too! It's very simple, but I'm feally proud of it. I've signed up for a Kindle account so I can read on the go & now as I'm winding down I finally picked back up the hardcover copy of "Practices of the Python Pro" by Dane Hillard that my friend lent me. I'm feeling increasingly accomplished tonight.


# Thursday, 01/04/24
https://github.com/nitsua5/js30practice/commits/master

I spent a long time today fixing up my portfolio. I took the vanilla JS & stored it in a main.js file to save some space, fixed up some styling too. Now I finally feel confident sharing it with others. It's hosted on Pair already, but now it's on GitHub too.

Back at the JavaScript30 challenge, today is all about keeping the position of the nav in place. I feel like I've been going into the weeds a little too much on some of my previous entries. So today, I'll focus mostly on the topic of something I learned new today as opposed to going thru every line of code.

Using the transform property to maintain an elements initial demensions proved to be super useful; I already know a project that could use something like this.


# Wednesday, 01/03/23
https://github.com/nitsua5/multiple-choices

I created a small game using python to help study for anything I want to learn more about. After being properly forked &
cloned, users can input their own unique datasets & then play the game when running 'python main.py' inside their own
terminal. Questions & answers are formatted in classic A, B, C, D multiple choice style.

Later on this week I'll write more in detail about it, but for now I'm redesigning my portfolio that I built using jQuery. I wrote a function using vanilla JavaScript to make all h4 elements flash on & off to make the application a little more dynamic. Finished the day by practicing some more Python & JavaScript via Codecademy trivia.


# DECEMBER 2023

# 12/28/23
# https://github.com/nitsua5/js30practice/commits/master

Reset my mind over the past week. Taking time to pause from thinking critically in this setting is necessary at times in my
humble opinion. I still want to write some code before the new year starts there to maintain consistency throughout 2024.
The SpeechSynthesis API exists in most browsers, like the SpeechRecognition API I just worked with the other week.

The foundational code in the index-START.html file creates a web interface called "The Voiceinator 5000" where users can
select voices, adjust speech rate & pitch, input text & trigger speech synthesis using JavaScript's SpeechSynthesisUtterance
object, while handling user interactions through event listeners. Some basic styling is included in the style.css file.

On line 39 I set msg.text equal to a querySelector where the name is equal to text & then I called the value afterwards.
I wrote the msg variable into the console & it's returning the SpeechSynthesisUtterance variable. I can tell it's working
because inside the variable is the pre-written text value of "Hello! I love JavaScript 👍".

I then learned that SpeechSynthesis is another global variable in the console which when calling .speak, allows you to
pass it an utterance. I tried making it work just now with the msg variable, but it's returning undefined because the
program still can't officially detect any speech just yet.

Next I wrote an EventListener for the speechSynthesis global variable which called the 'voiceschanged element' & the 
populateVoices function which is being written above it. The voices variable inside it is set equal this.getVoices(), &
finally I logged the voices variable to the console to check what would be returned.

Each voice is now being displayed in the console upon the page loading, inside of the SpeechSynthesisVoice object. These are
the contents inside 9 - default: false, lang: "fr-FR", localService: false, name: "Google français", voiceURI: "Google français".

Now I am going to loop over the all of the voices & set them as options in the Select a Voice dropdown menu. I used the .map
& .join methods once more to display the options when called via the voice function which includes the .name & .lang attributes.
I also changed the voiceOptions variable to now use the .innerHTML method on a variable named voicesDropdown set equal to voices.

It's working so far! I can see a new dropdown menu with each voice & when I pass the utterance into the console now, a voice is
returning the default text that I wrote above with the emoji. I also tried changing the value of msg via the console & the audio is
being played now too. I love this feeling. Now it's time to get the options to actually work once selected.

I wrote a new function named setVoice & console.logged this.value which corresponds to a new EventListener for the voicesDropdown
variable. It calls 'change' & the setVoice function. Next we set msg.voice is equal to voices.find which loops over the list to find
the correct voice attribute that responds to the option being selected. 

But nothing is working in the console. When I input speechSynthesis.speak(msg), I hear the old the original voice of 'David',
however once I select another name & input the same command into the console, nothing changes. I feel ike everything should
work just fine... what could it be? Instead of panicking, I paused & rewinded the tutorial. 

It looked like everything I was supposed to do checked out & there weren't any errors in the console either...
I scanned my code like a hawk to see if something else had transpired & low & behold I had a syntax issue. Instead of 
checking if voice.name matched this.value, I had written this.valaue. That was easy & now it's all working as it should.

A function named toggle is written now to switch between each voice selected. I call speechSynthesis.cancel() to stop it from
speaking & then speechSynthesis.speak(msg) to start it all over again. toggle() is now being called within the setVoice function
on the next line & now everything is working when it's toggled between the different options just like it should.

A new event listener is added next so that forEach of the 'options' selected, we wait for the setOption function to be
called. After the toggle function the setOption is created & accepts msg[this.value] set equal to this.value which is
whatever the value selected currently is. The pitch & rate knobs are working properly now too & it's weird, lol.

In succession are the buttons that need to be listened to. So I add a fourth one beneath the other three which
listens for the speakButton which simply toggles when clicked. The stopButton however looks for toggle(false) to
be called within a fat arrow function. Lastly I will add the .filter method inside of the populateVoices function.


# 12/21/2023 / repo: github.com/nitsua5/js30practice/commits/master
Speech recogniton is going to be the focal point for today's mini-project. Apparently there's a built-in method with Firefox &
Chrome window.SpeechRecognition || webkitSpeechRecognition (as of the date of the video which is around five years old). First,
I'm figuring out how to at least get the tool to recognize someone talking by creating a new instance of SpeechRecognition();.
Then we set the recognition of interimResults equal to the boolean value of true. So as we speak, the recognition works alongside
us. As instructed, I utilized Node.js once more by inputting "npm install" followed by "npm start" into my terminal to build
a custom server for this project. At this point using these commands feel like muscle memory which definitely makes me happy!

Caught another error as I implemented the recognition to begin each time the page was loaded through recognition.start();
When I loaded the page, nothing changed. So I went into the console & read an error message that said "Uncaught ReferenceError:
recognition is not defined at index-START.html:20:3. When I see these I can almost immediately recognize there was a typo, as I
had intentionally defined recognition on line 16 - it was the second line I wrote. I used CTRL+F to scan every instance of the
value "recognition" & oddly enough the one on line 16 wasn't appearing in the list. I carefully observed every variable with
said value until I realized I didn't add a second 'i' in the word recognition. Problem solved.

I used addEventListener on the recognition object so that when 'result' is triggered, the speech recogniton commences. Then I
converted the e.results array into a normal JS array using Array.from, after I map over the array using the .map method again
like from yesterday's project. Now my speech is being recognized in the console! This is pretty cool, but it only works when
you keep talking. If you pause, it stops working too because we are always listening for the 'result' & when that finishes,
nothing else is supposed to happen as of now. Gotta fix that by adding in another addEventListener + get it working in the
browser too. Text is showing in the DOM, but I need to get it so that it keeps a record of what's said instead of starting
over each time. I wrote an if statement that checks if the 'results' are final, then the <p> element is appended o the .words
container in the DOM, ensuring that each finalized segment of recognized speech appeared distinctly.

I wanted to practice with a second mini project again today, but apparently the next one on geolocation only works for apple
devices & I only use Windows as of now so I'll just skip to the next one about links. As I get closer to finishing this vanilla
JavaScript course, I'm starting to look for something new to practice with. Ok, time to learn some more. This time we're
replacting something built on Stripe's homepage. Essentially what is happening is that when you hover over different tabs
in the navbar, the links reveal a dropdown menu but instead of the normal one you're used to, the menu expands & has
unique content. We won't replicate the whole thing today, but start with something small. I used const to declare a
variable named "triggers" set equal document.querySelectorAll('a') which selects any <a> element in the DOM & returns
a NodeList that match the previous. Then I created a 'span' element with the class of 'highlight' which attaches
a message into the consolee of "Highlight!!" when the mouse hovers of any <a> element. It's working so far!!

I've been introduced to a new method named .getBoundingClientRect which if used properly will return the exact location where
an element is on the DOM. Now we apply styling to the highlightLink function so that whenever an element is hovered over,
not only do we have an exact location of the element, but this time CSS is applied each time. In our case, a highlighter
is used. It appears to be working at first glance, but when scrolling down & hovering over some more links, the exact
location is not being applied correctly. So in order to make everything match perfectly for this particular application
we will make our own unique coordinates. This was accomplished by adjusting the top & left values to account for the scroll
position of the webpage. Awesome. Tomorrow I'll do some more + I'm finally going to dive back into recreating an
algorithm a friend showed me recently. It can be found on Leetcode too: leetcode.com/problems/valid-parentheses/


# 12/20/2023 / repo: github.com/nitsua5/js30practice/commits/master
Trying to tally strings with the .reduce method this morning. There is a list of video's time-length as strings & I am going to
find the total length of all videos as a number. I've used .reduce before too, so it'll be good to utilize it again & learn
something new in the process. First I declared a variabled named timeNodes & set it equal to Array.from(document.querySelectorAll(
'[data-time]')); which selects all the DOM elements that have a data-time attribute. Then I declared a new variable 'seconds'
to retrieve the seconds for each time listed by using the .map & .reduce function to extract all of the data-time values & store
the data in a new array containing the values. I revisited using the % operator to return whatever is left over from the seconds
variable to determine how many seconds are left from the original <ul> elements with a class of "videos". Everything works, then
I calculated the total number of minutes by declaring a variable named mins & setting it equal to Math.floor(secondsLeft / 60);
which is basically the same thing I did for the secondsLeft variable. Math.floor rounds down to the nearest whole number.

Now I'm going to work on a different project that's about utilizing webcams through code. To begin, we're using Node.js to input
npm install & then npm start into the terminal. There is a really powerful dependency used inside of our package.json file so
this project can be used on my local machine: "browser-sync": "^2.12.5 <2.23.2". Essentially, you cannot use webcams interchangeably
over the internet for obvious privacy concerns so it must be tied to a secure origin. Localhost is still considere a secure origin
even if the padlock / belt symbol is present like normal sites with https. So this dependency is installed to take a photo through
the webcam. Now that it's installed, both localhost:3000 & localhost:3001 are utilized so not only can it be used on a local machine,
but potentially through a mobile device too. Then inside of my srcipt.js file I wrote a function named getVideo. Inside of the function
is a new (for me), built-in method named navigator.mediaDevices.getUserMedia which gets the video inside of the video element & then video
is set to true & audio to false. This returns a promise so we use the built-in method of .then & pass a callback function to retrieve
localMediaStream. Finally the getVideo() function is called again in order for this to load. It's working in the console now.

But then I followed Wes' video some more & the webcam light was on but I was not appearing in the upper right hand corner
as it should have worked inititally. He said to declare the video.srcObject equal to window.URL.createObjectURL(localMediaStream);
but in the console an error persisted: scripts.js:8 Uncaught TypeError: Cannot read properties of undefined (reading 'getUserMedia')
at getVideo (scripts.js:8:28) at scripts.js:19:1. I knew it was calling for an error in regards to getUserMedia, which made sense
because the media in literal terms wasn't appearing & sequentially it probably had to do with line 11 given the logic being
performed: video.srcObject = window.URL.createObjectURL(localMediaStream);. I also knew I had previously clicked allow when
asked for permission by the browser so my setting were correct. I looked inside the files some more & realized Wes left
a comment in the scripts-finished.js file after all.
 
The takePhoto function I wrote is working; I downloaded the image & then opened it to view. I'm happy, this is getting
complex but could definitely be used in the future for some sort of project, this really has become a great resource. 
I used the debugger method to naviagte through each action being taken, in order not to log millions of pixels to the
console via the setInterval function. All the filters are working now, phew, that was a lot.


# 12/19/2023
Introduced to the .replace method today when making a function called sortedBands which should display a list of bands in array
named bands. Implement logic to match prefixes of "a", "the" or "an" at the beginning of every name: return bandName.replace(
/^(a |the |an )/i, '').trim(); The | operator tests if the input is present or not. Then the .sort method is used to see which
order the names should be displayed in. Then the bands are displayed using DOM manipulation & finally the .map & .join method
are used to create a new array which each band name wrapped in an <li> tag & then brought together into a sigle string. I've
used the .sort & .join method before, but .replace definitely earned it's place in my toolbox.
As always, check the repo out at https://github.com/nitsua5/js30practice/commits/master.


# 12/14/2023
It's been good being able to learn a little more in my spare time before the year's over. Building & viewing a variety of projects
has taught me a lot of random things that I probably wouldn'tve picked up on by myself. I used this to help fine-tune another
project I've been working on that didn't even necessarily have to do with the lesson I was learning (it was about adding an
addEventListener to detect when a user is scrolling *12/11/23*). But it made me realize the importance of UX when scrolling
down/up & so I redesigned the project's homepage. Now I'm working on this mini-project back in JS30 where I'll be working mostly
on adjusting CSS in an HTML file to work properly. I'm trying to add 'shadow' to an image by writing an addEventLister to detect
when someone moves their mouse over the image. I used DOM manipulation to fetch an element with the class of 'hero' & then find the first
h1 element within the '.here' element like this: const hero = document.querySelector('.hero'); const text = hero.querySelector('h1');.
Then I created a function named shadow & added an addEventListener to check for an element of 'mousemove' which shows where
the user's mouse is. I used the offsetWidth/Height method to show exactly where the mouse is on the page & now wherever I hover,
a specific number is returned in the console. I'm feeling a lot more confident in debugging small issues then I did before too. In the
past when an error appeared in the console, I got a small wave of panic, but now I just feel reassured everytime it points out
any error because it's almost always a syntax issue. The shadow function now shows some color when hovering over it because I added
text.style.textShadow. After applying some more styling & math, the cursor is responding perfectly! That's all for today folks.
https://github.com/nitsua5/js30practice/commits/master


# 12/13/2023
First time utilizing the localStorage method & it's pretty straight forward, it saves what you do onto your local machine. I got
refamiliarized with the JSON.stringify method which is a little more specific then the .toString() method which has more of a general
purpose use to display something quickly whereas JSON serilizes the data completely. I also used JSON.parse() again which I've used
many times already. It converts whatever it's calling back into it's original state. So here's what's happening with this little menu
ordering app: when we add an item we put it in localStorage & then when once the page loads, we check if something is in localStorage
or use an empty array as a placeholder. Near the end, event delegation takes place with the toggleDown function by listening for
something higher that's called & then inside of it we check for the item we actually want. Essentially everytime a change is made,
the same action will be performed inside localStorage & then re-write the list. This one was a little more in depth & I really need
to look it over again but for now, that's all for today. Please check the repo for yourself to look over my code & give any feedback!
https://github.com/nitsua5/js30practice/commits/master


# 12/12/2023
Practice began today by doing something easy with arrays. I started by declraring variables set equal to an array with a list of names as
strings. Then adding more names to the original array & comparing it with a second variable that was set equal to the previous variable.
...here's what it looked like below..
const players = ['Savi', 'Sage', 'Snickers']
// declared a variable named players equal to an array of names as strings
const team = players;
// declared second variable equal to first variable
console.log(players, team);
// printed both variables in console
team[3] = 'Sadie';
// added a new name to team array
...this is what i printed to the console when i input the team & players variables...
(4) ['Wes', 'Sarah', 'Ryan', 'Poppy']
(4) ['Wes', 'Sarah', 'Ryan', 'Poppy']
team
(4) ['Wes', 'Sarah', 'Ryan', 'Sage']
players
(4) ['Wes', 'Sarah', 'Ryan', 'Sage']
...utilized the .concat method to make a copy of the old array & then with an es6 spread operator... (no pun intended)
const team4 = [...players];
// declared variable equal to an array of a copy of players
team4[3] = 'lee-paw';
// added a new name to team array
console.log(team4);
// printed team4 array to console
const team5 = Array.from(players);
// declare new variable named team5 set equal to the Array.from() method which is calling the players variable
...this is what i printed to the console when i input the team & players variables...
team5
(4) ['Wes', 'Sarah', 'Ryan', 'Poppy']
team5[3] = 'cool'
'cool'
players
(4) ['Wes', 'Sarah', 'Ryan', 'Poppy']
team5
(4) ['Wes', 'Sarah', 'Ryan', 'cool']
The differences between references & copies seem subtle at first but after practicing in the console with making them too I now realize
their differences in literal terms too. I will write out the code I used once more below...
const person = {
name: 'Sage S',
age: 80
};
const captain = person;
captain.number = 99;
I'm running out of time to write out the code but for the next few steps I learned to copy / reference objects, but I will talk about what
I wrote on line 99 real quick: const sage = Object.assign({}, savi);  The Object.assign() method is used to copy the properties from
the savi object to a new object which in this case is a blank one with nothing in it by default. I'm also going to reverse the
direction I'm writing this journal in. Instead of progressively moving down, I'm going up now. Check out the repo for all my code:
https://github.com/nitsua5/js30practice/commits/master


12/11/2023
After practicing some questions on Codecademy about JavaScript & Python I began working on the JS30 project again, today's challenge is
called Slide In on Scroll. I learned about another way to use DevTools, this time with console.count() for printing how many times
something has appeared in the console, this time it was with a new function I wrote called checkSlide that ran everytime a user
scrolled up or down on the .html page. I finished the challenge & was definitely confused at times but it makes sense with some
hindsight. The function checkSlide iterates over each image selected & performs the same operation. Then it calculates the right pixel
value for when the slide comes in with some other checks like if the user has scrolled past the image or not. If those conditions
are met then a CSS class 'active' is added to the image. Phew, that's a mouthful. I'm calling it quits for today. Visit this url to
check out any of the commits I made: https://github.com/nitsua5/js30practice/commits/master


12/10/2023
Worked on a tiny little project that detects which keys have pressed on the keyboard or not. I wrote an if statement that checked if said event happened, which
looked for a variable I declared named secretCode. If the secretCode value appeared in the console after being written in the browser then a built in
JavaScript function named cornify_add() was called. This built in function is a random thing built by developers that makes raindows & unicorns
stuff like that appear in the browser when it it's called, lol. In my spare time I used a CMS program called Square to develop a demo site
for a project I'm working. The domain was purchased, it's now hosted by Square & it's live. It needs more content though so I will
work on that starting tomorrow while I continue to push through this 30 day coding challenge. Find my most recent commit below
https://github.com/nitsua5/js30practice/commits/master


12/08/2023
I got a late start today but squeezed in some code nonetheless which made me happy because the momentum is definitely building & I'm feeling more comfortable
writing my own functions & using different methods. As I continue along this JavaScript course, I'm noticing the continued important role that .addEventListener
plays in using vanilla JavaScript. Today's project was redeveloping a dysfunctional video media player. I think the file is a little old itself but I still
was able to practice declaring different variables using const, the .this method to direct where the video was being played directly & using fat arrow
functions inside of .addEventListener. You can find the last commit I made for that project here: https://github.com/nitsua5/js30practice/commits/master


12/07/2023
Documentating everything I'm learning like this helping me a lot, I'm really happy I finally started this. After a few more additons I'll make a basic web
application for this whole project. Working again with the JavaScript30 Challenge, always to find that there really is something new to learn everyday.
I began making a function called handleCheck which finds if a user has clicked on a checkbox or not. I'm also installing GitHub Co-Pilot today since
I am learning all of these commands on my own for the first time, I need some assistance. After installing it, I thought it was more geared towards
making commands in the terminal instead of vscode but It's working I suppose. I'm also starting to fully realize the depth of GitHub as I
start to work in other branches now. The handleCheck function works now, when you select a checkbox on the form & then click shift, after if you click
on another item in the form, you will have selected every option in between. That's why I declared variable named inBetween to clarify which items
must be selected from the if statement in the handleCheck function. You can find the last commit I made for that project here below
https://github.com/nitsua5/js30practice/commits/master


12/06/2023
Today I picked up where I left off & started working on this 30 day JavaScript challenge I was told to practice with again & it's made a big difference so far.
I familiarized myself with methods like .strokeStyle & .moveTo, grew accustom to using tools like console.table & console.group instead of just console.log
while also getting to know how to use GitHub better. I'm more familiar with GitLab, so I know a lot of Git commands already but it's still new terrain.
After many attempts of failing to push to the proper branch, I stepped back to think & realized that I forgot to merge my old branch with the new before
inputting add ., commit -m "your-text-here" & git push origin main into my terminal. I also discovered a few other standard commands like git config
user.name & user.email. Now all my work is published.
