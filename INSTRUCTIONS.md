# An Intro to Git

We're going to create a plot of the Covid-19 cases around the world using publicly available data compiled by [Johns Hopkins](https://github.com/CSSEGISandData). We'll write a script we can use to update the data, create a visualizations and then try contributing to someone else's code with a merge request.

[![example-plot](images/example-plot.png)](https://www.ft.com/content/ff3affea-63c7-11ea-b3f3-fe4680ea68b5)




## But first, what is Git?

Git is a distributed version control system. It's software to help track and manage source code, which means it works with any kind of text files. It was developed by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) (the creator of Linux) to manage the Linux kernel. The software is open source and freely distributed.

* Keep a canonical working version
* Easily restore or reset changes that break your code
* Separate valid code from new analysis or "features" 
* Collaborate with others on the same files

But Git is not a panacea and there are many ways to tie yourself up in knots. However, it can reinforce good habits and help save you from yourself. Plus, if you want to work in software, basic familiarity is a job requirement.



### Git vs. GitHub

**Git** is the tool you run on your computer to manage local repositories. **GitHub** is a service that hosts remote git repositories (like this one) so you can share your code and collaborate with others. Git can be used locally but GitHub lets users keep a secure, canonical copy in the cloud and give others access as needed. 

GitHub repositories can be **public** (like [Git itself](https://github.com/git/git), [Python](https://github.com/python/cpython), various [BC Government Projects](https://github.com/bcgov)) or **private** (users include the [US Dept of Defense](https://github.com/deptofdefense), [Microsoft](https://github.com/Microsoft), and [UBC](https://github.com/ubc-library)). While there are other services (I like GitLab), GitHub is the defactor standard in the industry so we're going to use it for this tutorial.

![example-git-repo](images/example-git-repo.png)  



## Create a Repository

A repository starts as just a folder on your computer. Then we'll use git to initialize a repository and add files. 


> We're going to use the terminal to do this, so prepare yourself. I'll use `$` to denote the bash prompt (although yours may be `>`  or `%` or something else entirely) and `# <a comment>` to add additional context. The output  of commands will not have any symbol.



```bash
$ # print the current directory (i.e. folder) 
$ pwd  
/Users/willjenden/Projects
$ # create a new directory
$ mkdir covid-19
$ # change directories into the new directory. 
$ cd covid-19
$ pwd
/Users/willjenden/Projects/covid-19
$ # list the contents of the directory
$ ls
```



We know have a new directory with nothing in it. It's not even a git repository yet. In order to make it a git repository we need to run `git init` from the directory. You can do this at any time in any folder (that's not a child of another git repository) not just an empty one.

```bash
$ git init
Initialized empty Git repository in /Users/willjenden/Projects/covid-19/.git/
$ ls
```



And we have a repository. It's empty, but now it's an empty git repository. If you execute `ls -a` (list all) then should see a `.git` folder. This is where git keeps track of your repository. As a general rule of thumb, you don't need to go in here so just let git do it's thing.



> Note: Along with `.git`, you should have seen two other entires: `.` and `..`.  `.` is a reference to the current directory and `..` is a reference to the parent directory. You can try navigating around with different combinations of `.` and `..` like `cd ..` will bring you to `covid-19` and `cd covid-19/../` will take you on trip into the covid directory and then back out.



## Add a file

Let's create a README in our repository. A README is a text document (usually in Markdown) that provides new users (and sometimes, yourself in six months) an introduction to the project. It should explain the purpose of the project, how to set up the development environment and how to run links to other useful information, either in the repository or externally.

I'm not going to make you write files from command line, so let's open an editor in this folder. I'm using Visual Studio Code so I can run `code .` to open the current directory (`.`) in VSCode.

```bash
$ code .
```



 You should see something like this:

![vs-code-empty](images/vs-code-empty.png)

You'll see a folder on the left side, and not much else. Go back to your terminal and type `touch README.md`. You should now see a file called *README.md* in the left panel. Open it up and let's start our file.

```markdown
# COVID-19 Confirmed Cases Visualization

This project recreates the COVID-19 growth trajectory plots using publicly available data
compiled by [Johns Hopkins](https://github.com/CSSEGISandData).
```



>  By the way, this syntax (and the *\*.md* file extension) is markdown. It's lightweight and meant to be readable as plain text or quickly formatted and styled for display on the Web. I highly recommend getting comfortable with [GitHub flavored markdown](https://guides.github.com/features/mastering-markdown/) for writing documents in version control.



Now we're finally going to start using Git. From the terminal let's look at our changes, add the file to the staging area and then commit it to the repository. 

```bash
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```



We use the git status to tell us what's going in the repo and often gives us useful hints about what we should do next. The important take away here is that we have "untracked" files. Untracked files are files that existing in the git repository (the top level directory or any child directory) but are not being managed by Git. We can tell git to start tracking a file with the `git add <file>` command.

```bash
$ git add README.md
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```



The *README.md* file is now in the staging area for our repository with a note that says it's a new file. For git to create an indelible copy of the file with it's current contents, we need to create a "commit". A commit is the immutable, atomic unit of git because the state of the repository is built up from a graph of related commits. 

```bash
$ git commit -m "Add README"
[master (root-commit) 116767f] Add README
 1 file changed, 3 insertions(+)
 create mode 100644 README.md
```



Now our repository has a single commit which contains the small README we just wrote, our name as author and a helpful message to remind us why we made the commit. 



Commits are identified by a hash which is cryptographically determined by the contents of the commit. If any of the contents change, even by a single bit, we would get a different hash. This 40-digit alpha-numeric number is often abbreviated to the first 8 digits. We can check the history of commits and see the full log with the `git log` comand.

```bash
$ git log
commit 116767f52e0caddd8505b2f8becf247988ad076e (HEAD -> master)
Author: jenden <some-email-address@gmail.com>
Date:   Wed Apr 29 22:06:27 2020 -0700

    Add README
```



## Add some more files

Let's make this repository do something useful. I've created a script to pull the daily COVID-19 data curated by Johns Hopkins. Create a new directory called `scripts` in your repository and then add the [`update_data.py`](scripts/update_data.py) script to the directory. 

In order to run this script we'll need to tell our future selves (and other users) how to set up a python environment and how to use the script to update data. A README is the obvious place to document this. 



> A quick aside. Documentation is hard to get right. If we carefully document every bit of our script (or comment it for that matter), it's very easy for it to get out of sync with what the code actually does. Our goal is to strike a balance to let people know what to do but not to create technical debt for ourselves in the future with stacks of documentation we need to update every time we modify the code. And, like many things, there are diminishing returns to our efforts. A little, well-maintained documentation goes a long way.



Add the following sections to the README file.

```markdown
### Environment

Create your python virtual environment of choice. When that environment is active, 
run the following command:

​```bash
pip install -r requirements.txt
​```

### Data

The Center for Systems Science and Engineering at Johns Hopkins maintains daily summary 
of Coronavirus data around the world in a [GitHub repository](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports). 
Run the `update_data.py`script to update the data. The command below will download the
data from Jan 22 to April 25 and save it in the `data/` folder of this directory.

​```bash
python scripts/update_data.py --start 2020-01-22 --end 2020-04-25 data/
​```
```



Now create the requirements.txt file with the following contents.

```
# requirements.txt
requests==2.23
pandas==1.0

```



That's all done. Let's check the status of our git repository:

```bash
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        requirements.txt
        scripts/

no changes added to commit (use "git add" and/or "git commit -a")
```



This is more complicated than before. We have untracked files *requirements.txt* and *scripts/* and modified file *README.md*. Now is a good time to talk about the life cycle of git files. All files we create start out as "untracked" in our working tree. When we use `git add` we checkpoint the current contents of the file in the "staging area". Then when we are happy with the changes we've staged, we can create a permanent record of those changes by creating a commit.

<img alt="git-workflow-local" src="images/git-workflow-local.png" width=400px>

In this commit, we have changes to the README file that git is tracking (because it was previously committed) and new files we have just created. Let's add them all to the staging area and commit them. We can tell git to add the files by listing them one by one like `git add requirements.txt scripts/update_data.py` or we can tell git to add all files in the current directory using the `.` shorthand.  Now run git commit like before.

```bash
$ git add .
$ git commit -m "Add data update script and environment requirements"
[master 4bc6f91] Add data update script and environment requirements
 3 files changed, 111 insertions(+)
 create mode 100644 requirements.txt
 create mode 100644 scripts/update_data.py
```



You can use `git log` to assure yourself the commit worked. You can also check `git status` and see that you have "nothing to commit" because the working tree is "clean".



## Get some data

Now let's create a virtual environment, install our requirements and run our `update_data.py` script so we can start to visualize the data!

```bash
$ # create a python virtualenv, activate it and install requirements
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```



> Alternatively, you could create a conda environment. I generally prefere these environments, but they don't create a folder we need to ignore so it's not as useful for this demonstration. Install a conda environment using python 3.8 and the dependencies in requirements.txt like this.
>
> ```bash
> $ conda create --name covid-19 python=3.8 --file requirements.txt
> $ conda activate covid-19
> ```
>
> Once you activate the environment, your shell should contain the active environment in the prompt (although it probably won't look quite like this)
>
> ```bash
> (covid-19) $
> ```



Once your python environment is active and you have the dependencies installed, create a diretory for the data and run the script to populate it.

```bash
$ # make directory for the data
$ mkdir data
$ python scripts/update_data.py data/
INFO:scripts/update_data.py:Downloading data for 2020-01-22 - 2020-04-28 to /Users/willjenden/Projects/covid-19/data/original
INFO:scripts/update_data.py:01-22-2020 -- downloading file: https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-22-2020.csv
...
INFO:scripts/update_data.py:04-25-2020 -- downloading file: https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-25-2020.csv
INFO:scripts/update_data.py:04-25-2020 -- saved to /Users/willjenden/Projects/covid-19/data/original/04-25-2020.csv
```



Hopefully that all went smoothly. If the script failed, check that you created and specified the right data directory beforehand and that the URL for the CSV files hasn't changed. 

We just created a bunch of new files in our repository. Check the status and you can see two new directories, *env* and *data*.

```bash
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        data/
        env/

nothing added to commit but untracked files present (use "git add" to track)
```



Unlike previous files, the *env* directory is specific to our local machine and shouldn't be contributed to the repository. The contents of *data* doesn't need to be version controlled because it can be downloaded from the source at any point in time. In general, it's good practice to keep data out of version control and separate from the code to process it. Luckily it's easy to tell git to ignore files with a [`.gitignore`](https://help.github.com/en/github/using-git/ignoring-files) file. Create a file in the root directory and put in the following contents:

```
# .gitignore
.vscode
env/
data/

```



Now try checking the status of the repository again. You can use`ls` to confirm that the directories still exist but that git is ignoring them. Now commit the contents of the *.gitignore* file and let's continue.

```bash
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)
$ ls
README.md
data
env
requirements.txt
scripts
$ git add .gitignore
$ git commit -m "Create gitignore"
```



## Under the hood

You may have noticed that every time we get the status or make commits, git tells us something about being on "branch master". This raises two questions: what's a branch, and what's master?

Under the hood, a git repository is a graph of commits. So far our repository is just a linear network of commits where each new commit references the previous commit. We refer to this history of commits as a branch.

Master is the name given, by convention, to the main or default branch. It represents a label or "tag" which points to one commit. Every time we make a new commit to the master branch what we're really doing is creating a commit with a parent of the current master branch and then reassigning the master label to this new commit. 

This animation shows how each new commit points to the previous commit and the master label moves to the new commit. 

<img alt="git-gif-commits" src="images/git-gif-commits.gif" width=600px>



This animation also introduces the concept of the HEAD. The HEAD refers to the last commit in the current branch. When we checkout a new branch, our HEAD will move to the last commit on that branch.

These animations were created with the excellent [Explaint Git](https://onlywei.github.io/explain-git-with-d3/#commit). If you want to dive deeper and understand how Git works under the hood, I strongly recommend exploring this site.

Okay, back to creating our plot.



## Create the plot!

Now we have our data, we're ready to visualize the data and save a plot. We'll use [plotly express](https://plotly.com/python/plotly-express/) so we'll need to add `plotly==4.6` to the *requirements.txt* file. If you check the status of the repository you'll see a modified file. We can check what's been modified by running `git diff`.

```bash
$ git diff
diff --git a/requirements.txt b/requirements.txt
index 99510e7..aaab375 100644
--- a/requirements.txt
+++ b/requirements.txt
@@ -1,2 +1,3 @@
 requests==2.23
 pandas==1.0
+plotly==4.6
```



There's a lot of output here, but the critical pieces are the lines with that are prefixed with a + or – symbol. Commit the change with an appropriate message and then install the new dependency in your local environment.

Let's add the [`make_plot.py`](scripts/make_plot.py) to out scripts directory. This script is hard-coded to perform the following steps:

* reads each CSV in the *data* directory, 

* normalizes the data by correcting for small changes over time (e.g. a column renamed from "Country/Region" to "Country_Region", some country references changing like "Mainland China" becoming just "China") and creates a single pandas dataframe

* counts days since the 100th case and then 

* plots the confirmed number of cases by country on a log scale against days since the 100th case

* saves the plot to the *figures* directory

  

Now add a bit of a description to the README to explain how to create the visualization.

```markdown
### Visualization

Once the data is downloaded, run the `make_plot.py` script to create an interactive 
plot of the confirmed cases by country. 

​```bash
mkdir figures
python scripts/make_plot.py
​```

```



Try running the script per the README instructions. You should see something like this open in your browser.

![covid-19-case-plot](images/covid-19-case-plot.png)

Okay, let's check what this has done to our repository.

```bash
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        figures/
        scripts/make_plot.py

no changes added to commit (use "git add" and/or "git commit -a")
```



That looks about right. Let's clean up our working tree by staging the changes to the README, adding the script and adding `figures/` to the *.gitignore*.

```bash
# append "figures/" to the end of the .gitignore file
$ echo "figures/" >> .gitignore
$ git add README.md scripts/make_plot.py .gitignore
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   .gitignore
        modified:   README.md
        new file:   scripts/make_plot.py

```



Now that these changes are staged and ready to be committed. Our working tree is clean (we can verify by running `git diff` which will not indicate any changes). If we want to see the changes that are staged, we need to tell git to look at the staged files with `git diff --staged`. This will create a lot of of output. If you want to look at a single file, you can pass the filename as the last argument.

```bash
$ git diff --staged .gitignore
diff --git a/.gitignore b/.gitignore
index 48656a6..923db9e 100644
--- a/.gitignore
+++ b/.gitignore
@@ -1,3 +1,4 @@
 .vscode/
 env/
 data/
+figures/
```

> Note: When there are more changes than can fit on the screen, you can scroll up and down using the ⬆️ and ⬇️ arrow keys or `j` and `k` (so you don't need to move your hands from the home row). Exit by pressing `q`.



Commit your changes with an appropriate commit message and then let's push a copy of our entire repository up to GitHub.



## Remote repository on GitHub

So far we've been grouping our file changes into commits, and adding commits into our local repository. Now we're ready to start synchronizing our commits with a remote repository. 

<img alt="git-workflow-remote" src="images/git-workflow-remote.png" width=500px>

Login to your account on [GitHub](https://github.com/login). Look for the green "new" button and create a repository. Give it a reasonable name a short description. You can choose to make it private (only you can see it) or public. 

![create-repository](images/github-create-repository.png)

Once created, you'll see the main page which lists a number of options for how to get started with your repository. We're looking to "push an existing repository" because we have an existing local repository and we want to "push" the commits to the new GitHub remote repository we've just created. Before you copy and run the commands, let's take a look at what they do.

The `git remote` command manages references to other repositories. We're going to create a reference to our git remote repository and give it the shorthand name `origin` by convention. This makes more sense when you think that you often get a copy of someone else's repository in which case "origin" refers to the place where your copy originated.

> Note: There are two ways to authenticate with Git. The recommended method is by using an SSH key and a url that looks like `git@github.com:<username>/<repository>.git` but this requires a bit of initial set up. You can also use the url that looks like `https://github.com/<username>/<respository>.git`  and authenticate with your GitHub username and password when prompted. Git will know what to do depending on which url you give it.



The `git push` command pushes the set of commits in your local repository to a remote repository. The `-u` flag is necessary for the first commit to a new branch and tells git that our local branch should be linked with the `master` branch on the remote repository.

Now let's give it a shot.

```bash
$ git remote add origin https://github.com/jenden/covid-19.git
$ git push -u origin master
Enumerating objects: 27, done.
Counting objects: 100% (27/27), done.
Delta compression using up to 4 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (27/27), 4.46 KiB | 1.11 MiB/s, done.
Total 27 (delta 6), reused 0 (delta 0)
remote: Resolving deltas: 100% (6/6), done.
To https://github.com/jenden/covid-19.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

Congratulations! You've just pushed your first commits up to a GitHub repo. Let's go check it out what it looks like on the GitHub website.

![github-repository](images/github-repository.png)

You can see that all the commits we made on our local machine now show up here. Also, none of the files we excluded from the repository like *data* or *env* have been pushed to the remote repository.



## Cloning a repository





## Branching

In the animation below, we create a new branch called *my-branch*. This creates a new label attached to the commit. However, we don't checkout the branch so when we make another commit we are commiting against master. This results in the master label and the HEAD moving to a new commit while the *my-branch* tag stays put. When we checkout *my-branch* our HEAD moves to the commit at that point. Each subsequent commit while *my-branch* is checked out results in the *my-branch* label and the HEAD reference moving while the *master* label stays put.

<img alt="git-gif-branches" src="images/git-gif-branches.gif" width=600px>



## Add a feature





## Merge requests





## We're done!

That was a lot. You should know enough now to get by with using git for your work. It will take a while to become proficient but it's a very valuable, even a foundational, skill. Not to mention a GitHub repo with a few demo projects is always a plus when applying for a job.



Check the README in this repository for additional resources and good luck!
