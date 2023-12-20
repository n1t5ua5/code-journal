# DECEMBER '23

# 12/21/2023
# ???

# 12/20/2023 / repo: github.com/nitsua5/js30practice/commits/master
# Trying to tally strings with the .reduce method this morning. There is a list of video's time-length as strings & I am going to
# find the total length of all videos as a number. I've used .reduce before too, so it'll be good to utilize it again & learn
# something new in the process. First I declared a variabled named timeNodes & set it equal to Array.from(document.querySelectorAll(
# '[data-time]')); which selects all the DOM elements that have a data-time attribute. Then I declared a new variable 'seconds'
# to retrieve the seconds for each time listed by using the .map & .reduce function to extract all of the data-time values & store
# the data in a new array containing the values. I revisited using the % operator to return whatever is left over from the seconds
# variable to determine how many seconds are left from the original <ul> elements with a class of "videos". Everything works, then
# I calculated the total number of minutes by declaring a variable named mins & setting it equal to Math.floor(secondsLeft / 60);
# which is basically the same thing I did for the secondsLeft variable. Math.floor rounds down to the nearest whole number.
# 
# Now I'm going to work on a different project that's about utilizing webcams through code. To begin, we're using Node.js to input
# npm install & then npm start into the terminal. There is a really powerful dependency used inside of our package.json file so
# this project can be used on my local machine: "browser-sync": "^2.12.5 <2.23.2". Essentially, you cannot use webcams interchangeably
# over the internet for obvious privacy concerns. So this dependency is installed to take a photo through the webcam. Now that it's
# installed, both localhost:3000 & localhost:3001 are utilized so not only can it be used on a local machine, but potentially through
# a mobile device too. Then inside of my srcipt.js file I wrote a function named getVideo. Inside of the function is a new (for me),
# built-in method named navigator.mediaDevices.getUserMedia which gets the video inside of the video element & then video is set
# to true & audio to false. This returns a promise so we use the built-in method of .then & pass a callback function to retrieve
# localMediaStream. Finally the getVideo() function is called again in order for this to load. It's working in the console now.
# 
# 

# 12/19/2023
# Introduced to the .replace method today when making a function called sortedBands which should display a list of bands in array
# named bands. Implement logic to match prefixes of "a", "the" or "an" at the beginning of every name: return bandName.replace(
# /^(a |the |an )/i, '').trim(); The | operator tests if the input is present or not. Then the .sort method is used to see which
# order the names should be displayed in. Then the bands are displayed using DOM manipulation & finally the .map & .join method
# are used to create a new array which each band name wrapped in an <li> tag & then brought together into a sigle string. I've
# used the .sort & .join method before, but .replace definitely earned it's place in my toolbox.
# As always, check the repo out at https://github.com/nitsua5/js30practice/commits/master.

# 12/14/2023
# It's been good being able to learn a little more in my spare time before the year's over. Building & viewing a variety of projects
# has taught me a lot of random things that I probably wouldn'tve picked up on by myself. I used this to help fine-tune another
# project I've been working on that didn't even necessarily have to do with the lesson I was learning (it was about adding an
# addEventListener to detect when a user is scrolling *12/11/23*). But it made me realize the importance of UX when scrolling
# down/up & so I redesigned the project's homepage. Now I'm working on this mini-project back in JS30 where I'll be working mostly
# on adjusting CSS in an HTML file to work properly. I'm trying to add 'shadow' to an image by writing an addEventLister to detect
# when someone moves their mouse over the image. I used DOM manipulation to fetch an element with the class of 'hero' & then find the first
# h1 element within the '.here' element like this: const hero = document.querySelector('.hero'); const text = hero.querySelector('h1');.
# Then I created a function named shadow & added an addEventListener to check for an element of 'mousemove' which shows where
# the user's mouse is. I used the offsetWidth/Height method to show exactly where the mouse is on the page & now wherever I hover,
# a specific number is returned in the console. I'm feeling a lot more confident in debugging small issues then I did before too. In the
# past when an error appeared in the console, I got a small wave of panic, but now I just feel reassured everytime it points out
# any error because it's almost always a syntax issue. The shadow function now shows some color when hovering over it because I added
# text.style.textShadow. After applying some more styling & math, the cursor is responding perfectly! That's all for today folks.
# https://github.com/nitsua5/js30practice/commits/master

# 12/13/2023
# First time utilizing the localStorage method & it's pretty straight forward, it saves what you do onto your local machine. I got
# refamiliarized with the JSON.stringify method which is a little more specific then the .toString() method which has more of a general
# purpose use to display something quickly whereas JSON serilizes the data completely. I also used JSON.parse() again which I've used
# many times already. It converts whatever it's calling back into it's original state. So here's what's happening with this little menu
# ordering app: when we add an item we put it in localStorage & then when once the page loads, we check if something is in localStorage
# or use an empty array as a placeholder. Near the end, event delegation takes place with the toggleDown function by listening for
# something higher that's called & then inside of it we check for the item we actually want. Essentially everytime a change is made,
# the same action will be performed inside localStorage & then re-write the list. This one was a little more in depth & I really need
# to look it over again but for now, that's all for today. Please check the repo for yourself to look over my code & give any feedback!
# https://github.com/nitsua5/js30practice/commits/master

