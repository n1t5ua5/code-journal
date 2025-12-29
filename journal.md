## Monday, 12/29/2025 🎉
## https://youtu.be/xi4C42VD0ko?si=p-POWbHdKHmlbLgV


<img width="1885" height="854" alt="image" src="https://github.com/user-attachments/assets/7b254223-0eaa-4be4-a00e-3cf55ce59fcb" />


The end of the year is just around the corner & I'm feeling very relieved. I've accomplished almost everything I wanted to this year, except for redeploying that ol' MLS-Monitor app via Railway. I might be able to get it finished up before the 1st, but it's unlikely due to my current schedule. However, it's at the very top of my to-do list. One of my friends gave me some pretty clear instructions months ago on how to accomplish this, but I started reviewing some generic 'how-to' videos just to refresh myself a little first before I dive back in. Incredibly grateful for the people in my life who've given me feedback or helped me in any way on this coding journey of mine, I'm not quite sure what I'd do without them & promise to pay it forward myself.

Next year, I plan to obtain my AA degree in Computer Programming & also get accepted into another university, where I'll pursue a Bachelor's degree in Computer Science. Outside of technology & school, I really want to focus on learning how to read & write music. I know some of the basics, but without a better foundation, I'm missing too much to consider myself literate. While I don't plan on pursuing this outside of a hobby of mine, it's something that's been in the back of my mind for years & I'm excited that I'm finally going to get the hang of it. Duolingo actually inspired me to revisit this dream, because they added three new courses to their application this past year, which don't revolve around linguistics: Math, Music & Chess (I use them all, too). Also, special shout-out to Grammarly! I've known about this application for years, but never tried using it before this past semester & now that I have - I can't imagine working without it again. I knew I was prone to making grammatical errors, but I didn't realize the full extent until now.

-----
-----
-----

## Wednesday, 12/11/2025 ✒️
## https://bit.ly/48OAx5e


<img width="547" height="418" alt="Screenshot 2025-11-20 202819" src="https://github.com/user-attachments/assets/23d2bdb5-08fa-4bc3-b2b6-357b21ed4474" />
<img width="830" height="320" alt="Screenshot 2025-12-10 231521" src="https://github.com/user-attachments/assets/e0cf19d0-c14c-4fec-aed7-f23e2894a51d" />


The Fall semester is coming to an end this week & I'm starting to feel less stressed already. I believe I did well in most of my classes, but I won't know my grades for another week or so. Next semester I'm taking three more: Algebra, Network Technologies & Security Essentials. I'm looking forward to starting them, but I just hope I get to take more in the future about Linux, Python & System Design because I enjoyed all of them this past semester. In addition to the other markdown-journal files I have in this directory, I decided to upload some of my discussion posts in their own markdown files too because they're essentially journal entries in themselves & I want to be able to reference some of the things I've learned later on before I no longer have access to them. I've also taken screenshots like the one I used above, which I added into my Notion account so I can see all the posts in their original format, along with having the text in markdown files.

However, now that I have these examples from this past semester, it will be easier to replicate in the future for any new discussion posts. In addition to my YouTube account that has new videos I've uploaded from a project about Linux that I completed this past semester, I'm going to upload some of the other important projects I've completed into my repository here soon, so I can formally add them to my portfolio instead of only having them locally on my device. Shout out to my Python tutor from this past semester! They're good people & advised me to do well but they also taught me one extremely valuable lesson that's going to save me a ton of space on my computer. I was using VS code during our tutoring sessions, when they showed me how to use Codespaces here on GitHub. So instead of jumping on my local terminal by default because it seems like the quickest option, I'm going to work here on the Linux terminal in Codespaces a lot more. I also love the preview mode inside the terminal so I don't have to go back & forth as much between here & the browser! I need to mess around with it a little more tomorrow though. Online GDB is another Linux virtual terminal I learned about this past semester & I really liked using it too to officiate code that I submitted to my professors, but I will still probably keep most of my code here in GitHub. 

-----
-----
-----

## Wednesday, 10/08/2025 📁
## https://www.teamgantt.com/
## https://www.youtube.com/watch?v=bbmWOjuFmgA


<img width="940" height="448" alt="image" src="https://github.com/user-attachments/assets/56cadbfa-0436-4810-a992-0a5db5142196" />


