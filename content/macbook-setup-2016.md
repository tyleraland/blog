title: Setting up a new Macbook in 2016
date: 2016-01-16
tags:
category: tech

On the first day of the new year, I suffered the loss of my 3.5 year-old Macbook Air and quickly set out to find a replacement.  I ultimately settled on a 13" Macbook Pro with Retina Display.  From my previous workhorse, I've doubled my memory and SSD storage to 8GB and 250GB, respectively, without noticing the slight weight increase.

Getting up and running on a new machine can be an arduous task, so I've taken some notes on what I ultimately needed.
Note that some of these installs (e.g. Slate) may come from third-party developers or require some sort of privileged access that requires fiddling with some settings to enable.  Two places to remember are System Preferences -> General (Toggle to "Allow apps from Anywhere" temporarily), System Preferences -> Privacy -> Accessibility (Toggle which apps can "control your computer").

# OS and GUI applications

* Open the App Store
* First thing, upgrade OS if applicable (in my case, Yosemite to El Capitan)
* Install XCode from the App Store
* Install Evernote from the App Store, while we're at it.
* Install Alfred from the App store, too.
* Install Caffeine.
* [Chrome](https://www.google.com/chrome/browser/desktop/index.html) - because Safari just won't do.
* [Firefox](https://www.mozilla.org/en-US/firefox/new/) - when Chrome isn't supported.
* [XQuartz](http://www.xquartz.org/) - for GUIs
* [Spotify](https://www.spotify.com/us/download/mac/#_=_) - for music
* [f.lux](https://justgetflux.com/news/pages/macquickstart/) - so I can sleep at night
* [iTerm2](https://iterm2.com/) - my preferred terminal
* [Rescuetime "Lite"](https://www.rescuetime.com/signup/solo/lite) - Note: log in first, then download rescuetime to track your device
* [Virtualbox](https://www.virtualbox.org/) - I like to target Ubuntu environments
* [Dropbox](https://www.dropbox.com/downloading?os=mac) - for file sharing
* [Hipchat](https://www.hipchat.com/downloads) - work chat

# Command Line installs
Now we're getting into the command line configuration

## Homebrew installs
* [Homebrew](http://brew.sh/)
* After installing homebrew, you may need to restore permissions: ```sudo chown -R $(whoami) /usr/local```

```
brew install r
brew install git
brew install htop-osx
brew install openssh
brew install readline
brew install sqlite
brew install tmux
brew install tree
brew install wget
brew install vagrant
```

## Misc
* Install my dotfiles
```git clone https://github.com/tyleraland/dotfiles.git && bash dotfiles/install.sh```
* [Slate](https://github.com/jigish/slate) is a fantastic tool for window management in OSX with keyboard shortcuts.  I use CMD+CTRL+X, where X is a key easily within reach.  I use slate for summoning frequently used applications, hiding windows, resizing windows, and moving windows.  Note you'll need to allow Slate to "control your computer", as described above.
* sshfs - for mounting remote filesystems using the SSH protocol

```
wget http://sourceforge.net/projects/osxfuse/files/osxfuse-2.8.2/osxfuse-2.8.2.dmg && open osxfuse-2.8.2.dmg
wget https://github.com/osxfuse/sshfs/releases/download/osxfuse-sshfs-2.5.0/sshfs-2.5.0.pkg && open sshfs-2.5.0.pkg
```

Note: On my remote filesystem, I want to access files that are not owned by me but are controlled by groups that are not defined locally on my Mac.  As a result, I get "Permission Denied".  The solution I've found to this problem is to add those groups to my local mac and add my local user to those groups, like so:
```
$ sudo dseditgroup -o create -i $REMOTEGID $REMOTEGROUP # Create the group
$ sudo dseditgroup -o edit -a $(whoami) -t user $REMOTEGROUP # Append my user name to the group definition
```

## Python Installs

With homebrew + python, don't make the mistake of using sudo.  The result will be initial success, but files will ultimately be owned by root (and not your user).  This may be what you want, but you may also have issues down the road.  You can ``chown -R $(whoami) /usr/local`` to attempt to reset ownership.  Failing that (as in my case), you can ``sudo pip uninstall`` your packages and attempt to re-install without sudo.

```
brew install python --with-berkeley-db4 --with-tcl-tk # python >= 2.7.11
pip install -U pip
pip install -U setuptools
pip install -U virtualenv
# Scientific python stack
pip install numpy
pip install pandas
pip install scipy
pip install matplotlib
pip install ipython
# Misc
pip install beautifulsoup4
pip install ghp-import
pip install jinja2
pip install Markdown
pip install markdown2
pip install pelican
pip install scons
pip install jupyter
pip install csvkit
pip install ansible
```

Systems settings
====
* Map Caps Lock to CTRL: System Preferences -> Keyboard -> Keyboard -> Modifier Keys -> 

Java
====

* Download and install [Java SDK](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
* Download and install [Eclipse SDK](https://www.eclipse.org/downloads/download.php?file=/oomph/epp/mars/R1a/eclipse-inst-mac64.tar.gz)

# Thanks
Lots of thanks to my boss Noah Hoffman for his (very similar) [blog post](http://nhoffman.github.io/borborygmi/mac-setup-el-capitan.html).
