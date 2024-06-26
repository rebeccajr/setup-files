---
# New Environment Setup
---

# Description

This file includes steps for setting up my linux environment on a new machine. It's like my personal on-boarding guide.

# Ubuntu

## Create root password
```bash
passwd
```


## Install from apt
Use `sudo` before all `apt` commands if you do not have a root password.

```
su
apt install vim
apt install emacs
apt install git
apt install zsh
apt install curl
apt install tmux

```

## Install from snap
``
sudo snap install discord
``

## From App Center
- Steam
- Slack
- code

## Download `.deb` files
Chrome

From directory with `.deb` file

```
sudo dpkg -i <.deb file>
```

## Arduino CLI

### Install Arduino CLI
Source:  [Arduino CLI ](https://arduino.github.io/arduino-cli/0.35/installation/)

1. Create `~/local/` if it doesn't already exist:
   ```bash
   mkdir ~/local
   ```

1. Navigate to `~/local` and run command to install `arduino-cli`
   ```bash
   curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
   ```

1. Pre-pended `$PATH` environment variable with this line in `~/.bash_profile`
   ```bash
   export PATH=~/local/bin:$PATH
   ```
1. Source `.bash_profile`
   ```bash
   source ~/.bash_profile
   ```

1. Verify `arduino-cli` was installed
   ```bash
   > which arduino-cli
   /home/flux/local/bin/arduino-cli
   ```
1. Update `arduino-cli`
   ```bash
   arduino-cli upgrade
   ```
### Install Cores
```
arduino-cli core install arduino:samd
arduino-cli core install arduino:esp32
```
--
# Git

After installing Git (`sudo apt install git`), edit the configuration
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

## SSH Key

### GitHub

[Source](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Generate an ssh key and add the public key to GitHub settings.
```
>> ssh-keygen -t ed25519 -C "email@address.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/<user_name>/.ssh/id_ed25519): (hit enter)
Enter passphrase (empty for no passphrase): (hit enter)
Enter same passphrase again: (hit enter)
Your identification has been saved in /home/<user_name>/.ssh/id_ed25519
Your public key has been saved in /home/<user_name>/.ssh/id_ed25519.pub
The key fingerprint is:
################################################## email@address.com
The key's randomart image is:
+--[ED25519 256]--+
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
+----[SHA256]-----+

```

Start the ssh-agent in the background.
```bash
> eval "$(ssh-agent -s)"
Agent pid 59566
```
```bash
> ssh-add ~/.ssh/id_ed25519
Identity added: /home/flux/.ssh/id_ed25519 (email@address.com)
```
From GitHub, go to settings

![image](https://github.com/rebeccajr/setup-files/assets/26588191/b3687c61-8f91-4205-bc94-00f0debf50a7)

![image](https://github.com/rebeccajr/setup-files/assets/26588191/cff278ee-08f4-4d9a-a314-7c2d9f7c9176)

Click `New SSH key` button

![image](https://github.com/rebeccajr/setup-files/assets/26588191/a3783b60-4c7f-42e6-9bbe-7428a89eac61)


### Azure DevOps
[Source](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed)

```
> ssh-keygen -m PEM -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/<user_name>/.ssh/id_rsa): (hit enter)
Enter passphrase (empty for no passphrase): (hit enter)
Enter same passphrase again: (hit enter)
Your identification has been saved in /home/<user_name>/.ssh/id_rsa
Your public key has been saved in /home/<user_name>/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:########################################### user@computer
The key's randomart image is:
+---[RSA 4096]----+
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
|   ###########   |
+----[SHA256]-----+

```

Verify
```
> eval "$(ssh-agent -s)"
Agent pid 12956
```

From Azure DevOps web interface

![image](https://github.com/rebeccajr/setup-files/assets/26588191/22794730-1a2b-4cff-a34f-0d5d541819db)

![image](https://github.com/rebeccajr/setup-files/assets/26588191/dc7e2c15-d796-49a2-936f-831475221637)

![image](https://github.com/rebeccajr/setup-files/assets/26588191/63636e8a-72a9-41f1-96c6-cbda6de0ba4a)

## Git

1. Create a folder called `git` in `/home/user`
```bash
mkdir ~/git
```
1. Clone the setup-files repo.
```
git clone git@github.com:rebeccajr/setup-files.git
```
1. Run `cp-dot-files.sh`
```
source cp-dot-files.sh
```

## Visual Studio Code

Extensions


---
# Windows

## Turn off alert sounds

Windows likes to make an alert sound every time tab complete doesn't work or other silly things. Turn it off in settings.

Go to Audio - change other sound settings
or

Sound -> sound control panel -> Sounds tab -> Sound Scheme dropdown -> No Sounds

In the window labeled `Sound` -> tab labeled `Sounds` select the menu option `No Sounds`

![image](https://github.com/rebeccajr/setup-files/assets/26588191/e0ed896a-65d4-4c45-9188-5a8fbb7f12dd)


---
## Cygwin

Download cygwin, install packages

- lynx
- wget
- tar
- git
- vim



---
## Software Downloads

- Spotify
- Slack
- Steam


