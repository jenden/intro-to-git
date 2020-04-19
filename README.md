# Intro to Git

>  If you write code, you should be using a version control system. 


At it's most basic, version control tracks changes in files over time and allows you to easily view differences and restory the last working version if you break something (which you will). Most version control systems work at the file level so they don’t care if you’re writing R, Python, GAMS, C++ or CSS or just text like this tutorial. 

If you're writing software, then you can connect your version control system into a continuous integration (CI) and continuous delivery or deployment (CD) pipeline that will help you ship faster and better quality products.



### What you'll learn

The goal is at the end of this lab you should are Git literate (giterate?). You'll know why it's useful, the basics of how it works, how to follow a simple analysis workflow and enough about advanced capabilities that you can decide if you want to learn more.


### Questions

1. Have you used a version control system before?
2. How comfortable are you with using a command line interface?
3. How often do you anticipate writing code in your career?


### What you'll need

1. Git installed on your computer. Depending on your system, it may already be installed. 

   - On a Mac, open the Terminal application type `git --version` and then hit enter. If you see a response like the one below you're all set. If git is not installed, you should be prompted to install the Xcode Command Line tools from Apple. If all else fails, follow the instructions on [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install for macOS.

     <img src="images/macos-git-version.png" alt="macos-git-version" width="500"/>

   - Windows doesn't come pre-installed with Git so you'll need to download it from [git-scm.com](https://git-scm.com/downloads) for Windows. During the installation you should select the defaults for all prompts except the text editor. Here I highly recommend selecting `nano` because the default `vim` , while powerful, is not at all user friendly. 

     <img src="images/windows-git-text-editor.png" alt="windows-git-text-editor" width="500"/>

     Find *Git Bash* in your start menu and open a new prompt. Type `git --version` to confirm that git is available and installed. You should see something like this:

     <img src="images/windows-git-bash.png" alt="windows-git-bash" width="500"/>

   - If you use Linux, my guess is you already know what you're doing. If not, use Google to install git for your specific distribution. 

2. An account on the git server of your choice. I'm going to be using [GitHub](https://github.com) in the lecture because it's very popular and I recommend you do as well unless you already have an account somewhere else. 
   - [Sign-up for GitHub](https://github.com/join) or [login](https://github.com/login) in to an existing account. You'll need these credentials during the lab in order to commit code to your repository.
3. A proper text editor or IDE. I plan to use [Visual Studio Code](https://code.visualstudio.com) because it's nice middle ground between a barebones text editor and a full fledged Integrated Development Environment (IDE). You can use whatever editor you're comfortable with as long as it can manage plain text and code (i.e. not Microsoft Word).
4. Basic familiarity with using a terminal. If you're on Windows I recommend getting familiar with *Git Bash* which is packaged with Git. On Mac or Linux just open a Terminal application. If you're unfamiliar with bash or need a refresher, please check out these links *before* we start the lab. I recommend [this lecture](https://missing.csail.mit.edu/2020/course-shell/) or this [blog post](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a). At a minimum you should be comfortable
   - Navigating the file system with `pwd` and `cd` 
   - Listing files in a directory with `ls`
   - Looking at the contents of a file with `cat` or `less`


### Activity

We're going to recreate the plot of Covid-19 cases by region since the 100th case using the data compiled by [John's Hopkins](https://github.com/CSSEGISandData). We'll start with an empty folder, initialize a repository and we'll build up the contents together to create a simple version of this plot. While we're going through this process we'll talk about how git works under the hood and what each action is doing. This should take about an hour.

Then you should find a partner, clone your partner's repository and make an improvement like adding growth rate lines, filters for country, hover tools, etc. Once the changes are working locally, you will submit a pull request for your partner which explains the changes. We'll go through how to review the changes and merge them into your repository.

At the end we'll try to save a bit of time to through some useful next steps and answer questions. 


## Recommended Resources

**Getting started**
* [Version Control with GitHub](https://raw.githack.com/uo-ec607/lectures/master/02-git/02-Git.html#1) from Data Science for Economists course at University of Oregon. 
* [Happy Git and GitHub for the useR](https://happygitwithr.com)
* [Development Workflows for Data Scientists](https://resources.github.com/downloads/development-workflows-data-scientists.pdf)

**When things go wrong**
* [Oh Sh!t Git](https://ohshitgit.com) when you've made a mistake

**How git works**
* [Explain Git in Simple Words](https://smusamashah.github.io/explain-git-in-simple-words)
* Interactive [Visualizing Git Concepts](https://onlywei.github.io/explain-git-with-d3/) web app

**Going deeper**
* [Missing CS Semester](https://missing.csail.mit.edu/2020/version-control/) from MIT
* This free [video course](https://www.git-tower.com/learn/) from the creators of Git Tower that goes into a lot of the nitty gritty details.
