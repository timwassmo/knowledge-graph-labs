<div id="mw-content-container" class="ts-container"><div id="mw-content-block" class="ts-inner"><div id="mw-content-wrapper"><div id="mw-content"><div id="content" class="mw-body" role="main"><div class="mw-indicators mw-body-content">
</div>
<h1 id="firstHeading" class="firstHeading">Lab: Getting started with VSCode, Python and RDFlib</h1><div id="bodyContentOuter"><div id="siteSub">From Info216</div><div id="mw-page-header-links"><div role="navigation" class="mw-portlet tools-inline" id="p-namespaces" aria-labelledby="p-namespaces-label"><h3 id="p-namespaces-label" lang="en" dir="ltr">Namespaces</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"><li id="ca-nstab-main" class="selected"><a href="/info216/index.php?title=Lab:_Getting_started_with_VSCode,_Python_and_RDFlib" title="View the content page [ctrl-option-c]" accesskey="c"><span>Page</span></a></li><li id="ca-talk" class="new"><a href="/info216/index.php?title=Talk:Lab:_Getting_started_with_VSCode,_Python_and_RDFlib&amp;action=edit&amp;redlink=1" rel="discussion" title="Discussion about the content page (page does not exist) [ctrl-option-t]" accesskey="t"><span>Discussion</span></a></li></ul></div></div><div role="navigation" class="mw-portlet tools-inline" id="p-more" aria-labelledby="p-more-label"><h3 id="p-more-label" lang="en" dir="ltr">More</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"><li id="ca-more" class="dropdown-toggle"><span>More</span></li><li id="ca-languages" class="dropdown-toggle"><span>Languages</span></li></ul></div></div><div role="navigation" class="mw-portlet tools-inline" id="p-views" aria-labelledby="p-views-label"><h3 id="p-views-label" lang="en" dir="ltr">Page actions</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"><li id="ca-view" class="selected"><a href="/info216/index.php?title=Lab:_Getting_started_with_VSCode,_Python_and_RDFlib"><span>Read</span></a></li><li id="ca-viewsource"><a href="/info216/index.php?title=Lab:_Getting_started_with_VSCode,_Python_and_RDFlib&amp;action=edit" title="This page is protected.
You can view its source [ctrl-option-e]" accesskey="e"><span>View source</span></a></li><li id="ca-history"><a href="/info216/index.php?title=Lab:_Getting_started_with_VSCode,_Python_and_RDFlib&amp;action=history" title="Past revisions of this page [ctrl-option-h]" accesskey="h"><span>History</span></a></li></ul></div></div></div><div class="visualClear"></div><div class="mw-body-content" id="bodyContent"><div id="contentSub"></div><div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><div class="mw-parser-output"><div id="toc" class="toc" role="navigation" aria-labelledby="mw-toc-heading"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none"><div class="toctitle" lang="en" dir="ltr"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Topics"><span class="tocnumber">1</span> <span class="toctext">Topics</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Useful_materials"><span class="tocnumber">2</span> <span class="toctext">Useful materials</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Tasks"><span class="tocnumber">3</span> <span class="toctext">Tasks</span></a>
<ul>
<li class="toclevel-2 tocsection-4"><a href="#Install_Python.2C_Pip.2C_VSCode.2C_and_RDFlib"><span class="tocnumber">3.1</span> <span class="toctext">Install Python, Pip, VSCode, and RDFlib</span></a></li>
<li class="toclevel-2 tocsection-5"><a href="#Programming_tasks"><span class="tocnumber">3.2</span> <span class="toctext">Programming tasks</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-6"><a href="#If_you_have_more_time..."><span class="tocnumber">4</span> <span class="toctext">If you have more time...</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Topics">Topics</span></h2>
<ol><li>Prepare for programming knowledge graphs with rdflib in Python.</li>
<li>Get started with basic RDF programming.</li></ol>
<h2><span class="mw-headline" id="Useful_materials">Useful materials</span></h2>
<p>VSCode:
</p>
<ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://code.visualstudio.com/docs/python/python-tutorial">Getting Started with Python in VS Code</a></li>
<li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://code.visualstudio.com/docs/python/environments#">Using Python environments in VS Code</a> (pip is easiest to start with)</li></ul>
<p>RDFlib:
</p>
<ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://rdflib.readthedocs.io/en/stable/gettingstarted.html">Intro to RDFlib</a></li>
<li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://rdflib.readthedocs.io/en/stable/intro_to_creating_rdf.html">Intro to creating triples</a></li>
<li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html">Serialising and parsing</a></li>
<li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.youtube.com/watch?v=sCU214rbRZ0">8 min introduction video to RDFlib</a></li></ul>
<p>RDFlib classes/interfaces and methods:
</p>
<ul><li>Graph (add, close, and perhaps remove methods)</li>
<li>URIRef</li>
<li>Literal</li>
<li>Namespace</li></ul>
<h2><span class="mw-headline" id="Tasks">Tasks</span></h2>
<h3><span id="Install_Python,_Pip,_VSCode,_and_RDFlib"></span><span class="mw-headline" id="Install_Python.2C_Pip.2C_VSCode.2C_and_RDFlib">Install Python, Pip, VSCode, and RDFlib</span></h3>
<p><b>1)</b> You need to have Python version &gt;= 3.7 on your computer. Use the command <i>python --version</i> in a command/terminal window to check. You can download Python and Pip <a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.python.org/downloads/">here</a>. To ensure you have the most recent Pip, you can do
</p>
<pre>python -m pip install --upgrade pip
</pre>
<p><b>2)</b> You need to have an Integrated Development Environment (IDE) that supports Python. If you are unsure, you can download the free and open source Visual Studio Code (VSCode) <a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://code.visualstudio.com/Download">here</a>.
</p><p><b>3)</b> Create a folder for INFO216. Start VSCode and <i>create a workspace</i> in the file menu (File Menu --&gt; Save Workspace As) and save it in your folder. Afterwards, on the left side of VSCode, click on the document icon (explorer). Click Open Folder, and open your INFO216 folder. Create a new file with <i>.py</i> extension. 
</p><p><b>4)</b> You will be asked to install the Python extension, install it. If you weren't asked, on the left side of VSCode click on the 4 cubes (extension manager). Within here search for Microsoft's Python extension and install it. 
</p><p><b>5)</b> If you don't have your terminal open, go to the top menu and click on terminal, and then <i>New Terminal</i>. Check where your terminal window is currently located. The bottom line starting with <i>PS</i> or <i>(base)</i> shows where it's located. If you added the folder earlier, then you should be located in your INFO216 folder. However, if the destination after PS is not your INFO216 folder, you need to locate to this folder. You can move through folders with the <i>cd</i> command in the terminal. For instance, if you are at <i>PS C:\Users\YourName&gt;</i> and your INFO216 folder is at your desktop, you could type the following <i>cd .\Desktop\INFO216\</i>.     
</p><p><b>6)</b> If you are correctly located, type in the following command into your terminal window 
</p><p>(Windows)
</p>
<pre>py -3 -m venv .venv
.venv\scripts\activate
</pre>
<p>(Mac / Linux)
</p>
<pre>python3 -m venv .venv
source .venv/bin/activate
</pre>
<p><b>7)</b> If you get the message <i>"... is not digitally signed. You cannot run this script on the current system."</i> copy and paste the following in the terminal, and repeat step 6:
</p>
<pre>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
</pre>
<p><b>8)</b> This should now have created a virtual environment in your folder called <i>.venv</i>. In the bottom right corner you will receive a notification asking your to select the new environment for the workspace folder, select yes. You should now see a <i>(.venv)</i> in front of PS/(base) in the terminal window. Your virtual environment should now automatically be selected when you open your workspace. However, sometimes you might need to open a new terminal for the (.venv) to appear.  
</p><p><b>9)</b> In the terminal, type the following to install RDFlib:
</p>
<pre>pip install rdflib
</pre>
<p><b>10)</b> You might need to close and reopen VSCode for RDFlib to work. You can now <i>import rdflib</i> into your <i>.py</i> file, or import specific classes/inferfaces such as <i>from rdflib import Namespace, Graph</i>. 
</p><p><b>11)</b> Right click in your code and click "Run Current File in Interactive Window". When running your program for the first time, you might be asked to install <i>ipykernel package</i>, install it. 
</p>
<h3><span class="mw-headline" id="Programming_tasks">Programming tasks</span></h3>
<p><b>Task:</b> 
Represent the sentences below as triples. Note that some sentences can result in several triples. 
</p>
<ul><li>The Mueller Investigation was lead by Robert Mueller.
<ul><li>It involved Paul Manafort, Rick Gates, George Papadopoulos, Michael Flynn, Michael Cohen, and Roger Stone.</li></ul></li>
<li>Paul Manafort was business partner of Rick Gates.
<ul><li>He was campaign chairman for Donald Trump</li>
<li>He was charged with money laundering, tax evasion, and foreign lobbying.</li>
<li>He was convicted for bank and tax fraud.</li>
<li>He pleaded guilty to conspiracy.</li>
<li>He was sentenced to prison.</li>
<li>He negotiated a plea agreement.</li></ul></li>
<li>Rick Gates was charged with money laundering, tax evasion and foreign lobbying.
<ul><li>He pleaded guilty to conspiracy and lying to FBI.</li></ul></li></ul>
<p><b>Task:</b> Write a program that creates an RDF graph and adds the triples you just created. 
</p><p>For the URIs, you can just use an example path like <i><a target="_blank" rel="nofollow noreferrer noopener" class="external free" href="http://example.org/">http://example.org/</a></i>. 
So if you want to represent Donald Trump, the URI could be <i><a target="_blank" rel="nofollow noreferrer noopener" class="external free" href="http://example.org/Donald_Trump">http://example.org/Donald_Trump</a></i>, and you can create the resource like this:
</p>
<pre>from rdflib import URIRef

