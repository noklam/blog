---
keywords: fastai
description: Do you know what differentiate a Powerpoint prepared by data scientist and a Business Analyst? Your Charts! But not the good way.
title: Beyond Unit Testing - What is Property-based Testing?
toc: true 
badges: true
comments: true
categories: [python]
hide: true
nb_path: _notebooks/2020-04-12-Property-based-testing-in-Python.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2020-04-12-Property-based-testing-in-Python.ipynb
-->

<div class="container" id="notebook-container">
        
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<details class="description">
      <summary class="btn btn-sm" data-open="Hide Code" data-close="Show Code"></summary>
        <p><div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#collapse-hide</span>
<span class="c1"># https://hypothesis.readthedocs.io/en/latest/quickstart.html</span>
<span class="o">!</span>pip install hypothesis 
<span class="o">%</span><span class="k">load_ext</span> ipython_pytest
</pre></div>

    </div>
</div>
</div>
</p>
    </details>
<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>Requirement already satisfied: hypothesis in c:\programdata\anaconda3\lib\site-packages (5.8.1)
Requirement already satisfied: sortedcontainers&lt;3.0.0,&gt;=2.1.0 in c:\programdata\anaconda3\lib\site-packages (from hypothesis) (2.1.0)
Requirement already satisfied: attrs&gt;=19.2.0 in c:\programdata\anaconda3\lib\site-packages (from hypothesis) (19.2.0)
The ipython_pytest extension is already loaded. To reload it, use:
  %reload_ext ipython_pytest
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Unit Testing is a common technique for software engineering. Even if you are not writing a unit test explicitly, you are still doing unit testing, as your function should at least works for what you intended. You give an input <em>x</em> to a function, it should return <em>y</em>, simple as that.</p>
<p>For example, imagine we have a function like this.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">add_ints</span><span class="p">(</span><span class="n">x1</span><span class="p">,</span> <span class="n">x2</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">x1</span> <span class="o">+</span> <span class="n">x2</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Case 1</span>
<span class="n">add_ints</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">



<div class="output_text output_subarea output_execute_result">
<pre>2</pre>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Case 2</span>
<span class="n">add_ints</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="s1">&#39;2&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-intense-fg ansi-bold">---------------------------------------------------------------------------</span>
<span class="ansi-red-intense-fg ansi-bold">TypeError</span>                                 Traceback (most recent call last)
<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-59-99ea9d9c8984&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-fg">      1</span> <span class="ansi-red-intense-fg ansi-bold"># Case 2</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 2</span><span class="ansi-yellow-intense-fg ansi-bold"> </span>add_ints<span class="ansi-yellow-intense-fg ansi-bold">(</span><span class="ansi-cyan-intense-fg ansi-bold">1</span><span class="ansi-yellow-intense-fg ansi-bold">,</span><span class="ansi-blue-intense-fg ansi-bold">&#39;2&#39;</span><span class="ansi-yellow-intense-fg ansi-bold">)</span>

<span class="ansi-green-intense-fg ansi-bold">&lt;ipython-input-57-d4599be2ffda&gt;</span> in <span class="ansi-cyan-fg">add_ints</span><span class="ansi-blue-intense-fg ansi-bold">(x1, x2)</span>
<span class="ansi-green-fg">      1</span> <span class="ansi-green-intense-fg ansi-bold">def</span> add_ints<span class="ansi-yellow-intense-fg ansi-bold">(</span>x1<span class="ansi-yellow-intense-fg ansi-bold">,</span> x2<span class="ansi-yellow-intense-fg ansi-bold">)</span><span class="ansi-yellow-intense-fg ansi-bold">:</span>
<span class="ansi-green-intense-fg ansi-bold">----&gt; 2</span><span class="ansi-yellow-intense-fg ansi-bold">     </span><span class="ansi-green-intense-fg ansi-bold">return</span> x1 <span class="ansi-yellow-intense-fg ansi-bold">+</span> x2

