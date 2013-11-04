<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<databrowser>
    <title>
        <text>CPU Livetimes TAPS</text>
        <color>
            <red>49</red>
            <green>55</green>
            <blue>57</blue>
        </color>
        <font>1|Sans|12.0|1|GTK|1|</font>
    </title>
    <graph_settings>
        <show_title>true</show_title>
        <show_legend>true</show_legend>
        <show_plot_area_border>true</show_plot_area_border>
        <transparent>true</transparent>
    </graph_settings>
    <scroll>true</scroll>
    <update_period>1.0</update_period>
    <start>-2 minutes 0.0 seconds</start>
    <end>now</end>
    <time_axis>
        <axis>
            <name>Time</name>
            <font>1|Sans|10.0|1|GTK|1|</font>
            <scale_font>1|Sans|10.0|0|GTK|1|</scale_font>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <min>1.383558117283E12</min>
            <max>1.383558237283E12</max>
            <log_scale>false</log_scale>
            <autoscale>false</autoscale>
            <visible>true</visible>
            <grid_line>
                <show_grid_line>true</show_grid_line>
                <dash_grid_line>false</dash_grid_line>
                <color>
                    <red>200</red>
                    <green>200</green>
                    <blue>200</blue>
                </color>
            </grid_line>
            <format>
                <auto_format>true</auto_format>
                <time_format>true</time_format>
                <format_pattern>HH:mm:ss</format_pattern>
            </format>
        </axis>
    </time_axis>
    <background>
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
    </background>
    <archive_rescale>NONE</archive_rescale>
    <axes>
        <axis>
            <name>Livetime [%]</name>
            <font>1|Sans|10.0|1|GTK|1|</font>
            <scale_font>1|Sans|10.0|0|GTK|1|</scale_font>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <min>0.0</min>
            <max>110.0</max>
            <log_scale>false</log_scale>
            <autoscale>false</autoscale>
            <visible>true</visible>
            <grid_line>
                <show_grid_line>true</show_grid_line>
                <dash_grid_line>true</dash_grid_line>
                <color>
                    <red>200</red>
                    <green>200</green>
                    <blue>200</blue>
                </color>
            </grid_line>
            <format>
                <auto_format>true</auto_format>
                <time_format>false</time_format>
                <format_pattern>############.##</format_pattern>
            </format>
        </axis>
    </axes>
    <annotations>
    </annotations>
    <pvlist>
        <pv>
            <name>TAPS:TRIG:TriggerLivetimeCoupled</name>
            <display_name>taps-trigger</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>21</red>
                <green>21</green>
                <blue>196</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TRIG:TAPS:TriggerLivetimeStandalone</name>
            <display_name>taps-trigger(standalone)</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>242</red>
                <green>26</green>
                <blue>26</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:BAF:SectorA:TRIG:Livetime</name>
            <display_name>taps-baf-a</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>33</red>
                <green>179</green>
                <blue>33</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:BAF:SectorB:TRIG:Livetime</name>
            <display_name>taps-baf-b</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>127</red>
                <green>127</green>
                <blue>127</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:BAF:SectorC:TRIG:Livetime</name>
            <display_name>taps-baf-c</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>30</red>
                <green>144</green>
                <blue>255</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:BAF:SectorD:TRIG:Livetime</name>
            <display_name>taps-baf-d</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>255</red>
                <green>255</green>
                <blue>0</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:BAF:SectorE:TRIG:Livetime</name>
            <display_name>taps-baf-e</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>255</red>
                <green>165</green>
                <blue>0</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:BAF:SectorF:TRIG:Livetime</name>
            <display_name>vme-baf-f</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>0</red>
                <green>0</green>
                <blue>0</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:VETOBAF:SectorAB:TRIG:Livetime</name>
            <display_name>taps-veto-ab</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>128</red>
                <green>0</green>
                <blue>128</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:VETOBAF:SectorCD:TRIG:Livetime</name>
            <display_name>taps-veto-cd</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>0</red>
                <green>128</green>
                <blue>0</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:VETOBAF:SectorEF:TRIG:Livetime</name>
            <display_name>taps-veto-ef</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>144</red>
                <green>238</green>
                <blue>144</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
        <pv>
            <name>TAPS:PWO:TRIG:Livetime</name>
            <display_name>taps-pwo</display_name>
            <visible>true</visible>
            <axis>0</axis>
            <linewidth>2</linewidth>
            <color>
                <red>139</red>
                <green>105</green>
                <blue>20</blue>
            </color>
            <trace_type>AREA</trace_type>
            <waveform_index>0</waveform_index>
            <period>0.0</period>
            <ring_size>5000</ring_size>
            <request>OPTIMIZED</request>
            <archive>
                <name>Inst</name>
                <url>jdbc:oracle:thin:@snsoroda-scan.sns.gov:1521/scprod_controls</url>
                <key>1</key>
            </archive>
            <archive>
                <name>Accl</name>
                <url>jdbc:oracle:thin:@(DESCRIPTION=(LOAD_BALANCE=OFF)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1a.sns.ornl.gov)(PORT=1610))(ADDRESS=(PROTOCOL=TCP)(HOST=snsapp1b.sns.ornl.gov)(PORT=1610))(CONNECT_DATA=(SERVICE_NAME=ics_prod_lba)))</url>
                <key>1</key>
            </archive>
        </pv>
    </pvlist>
</databrowser>