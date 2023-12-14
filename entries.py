# DECEMBER 2023

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
