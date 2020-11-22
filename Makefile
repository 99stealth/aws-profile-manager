UTIL_NAME = aws-profile-manager

install: build
	@echo "Installing $(UTIL_NAME)"
	@pip install dist/$(UTIL_NAME)-* && echo "✅ Package successfully installed" || echo "❌ Something went wrong during the package installation"

remove:
	@echo "Uninstalling $(UTIL_NAME)"
	@pip uninstall $(UTIL_NAME) -y && echo "✅ Package successfully uninstalled" || echo "❌ Something went wrong during the package removal"

update: remove install

build:
	@python3 setup.py sdist bdist_wheel && echo "Building the package" && echo "✅ Package successfully built" || echo "❌ Something went wrong during the build"

check:
	@twine check dist/*

clean:
	@echo "Removing build"
	@rm -Rf dist/ *.egg-info/ build/ &&echo "✅ Build successfully removed" || echo "❌ Something went wrong during the build removal"

rebuild: clean build