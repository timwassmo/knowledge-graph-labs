<div id="content" class="mw-body" role="main"><div class="mw-indicators mw-body-content">
</div>
<h1 id="firstHeading" class="firstHeading">Lab: RDF programming with RDFlib</h1><div id="bodyContentOuter"><div id="siteSub">From Info216</div><div id="mw-page-header-links"><div role="navigation" class="mw-portlet tools-inline" id="p-namespaces" aria-labelledby="p-namespaces-label"><h3 id="p-namespaces-label" lang="en" dir="ltr">Namespaces</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"><li id="ca-nstab-main" class="selected"><a href="/info216/index.php?title=Lab:_RDF_programming_with_RDFlib" title="View the content page [ctrl-option-c]" accesskey="c"><span>Page</span></a></li><li id="ca-talk" class="new"><a href="/info216/index.php?title=Talk:Lab:_RDF_programming_with_RDFlib&amp;action=edit&amp;redlink=1" rel="discussion" title="Discussion about the content page (page does not exist) [ctrl-option-t]" accesskey="t"><span>Discussion</span></a></li></ul></div></div><div role="navigation" class="mw-portlet tools-inline" id="p-more" aria-labelledby="p-more-label"><h3 id="p-more-label" lang="en" dir="ltr">More</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"><li id="ca-more" class="dropdown-toggle"><span>More</span></li><li id="ca-languages" class="dropdown-toggle"><span>Languages</span></li></ul></div></div><div role="navigation" class="mw-portlet tools-inline" id="p-views" aria-labelledby="p-views-label"><h3 id="p-views-label" lang="en" dir="ltr">Page actions</h3><div class="mw-portlet-body"><ul lang="en" dir="ltr"><li id="ca-view" class="selected"><a href="/info216/index.php?title=Lab:_RDF_programming_with_RDFlib"><span>Read</span></a></li><li id="ca-viewsource"><a href="/info216/index.php?title=Lab:_RDF_programming_with_RDFlib&amp;action=edit" title="This page is protected.
You can view its source [ctrl-option-e]" accesskey="e"><span>View source</span></a></li><li id="ca-history"><a href="/info216/index.php?title=Lab:_RDF_programming_with_RDFlib&amp;action=history" title="Past revisions of this page [ctrl-option-h]" accesskey="h"><span>History</span></a></li></ul></div></div></div><div class="visualClear"></div><div class="mw-body-content" id="bodyContent"><div id="contentSub"></div><div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><div class="mw-parser-output"><div id="toc" class="toc" role="navigation" aria-labelledby="mw-toc-heading"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none"><div class="toctitle" lang="en" dir="ltr"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#Topics"><span class="tocnumber">1</span> <span class="toctext">Topics</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Useful_materials"><span class="tocnumber">2</span> <span class="toctext">Useful materials</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Tasks"><span class="tocnumber">3</span> <span class="toctext">Tasks</span></a></li>
<li class="toclevel-1 tocsection-4"><a href="#If_you_have_more_time..."><span class="tocnumber">4</span> <span class="toctext">If you have more time...</span></a></li>
<li class="toclevel-1 tocsection-5"><a href="#Triples_you_can_extend_for_the_tasks_.28turtle_format.29"><span class="tocnumber">5</span> <span class="toctext">Triples you can extend for the tasks (turtle format)</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="Topics">Topics</span></h2>
<ul><li>RDF graph programming with RDFlib</li></ul>
<h2><span class="mw-headline" id="Useful_materials">Useful materials</span></h2>
<p>RDFLib:
</p>
<ul><li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://rdflib.readthedocs.io/en/stable/intro_to_creating_rdf.html">Creating Triples</a></li>
<li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://rdflib.readthedocs.io/en/stable/rdf_terms.html">RDF Terms</a></li>
<li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://rdflib.readthedocs.io/en/stable/namespaces_and_bindings.html">Namespaces and Bindings</a></li>
<li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://rdflib.readthedocs.io/en/stable/intro_to_graphs.html">Navigating Graphs</a></li>
<li><a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html">Serialising and parsing</a></li></ul>
<p>RDFlib classes/interfaces: 
</p>
<ul><li>from rdflib import Graph, Namespace, URIRef, BNode, Literal</li>
<li>from rdflib.namespace import RDF, FOAF, XSD</li>
<li>from rdflib.collection import Collection</li></ul>
<p>RDFlib methods: 
</p>
<ul><li>Graph: add(), remove(), triples(), serialize(), parse(), bind()</li></ul>
<h2><span class="mw-headline" id="Tasks">Tasks</span></h2>
<p>Continue with the graph you created in <a href="/info216/index.php?title=Lab:_Getting_started_with_VSCode,_Python_and_RDFlib" title="Lab: Getting started with VSCode, Python and RDFlib"> Exercise 1</a>.
</p><p><b>Task:</b> Continue to extend your graph:
</p>
<ul><li>Michael Cohen was Donald Trump's attorney.
<ul><li>He pleaded guilty for lying to Congress.</li></ul></li>
<li>Michael Flynn was adviser to Donald Trump.
<ul><li>He pleaded guilty for lying to the FBI.</li>
<li>He negotiated a plea agreement.</li></ul></li></ul>
<p>If you want, you can try to use properties and types from standard vocabularies like FOAF (friend-of-a-friend) and DC (Dublin Core), but this is something we will look at in later exercises.
</p><p><b>Task:</b> According to <a target="_blank" rel="nofollow noreferrer noopener" class="external text" href="https://www.pbs.org/wgbh/frontline/article/the-mueller-investigation-explained-2/">this FRONTLINE article</a>, Gates', Cohen's and Flynn's lying were different and are described in different detail. 
</p>
<ul><li>How can you represent "different instances of lying" as triples?</li>
<li>How can you modify your knowledge graph to account for this?</li></ul>
<p><b>Task:</b> It is possible to solve the task above without blank (or anonymous nodes). But to do so, you need to create a URI for each "instance of lying". This is a situation where blank nodes may be more suitable. Change your graph so it represents instances of lying as blank nodes.
</p><p><b>Task:</b> Save (<i>serialize</i>) your graph to a Turtle file. Add a few triples <i>to the Turtle file</i> with more information about Donald Trump. For example, you can add that Donald Trump is married to Melania and has several children. You can also use blank nodes to represent two of Trump's addresses when he was president:
</p>
<ul><li>The White House, 1600 Pennsylvania Ave., NW Washington, DC 20500, United States, phone: 1-202-456-1414</li>
<li>Mar-a-Lago Club, 1100 S Ocean Blvd, Palm Beach, FL 33480, United States</li></ul>
<p>Visualise the result if you want. Read (<i>parse</i>) the Turtle file back into a Python program, and check that the new triples are there.
</p>
<h2><span class="mw-headline" id="If_you_have_more_time...">If you have more time...</span></h2>
<p><b>Task:</b> Write a method (function) that starts with Donald Trump prints out a graph depth-first to show how the other graph nodes are connected to him. An excerpt of the output could be:
</p>
<pre>ex:Donald_Trump
    &lt;== ex:campaignManager ex:Paul_Manafort
        ==&gt; ex:convictedFor ex:BankAndTaxFraud
        ...
    &lt;== ex:attorneyFor ex:Michael_Cohen
        ==&gt; ex:pleadedGuilty ex:LyingToCongress
