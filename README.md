# cloud
A repo for more efficient work an a cloud computation infrastructure, circumventing the need for tedious manual transfers (e.g., through globus connect, or using scp, etc.) by using the more efficient git.

## How to `git clone` this repository (repo)
Because this repo is private, https cloning is not supported via CLI (e.g., linux bash interfaces on remote computing clusters) (this includes providing github username and password). Cloning via ssh keys is required (as other methods, e.g., github's so-called personal access tokens, were tried previously and did not succeed). For github's guide on [Cloning with SSH URLs](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-ssh-urls), click that link.

Here is a link to one's [github account associated ssh keys](https://github.com/settings/keys), where one can see whether there are ssh keys already in one's github account, amongst others.

Although this is redundant regarding above guides, I recommend to [generate a new ssh keypair & adding them to your github account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) for every new remote.

Another redundant but useful information is how to actually clone (this repo) via ssh from the CLI (e.g., via Git Bash), assuming correct set up of ssh key pairs (above guides): `git clone git@github.com:radRoy/cloud.git`.
