# CS659

Course project done in CS659A (Autnomous Cyber-Physical Systems) at IIT Kanpur (January - April 2021).

Note: Cloning this repository may take some time since the folder "tl/weights" is humongous.

### Installation
Installation is highly specific to machines. The following were installed to successfully conduct the project:
  - python3 + pip3 + virtualenv + Flask
  - OpenCV (4.5.2-dev)
  - nvcc (Nvidia C Compiler) to take advantage of Nvidia GPU CUDA support.
  - ffmpeg

Makefile needs to be edited according to the locations of libraries of OpenCV and NVCC. Some changes also required in files located in "src" folder of original Darknet repository. No particular script can be made, since highle specific errors can arise. Finally run the make file.

```bash
$ make
```

Training has already been done and model weights (in multiples on 10000) have been saved in "tl/weights" folder. If you still wish to train:
```bash
$ wget https://pjreddie.com/media/files/darknet53.conv.74 # these are the "prior" weights that CNN has to start with
$ ./darknet detector train tl/loader.txt tl/train.cfg darknet53.conv.74
```

The files in this repository contain absolute paths that were used on a particular local machine. They have not been cleaned for the purpose of a future demo (since it had been difficult for an inexperienced member to install stuff and get things running).

Download the file at https://www.youtube.com/watch?v=P7j6XFmImAg and rename it "bosch.mp4". This is the original video file on which the project's main research paper was written. Note that
it has green/red boxes around traffic lights already, but our project marks them in bold, so they can be easily distinguished.

### Making Predictions
```bash
$ ./darknet detector demo tl/loader.txt tl/test.cfg tl/weights/120000.weights # opens webcam (if there is no error)
$ ./darknet detector demo tl/loader.txt tl/test.cfg tl/weights/120000.weights eg/bosch.mp4 # video file
$ python3 label.py image eg/27346.png
$ python3 label.py video eg/predictions.jpg
$ python3 label.py video # opens webcam (if there is no error)
```

The python scripts label.py and server.py are also available in tl/scripts directory.

### Running the Robot
On the machine with the GPU:
```bash
$ virtualenv venv # assuming python3 and virtualenv are installed already.
$ source venv/bin/activate
$ pip3 install Flask
$ cd ./tl/scripts
$ python3 server.py
```

On the Raspberry Pi 4, edit the script "basic.py" to change IP address of host and run:
```bash
$ python3 basic.py 
```

Finally, we cannot assure that this project will run as desired on everyone's machine, but the instructor/mentor can please contact us to see real-time demonstration as done on April 20, 2021. We think it is best for the team to demonstrate again rather than the checker to install stuff on her/his machine and run this code.

