# github-tpm-screener
I created this repo to share my answers to the GitHub Technical Program Manager screener questions.

### Part 1
*In your own words, please describe the most challenging project you coordinated in the past that had tight deadlines and involved collaboration from multiple teams. How did you go about it? What were the biggest challenges? If you were tasked with coordinating for that project now, what would you do differently?*

### Response
The most challenging project I've managed was building the new UX Design desktop tool from concept to release: Adobe Experience Design (XD). In the process of bootstrapping a new Creative Cloud app, I partnered & collaborated with many internal Adobe core tech teams upon which we had dependencies for deliverables and services. These teams included Licensing, Identity Management Services, Analytics, Localization, Enterprise Enablement, Documentation, Web (Adobe.com), Social & Marketing, and of course, Creative Cloud. The sheer volume of people and teams I dealt with was challenging in itself, but engagement with each of the individual teams also presented unique challenges. With core tech teams, the challenges were often technical in nature when integrating core libraries into our product. Here, I'd partner with Program Managers on those teams to identify blocking issues & (sometimes) new requirements, and facilatated many technical discussions among respective engineering teams. All of our coretech teams are in India, so timezone latency and evening/early morning meetings added challenge. With other partner teams who provided services and deliverables to us, schedule alignment (and slippage) was especially challenging. Again here, the Program Managers on these teams were my inner circle. We overcommunicated all schedule-impacting info, we negotiated through slippages, we shared and maintained blocking schedules & wikis, we were the neural network of Adobe XD. All of this culiminated when we launched for the first time to millions of Creative Cloud subcribers in March 2016.  The actual launch plan I built and relied upon heavily can be seen [here](https://drive.google.com/file/d/0B-u9VXyw_OlMazJUeXFWY2dxR0k/view?usp=sharing).  (please forgive the poor wiki to PDF export quality).

Within my core team, consisting of ~70 people divided into 5 squads, I also managed intra-team coordination among the squads, ensuring sprint goals were set & achieved, tracking feature completion status, and controlling & communicating risk. The biggest challenges in this part of the program were around intra-team deliverables. For example, PM needs to write out detailed stories to hand off to Engineers, the Analytics teams needs to define instrumentation spec for a feature story, and XD needs to provide designs to hand to Engineers.  The design deliverables were always the most problematic so if I had to start this project over again, this is where I'd do things differently. When the deliverables are coming from an external agency (which was about 25% of the time), I'd be fairly dogmatic (which I am only when absolutely necessary) about thorough requirements definition & signoff before moving to the execution phase. I'd put more structure in the iterative design reviews to ensure all perspectives are considered. For deliverables fron internal Design teams, I'd explore better tools & processes for sharing, presenting, and version controlling assets.  Designers love Dropbox; Engineers love GitHub. Jumping between the two to track assets and design comps caused much pain and I'd really want to fix that.


### Part 2

*1. Clone https://github.com/defunkt/jquery-pjax onto your computer.*

*2. So now we want to write a script/program to show the emails of everyone who has committed to this repository, and how many times each person has committed.*

*3. There's already a git command that does basically this: git shortlog -nse. Run it so you can see how it looks.*

*4. You'll simplify it to just print out the email and number of commits (rather than email, name, and number of commits as shortlog -nse does).*

*5. Make your script/program do that using the output of git log. You may use any options to git log that you wish.*


*Sample output:  12 contributor1@gmail.com 12 contributor2@gmail.com 10 anotehrcontributor@github.com ...  3. Test your output and write your script in the language of your choice. Make sure to include a short description of your provided implementation. Similar to the way you would describe it if you were to open a pull request with your solution.*


### Response
- For #1, I forked it and cloned it from here: [https://github.com/rhauck/jquery-pjax](https://github.com/rhauck/jquery-pjax)
- For #2-5, I submitted the script as [PR #1 on this repo](https://github.com/rhauck/github-tpm-screener/pull/1)
