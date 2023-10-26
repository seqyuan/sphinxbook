# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


html:
	sphinx-build -a ./docs ./build

install:
	pip install -r requirements.txt
	#pip install recommonmark
	#pip install pyOpenSSL==18.0.0
	cat /proc/version
	yum install wget
	wget https://github.com/jgm/pandoc/releases/download/2.14.0.3/pandoc-2.14.0.3-linux-amd64.tar.gz
	tar -xvf pandoc-2.14.0.3-linux-amd64.tar.gz
	yum install texlive-xetex
	pwd
	ln -s /vercel/path0/pandoc-2.14.0.3/bin/pandoc /usr/bin/pandoc
	export PATH="/usr/bin:$PATH"
	chmod +x ./pandoc-2.14.0.3/bin/pandoc
	/usr/bin/pandoc -v

