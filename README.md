


<body bgcolor="#1e1f22">
 <style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #7a7e85;}
.s3 { color: #bcbec4;}
.s4 { color: #2aacb8;}
.s5 { color: #6aab73;}
.ln { color: #4b5059; font-weight: normal; font-style: normal; }
</style>
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Snake-in-nokia-game</font>
</center></td></tr></table>
<pre><a name="l1"><span class="ln">1    </span></a><span class="s0">import </span><span class="s1">pygame</span>
<a name="l2"><span class="ln">2    </span></a><span class="s0">import </span><span class="s1">time</span>
<a name="l3"><span class="ln">3    </span></a><span class="s0">import </span><span class="s1">random</span>
<a name="l4"><span class="ln">4    </span></a>
<a name="l5"><span class="ln">5    </span></a><span class="s2"># Initialize Pygame</span>
<a name="l6"><span class="ln">6    </span></a><span class="s1">pygame</span><span class="s3">.</span><span class="s1">init</span><span class="s3">()</span>
<a name="l7"><span class="ln">7    </span></a>
<a name="l8"><span class="ln">8    </span></a><span class="s2"># Screen dimensions</span>
<a name="l9"><span class="ln">9    </span></a><span class="s1">screen_width </span><span class="s3">= </span><span class="s4">800</span>
<a name="l10"><span class="ln">10   </span></a><span class="s1">screen_height </span><span class="s3">= </span><span class="s4">600</span>
<a name="l11"><span class="ln">11   </span></a>
<a name="l12"><span class="ln">12   </span></a><span class="s2"># Colors</span>
<a name="l13"><span class="ln">13   </span></a><span class="s1">white </span><span class="s3">= (</span><span class="s4">255</span><span class="s3">, </span><span class="s4">255</span><span class="s3">, </span><span class="s4">255</span><span class="s3">)</span>
<a name="l14"><span class="ln">14   </span></a><span class="s1">black </span><span class="s3">= (</span><span class="s4">0</span><span class="s3">, </span><span class="s4">0</span><span class="s3">, </span><span class="s4">0</span><span class="s3">)</span>
<a name="l15"><span class="ln">15   </span></a><span class="s1">red </span><span class="s3">= (</span><span class="s4">255</span><span class="s3">, </span><span class="s4">0</span><span class="s3">, </span><span class="s4">0</span><span class="s3">)</span>
<a name="l16"><span class="ln">16   </span></a><span class="s1">green </span><span class="s3">= (</span><span class="s4">0</span><span class="s3">, </span><span class="s4">255</span><span class="s3">, </span><span class="s4">0</span><span class="s3">)</span>
<a name="l17"><span class="ln">17   </span></a><span class="s1">blue </span><span class="s3">= (</span><span class="s4">0</span><span class="s3">, </span><span class="s4">0</span><span class="s3">, </span><span class="s4">255</span><span class="s3">)</span>
<a name="l18"><span class="ln">18   </span></a>
<a name="l19"><span class="ln">19   </span></a><span class="s2"># Clock</span>
<a name="l20"><span class="ln">20   </span></a><span class="s1">clock </span><span class="s3">= </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">time</span><span class="s3">.</span><span class="s1">Clock</span><span class="s3">()</span>
<a name="l21"><span class="ln">21   </span></a>
<a name="l22"><span class="ln">22   </span></a><span class="s2"># Create screen object</span>
<a name="l23"><span class="ln">23   </span></a><span class="s1">screen </span><span class="s3">= </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">display</span><span class="s3">.</span><span class="s1">set_mode</span><span class="s3">((</span><span class="s1">screen_width</span><span class="s3">, </span><span class="s1">screen_height</span><span class="s3">))</span>
<a name="l24"><span class="ln">24   </span></a><span class="s1">pygame</span><span class="s3">.</span><span class="s1">display</span><span class="s3">.</span><span class="s1">set_caption</span><span class="s3">(</span><span class="s5">&quot;Snake Game&quot;</span><span class="s3">)</span>
<a name="l25"><span class="ln">25   </span></a>
<a name="l26"><span class="ln">26   </span></a><span class="s2"># Snake variables</span>
<a name="l27"><span class="ln">27   </span></a><span class="s1">snake_block </span><span class="s3">= </span><span class="s4">10</span>
<a name="l28"><span class="ln">28   </span></a><span class="s1">snake_speed </span><span class="s3">= </span><span class="s4">15</span>
<a name="l29"><span class="ln">29   </span></a>
<a name="l30"><span class="ln">30   </span></a><span class="s2"># Fonts</span>
<a name="l31"><span class="ln">31   </span></a><span class="s1">font_style </span><span class="s3">= </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">font</span><span class="s3">.</span><span class="s1">SysFont</span><span class="s3">(</span><span class="s0">None</span><span class="s3">, </span><span class="s4">50</span><span class="s3">)</span>
<a name="l32"><span class="ln">32   </span></a><span class="s1">score_font </span><span class="s3">= </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">font</span><span class="s3">.</span><span class="s1">SysFont</span><span class="s3">(</span><span class="s0">None</span><span class="s3">, </span><span class="s4">35</span><span class="s3">)</span>
<a name="l33"><span class="ln">33   </span></a>
<a name="l34"><span class="ln">34   </span></a>
<a name="l35"><span class="ln">35   </span></a><span class="s0">def </span><span class="s1">message</span><span class="s3">(</span><span class="s1">msg</span><span class="s3">, </span><span class="s1">color</span><span class="s3">):</span>
<a name="l36"><span class="ln">36   </span></a>    <span class="s1">screen</span><span class="s3">.</span><span class="s1">fill</span><span class="s3">(</span><span class="s1">black</span><span class="s3">)</span>
<a name="l37"><span class="ln">37   </span></a>    <span class="s1">message_surface </span><span class="s3">= </span><span class="s1">font_style</span><span class="s3">.</span><span class="s1">render</span><span class="s3">(</span><span class="s1">msg</span><span class="s3">, </span><span class="s0">True</span><span class="s3">, </span><span class="s1">color</span><span class="s3">)</span>
<a name="l38"><span class="ln">38   </span></a>    <span class="s1">screen</span><span class="s3">.</span><span class="s1">blit</span><span class="s3">(</span><span class="s1">message_surface</span><span class="s3">, [</span><span class="s1">screen_width </span><span class="s3">// </span><span class="s4">3</span><span class="s3">, </span><span class="s1">screen_height </span><span class="s3">// </span><span class="s4">3</span><span class="s3">])</span>
<a name="l39"><span class="ln">39   </span></a>    <span class="s1">pygame</span><span class="s3">.</span><span class="s1">display</span><span class="s3">.</span><span class="s1">update</span><span class="s3">()</span>
<a name="l40"><span class="ln">40   </span></a>    <span class="s1">time</span><span class="s3">.</span><span class="s1">sleep</span><span class="s3">(</span><span class="s4">2</span><span class="s3">)</span>
<a name="l41"><span class="ln">41   </span></a>
<a name="l42"><span class="ln">42   </span></a>
<a name="l43"><span class="ln">43   </span></a><span class="s0">def </span><span class="s1">your_score</span><span class="s3">(</span><span class="s1">score</span><span class="s3">):</span>
<a name="l44"><span class="ln">44   </span></a>    <span class="s1">score_surface </span><span class="s3">= </span><span class="s1">score_font</span><span class="s3">.</span><span class="s1">render</span><span class="s3">(</span><span class="s5">&quot;Score: &quot; </span><span class="s3">+ </span><span class="s1">str</span><span class="s3">(</span><span class="s1">score</span><span class="s3">), </span><span class="s0">True</span><span class="s3">, </span><span class="s1">green</span><span class="s3">)</span>
<a name="l45"><span class="ln">45   </span></a>    <span class="s1">screen</span><span class="s3">.</span><span class="s1">blit</span><span class="s3">(</span><span class="s1">score_surface</span><span class="s3">, [</span><span class="s4">0</span><span class="s3">, </span><span class="s4">0</span><span class="s3">])</span>
<a name="l46"><span class="ln">46   </span></a>
<a name="l47"><span class="ln">47   </span></a>
<a name="l48"><span class="ln">48   </span></a><span class="s0">def </span><span class="s1">snake</span><span class="s3">(</span><span class="s1">snake_block</span><span class="s3">, </span><span class="s1">snake_list</span><span class="s3">):</span>
<a name="l49"><span class="ln">49   </span></a>    <span class="s0">for </span><span class="s1">x </span><span class="s0">in </span><span class="s1">snake_list</span><span class="s3">:</span>
<a name="l50"><span class="ln">50   </span></a>        <span class="s1">pygame</span><span class="s3">.</span><span class="s1">draw</span><span class="s3">.</span><span class="s1">rect</span><span class="s3">(</span><span class="s1">screen</span><span class="s3">, </span><span class="s1">green</span><span class="s3">, [</span><span class="s1">x</span><span class="s3">[</span><span class="s4">0</span><span class="s3">], </span><span class="s1">x</span><span class="s3">[</span><span class="s4">1</span><span class="s3">], </span><span class="s1">snake_block</span><span class="s3">, </span><span class="s1">snake_block</span><span class="s3">])</span>
<a name="l51"><span class="ln">51   </span></a>
<a name="l52"><span class="ln">52   </span></a>
<a name="l53"><span class="ln">53   </span></a><span class="s0">def </span><span class="s1">game_loop</span><span class="s3">():</span>
<a name="l54"><span class="ln">54   </span></a>    <span class="s2"># Initialize variables</span>
<a name="l55"><span class="ln">55   </span></a>    <span class="s1">game_over </span><span class="s3">= </span><span class="s0">False</span>
<a name="l56"><span class="ln">56   </span></a>    <span class="s1">game_close </span><span class="s3">= </span><span class="s0">False</span>
<a name="l57"><span class="ln">57   </span></a>
<a name="l58"><span class="ln">58   </span></a>    <span class="s1">x1 </span><span class="s3">= </span><span class="s1">screen_width </span><span class="s3">/ </span><span class="s4">2</span>
<a name="l59"><span class="ln">59   </span></a>    <span class="s1">y1 </span><span class="s3">= </span><span class="s1">screen_height </span><span class="s3">/ </span><span class="s4">2</span>
<a name="l60"><span class="ln">60   </span></a>
<a name="l61"><span class="ln">61   </span></a>    <span class="s1">x1_change </span><span class="s3">= </span><span class="s4">0</span>
<a name="l62"><span class="ln">62   </span></a>    <span class="s1">y1_change </span><span class="s3">= </span><span class="s4">0</span>
<a name="l63"><span class="ln">63   </span></a>
<a name="l64"><span class="ln">64   </span></a>    <span class="s1">snake_list </span><span class="s3">= []</span>
<a name="l65"><span class="ln">65   </span></a>    <span class="s1">length_of_snake </span><span class="s3">= </span><span class="s4">1</span>
<a name="l66"><span class="ln">66   </span></a>
<a name="l67"><span class="ln">67   </span></a>    <span class="s2"># Food position</span>
<a name="l68"><span class="ln">68   </span></a>    <span class="s1">food_x </span><span class="s3">= </span><span class="s1">round</span><span class="s3">(</span><span class="s1">random</span><span class="s3">.</span><span class="s1">randrange</span><span class="s3">(</span><span class="s4">0</span><span class="s3">, </span><span class="s1">screen_width </span><span class="s3">- </span><span class="s1">snake_block</span><span class="s3">) / </span><span class="s4">10.0</span><span class="s3">) * </span><span class="s4">10.0</span>
<a name="l69"><span class="ln">69   </span></a>    <span class="s1">food_y </span><span class="s3">= </span><span class="s1">round</span><span class="s3">(</span><span class="s1">random</span><span class="s3">.</span><span class="s1">randrange</span><span class="s3">(</span><span class="s4">0</span><span class="s3">, </span><span class="s1">screen_height </span><span class="s3">- </span><span class="s1">snake_block</span><span class="s3">) / </span><span class="s4">10.0</span><span class="s3">) * </span><span class="s4">10.0</span>
<a name="l70"><span class="ln">70   </span></a>
<a name="l71"><span class="ln">71   </span></a>    <span class="s0">while not </span><span class="s1">game_over</span><span class="s3">:</span>
<a name="l72"><span class="ln">72   </span></a>
<a name="l73"><span class="ln">73   </span></a>        <span class="s0">while </span><span class="s1">game_close</span><span class="s3">:</span>
<a name="l74"><span class="ln">74   </span></a>            <span class="s1">message</span><span class="s3">(</span><span class="s5">&quot;Game Over! Press C to Play Again or Q to Quit&quot;</span><span class="s3">, </span><span class="s1">red</span><span class="s3">)</span>
<a name="l75"><span class="ln">75   </span></a>
<a name="l76"><span class="ln">76   </span></a>            <span class="s0">for </span><span class="s1">event </span><span class="s0">in </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">event</span><span class="s3">.</span><span class="s1">get</span><span class="s3">():</span>
<a name="l77"><span class="ln">77   </span></a>                <span class="s0">if </span><span class="s1">event</span><span class="s3">.</span><span class="s1">type </span><span class="s3">== </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">KEYDOWN</span><span class="s3">:</span>
<a name="l78"><span class="ln">78   </span></a>                    <span class="s0">if </span><span class="s1">event</span><span class="s3">.</span><span class="s1">key </span><span class="s3">== </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">K_q</span><span class="s3">:</span>
<a name="l79"><span class="ln">79   </span></a>                        <span class="s1">game_over </span><span class="s3">= </span><span class="s0">True</span>
<a name="l80"><span class="ln">80   </span></a>                        <span class="s1">game_close </span><span class="s3">= </span><span class="s0">False</span>
<a name="l81"><span class="ln">81   </span></a>                    <span class="s0">if </span><span class="s1">event</span><span class="s3">.</span><span class="s1">key </span><span class="s3">== </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">K_c</span><span class="s3">:</span>
<a name="l82"><span class="ln">82   </span></a>                        <span class="s1">game_loop</span><span class="s3">()</span>
<a name="l83"><span class="ln">83   </span></a>
<a name="l84"><span class="ln">84   </span></a>        <span class="s0">for </span><span class="s1">event </span><span class="s0">in </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">event</span><span class="s3">.</span><span class="s1">get</span><span class="s3">():</span>
<a name="l85"><span class="ln">85   </span></a>            <span class="s0">if </span><span class="s1">event</span><span class="s3">.</span><span class="s1">type </span><span class="s3">== </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">QUIT</span><span class="s3">:</span>
<a name="l86"><span class="ln">86   </span></a>                <span class="s1">game_over </span><span class="s3">= </span><span class="s0">True</span>
<a name="l87"><span class="ln">87   </span></a>            <span class="s0">if </span><span class="s1">event</span><span class="s3">.</span><span class="s1">type </span><span class="s3">== </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">KEYDOWN</span><span class="s3">:</span>
<a name="l88"><span class="ln">88   </span></a>                <span class="s0">if </span><span class="s1">event</span><span class="s3">.</span><span class="s1">key </span><span class="s3">== </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">K_LEFT</span><span class="s3">:</span>
<a name="l89"><span class="ln">89   </span></a>                    <span class="s1">x1_change </span><span class="s3">= -</span><span class="s1">snake_block</span>
<a name="l90"><span class="ln">90   </span></a>                    <span class="s1">y1_change </span><span class="s3">= </span><span class="s4">0</span>
<a name="l91"><span class="ln">91   </span></a>                <span class="s0">elif </span><span class="s1">event</span><span class="s3">.</span><span class="s1">key </span><span class="s3">== </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">K_RIGHT</span><span class="s3">:</span>
<a name="l92"><span class="ln">92   </span></a>                    <span class="s1">x1_change </span><span class="s3">= </span><span class="s1">snake_block</span>
<a name="l93"><span class="ln">93   </span></a>                    <span class="s1">y1_change </span><span class="s3">= </span><span class="s4">0</span>
<a name="l94"><span class="ln">94   </span></a>                <span class="s0">elif </span><span class="s1">event</span><span class="s3">.</span><span class="s1">key </span><span class="s3">== </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">K_UP</span><span class="s3">:</span>
<a name="l95"><span class="ln">95   </span></a>                    <span class="s1">y1_change </span><span class="s3">= -</span><span class="s1">snake_block</span>
<a name="l96"><span class="ln">96   </span></a>                    <span class="s1">x1_change </span><span class="s3">= </span><span class="s4">0</span>
<a name="l97"><span class="ln">97   </span></a>                <span class="s0">elif </span><span class="s1">event</span><span class="s3">.</span><span class="s1">key </span><span class="s3">== </span><span class="s1">pygame</span><span class="s3">.</span><span class="s1">K_DOWN</span><span class="s3">:</span>
<a name="l98"><span class="ln">98   </span></a>                    <span class="s1">y1_change </span><span class="s3">= </span><span class="s1">snake_block</span>
<a name="l99"><span class="ln">99   </span></a>                    <span class="s1">x1_change </span><span class="s3">= </span><span class="s4">0</span>
<a name="l100"><span class="ln">100  </span></a>
<a name="l101"><span class="ln">101  </span></a>        <span class="s0">if </span><span class="s1">x1 </span><span class="s3">&gt;= </span><span class="s1">screen_width </span><span class="s0">or </span><span class="s1">x1 </span><span class="s3">&lt; </span><span class="s4">0 </span><span class="s0">or </span><span class="s1">y1 </span><span class="s3">&gt;= </span><span class="s1">screen_height </span><span class="s0">or </span><span class="s1">y1 </span><span class="s3">&lt; </span><span class="s4">0</span><span class="s3">:</span>
<a name="l102"><span class="ln">102  </span></a>            <span class="s1">game_close </span><span class="s3">= </span><span class="s0">True</span>
<a name="l103"><span class="ln">103  </span></a>
<a name="l104"><span class="ln">104  </span></a>        <span class="s1">x1 </span><span class="s3">+= </span><span class="s1">x1_change</span>
<a name="l105"><span class="ln">105  </span></a>        <span class="s1">y1 </span><span class="s3">+= </span><span class="s1">y1_change</span>
<a name="l106"><span class="ln">106  </span></a>        <span class="s1">screen</span><span class="s3">.</span><span class="s1">fill</span><span class="s3">(</span><span class="s1">black</span><span class="s3">)</span>
<a name="l107"><span class="ln">107  </span></a>        <span class="s1">pygame</span><span class="s3">.</span><span class="s1">draw</span><span class="s3">.</span><span class="s1">rect</span><span class="s3">(</span><span class="s1">screen</span><span class="s3">, </span><span class="s1">blue</span><span class="s3">, [</span><span class="s1">food_x</span><span class="s3">, </span><span class="s1">food_y</span><span class="s3">, </span><span class="s1">snake_block</span><span class="s3">, </span><span class="s1">snake_block</span><span class="s3">])</span>
<a name="l108"><span class="ln">108  </span></a>        <span class="s1">snake_head </span><span class="s3">= []</span>
<a name="l109"><span class="ln">109  </span></a>        <span class="s1">snake_head</span><span class="s3">.</span><span class="s1">append</span><span class="s3">(</span><span class="s1">x1</span><span class="s3">)</span>
<a name="l110"><span class="ln">110  </span></a>        <span class="s1">snake_head</span><span class="s3">.</span><span class="s1">append</span><span class="s3">(</span><span class="s1">y1</span><span class="s3">)</span>
<a name="l111"><span class="ln">111  </span></a>        <span class="s1">snake_list</span><span class="s3">.</span><span class="s1">append</span><span class="s3">(</span><span class="s1">snake_head</span><span class="s3">)</span>
<a name="l112"><span class="ln">112  </span></a>        <span class="s0">if </span><span class="s1">len</span><span class="s3">(</span><span class="s1">snake_list</span><span class="s3">) &gt; </span><span class="s1">length_of_snake</span><span class="s3">:</span>
<a name="l113"><span class="ln">113  </span></a>            <span class="s0">del </span><span class="s1">snake_list</span><span class="s3">[</span><span class="s4">0</span><span class="s3">]</span>
<a name="l114"><span class="ln">114  </span></a>
<a name="l115"><span class="ln">115  </span></a>        <span class="s0">for </span><span class="s1">block </span><span class="s0">in </span><span class="s1">snake_list</span><span class="s3">[:-</span><span class="s4">1</span><span class="s3">]:</span>
<a name="l116"><span class="ln">116  </span></a>            <span class="s0">if </span><span class="s1">block </span><span class="s3">== </span><span class="s1">snake_head</span><span class="s3">:</span>
<a name="l117"><span class="ln">117  </span></a>                <span class="s1">game_close </span><span class="s3">= </span><span class="s0">True</span>
<a name="l118"><span class="ln">118  </span></a>
<a name="l119"><span class="ln">119  </span></a>        <span class="s1">snake</span><span class="s3">(</span><span class="s1">snake_block</span><span class="s3">, </span><span class="s1">snake_list</span><span class="s3">)</span>
<a name="l120"><span class="ln">120  </span></a>        <span class="s1">your_score</span><span class="s3">(</span><span class="s1">length_of_snake </span><span class="s3">- </span><span class="s4">1</span><span class="s3">)</span>
<a name="l121"><span class="ln">121  </span></a>        <span class="s1">pygame</span><span class="s3">.</span><span class="s1">display</span><span class="s3">.</span><span class="s1">update</span><span class="s3">()</span>
<a name="l122"><span class="ln">122  </span></a>
<a name="l123"><span class="ln">123  </span></a>        <span class="s0">if </span><span class="s1">x1 </span><span class="s3">== </span><span class="s1">food_x </span><span class="s0">and </span><span class="s1">y1 </span><span class="s3">== </span><span class="s1">food_y</span><span class="s3">:</span>
<a name="l124"><span class="ln">124  </span></a>            <span class="s1">food_x </span><span class="s3">= </span><span class="s1">round</span><span class="s3">(</span><span class="s1">random</span><span class="s3">.</span><span class="s1">randrange</span><span class="s3">(</span><span class="s4">0</span><span class="s3">, </span><span class="s1">screen_width </span><span class="s3">- </span><span class="s1">snake_block</span><span class="s3">) / </span><span class="s4">10.0</span><span class="s3">) * </span><span class="s4">10.0</span>
<a name="l125"><span class="ln">125  </span></a>            <span class="s1">food_y </span><span class="s3">= </span><span class="s1">round</span><span class="s3">(</span><span class="s1">random</span><span class="s3">.</span><span class="s1">randrange</span><span class="s3">(</span><span class="s4">0</span><span class="s3">, </span><span class="s1">screen_height </span><span class="s3">- </span><span class="s1">snake_block</span><span class="s3">) / </span><span class="s4">10.0</span><span class="s3">) * </span><span class="s4">10.0</span>
<a name="l126"><span class="ln">126  </span></a>            <span class="s1">length_of_snake </span><span class="s3">+= </span><span class="s4">1</span>
<a name="l127"><span class="ln">127  </span></a>
<a name="l128"><span class="ln">128  </span></a>        <span class="s1">clock</span><span class="s3">.</span><span class="s1">tick</span><span class="s3">(</span><span class="s1">snake_speed</span><span class="s3">)</span>
<a name="l129"><span class="ln">129  </span></a>
<a name="l130"><span class="ln">130  </span></a>    <span class="s1">pygame</span><span class="s3">.</span><span class="s1">quit</span><span class="s3">()</span>
<a name="l131"><span class="ln">131  </span></a>    <span class="s1">quit</span><span class="s3">()</span>
<a name="l132"><span class="ln">132  </span></a>
<a name="l133"><span class="ln">133  </span></a>
<a name="l134"><span class="ln">134  </span></a><span class="s1">game_loop</span><span class="s3">()</span></pre>
</body>
</html>
