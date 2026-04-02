requirements:
	@sudo pip install -r requirements.txt --break-system-packages
	@python3 -m pip install --upgrade requests --break-system-packages

install:
	@export REPO_DIR=$(pwd)
	@git clone https://github.com/vgomes-p/CodeSim.git ~/.codesim
	@sudo pip install ~/.codesim/program/. --break-system-packages
	@echo "Now you can run CodeSim by executing 'codesim' in your terminal."
	@echo "To uninstall CodeSim, please run: sudo pip uninstall codesim --break-system-packages"
	@echo "Note: We will try to remove the directory ${REPO_DIR} since we reclone codesim repository at  ~/.codesim"
	@echo "We will try to do is assuming you just cloned the repository and didn't rename it, if you renamed it,"
	@echo "please remove the directory ${REPO_DIR} manually."
	@echo "If this make returned an error, it might be because the ${REPO_DIR} was deleted of not found!"
	@rm -rfd ${REPO_DIR}