Finally finished Part 2 of my System Analysis & Design project before the submission deadline. It's tedious, but I'm enjoying going through a hypothetical scenario where I'm setting up industrial grade wi-fi for a plant nursery retail chain! I find it satisfying mostly because I'm thoroughly analyzing every single step I make & I'm accomplishing everything I set out to do. Please refer to the image above regarding the GANTT chart I made for my project. The full twelve page document also includes a feasability study, cost estimations & a prelimary investigative report - although this isn't the final product, just a draft for now.

Later on in the evening I switched gears to focus on my Linux Fundamentals course. This module, we're mostly learning about filesystem management by watching youtube videos (like I added above) & working inside a virtual terminal via Cengage. Below are some of the commands that I used today specifically. I'm finding that the `sudo` command to be incredibly important when it comes to navigating in the terminal. The `sudo` command (Substitute User DO) permits a user to execute a single command with the same security privliges of another user, which is referred to as the "root" user or `superuser`. This gives administrators a safe way to perform tasks without having to log in as the root user, which reduces the chance of inflicting digital damage.

We also learned about designing hard disk layout, creating partitions & I used the `fdisk`, `mount` & `unmount` commands for the first time. If I'm understanding things correctly, `fdisk` allows us to view, create, delete & manipulate disk partions (dividing a single physical hard drive into one or more seperate, independent regions) on a hard drive. Mounting is the process of attaching a separate storage drive to a specific empty branch on that tree, while unmounting is the process of detaching the storage device from its `mount` point.

`su root`
`p@ssw0rd`
`visudo`
`Student1   ALL=(ALL) 	ALL`
`esc` + `:wq`
`su Student1`

`sudo fdisk /dev/sda`
`m`
`l`
`q`
`clear`

`sudo mkdir /mnt/cdrom`
`sudo mount -r -t iso9660 /dev/cdrom /mnt/cdrom`
`ls -l /mnt/cdrom`

-----
-----
-----

## Wednesday, 10/01/2025 ⌨️
## https://www.youtube.com/watch?v=u-OmVr_fT4s&t=1s


<img width="928" height="873" alt="image" src="https://github.com/user-attachments/assets/877c65a0-3ce3-41fd-984d-2e0a02a1d295" />


Today I worked with my tutor from college once more on some python practice problems assigned to me that involves creating functions. The YouTube video link above is one way we learned about functions before working on something similar to the assignment for Module 6, which is what I worked on with my tutor. One thing they pointed out that ties into another class I'm currently taking, Linux Fundamentals; is how they no longer use VScode for hands-on coding. Instead, they use Codespaces here inside GitHub & the terminal used by GitHub is Linux.

I only have experience working inside of Windows Powershell, but after taking my Linux Fundamentals course this semester, I'm looking for other ways to practice using Linux commands in the terminal & this is the perfect way I can practice from here on out. Normally in class, I'm working from a virtual terminal anyways, so this works & functions exactly the same as I've been taught + the syntax really isn't that much different from what's used with Windows. I also started a Linux Journal to document my Linux journey specifically which is the second link above, just like I did with my Java projects from earlier this year. 

-----
-----
-----

## Thursday, 09/25/2025 🐍
## https://youtu.be/g1AFlLhgMR8?si=GDUwlqEKlTjj5xRo


<img width="1014" height="456" alt="image" src="https://github.com/user-attachments/assets/d4a0d934-5581-4f63-8e43-7ee830730f36" />


I cannot express how fulfilling it's been for me to start working with a tutor again. Thankfully someone at my school has been working with me this semester because although a lot of the stuff I'm learning about in my Python class so far isn't necessarily new to me, I'm still a little shaky when it comes to hands on coding. My biggest issue continues to be having difficulty parsing the questions from english into code when I'm given a blank canvass but I know I have to overcome this through practice. For now & the foreseeable future, I can't imagine learning without meeting with a tutor on a regular basis.

Above is one of the video lessons from YouTube that we watched for my class this module & beneath that is a screenshot of some of the code I wrote out during it, it's about the differences between for loops & while loops. The biggest takeaway for me was clearly seeing how for loops are best used when you already know how many times you must iterate, while loops on the other hand are best used when conditions must be met beforehand. I worked on a different assignment with my tutor that elaborated further on using while loops with conditional statements. Until next Wednesday when I meet with my tutor next, I've got to refocus on my Linux & System Design classes which I plan on writing a little more about in here soon too. 

