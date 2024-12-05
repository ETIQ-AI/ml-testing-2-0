# Etiq 2.0 - Beta Testing

This repo should contain everything you need to install and test the new Etiq 2.0 software.

### Requirements

-   VS Code

-   Python 3.9-3.11

-   A brand new virtual environment

### Downloading of Etiq 2.0 Software

You will have been sent a link to a Google Drive directory. Please access the directory and download the relevant zip package for your computer based on operating system and Python version.

-   Linux - Python 3.9, 3.10 and 3.11

-   MacOS (Apple Silicon Processors) - Python 3.9, 3.10, 3.11

-   MacOS (Intel Processors) - Python 3.9, 3.10, 3.11

-   Windows - Python 3.9, 3.10, 3.11

### Installation of Etiq 2.0 Software

**Note:** if you are on MacOS with Apple Silicon there are some additional dependencies to install first:

-   If you haven't already, install homebrew on your computer: <https://brew.sh/>

-   Then run the following in your terminal: `brew install libomp`

Unzip the package you download from Google drive and there should be three files in there:

-   `etiq1-wheels/etiq-1.6.3-***.whl`

-   `etiq2_wheels/etiq_v2-0.2.0-***.whl`

-   `etiq-vscode-extension-0.2.0.vsix`

Within your new virtual environment you need to install the python wheels in this order:

-   `pip install etiq1-wheels/etiq-1.6.3-***.whl (replace with the correct name of the file)`

-   `pip install etiq2_wheels/etiq_v2-0.2.0-***.whl (replace with the correct name of the file)`

We then need to register ourselves with the Etiq Dashboard to get the appropriate license:

Navigate to: [dashboard.etiq.ai](https://dashboard.etiq.ai/) and sign up for a free trial account

We now need to create a token to associate your session with your account. To create this token:

-   Click on your initials on the top right of the dashboard screen

-   Click Manage access tokens

-   On the next screen create a new token by giving it a name in the Token Name dialogue

-   Click Add

-   The copy the token

We now need to return to the Python virtual environment where we have installed the two Etiq python packages and run the following script:

```         
import etiq

from etiq import login as etiq_login
etiq_login("https://dashboard.etiq.ai/", "<token>")
```

Replacing the `<token>` with the token you copied from the dashboard.

Finally we need to install the VSCode extension

-   On VSCode select Extensions from the left hand navigation bar

-   Then click the ... at the top of the Extensions dialogue

-   Select `Install from VSIX...`

-   Select the `etiq-vscode-extension-0.2.0.vsix` from the File Browser

-   This will install the extension

And you will be good to go!
