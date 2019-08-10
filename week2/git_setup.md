# Git for code class

**Setup**

OSX has git pre-installed; Windows users will need to install git (from your bash terminal):


```
apt-get install git
```


Next, install git-completion and git-prompt (both windows and mac users should do this):


```
    $ curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh >~/.git-prompt.sh
    $ curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash > ~/.git-completion.sh
    $ cat >> ~/.bash_profile << EOF
    [[ -r "$HOME/.git-completion.sh" ]] && .  "$HOME/.git-completion.sh"
    [[ -r "$HOME/.git-prompt.sh" ]] && .  "$HOME/.git-prompt.sh"
    PROMPT_COMMAND='__git_ps1 "\u@\h:\w" "\\\$ "'
    EOF
    $ source ~/.bash_profile
```


These two scripts make it easier to work with branches in git by adding the current branch to your prompt and allowing you to use tab completion to type branch names.

**Learn you some git**

Download and run the git-it app([https://github.com/jlord/git-it-electron/releases](https://github.com/jlord/git-it-electron/releases)) it will walk you through some git basics (Ignore the instructions for installing git, you’ve already done that).

**Create a repository for code class**

First create a “codeclass” repository on github ([https://github.com/new](https://github.com/new) Just accept all the defaults). Then, upload your work so far:




```
    # Switch into the directory you've been using for your code class files
    # and initialize a new repository:
    $ cd workspace/codeclass
    $ git init

    # Add all the files you've created so far to a new commit:
    $ git add .
    $ git commit -m"Initial files"

    # provide the path for the repository you created on github
    $git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

    # push changes to github
    $ git push --set-upstream origin master
```


 Visit https://github.com/YOUR-USERNAME/codeclass to see your code published online! Try creating a short README file in your repository and pushing it to github. (Create the file with your editor, save it in your code class directory, `git add README`, `git commit -m"Adding a readme file"`)
