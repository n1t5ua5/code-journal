-----
-----
-----

## Tuesday, 02/10/2026 🌤️
https://www.cloudns.net/blog/domain-parking/


<img width="538" height="288" alt="image" src="https://github.com/user-attachments/assets/9a7b50b0-c7b3-42ec-ba87-265b5537871d" />


Been knee-deep in homework these past few weeks, but I found time to sneak in a quick personal project that I've been wanting to take care of for a while now. I discovered a few of my idle domains had fallen victim to unauthorized domain parking. This happens when a third party - or sometimes the registrar by default - points your DNS records to their own servers to profit from the traffic. I suspected my host might have enabled this, which is common practice. Upon inspection, I found several "A" records I never created, so I removed them immediately. Wanting more control, I migrated the domains to Cloudflare by updating my nameservers.

To keep the domains active with a "Coming-Soon" page, I wrote a custom index.html file & deployed it using Cloudflare's Workers segments. By using Cloudflare Workers, I've eliminated the need for traditional hosting. My index.html file isn't sitting on a server; it’s baked into a serverless function that executes at the network edge. This means my 'Coming-Soon' page is served with near-zero latency from whatever data center is closest to the visitor. Aside from the domain registration fees, this setup is entirely free & takes less than an hour to implement. I’m hoping to film a quick tutorial for my YouTube channel soon because this is an awesome way to completely secure your digital assets.

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
