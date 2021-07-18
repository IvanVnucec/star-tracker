# Get started
1. Install [Ubuntu 20.04.2 LTS](https://releases.ubuntu.com/20.04/).
2. Open terminal and run `sudo apt-get install -y make git python3 python3-pip wget`
3. Clone repo with `git clone git@github.com:IvanVnucec/star-tracker.git` and cd into folder with `cd star-tracker`. It might ask you to login with your Github acc.
4. Download a Star catalog with `make download`. Needs to be done only once on clone.
5. Install Python libraries with `pip install -r requirements.txt`
6. Run algorithm with `make run` or shorter `make`.
