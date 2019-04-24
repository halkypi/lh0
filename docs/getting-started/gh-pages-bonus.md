---
layout: default
title: Extra Credit 
parent: Intro to Python
categories: data wrangling
nav_order: 1
---
# Setting up a website using Jekyll and GitHub pages. 
{: .no_toc }

* TOC
{:toc}
## Jekyll
{: .no_toc }

These are the steps for setting up on a Mac.  Windows and Linux can be found on the main [Jekyll](https://jekyllrb.com/docs/installation/) site, and [below](#windows).  

### Useful resources

*    [video-walkthroughs](https://jekyllrb.com/tutorials/video-walkthroughs/) by Giraffe Academy
*    [jekyll](https://github.com/jekyll/jekyll)
*    [GH pages learning lab](https://lab.github.com/githubtraining/github-pages)

### Setting up GitHub Pages

There are a couple of gotchas here, for example don't add a README file to the initial repo.  Everything here was taken from the [video-walkthroughs](https://jekyllrb.com/tutorials/video-walkthroughs/), this is meant to be a cheat sheet/quick start guide.

#### Install Jekyll

*    Check Ruby and Gem installation - make sure it's local, if not [troubleshoot](https://jekyllrb.com/docs/troubleshooting/), then install gem and bundler
```
which ruby
/usr/local/bin/ruby
which gem
/usr/local/bin/gem
gem install jekyll bundler
```

#### Create local site
When creating for the first time use `bundle exec jekyll serve`, thereafter `jekyll serve` should work fine.

```
jekyll new lh
cd lh
```

*    add base url to `_confiq.yml`

![base-url](/lh/assets/images/base-url.png?raw=true)

*   launch site locally
```
bundle exec jekyll serve
```
*    server address: http://127.0.0.1:4000/lh
*    press ctrl-c to stop

#### Create new GitHub repository

*    **do not** Initialize repository with README
![](/lh/assets/images/new-repository.png?raw=true)

#### Initialize git repository

```
git init
git checkout -b gh-pages
git status
git add .
git commit -m "initial commit"
```
*    grab repository url
![](/lh/assets/images/initial-commit.png?raw=true)

```
git remote add origin https://github.com/halkypi/lh.git
git push -u origin gh-pages
```
#### Reload repository

![](/lh/assets/images/initial-commit-reload.png?raw=true)

![](/lh/assets/images/published-at.png?raw=true)

## Windows
Bundler/Jekyll is not well supported on Windows unfortunately but running: [Ubuntu linux inside Windows 10](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0) works flawlessly.

The steps are listed here:  [https://jekyllrb.com/docs/installation/ubuntu/](https://jekyllrb.com/docs/installation/ubuntu/).  

```
sudo apt-get install ruby-full build-essential zlib1g-dev
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
gem install jekyll bundler
jekyll new lh
cd lh
bundle exec jekyll serve
```
### Tips

To pass files between Linux and Windows it is necessary to create symbolic links (or shortcuts).  It is important to do this from the bash terminal as opposed to the Windows machine for encoding reasons.  Use the `ln -s` command, for example:

```
ln -s /path/to/file /path/to/symlink
ln -s  ln -s /mnt/c/Users/your-name/Downloads/ ~/Downloads
```

Once this is done, anything downloaded to the Windows `Downloads` directory will automatically appear in the linked folder in linux and vice versa.  The same can be done for `Documents` and `Desktop`:

![](/lh/assets/images/sym-links.png?raw=true)

## Next Steps
*    Browse other [GH Pages](https://github.com/collections/github-pages-examples)
*    Explore [Open Source](https://github.com/explore) repositories
*    Peruse the civic hackers site at [https://github.com/github/government.github.com](https://github.com/github/government.github.com)

> Gather, curate, and feature stories of public servants and civic hackers using GitHub as part of their open government innovations [http://government.github.com/](http://government.github.com/).

*    Complete [Introduction to GitHub](https://lab.github.com/githubtraining/introduction-to-github) in learning lab

