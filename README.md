GTA self driving Agent
===================


The goal is to program a self-propelled agent, that is capable of driving a car in gtaIV.
The agent's driving skills are concentrated on motorways and long straight streets.

----------


Realization
-------------

The Agent is programmed in python and trained with a [CNN](https://www.tensorflow.org/tutorials/wide_and_deep) which is based on [TensorFlow](https://www.tensorflow.org/).

#### <i class="icon-down-big"></i> Installation

	> - Clone Repository
	> - Install Dependencies

#### <i class="icon-camera"></i> Capture data

	To collect data use collect_data.py.
	Gta window has to be shrunk down to a resolution of 800x600
	and moved to the left upper corner.
	
	Set path variable to your prefered location.
	Files will be saved in approximately 300KB .npy files(uncompressed).
	
	To start collect_data.py several arguments can be used.
	> - -s can be a number to define starting step manualy or "forward" to 
	use existing files as step indicator.

#### <i class="icon-ccw"></i> Training

	To train your model use train.py.
	Set path variable to location where training data is saved.
	Name your model by setting MODEL_NAME variable to your most preferred name.
	
#### <i class="icon-right-big"></i> Testing

	To test your model use test_model.py.
	Choose your already trained model by setting MODEL_NAME variable to your best trained one.
	
	To test the agent the Gta window has to be shrunk down to a resolution of 800x600
	and moved to the left upper corner.
	
	Now, everything is ready to be tested.

#### <i class="icon-archive"></i> Prefabricated models

	Prefabricated models will be provided as far as I can produce them myself and 
	as far as they fit my own requirements.


Dependencies
-------------------

> - numpy
> - TensorFlow
> - tflearn
> - cv2
> - sys
> - glob
> - optparse
> - threading
> - keyboard
> - win32gui, win32ui, win32con, win32api <br>
>  If you get this error: `ImportError: DLL load failed: The specified module could not be found.`,
>  move *pythoncom36.dll* and *pywintypes36.dll* from 
>  `Python36\Lib\site-packages\pywin32_system32` to 
>  `Python36\Lib\site-packages\win32` <br>
>  If you get this error: `ImportError: No module named win32gui`, after installing win32 and you are using 64 bit python install 64 bit win32 wheel from http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32 by using `pip install <name>.whl`
> - re

Contributing
-------------------
1: Fork it! <br>
2: Create your feature branch: `git checkout -b my-new-feature` <br>
3: Commit your changes: `git commit -am 'Add some feature'` <br>
4: Push to the branch: `git push origin my-new-feature` <br>
5: [Submit](https://help.github.com/articles/about-pull-requests/) a pull request <br>