</pre>
<p>Here, the &lt;== and ==&gt; arrows are printed to indicate the reverse of a property. We do that with a <i>print()</i> statement in Python, not from inside rdflib. 
</p><p><i>Note:</i> Because you must follow triples in both subject-to-predicate and predicate-to-subject direction, you must keep a list of already visited nodes, and never return to a previously visited one.
</p><p><i>Note:</i> If you want a neat solution, it may be best to combine two graph traversals: first traverse the model breadth-first to create a new tree-shaped model, and then traverse the tree-shaped model depth-first to print it out with indentation. (The point of the first breadth-first step is to find the shortest path to each node.)
</p>
<h2><span id="Triples_you_can_extend_for_the_tasks_(turtle_format)"></span><span class="mw-headline" id="Triples_you_can_extend_for_the_tasks_.28turtle_format.29">Triples you can extend for the tasks (turtle format)</span></h2>
<pre class="code2highlight hljs css">@<span class="hljs-keyword">prefix</span> ex: &lt;http://example.org/&gt; .

ex:Mueller_Investigation ex:involved ex:George_Papadopoulos,
        ex:Michael_Cohen,
        ex:Michael_Flynn,
        ex:Paul_Manafort,
        ex:Rick_Gates,
        ex:Roger_Stone&nbsp;;
    <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:leadBy</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:Robert_Muller</span> .

<span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:Paul_Manafort</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:businessManager</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:Rick_Gates</span>&nbsp;;
    <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:campaignChairman</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:Donald_Trump</span>&nbsp;;
    <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:chargedWith</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:ForeignLobbying</span>,
        <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:MoneyLaundering</span>,
        <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:TaxEvasion</span>&nbsp;;
    <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:convictedFor</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:BankFraud</span>,
        <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:TaxFraud</span>&nbsp;;
    <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:negoiated</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:PleaBargain</span>&nbsp;;
    <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:pleadGuiltyTo</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:Conspiracy</span>&nbsp;;
    <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:sentencedTo</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:Prison</span> .

<span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:Rick_Gates</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:chargedWith</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:ForeignLobbying</span>,
        <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:MoneyLaundering</span>,
        <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:TaxEvasion</span>&nbsp;;
    <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:pleadGuiltyTo</span> <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:Conspiracy</span>,
        <span class="hljs-selector-tag">ex</span><span class="hljs-selector-pseudo">:LyingToFBI</span> .</pre>
<!-- 
NewPP limit report
Cached time: 20230509083218
Cache expiry: 86400
Dynamic content: false
Complications: []
CPU time usage: 0.024 seconds
Real time usage: 0.025 seconds
Preprocessor visited node count: 18/1000000
Post‐expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Highest expansion depth: 2/40
Expensive parser function count: 0/100
Unstrip recursion depth: 0/20
Unstrip post‐expand size: 802/5000000 bytes
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%    0.000      1 -total
-->

<!-- Saved in parser cache with key info216-mediawiki-:pcache:idhash:87-0!canonical and timestamp 20230509083218 and revision id 2039
 -->
</div></div><div class="printfooter">
Retrieved from "<a dir="ltr" href="https://wiki.app.uib.no/info216/index.php?title=Lab:_RDF_programming_with_RDFlib&amp;oldid=2039">https://wiki.app.uib.no/info216/index.php?title=Lab:_RDF_programming_with_RDFlib&amp;oldid=2039</a>"</div>
<div class="visualClear"></div></div></div></div>