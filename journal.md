## Tuesday, 11/3/2026 🗳️
https://accessibility-widget.pages.dev/


<img width="1913" height="896" alt="image" src="https://github.com/user-attachments/assets/31e8d20d-25a7-4eda-9349-f80539cd5472" />


Hey y'all, I didn't forget about my last entry & there's even been a few times I've wanted to jump back in here & write a little, but today calls for a small, but necessary update to one of the main domains that I manage. I've already added widgets for users to update either/both language & cookie preferences awhile back, but I've been dwelling internally about the lack of options for people with other accessibility preferences & knew I could find a quick fix after recalling how easy it was to input the other two I customized. I searched online & found the website tagged above, but I'm sure there are other good options out there, I just needed a quick, reliable fix because the overhaul this site needs won't take place for at least another six months (or, maybe even up to one year depending on my workload in 2027). Other than that, college is going well overall still, though I'm definitely tiring of this never ending flow of classwork. However, that will be ending in 2027 when I switch from attending as a full-time student, to part-time.

Once I got the right code snippet from the website I previously references, I logged onto my Weebly site editor & went inside the site settings, input the snippet & published the site again to make the updates live. Immediately I noticed a major problem in the browser, the new widget was now appearing underneath the cookie widget. After applying different in-line styling methods to the snippet such as bottom-left, I figured I should just update the CSS of these objects directly because there wasn't any pre-existing styling done to the cookie widget anyways, so this new fix should be quick. I also knew that while I haven't looked quite yet, there's no way that this - or a similar issue - was occurring with the mobile version, but I wanted to focus on that part last. I created two new classes for both of the widgets inside the CSS section for my site's footer code & then adjusted their positioning accordingly. The only micro-issue I faced there was taking a little longer to adjust the pixel size for the bottom positioning of the cookie widget, but that's all thankfully. Then I published the site again to ensure the changes were made live & eureka! Those changes are pictured in the screenshot above. Afterwards, I went inside the mobile CSS section & input a media tag which encapsulated the rest of the mobile CSS code. I published the site once more & then I viewed the project through the browser on my mobile device & was successful.

On a separate note, today's election day in the United States, so don't forget to get out there & VOTE everybody; see ya next year!


-----
-----
-----

## Monday, 07/13/2026 💤
https://www.api-football.com/


<img width="1641" height="632" alt="apiFootballimage" src="https://github.com/user-attachments/assets/15bf31e8-921d-4c6d-8cb3-7cd4a6986a7d" />


I want to write another journal entry today because I'm not going to be using this as much in the near future once I finish a small how-to video today. Despite not achieving my goal of writing something inside here once per month, I'm more than proud of the input I've managed to accomplish so far. However, I need to transition from computers into mathematics due to my coursework at college. While I'll always dabble in web development in the background & write more about the things I learn, for the sake of brevity, I can't afford to shift my attention beyond math for now. I know I can still write about math too, but for now I prefer to use any of my free time towards working with a math tutor. I'm not sure exactly when I'll write inside here again in the near term, but I predict finishing all of that coursework by around this time next year. Until then, folks! 


-----
-----
-----

## Friday, 05/08/2026 🪴
https://bit.ly/4tkrvFj


<img width="730" height="730" alt="image" src="https://github.com/user-attachments/assets/b86ffaae-793a-493f-bb23-ffe0923cf951" />


Another semester is down & now it's on to the next. No major surprises in my course selection this go-around, other than Intro to C. I wasn't planning on learning another programming language before finishing my degree, but it's helping me obtain a certification alongside my studies. While I haven't written much in C yet, learning the basics on Codecademy & FreeCodeCamp have been super helpful so far. Reflecting on the previous semester, I’ve realized how much my interest in cybersecurity grew after taking my Security Essentials course. I won't have any related courses for the next two semesters, but I look forward to exploring the field further during my graduate degree.

For my final project in that Security Essentials class, I created a video presentation about Security Through Obscurity (STO). I’ve always believed that 'camouflage' is an effective tool, provided it’s recognized as a single layer of a broader security approach rather than a total fix. STO helps in reducing attack surface & defending a system through multiple layers. Outside of tech, I’ve been working in the garden a lot recently & finally harvested enough plants to create a powdered fertilizer. I can’t wait to write more about this in the coming months because soon I'll have enough product to sell at the farmer's markets & online!

-----
-----
-----

## Tuesday, 02/10/2026 🌤️
https://bit.ly/4dvniK2


<img width="538" height="288" alt="image" src="https://github.com/user-attachments/assets/9a7b50b0-c7b3-42ec-ba87-265b5537871d" />


Been knee-deep in homework these past few weeks, but I found time to sneak in a quick personal project that I've been wanting to take care of for a while now. I discovered a few of my idle domains had fallen victim to unauthorized domain parking. This happens when a third party - or sometimes the registrar by default - points your DNS records to their own servers to profit from the traffic. I suspected my host might have enabled this, which is common practice, but it doesn't appear to have been them based on my account settings. Upon further inspection of my DNS records, I found several "A" records I never created, so I removed them immediately. Wanting more control, I migrated the domains to Cloudflare by updating my nameservers.

To keep the domains 'active' with a "Coming-Soon" page, I wrote a custom index.html file & deployed it using Cloudflare's Workers segments. By using Cloudflare Workers, I've eliminated the need for traditional hosting. My index.html file isn't sitting on a server; it’s baked into a serverless function that executes at the network edge. This means my 'Coming-Soon' page is served with near-zero latency from whatever data center is closest to the visitor. Aside from the domain registration fees, this setup is entirely free & takes less than an hour to implement. I’m hoping to film a quick tutorial for my YouTube channel soon because this is an awesome way to completely secure your digital assets.

-----
-----
-----

## Tuesday, 1/13/2026 🛜
https://bit.ly/4bwuqFm


<img width="1010" height="526" alt="image" src="https://github.com/user-attachments/assets/e13693c2-22a0-477f-95ec-29dcd87444f2" />


It's always rough starting a new semester but I feel more prepared than usual this time. The most helpful thing is having access to a tutor that can guide me in the right direction when I'm going off-path. The most difficult class so far is my math class & I probably won't do too much journaling about that one mostly due to the fact that we don't have any written assignments. However, the other two will both have many written assignments (neither course requires hands on coding either). I know a little from my own research regarding my Network Technologies class but there's a lot for me to discover about my Security Essentials course.

So far I've conducted some written research regarding different network topologies for the first class & submitted another written assignment about threat actors for the second. For the record, I'm posting all of these without any sort of revisions from my professor(s), so it's possible that some of the information in these journal sections are incorrect, although I try my best to only include things I'm able to fully grasp. That's all for now, folks!

-----
-----
-----
