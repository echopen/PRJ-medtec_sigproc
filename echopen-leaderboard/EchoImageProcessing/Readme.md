**Welcome to our collaborative development platform !**

We choose to share our passion with you guys and so to develop together on the same [Cloud9 space](https://ide.c9.io/newben/echotest). To get credentials and be invitesd, just send us to [contact@echopen.org], we'll send you an invite. 

# Guide to set-up

### Preparing your workspace
To get a credential, send us an email to the address nowami@echopen.org. We will deploy for you an VM instance, which consists in a repo with data input, classic pre-installed packages,  and some routines code. Your code will happen in the `/home/ubuntu/workspace/` directory, which is on a git source control system. The central repo is here [https://github.com/echopen/kit-soft]. 

** `kit-soft` repo contains a lot of tools, here we only need the `Cloud9Tools` directory, so do not be surprised finding this very and only directory on your local Cloud9. We used a git's sparse checkout trick to do that **

For the community to benefit from your insights, you’ll have to create a custom branch in the format `your_name`.

**Please do not commit on master !**

### Where to get images

The images are available in the input folder `/home/ubuntu/ImageProcessing/Cloud9Tools/scanconversion/data`, in `csv` format. Images are present in scan converted format under the subfolder `scan_converted`  and `raw` images are available under the subfolder `raw`

### To submit

The output should be provided in scan converted format and stored in  `/home/ubuntu/ImageProcessing/output`

If you run the the `run()` method, then your code is compiled.
When you run the `run_and_summit()`, your code is compiled, a script stress-tests it and the performance KPIs update a leaderboard on our website.

All code are opened to your contribution and improvement 😉

# Our KPIs

For people wishing to work on non scan converted data, we bring to you a `scan version` tool based on `OpenCV`. You’ll find it under ` /home/ubuntu/workspace/ref_scanconversion`. It takes as an input a `csv` formated image (in polar coordinates) under the `/data` folder and scan converts it.

As for the moment, we begin to monitor the following KPI’s. We measure :

- noise

- time processing

- CPU usage

- Memory usage

# Declaring issues and feature request
Issues or feature requests should be put here `https://github.com/echopen/kit-soft/issues`

# Machine type 

The machine is an 8 cored running 4.2.0-c9 GNU/Linux.

In addition to classical packages, these tools are installed

- libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

- archi i386

- opencv, version 3.0.0 + openCV python

- scipy