donaldTrump = URIRef('<a target="_blank" rel="nofollow noreferrer noopener" class="external free" href="http://example.org/Donald_Trump'">http://example.org/Donald_Trump'</a>)
</pre>
<p>You can even use a Namespace so you don't have to write the full URI every time:
</p>
<pre>from rdflib import Namespace

ex = Namespace('<a target="_blank" rel="nofollow noreferrer noopener" class="external free" href="http://example.org/'">http://example.org/'</a>)
donaldTrump = ex.Donald_Trump
</pre>
<p><b>Task:</b> Use the <i>serialize</i> method of <i>rdflib.Graph</i> to write out the model in different formats (on screen or to file):
</p>
<ul><li>Turtle (format='ttl')</li>
<li>N-Triple (format='nt')</li>
<li>JSON-LD (format='json-ld')</li>
<li>RDF-XML (format='xml')</li></ul>
<p>Which one is easiest to read? What are the pros and cons of the different formats?
We will look more at some of them later in the course!
</p><p><b>Task:</b> Use the simple <a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.ldf.fi/service/rdf-grapher">online RDF grapher</a> to visualise your model. :isSemantic offers <a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://issemantic.net/rdf-visualizer">a more advanced RDF visualiser</a> that you can also test if you want.
</p><p><b>Task:</b> Loop through the triples in the model to print out all triples that have <i>pleading guilty</i> as predicate. If you have been inconsistent about some predicate or other term, you can first write loops that correct wrong terms everywhere in the model. (<i>Tip:</i> to correct a term in a model, you typically have to first <i>remove</i> the old triple and then <i>add</i> a new one.)
</p>
<h2><span class="mw-headline" id="If_you_have_more_time...">If you have more time...</span></h2>
<p><b>Task:</b> If you have more time you can continue extending your graph:
</p>
<ul><li>Michael Cohen was Donald Trump's attorney.
<ul><li>He pleaded guilty for lying to Congress.</li></ul></li>
<li>Michael Flynn was adviser to Donald Trump.
<ul><li>He pleaded guilty for lying to the FBI.</li>
<li>He negotiated a plea agreement.</li></ul></li></ul>
<p><b>Task:</b> According to <a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.pbs.org/wgbh/frontline/article/the-mueller-investigation-explained-2/">this FRONTLINE article</a>, Gates', Cohen's and Flynn's lying were different and are described in different detail. How can you modify your knowledge graph to account for this?
</p><p><b>Task:</b> Write a method (function) that submits your model to <a target="_blank" rel="nofollow noreferrer noopener" class="external free" href="https://www.ldf.fi/service/rdf-grapher">https://www.ldf.fi/service/rdf-grapher</a> for rendering and saves the returned image to file.
</p>
<!-- 
NewPP limit report
Cached time: 20230508075430
Cache expiry: 86400
Dynamic content: false
Complications: []
CPU time usage: 0.025 seconds
Real time usage: 0.027 seconds
Preprocessor visited node count: 17/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 0/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 -total
-->

<!-- Saved in parser cache with key info216-mediawiki-:pcache:idhash:79-0!canonical and timestamp 20230508075430 and revision id 2004
 -->
</div></div><div class="printfooter">
Retrieved from "<a dir="ltr" href="https://wiki.app.uib.no/info216/index.php?title=Lab:_Getting_started_with_VSCode,_Python_and_RDFlib&amp;oldid=2004">https://wiki.app.uib.no/info216/index.php?title=Lab:_Getting_started_with_VSCode,_Python_and_RDFlib&amp;oldid=2004</a>"</div>
<div class="visualClear"></div></div></div></div></div><div id="content-bottom-stuff"><div id="catlinks" class="catlinks catlinks-allhidden" data-mw="interface"></div></div></div><div id="mw-site-navigation"><div id="p-logo" class="mw-portlet" role="banner"><a class="mw-wiki-logo fallback" href="/info216/index.php?title=Main_Page" title="Visit the main page"></a></div><div id="site-navigation" class="sidebar-chunk"><h2><span>Navigation</span></h2><div class="sidebar-inner"><div role="navigation" class="mw-portlet" id="p-navigation" aria-labelledby="p-navigation-label"><h3 id="p-navigation-label" lang="en" dir="ltr">Navigation</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"><li id="n-INFO216-Wiki"><a href="/info216/index.php?title=INFO216_Wiki"><span>INFO216 Wiki</span></a></li><li id="n-Lectures-and-Readings"><a href="/info216/index.php?title=Readings"><span>Lectures and Readings</span></a></li><li id="n-Lab-Exercises"><a href="/info216/index.php?title=Python_Labs"><span>Lab Exercises</span></a></li><li id="n-Python-Examples"><a href="/info216/index.php?title=Python_Examples"><span>Python Examples</span></a></li><li id="n-SPARQL-Examples"><a href="/info216/index.php?title=SPARQL_Examples"><span>SPARQL Examples</span></a></li><li id="n-Lecture-Examples"><a href="/info216/index.php?title=Examples_from_the_lectures"><span>Lecture Examples</span></a></li><li id="n-Old-Exams"><a href="/info216/index.php?title=Exams"><span>Old Exams</span></a></li><li id="n-recentchanges"><a href="/info216/index.php?title=Special:RecentChanges" title="A list of recent changes in the wiki [ctrl-option-r]" accesskey="r"><span>Recent changes</span></a></li><li id="n-help"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Contents" target="_blank" title="The place to find out"><span>Help</span></a></li></ul></div></div></div></div><div id="site-tools" class="sidebar-chunk"><h2><span>Wiki tools</span></h2><div class="sidebar-inner"><div role="navigation" class="mw-portlet" id="p-tb" aria-labelledby="p-tb-label"><h3 id="p-tb-label" lang="en" dir="ltr">Wiki tools</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"><li id="t-specialpages"><a href="/info216/index.php?title=Special:SpecialPages" title="A list of all special pages [ctrl-option-q]" accesskey="q"><span>Special pages</span></a></li></ul></div></div></div></div></div><div id="mw-related-navigation"><div id="page-tools" class="sidebar-chunk"><h2><span>Page tools</span></h2><div class="sidebar-inner"><div role="navigation" class="mw-portlet emptyPortlet" id="p-cactions" aria-labelledby="p-cactions-label"><h3 id="p-cactions-label" lang="en" dir="ltr">Page tools</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"></ul></div></div><div role="navigation" class="mw-portlet emptyPortlet" id="p-userpagetools" aria-labelledby="p-userpagetools-label"><h3 id="p-userpagetools-label" lang="en" dir="ltr">Userpage tools</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"></ul></div></div><div role="navigation" class="mw-portlet" id="p-pagemisc" aria-labelledby="p-pagemisc-label"><h3 id="p-pagemisc-label" lang="en" dir="ltr">More</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"><li id="t-whatlinkshere"><a href="/info216/index.php?title=Special:WhatLinksHere/Lab:_Getting_started_with_VSCode,_Python_and_RDFlib" title="A list of all wiki pages that link here [ctrl-option-j]" accesskey="j"><span>What links here</span></a></li><li id="t-recentchangeslinked"><a href="/info216/index.php?title=Special:RecentChangesLinked/Lab:_Getting_started_with_VSCode,_Python_and_RDFlib" rel="nofollow" title="Recent changes in pages linked from this page [ctrl-option-k]" accesskey="k"><span>Related changes</span></a></li><li id="t-print"><a href="javascript:print();" rel="alternate" title="Printable version of this page [ctrl-option-p]" accesskey="p"><span>Printable version</span></a></li><li id="t-permalink"><a href="/info216/index.php?title=Lab:_Getting_started_with_VSCode,_Python_and_RDFlib&amp;oldid=2004" title="Permanent link to this revision of the page"><span>Permanent link</span></a></li><li id="t-info"><a href="/info216/index.php?title=Lab:_Getting_started_with_VSCode,_Python_and_RDFlib&amp;action=info" title="More information about this page"><span>Page information</span></a></li><li id="t-pagelog"><a href="/info216/index.php?title=Special:Log&amp;page=Lab%3A+Getting+started+with+VSCode%2C+Python+and+RDFlib"><span>Page logs</span></a></li></ul></div></div></div></div></div><div class="visualClear"></div></div></div>