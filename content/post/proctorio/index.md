---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Dissecting Proctorio"
subtitle: ""
summary: ""
authors: ['thom']
tags: []
categories: []
date: 2020-09-30T12:40:28+02:00
lastmod: 2021-02-23T12:35:28+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: "Proctorio's attempt at stopping the hacks is easily circumvented."
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

_This article previously appeared in [Thalia](https://thalia.nu)'s Thabloid, in the [2019–2020 issue number 5](https://thalia.nu/media/public/thabloids/thabloid-2019-2020-5.pdf). It was written at the end of May and may not reflect current practice at Radboud University._

{{% callout note %}
This article is getting a lot of traffic from people who appear to be looking for a way to defeat Proctorio.
This article is discussion of some of the technical and ethical issues about online proctoring.
It will not tell you how to cheat on your exam.
I also do not have a modified version of Proctorio that defeats any of its countermeasures.
{{% /callout %}}

Desperate times seem to call for desperate measures. Faced with a closed campus, universities have been scrambling to find a suitable alternative for the classic pen-and-paper exam. Digital exams, for example via Brightspace or Cirrus, are a more-or-less easily solvable problem. However, when taking the exam at home it may be slightly too tempting to leave the book and your phone on the table. Sending the people who monitor exams in the Gymnasion’s HAL2 to everyone’s homes obviously wouldn’t work, especially since a lot of them seem to be in the at-risk categories...

Following many other universities in the Netherlands, our university has been experimenting with Proctorio. Proctorio offers software that supposedly replaces the HAL2 invigilators. Some of you may even already have written exams that have been proctored via Proctorio. Either at TU/e or in one of the experiments that have also been undertaken in some of the courses of our education institute.

For those who have not (yet) suffered the Proctorio treatment, the current understanding of how it would be implemented at Radboud University is as follows.[^1][^BWK+20] You will need to have a somewhat reliable internet connection,[^2] a computer that can run a Chromium-based browser, a webcam and a microphone.[^3] You will need to install the Proctorio plugin into your browser. Then you can navigate to the Cirrus exam page, where Proctorio will be launched. Before you are allowed into the exam, Proctorio will have you enable your webcam and microphone. It closes all open tabs in the browser. It also uses the screen-sharing functionality in Chromium, originally built for video calls, to record your screen. You will have to show a photo ID to the webcam to identify yourself.[^4] Following this, you will be asked to take your webcam and film your entire room to prove you are alone, that your desk is clean and that you haven’t stuck sticky notes out of view of the webcam. After this, you can take the exam, during which the microphone and webcam will continue to record you.

Proctorio claims to use artificial intelligence to then determine if the person in front of the webcam is cheating. It records the screen, webcam and microphone and makes those recordings available to the university. In the Radboud proposal, these recordings will not be made available to the teachers, but only to a “specially trained team” of invigilators, who will look at the segments that Proctorio marked as suspicious and contact the exam committee if necessary.

It will be clear that such monitoring has far-reaching privacy implications. Although you are also being watched for two hours during an on-campus exam, this happens in a public place where there are only people who are taking the exam. The webcam of your laptop is pointed at a private living space, where other people may also live. Proctorio may thus record things that you may wish to keep private, like a poster for a political party, a weed grinder, medication for depression, furry handcuffs on your bed or an LGBTQIA+ flag. It will also record your screen. Browsers are typically pieces of software that reveal many things about someone’s life. Even though Proctorio may not access the browser history, the screen sharing might for example expose the bookmarks toolbar. The bookmarks there might reveal things that are also extremely private, like someone frequenting a mental health forum or cancer survivor forum. Or even worse, there could be links to Pottermore.

These privacy concerns can be somewhat addressed, but online invigilators will remain invasive. Although the author has no legal qualifications, we can pose the question if the privacy implications are proportional to the concerns of cheating and validity of exams. As such, we will now examine Proctorio. 



## Technical details of Proctorio
Many are concerned about running such invasive software on their personal computers. Fortunately, the architecture allows us to quell some of the concerns. Proctorio is implemented as a browser plugin for Chromium. Such plugins are mostly sandboxed and can only access things through the APIs exposed by the browser.[^Chrome20] This means that it can not view any files on the computer or read any browser history or passwords. It also does not have low-level access to the hardware, and can mostly only read some generic properties about some specific hardware, such as device names for microphones and webcams, or screen resolutions.

## Take-home hacking
One big difference between an exam in HAL2 and an exam at home is the fact that we have virtually unlimited time to maliciously prepare the exam environment: our bedroom or study. As such, any virtual proctoring has limitations and it can not be bullet-proof. None of the things we will discuss in the following are new or novel. SURF published a whitepaper[^SURF20] on proctoring that already mentions all the things that we propose. This also means that the university should already be aware of every single one of them. Some of the attacks are low-tech and may be solvable via enhanced procedures, but other attacks are much more difficult to address.

### The sticky note
It remains unclear to the author how thorough the room scan is. Can you hide a sticky note under your keyboard, and take it out during the exam? Or what if I stick it under the table? Can I carefully aim the laptop to keep part of my desk out of view?

### The virtual machine
You may have seen the attack by Peter Schwabe and Veelasha Moonsamy where they ran Proctorio in a virtual machine. This obviously defeats the screen recording, as only the screen inside the virtual machine can be seen by Proctorio. This allowed them to look up the answer to a question on Wikipedia.

This is not an attack that Proctorio can solve. If it had direct access to the ``CPUID`` registers of the CPU, it could figure out if it was run using hardware virtualisation. However, the Chromium ``system.cpu`` API only exposes fairly generic CPU features such as AVX2 support, which will not be influenced by virtualisation. What remains are the other system properties it can read. This includes the names of microphones, number of cores, screen resolutions, disk sizes and power status. These properties can be used to develop heuristics to detect virtual machines, but it is easy to see that these can be defeated by tweaking some settings in the virtualisation software and running the VM at the full screen resolution.

### Remote desktop
A remote desktop application allows your computer to be taken over by someone remotely, who can then type things and move the mouse, etc. I do not think Proctorio can see this at all, if the remote desktop application is not visible on the screen. Proctorio can not see running applications if they are not on the screen after all. The person behind the webcam just needs to act like they are taking the exam for however long the exam takes.

## Breaking Proctorio altogether
Because Proctorio is a Chromium browser plugin, we have access to the source code. Browser plugins are written in Javascript. We can simply install the plugin, open up the Chromium profile folder and access the source code. Although the source code is minified, meaning all the spaces have been deleted, a Javascript beautifier makes the code readable in seconds. Additionally, all the functions and variables have been renamed to `a`, `b`, `c`... — but once we figure out what a subroutine does or a variable represents, we can use refactoring tools to rename it throughout the program.

A good place to start is searching for Chrome browser API calls. If we search the source code for ``system.cpu`` We can quickly see that the Proctorio plugin reads the number of cores, as we expected. However, while we’re there, we can also replace that function call by something that simply returns false information... We can do the same with all the other 

Near this segment of code, we find some lists of strings. We see that Proctorio contains a blacklist of device names that it should block as representing valid webcams and microphones. We just delete the blacklist. Now we can run Snapchat Camera to make the exam as Nicolas Cage or simply use VLC to set up a fake webcam that plays back a recorded video.

{{<figure src="webcams.png" caption="A screenshot of the Proctorio source code" alt="A screenshot of the Proctorio source code showing lists of strings containing names of fake webcam and microphone software" >}}

Scrolling yet a bit further, we find something very curious. Sprinkled throughout the code are references to a page on the Proctorio domain ending in ``/hacker``. We find the page says “our IP has been blocked”. Oops. It turns out that there are a number of anti-tampering measures embedded in the plugin. It for example checks if the developer console is opened while Proctorio is running or if the plugin has been sideloaded instead of installed from the Chromium webstore. If that happens, it opens this ``/hacker`` page and uninstalls itself. Fortunately, we can simply search the source code for all occurrences of ``chrome.management.uninstallSelf()`` and of ``/hacker``, so we simply disable all those pieces of code. One of these occurrences, funnily enough, is triggered by the presence of the “Chrome extension source viewer” extension in your browser.

## Caveat emptor
I should point out again that I have not tried running the modified Proctorio plugin described above — I did not have access to a proctored exam to run it on. However, it seems that this would not be hard to do given, for example, a trial environment provided before the exam for testing your setup. Still, I would not advise anyone to execute any of these attacks. Any consequences will be your responsibility.

When faced with the VM attack, the response was that Proctorio can track cursor movement and keyboard sounds and should have detected it — but it clearly did not. It may not have been enabled correctly, but I am not sure if the video recording would look all that suspicious if you simply use a quiet keyboard or set up your microphone with a high noise filter such that it simply does not pick up keyboard sounds. Perhaps the university should not get into this cat-and-mouse style games, especially if it has a huge probability of turning into he-said, she-said discussions.

Alternatives for pen-and-paper exams may sometimes be hard to come up with and more effort to execute, but often they also make for better exams. As I am currently teaching 200 students myself, I very much appreciate the amount of time taken up by teaching. This is time that, the way universities are set up in the Netherlands, does not further your career in any meaningful way, as success is pretty much exclusively measured in publications and grant money collected. However, that should not be an excuse to stick to multiple-choice exams, push the concerns of trivial cheating off on a tech solution while invading the students’ privacy and sticking your fingers in your ears to pretend it is working. The RU proposal[^BWK+20] reveals that a large part of the concern is just to keep exam questions secret by disabling the clipboard and print functionality in your browser. Why that may be important for the validity of your exam will be left as an exercise to the reader – but clearly this will not stop anyone who ever heard about screen recording software.

## References

[^BWK+20]: Andrea Bonarius, Evelien Westerbeek, Jeroen Kassenberg, Muriël Deuss, Roel van Uden. Online-proctoring: voorstel gebruik online-proctoring voor veilige digitale toetsafname off-campus met toetssoftware Cirrus. 8 april 2020.
[^GV745]: CvB GV 745 - Antwoorden op UGV: Vragen over Privacy in tijden van corona en digitaal onderwijs. 20 april 2020
[^SURF20]: SURF Whitepaper online proctoring: vragen en antwoorden bij surveilleren op afstand. april 2020. https://www.surf.nl/files/2020-04/surf-rapport-online-proctoring_2020_update-april-2020.pdf
[^Chrome20]: https://developer.chrome.com/extensions/api_index

[^1]: The author has not written any exams with Proctorio and the “settings” may still change, so your specific experience may vary. Partially based on experiments by Peter Schwabe and Veelasha Moonsamy.
[^2]: Unlike TU/e, it seem the RU will not automatically invalidate exams if you disconnect during the exam. [^GV745] You will need to take the entire setup procedure again.
[^3]: The university did a survey,[^BWK+20] most students indicated to have this. The university intends to make loan devices available.
[^4]: It is not clear to me how the ID is processed.





<!-- vim: set ft=markdown ts=2 sw=2 tw=0 et -->
