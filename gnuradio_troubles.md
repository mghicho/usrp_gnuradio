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
