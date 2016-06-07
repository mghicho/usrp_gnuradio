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