<span class="ansi-red-intense-fg ansi-bold">TypeError</span>: unsupported operand type(s) for +: &#39;int&#39; and &#39;str&#39;</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Case 3</span>
<span class="n">add_ints</span><span class="p">(</span><span class="s1">&#39;2&#39;</span><span class="p">,</span> <span class="s1">&#39;2&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The first two cases are expected behaviors, but the last case is a side-effect of how Python works. We should probably checks the input are numbers, otherwise we should throw error explicitly. Now, checking function behave properly with intend use is easy, to test the opposite is much harder. You have to test a lot of edge case, which is much harder and make your test verbose.</p>
<p>In this article, I will introduce a library called <code>Hypothesis</code> that does property-based testing. If none of this make sense to you, please bare with me, I will explain with simple examples. I found the name of <code>Hypothesis</code> and property-based testing isn't adding a lot of information, but they are useful.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>Hypothesis</strong> comes in handy that it generated artificial input to make your test fails. Instead of specifying an input, you specify what kind of input you want to test loosely. For example, if you expect your input is number, often you may want to test when the value is negative, positive, a floating point number, or if it exceeds certain range. This list of condition can expands quickly, and <strong>Hypothesis</strong> make this easier.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Start-with-a-simple-function">Start with a simple function<a class="anchor-link" href="#Start-with-a-simple-function"> </a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Let's stick with our simple <code>add_ints</code> function above. To keep it simple, let test for this 3 cases first.</p>
<ol>
<li>Adding two number -&gt; Expect Pass</li>
<li>Adding number and string -&gt; Expect Fail</li>
<li>Adding two number -&gt; Expect Fail</li>
</ol>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%</span><span class="k">pytest</span> 
# ipython magic to run pytest within a cell. This whole blog is written in a Jupyter Notebook!
# https://github.com/akaihola/ipython_pytest/blob/master/ipython_pytest.py

import pytest

def add_ints(x1, x2):
    return x1 + x2

def test_add_ints():
    assert add_ints(1,1) == 2

@pytest.mark.xfail()
def test_add_ints_fail():
    assert add_ints(1,&#39;2&#39;)

@pytest.mark.xfail(strict=True)
def test_add_ints_string():
    assert add_ints(&#39;2&#39;, &#39;2&#39;)
    
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
rootdir: C:\Users\CHANNO\AppData\Local\Temp\tmp79u2a6x6
plugins: hypothesis-5.8.1, arraydiff-0.3, doctestplus-0.4.0, openfiles-0.4.0, remotedata-0.3.2
collected 3 items

_ipytesttmp.py .xF                                                       [100%]

================================== FAILURES ===================================
____________________________ test_add_ints_string _____________________________
[XPASS(strict)] 
=================== 1 failed, 1 passed, 1 xfailed in 0.12s ====================
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In <code>pytest</code>, you can use a mark <code>@pytest.mark.xfail</code> to annotate a function is expected to fail the test. We have 1 pass, 1xfailed, 1 failed.</p>
<p><code>_ipytesttmp.py .xF</code>
indicates the last test is failed. Let's try to fix it by throwing an error is input type is not a number.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%</span><span class="k">pytest</span> 
# ipython magic to run pytest within a cell. This whole blog is written in a Jupyter Notebook!
# https://github.com/akaihola/ipython_pytest/blob/master/ipython_pytest.py

import pytest

def add_ints(x1, x2):
    if isinstance(x1, int) and isinstance(x2, int):
        return x1 + x2
    else:
        raise TypeError(f&#39;Make sure your input is a number x1 {type(x1)}, x2 {type(x2)}&#39;)
    

def test_add_ints():
    assert add_ints(1,1) == 2

@pytest.mark.xfail()
def test_add_ints_fail():
    assert add_ints(1,&#39;2&#39;)

@pytest.mark.xfail(strict=True)
def test_add_ints_string():
    assert add_ints(&#39;2&#39;, &#39;2&#39;)
    
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
rootdir: C:\Users\CHANNO\AppData\Local\Temp\tmpfrh2uipy
plugins: hypothesis-5.8.1, arraydiff-0.3, doctestplus-0.4.0, openfiles-0.4.0, remotedata-0.3.2
collected 3 items

_ipytesttmp.py .xx                                                       [100%]

======================== 1 passed, 2 xfailed in 0.10s =========================
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Okay, now we checks if input are integers. In reality, this if often an iterative process. You start with coming up with test cases, then every now and then, you hit some edge cases and you add that into your collections of test cases.</p>
<p>How can we make out test cases more robust to input? <code>Hypothesis</code> is exactly the tool you need.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="strategy,-your-auto-genenerated-input-for-unit-test"><code>strategy</code>, your auto-genenerated input for unit test<a class="anchor-link" href="#strategy,-your-auto-genenerated-input-for-unit-test"> </a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><code>strategy</code> is your input for unit test. Instead of specify a number, or a string, you specify what kind of input you want, and <code>Hypothesis</code> wouuld take care the rest of it. You can even composite different <code>strategies</code> to form more complicated input.</p>
<p>But let's keep it simple, we would just use integer for this demo.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">hypothesis</span> <span class="kn">import</span> <span class="n">strategies</span> <span class="k">as</span> <span class="n">st</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%</span><span class="k">pytest</span> 
# ipython magic to run pytest within a cell. This whole blog is written in a Jupyter Notebook!
# https://github.com/akaihola/ipython_pytest/blob/master/ipython_pytest.py

import pytest
from hypothesis import given
from hypothesis import strategies as st

def add_ints(x1, x2):
    if isinstance(x1, int) and isinstance(x2, int):
        return x1 + x2
    else:
        raise TypeError(f&#39;Make sure your input is a number x1 {type(x1)}, x2 {type(x2)}&#39;)
    
@given(st.integers(), st.integers())
def test_add_ints(x1, x2):
    assert add_ints(x1, x2)
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
rootdir: C:\Users\CHANNO\AppData\Local\Temp\tmpmdbi_h6f
plugins: hypothesis-5.8.1, arraydiff-0.3, doctestplus-0.4.0, openfiles-0.4.0, remotedata-0.3.2
collected 1 item

_ipytesttmp.py F                                                         [100%]

================================== FAILURES ===================================
________________________________ test_add_ints ________________________________

    @given(st.integers(), st.integers())
&gt;   def test_add_ints(x1, x2):

_ipytesttmp.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

x1 = 0, x2 = 0

    @given(st.integers(), st.integers())
    def test_add_ints(x1, x2):
&gt;       assert add_ints(x1, x2)
E       assert 0
E        +  where 0 = add_ints(0, 0)

_ipytesttmp.py:16: AssertionError
--------------------------------- Hypothesis ----------------------------------
Falsifying example: test_add_ints(
    x1=0, x2=0,
)
============================== 1 failed in 0.30s ==============================
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The test was simple, as should pass as long as no error was thrown. Look what <code>Hypothesis</code> found, it found when both x1, x2=0, the assertion will fail, because we are asserting 0 + 0 = 0, thus evaluated as False in Python.</p>
<p>Hence, I modified my test to not assert anything, it should just keep silent as long as no error is thrown.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nd">@given</span><span class="p">(</span><span class="n">st</span><span class="o">.</span><span class="n">integers</span><span class="p">(),</span> <span class="n">st</span><span class="o">.</span><span class="n">integers</span><span class="p">())</span>
<span class="k">def</span> <span class="nf">test_add_ints</span><span class="p">(</span><span class="n">x1</span><span class="p">,</span> <span class="n">x2</span><span class="p">):</span>
    <span class="k">assert</span> <span class="n">add_ints</span><span class="p">(</span><span class="n">x1</span><span class="p">,</span> <span class="n">x2</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="o">%%</span><span class="k">pytest</span> 
# ipython magic to run pytest within a cell. This whole blog is written in a Jupyter Notebook!
# https://github.com/akaihola/ipython_pytest/blob/master/ipython_pytest.py

import pytest
from hypothesis import given
from hypothesis import strategies as st

def add_ints(x1, x2):
    if isinstance(x1, int) and isinstance(x2, int):
        return x1 + x2
    else:
        raise TypeError(f&#39;Make sure your input is a number x1 {type(x1)}, x2 {type(x2)}&#39;)
    
@given(st.integers(), st.integers())
def test_add_ints(x1, x2):
    add_ints(x1, x2)
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_stream output_stdout output_text">
<pre>============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0
rootdir: C:\Users\CHANNO\AppData\Local\Temp\tmpwicd08ny
plugins: hypothesis-5.8.1, arraydiff-0.3, doctestplus-0.4.0, openfiles-0.4.0, remotedata-0.3.2
collected 1 item

_ipytesttmp.py .                                                         [100%]

============================== 1 passed in 0.25s ==============================
</pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Yes, now our test finally pass.</p>

</div>
</div>
</div>
</div>
 

