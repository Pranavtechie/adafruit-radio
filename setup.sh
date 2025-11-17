sudo apt install tmux vim git --yes

curl -fsSL https://bun.sh/install | bash

curl -LsSf https://astral.sh/uv/install.sh | sh


source ~/.bashrc

git config --global user.name "pranav"
git config --global user.email "pranav.techiegeek@gmail.com"

git clone https://github.com/ASU-ASCEND/fall-2025-ascend-gsw gsw && cd gsw && uv sync
git clone https://github.com/asu-ascend/fall-2025-ascend-gsw-dashboard dashboard && cd dashboard && bun install