-----
-----
-----

## Monday, 09/22/2025 📝
## https://www.freecodecamp.org/news/start-a-career-in-technical-writing-through-open-source/ 


<img width="892" height="471" alt="image" src="https://github.com/user-attachments/assets/09f3fe80-eca4-4de5-b69f-4ca43681c92b" />


After a long day & evening of studying the basics of Linux once more for my college course, I found a lot of inspiration in reading more about technical writing via FreeCodeCamp. Through my background in marketing & writing newsletters, I've grown accustomed to writing out what I've done while I code. While I still might not be an expert technical writer myself, I know it's within my ability to bridge the gap between developers & users by explaining every step or process in a concise manner.

Next week I'll begin contributing to an open source project of my own choosing, so I can reengage in technical writing for others. This almost feels like being a Wikipedia editor & translating articles from language to another, but this is a little more complex & fulfilling to me. If you have any suggestions or experience in technical writing, please reach out so we can connect! As a side note, the new FreeCodeCamp app is amazing too; the daily coding challenges they provide are helping build my confidence in myself, particularly with Python.

-----
-----
-----

## Tuesday, 08/12/2025 🎬
## https://bit.ly/46SHD9w


<img width="327" height="228" alt="image" src="https://github.com/user-attachments/assets/e6658ed4-1455-4300-9309-1ddaffc56652" />


Spent the morning & afternoon finishing getting all of my projects organized for making these demo videos. It took a little longer than anticipated because I wanted to make sure that I had mostly everything in the videos on here as well, which took an hour or so working locally inside my terminal with Git to get everything compatible with what's on GitHub. This also included writing & editing some more technical documentation. But now that five out of the six videos are done, I only need to finish one more, but I won't do this until I finish working with my friend on getting that last project deployed live with it's own host because the previous system stopped functioning randomly earlier in 2024. I don't have an exact timeline on when that will be done precisely, but it should be finished before the month of October starts. Until then, I need to make four different proto-type landing pages for clients & prepare for this upcoming semester. But I won't be starting those things until next week so I haven't decided on any of the technical specifications yet either.

-----
-----
-----

## Monday, 08/11/2025 🎨
## https://bit.ly/46SHD9w


<img width="1158" height="400" alt="image" src="https://github.com/user-attachments/assets/48607f15-aa47-4bb8-8fd2-226eeff18333" />


My hiatus from journaling on here took a lot longer then expected. Between now & then I've read some books, finished some college courses & most importantly finally brought my portfolio to live here on GitHub. Take a look using the link above but the image below is in regards to adding an artist palette emoji (YouTube Link) to its footer by creating a new div wrapping around the old div (Flashlight Emoji) & new div with a class of footer-content, then added some new CSS properties like 'inline-block display' instead of just 'block display' to ensure they'd sit next to each other, as opposed to above or below. As for the rest of this week, I'm going to finish making some more video demos for all the different 'generations' I've projects I've made, then start preparing for the upcoming semester where I'll be taking a new Python course & another on Info Tech Project Management - wish me luck!

-----
-----
-----

## Tuesday, 01/07/2025  💡
## https://youtu.be/9cr1XZlEir0


<img width="1158" height="400" alt="image" src="https://github.com/user-attachments/assets/48607f15-aa47-4bb8-8fd2-226eeff18333" />


Though I definitely needed a break these past few weeks, I'm happy to be back learning something new again. Java's syntax never really grew on me in regards to learnability, but I do appreciate having a solid understanding of another object-oriented programming language. I'll be using it again soon but for now I'm going back to my Practices of the Python Pro book to continue reading again in my spare time, along with starting a Linux introduction course on CodeCademy to parallel the new college course that I just started taking today called Linux Fundamentals. In a few weeks I'll be starting another IT course as well, called Network Technologies. One major thing missing from this journl are screenshots, which I'll be including from here on out to showcase my progress in a more literal way. As for today, I'm mostly just reading, but ended it watching an interesting YouTube video suggested by my new professor.

-----
-----
-----
