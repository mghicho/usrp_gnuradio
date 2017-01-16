# Installing out of tree modules:
If GRC complains that it can't find some blocks like:
```
Error: Block key "name of block" not found in Platform - grc(GNU Radio Companion)
```
Most likely you used a different CMAKE_INSTALL_PREFIX for the module than for GNU Radio. Therefore, the blocks of the module ended up in a different directory and GRC can't find them. You have to tell GRC where these blocks are by creating/adding to your ~/.gnuradio/config.conf something like
```
[grc]
local_blocks_path = /usr/local/share/gnuradio/grc/blocks
```
But with the directories that match your installation.

If this is your problem you have probably installed python modules correctly but GRC can not find modules.

#####How to find the above address?
if you look at you installation report after `sudo make install` command you can find out where is the location of `*.xml` files. 
it's something like this:
```
-- Installing: /usr/local/share/gnuradio/grc/blocks/mac_simple_mac.xml
-- Installing: /usr/local/share/gnuradio/grc/blocks/mac_virtual_channel_encoder.xml
-- Installing: /usr/local/share/gnuradio/grc/blocks/mac_virtual_channel_decoder.xml
-- Installing: /usr/local/share/gnuradio/grc/blocks/mac_packet_framer.xml
-- Installing: /usr/local/share/gnuradio/grc/blocks/mac_packet_deframer.xml
-- Installing: /usr/local/share/gnuradio/grc/blocks/mac_packet_to_pdu.xml
-- Installing: /usr/local/share/gnuradio/grc/blocks/mac_802_3_tracker.xml
-- Installing: /usr/local/share/gnuradio/grc/blocks/mac_burst_tagger.xml
```
which indicates that the installation have copied xml files in `/usr/local/share/gnuradio/grc/blocks`


#uhd commands: 
there are some simple commands that one can use after installing GNURadio, specially if you want a simple spectrum analyzer or want to Record I/Q sample stream to a file and use in another software like MATLAB. they are listed below. they all include a "-h" switch which will display a help screen. more info [here](https://gnuradio.org/redmine/projects/gnuradio/wiki/HowToUse)
```
uhd_cal_rx_iq_balance
uhd_find_devices
uhd_siggen
uhd_cal_tx_dc_offset
uhd_image_loader
uhd_siggen_gui
uhd_cal_tx_iq_balance
uhd_rx_cfile
uhd_usrp_probe
uhd_fft     
uhd_rx_nogui           
```

# Adding new modules to gnuradio in mac os :
If you've installed your gnuradio with mac port, first you need to make sure that the mac port python is in use. then when you wanna compile the module use this:

```
cmake -DPYTHON_LIBRARY=/opt/local/lib/libpython2.7.dylib -DCMAKE_INSTALL_PREFIX=/opt/local/ ../
```

after compiling the code( make and sudo make install) put these two lines in .bash_profile :

```
export PYTHONPATH=/opt/local/lib/python2.7/site-packages:$PYTHONPATH
export GRC_BLOCKS_PATH=/usr/local/share/gnuradio/grc/blocks
```
### Adding a library for linking:
If an outside library has been used for a block. That library might be needed in linking phase of making. the standard place for libraries is `/usr/local/lib` , if the library is already build and installed its file must be there. If the use has the .a or .so or .dylib file they may put a copy of it in that folder so the gcc can easily find it with the flag `-l<name of library>`. for example if the name of library is levmar, the filename is liblevmar.a and the flag would -llevmar. 
in order to add the linking flag to all the codes, the function `target_link_libraries` in the file `CMakeLists.txt` found in the `lib` folder of the module has to be modified in the following order. For example in order to add the `levmar` library the line:
```
target_link_libraries(gnuradio-pnc ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
```
will change to :
```
target_link_libraries(gnuradio-pnc ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES} levmar)
```
The same thing happens to all other used of function `target_link_libraries` in that file. run the cmake command and make again after modifing this file.

##### While installing gr-cdma:
if you're getting a linking error related to lib4cpp, search the build directory for "link.txt" and add `-llib4cpp` at the end of all of those files.

#Multiple inputs:
put the `MAX_INT` parameter as -1. 
the `input_items` input of the work function is vector of void stars. these void stars can be casted to the desired type of input, e.g. to `gr_complex*` in case of complex input. Obviously the number of input ports can be obtained from size of the vector. Example:
```
int number_of_inputs=input_items.size();
for(int i=0;i<number_of_inputs;i++)
{
 int this loop, (const gr_complex *) input_items[i] is the array for i_th input.
 const gr_complex *in_i = (const gr_complex *) input_items[0];
 now we can iterate in in_i for items of i_th input.
}
```

# Working with tagged_stream_blocks:
The definition for the `work` function of tagged_stream_blocks looks like the one for `general_work` of other blocks. but the difference here is that the input `noutput_items` is "not" number of output items to write on each output stream. In this case, this variable shows The size of the writable output buffer which can be a lot larger than the pdu size. this essentially makes this variable unusable. Instead use `ninput_items[i]` where `i` is the index of input to find the pdu length.


# OOT modules in Ubuntu,
If after compilling and installing a new block in ubuntu, when everything is fine, you stil get this error:
```
AttributeError : 'module' object has no attribute 'block name'
```
in order to fix it, first check the enviroment variable `PYTHONPATH` and make sure it point to where the python blocks are, if it didn't solve the problem, then it might be because SWIG is not install. if that's the case, you must've got this error after cmakeing:
```
disabling swig because version check failed
```
in order to solve it, simply install swig on your ubuntu machine by running the below code:
```
sudo apt-get install swig
```