# 12/12/2023
# Practice began today by doing something easy with arrays. I started by declraring variables set equal to an array with a list of names as
# strings. Then adding more names to the original array & comparing it with a second variable that was set equal to the previous variable.
# ...here's what it looked like below..
# const players = ['Savi', 'Sage', 'Snickers']
# // declared a variable named players equal to an array of names as strings
# const team = players;
# // declared second variable equal to first variable
# console.log(players, team);
# // printed both variables in console
# team[3] = 'Sadie';
# // added a new name to team array
# ...this is what i printed to the console when i input the team & players variables...
# (4) ['Wes', 'Sarah', 'Ryan', 'Poppy']
# (4) ['Wes', 'Sarah', 'Ryan', 'Poppy']
# team
# (4) ['Wes', 'Sarah', 'Ryan', 'Sage']
# players
# (4) ['Wes', 'Sarah', 'Ryan', 'Sage']
# ...utilized the .concat method to make a copy of the old array & then with an es6 spread operator... (no pun intended)
# const team4 = [...players];
# // declared variable equal to an array of a copy of players
# team4[3] = 'lee-paw';
# // added a new name to team array
# console.log(team4);
# // printed team4 array to console
# const team5 = Array.from(players);
# // declare new variable named team5 set equal to the Array.from() method which is calling the players variable
# ...this is what i printed to the console when i input the team & players variables...
# team5
# (4) ['Wes', 'Sarah', 'Ryan', 'Poppy']
# team5[3] = 'cool'
# 'cool'
# players
# (4) ['Wes', 'Sarah', 'Ryan', 'Poppy']
# team5
# (4) ['Wes', 'Sarah', 'Ryan', 'cool']
# The differences between references & copies seem subtle at first but after practicing in the console with making them too I now realize
# their differences in literal terms too. I will write out the code I used once more below...
# const person = {
# name: 'Sage S',
# age: 80
# };
# const captain = person;
# captain.number = 99;
# I'm running out of time to write out the code but for the next few steps I learned to copy / reference objects, but I will talk about what
# I wrote on line 99 real quick: const sage = Object.assign({}, savi);  The Object.assign() method is used to copy the properties from
# the savi object to a new object which in this case is a blank one with nothing in it by default. I'm also going to reverse the
# direction I'm writing this journal in. Instead of progressively moving down, I'm going up now. Check out the repo for all my code:
# https://github.com/nitsua5/js30practice/commits/master

# 12/11/2023
# After practicing some questions on Codecademy about JavaScript & Python I began working on the JS30 project again, today's challenge is
# called Slide In on Scroll. I learned about another way to use DevTools, this time with console.count() for printing how many times
# something has appeared in the console, this time it was with a new function I wrote called checkSlide that ran everytime a user
# scrolled up or down on the .html page. I finished the challenge & was definitely confused at times but it makes sense with some
# hindsight. The function checkSlide iterates over each image selected & performs the same operation. Then it calculates the right pixel
# value for when the slide comes in with some other checks like if the user has scrolled past the image or not. If those conditions
# are met then a CSS class 'active' is added to the image. Phew, that's a mouthful. I'm calling it quits for today. Visit this url to
# check out any of the commits I made: https://github.com/nitsua5/js30practice/commits/master

# 12/10/2023
# Worked on a tiny little project that detects which keys have pressed on the keyboard or not. I wrote an if statement that checked if said event happened, which
# looked for a variable I declared named secretCode. If the secretCode value appeared in the console after being written in the browser then a built in
# JavaScript function named cornify_add() was called. This built in function is a random thing built by developers that makes raindows & unicorns
# stuff like that appear in the browser when it it's called, lol. In my spare time I used a CMS program called Square to develop a demo site
# for a project I'm working. The domain was purchased, it's now hosted by Square & it's live. It needs more content though so I will
# work on that starting tomorrow while I continue to push through this 30 day coding challenge. Find my most recent commit below
# https://github.com/nitsua5/js30practice/commits/master

# 12/08/2023
# I got a late start today but squeezed in some code nonetheless which made me happy because the momentum is definitely building & I'm feeling more comfortable
# writing my own functions & using different methods. As I continue along this JavaScript course, I'm noticing the continued important role that .addEventListener
# plays in using vanilla JavaScript. Today's project was redeveloping a dysfunctional video media player. I think the file is a little old itself but I still
# was able to practice declaring different variables using const, the .this method to direct where the video was being played directly & using fat arrow
# functions inside of .addEventListener. You can find the last commit I made for that project here: https://github.com/nitsua5/js30practice/commits/master

# 12/07/2023
# Documentating everything I'm learning like this helping me a lot, I'm really happy I finally started this. After a few more additons I'll make a basic web
# application for this whole project. Working again with the JavaScript30 Challenge, always to find that there really is something new to learn everyday.
# I began making a function called handleCheck which finds if a user has clicked on a checkbox or not. I'm also installing GitHub Co-Pilot today since
# I am learning all of these commands on my own for the first time, I need some assistance. After installing it, I thought it was more geared towards
# making commands in the terminal instead of vscode but It's working I suppose. I'm also starting to fully realize the depth of GitHub as I
# start to work in other branches now. The handleCheck function works now, when you select a checkbox on the form & then click shift, after if you click
# on another item in the form, you will have selected every option in between. That's why I declared variable named inBetween to clarify which items
# must be selected from the if statement in the handleCheck function. You can find the last commit I made for that project here below
# https://github.com/nitsua5/js30practice/commits/master

# 12/06/2023
# Today I picked up where I left off & started working on this 30 day JavaScript challenge I was told to practice with again & it's made a big difference so far.
# I familiarized myself with methods like .strokeStyle & .moveTo, grew accustom to using tools like console.table & console.group instead of just console.log
# while also getting to know how to use GitHub better. I'm more familiar with GitLab, so I know a lot of Git commands already but it's still new terrain.
# After many attempts of failing to push to the proper branch, I stepped back to think & realized that I forgot to merge my old branch with the new before
# inputting add ., commit -m "your-text-here" & git push origin main into my terminal. I also discovered a few other standard commands like git config
# user.name & user.email. Now all my work is published.
