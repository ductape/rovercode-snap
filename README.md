# rovercode-snap #

This is the snapped version of the rovercode engine that runs on the rover end of the system.

It is written to be compatible with Python 3.6+ and targeted to run on a Raspberry Pi 3 B with Ubuntu Core 18. Hopefully the code is more portable than the disclaimer implies, but it has yet to be tested as such.

## Build Instructions ##

Here are the instructions for building the rovercode-snap package. These instructions are for [Ubuntu 18.04 LTS](http://releases.ubuntu.com/18.04/) (Bionic Beaver). Because snapcraft is a Canonical product, it really only works on Ubuntu. And because snapcraft is still an immature build environment, the most recent LTS environment provided by Canonical is recommended to have the latest fixes included.

### Required tools ###

#### Install docker-ce on Ubuntu ####

Instructions for installing Docker on Ubuntu were taken from this page: [https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository).

```bash
sudo apt-get update
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Verify the key ends with '9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88'
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce
```

#### Install development dependencies ####

While we would prefer Python 3.6+, snapcraft still defaults to Python 3.5. Install Python 3.5, pip, and pipenv.

```bash
sudo apt-get install -y python3.5 python3-pip
sudo python3 -m pip install pipenv
```

### Build Steps ###

The entire build is performed in a docker container provided by snapcraft. Run the following command from _the project root directory_.

```bash
docker run --rm -v "$PWD":/build -w /build snapcore/snapcraft bash -c "apt-get update > /dev/null && snapcraft"
```

