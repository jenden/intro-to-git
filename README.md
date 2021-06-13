# Intro to Git

>  If you write code, you should be using a version control system. 
  
<br/><br/>



At it's most basic, version control tracks changes in files over time and allows you to easily view differences and restore the last working version if you break something (which you will). Most version control systems work at the file level so they don’t care if you’re writing R, Python, GAMS, C++, CSS or just plain text like this tutorial. 

Plus, if you're writing software, there are a world of tools you can connect to your version control system to perform continuous integration and continuous delivery or deployment (CI/CD) that will help you ship faster and create better quality products.


### What you'll learn

At the end of this lab you should be Git literate. You'll know why it's useful, the basics of how it works, how to follow a simple analysis workflow and enough about its more advanced capabilities that you can decide if you want to learn more.



### What you'll need

1. Git installed on your computer. Depending on your system, it may already be installed. I have some basic instructions for Mac and Windows below. If they don't work for you, turn to your friends, Google and Stack Overflow! 

   - On a Mac, open the Terminal application type `git --version` and then hit enter. If you see a response like the one below you're all set. If git is not installed, you should be prompted to install the Xcode Command Line tools from Apple. If all else fails, follow the instructions on [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install for macOS.

     <img src="images/macos-git-version.png" alt="macos-git-version" width="500"/>

   - Windows doesn't come pre-installed with Git so you'll need to download it from [git-scm.com](https://git-scm.com/downloads) for Windows. During the installation you should select the defaults for all prompts except the text editor. Here I highly recommend selecting `nano` because the default `vim` , while powerful, is not at all user friendly. 

     <img src="images/windows-git-text-editor.png" alt="windows-git-text-editor" width="500"/>

     Find *Git Bash* in your start menu and open a new prompt. Type `git --version` to confirm that git is available and installed. You should see something like this:

     <img src="images/windows-git-bash.png" alt="windows-git-bash" width="500"/>

     If you're familiar with [Chocalatey](https://community.chocolatey.org), the package manager for Windows, you can also install it with the single command `choco install git`. See the [community-maintained git package](https://community.chocolatey.org/packages/git) for more details.

   - If you use Linux, my guess is you already know what you're doing. If not, use Google to learn how to install git for your specific distribution. 

2. An account on the git server of your choice. I'm going to be using [GitHub](https://github.com) in the demo because it's very popular and I recommend you do as well unless you already have an account somewhere else. 
  
   - [Sign-up for GitHub](https://github.com/join) or [login](https://github.com/login) in to an existing account. You'll need these credentials during the lab in order to commit code to your repository.
   
3. A proper text editor or IDE. I plan to use [Visual Studio Code](https://code.visualstudio.com) because it's nice middle ground between a barebones text editor and a full fledged Integrated Development Environment (IDE). You can use whatever editor you're comfortable with as long as it can manage plain text and code (i.e. not Microsoft Word).

4. Basic familiarity with using a terminal. If you're on Windows I recommend getting familiar with *Git Bash* which is packaged with Git. On Mac or Linux just open a Terminal application. If you're unfamiliar with bash or need a refresher, please check out these links *before* we start the lab. I recommend [this lecture](https://missing.csail.mit.edu/2020/course-shell/) or this [blog post](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a). At a minimum you should be comfortable
   - Navigating the file system with `pwd` and `cd` 
   - Listing files in a directory with `ls`
   - Looking at the contents of a file with `cat` or `less`
   
   If you're already a wiz and want to try something fun, check out [fish](https://fishshell.com) for some great modern additions to a traditional shell.
   
5. If you want to participate in the activity, you will also need a python environment set up that includes `pandas`, `requests` and `plotly`. You can achieve this by creating a new environment and running `pip install -r requirements.txt` with the `requirements.txt` file from this repository.




<br/><br/>
## Activity

We're going to recreate the plot of Covid-19 cases by region since the 100th case using the data compiled by Johns Hopkins. We'll start with an empty folder, initialize a repository and we'll build up the contents together to create a simple version of this plot. While we're going through this process we'll talk about how git works under the hood and what each action is doing.

Then you will branch your repository and make an improvement like adding growth rate lines, filters for country, hover tools, etc. Once the changes are working locally, push the changes to the remote repository and open a merge request. If you want a more realistic example, try cloning a classmates repository and submit a pull request with improvements to their code. We'll go through how to review the changes and merge them into your repository.

I'll try to save a bit of time to through some useful next steps and answer questions at the end. You can follow along with the [instructions](INSTRUCTIONS.md) or catch up if you missed something.



<br/><br/>
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
