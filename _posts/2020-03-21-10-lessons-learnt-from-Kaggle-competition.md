---
keywords: fastai
description: Lesson learnt from kaggle competition
title: Lesson learnt from Kaggle - Bengali Image Classification Competition
toc: true
branch: master
badges: true
comments: true
categories: [ML]
image: images/bengali_00_header.png
nb_path: _notebooks/2020-03-21-10-lessons-learnt-from-Kaggle-competition.ipynb
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2020-03-21-10-lessons-learnt-from-Kaggle-competition.ipynb
-->

<div class="container" id="notebook-container">
        
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">

</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I have teamed up with a friend to participate in the <a href="https://www.kaggle.com/c/bengaliai-cv19/?utm_medium=email&amp;utm_source=intercom&amp;utm_campaign=bengaliai-email-launch">Bengali Image Classification Competition</a>. We struggled to get a high rank in the Public leaderboard throughout the competition.  In the end, the result is a big surprise to everyone as the leaderboard shook a lot.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="https://github.com/noklam/mediumnok/blob/master/_notebooks/nb_img/bengali_0_public_lb.png?raw=true" alt="Public Leaderboard" title="Public Leaderboard has a much higher score, &gt;0.99 recall!"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="https://github.com/noklam/mediumnok/blob/master/_notebooks/nb_img/bengali_1_private_lb.png?raw=true" alt="Public Leaderboard" title="Note that the rank shook for over 1000!"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The final private score was much lower than the public score. It suggests that most participants are over-fitting Public leaderboard.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="The-Classification-Task">The Classification Task<a class="anchor-link" href="#The-Classification-Task"> </a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This is an image classification competition. We need to predict 3 parts of <strong>Bengali</strong> characters <code>root</code>, <code>consonant</code> and <code>vowel</code>. It is a typical classification tasks like the <strong>MNIST</strong> dataset.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="https://github.com/noklam/mediumnok/blob/master/_notebooks/nb_img/bengali_2_grapheme.png?raw=true" alt="Grapheme example" title="Examples of characters"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Evaluation-Metrics">Evaluation Metrics<a class="anchor-link" href="#Evaluation-Metrics"> </a></h2><p>The competition use macro-recall as the evaluation metric. In general, people get &gt;96% recall in training, the tops are even getting &gt;99% recall.</p>

</div>
</div>
</div>
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<details class="description">
      <summary class="btn btn-sm" data-open="Hide Code" data-close="Show Code"></summary>
        <p><div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># collapse-hide</span>
<span class="n">python</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">sklearn.metrics</span>

<span class="n">scores</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">component</span> <span class="ow">in</span> <span class="p">[</span><span class="s1">&#39;grapheme_root&#39;</span><span class="p">,</span> <span class="s1">&#39;consonant_diacritic&#39;</span><span class="p">,</span> <span class="s1">&#39;vowel_diacritic&#39;</span><span class="p">]:</span>
    <span class="n">y_true_subset</span> <span class="o">=</span> <span class="n">solution</span><span class="p">[</span><span class="n">solution</span><span class="p">[</span><span class="n">component</span><span class="p">]</span> <span class="o">==</span> <span class="n">component</span><span class="p">][</span><span class="s1">&#39;target&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>
    <span class="n">y_pred_subset</span> <span class="o">=</span> <span class="n">submission</span><span class="p">[</span><span class="n">submission</span><span class="p">[</span><span class="n">component</span><span class="p">]</span> <span class="o">==</span> <span class="n">component</span><span class="p">][</span><span class="s1">&#39;target&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>
    <span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">sklearn</span><span class="o">.</span><span class="n">metrics</span><span class="o">.</span><span class="n">recall_score</span><span class="p">(</span>
        <span class="n">y_true_subset</span><span class="p">,</span> <span class="n">y_pred_subset</span><span class="p">,</span> <span class="n">average</span><span class="o">=</span><span class="s1">&#39;macro&#39;</span><span class="p">))</span>
<span class="n">final_score</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">average</span><span class="p">(</span><span class="n">scores</span><span class="p">,</span> <span class="n">weights</span><span class="o">=</span><span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>
</p>
    </details>
</div>
    {% endraw %}

<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Model-(Bigger-still-better)">Model (Bigger still better)<a class="anchor-link" href="#Model-(Bigger-still-better)"> </a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We start with <code>xresnet50</code>, which is a relatively small model. As we have the assumption that this classification task is a very standard task, therefore the difference of model will not be the most important one. Thus we pick xresnet50 as it has a good performance in terms of accuracy and train relatively fast.</p>
<p>Near the end of the competition, we switch to a larger model <code>se-resnext101</code>. It requires triple training time plus we have to scale down the batch size as it does not fit into the GPU memory. Surprisingly (maybe not surprising to everyone), the bigger model did boost the performance more than I expected with ~0.3-0.5% recall. It is a big improvement as the recall is very high (~0.97), in other words, it reduces <strong>~10%</strong>  error solely by just using a better model, not bad!</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Augmentation">Augmentation<a class="anchor-link" href="#Augmentation"> </a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>There are never "enough" data for deep learning, so we always try our best to collect more data. Since we cannot collect more data, we need data augmentation.
We start with rotation + scale. We also find <strong>MixUp</strong> and <strong>CutMix</strong> is very effective to boost the performance. It also gives us roughly <strong>10%</strong> boost initially from 0.96 -&gt; 0.964 recall.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="CutMix-&amp;-MixUp"><a href="https://arxiv.org/abs/1905.04899">CutMix</a> &amp; <a href="https://arxiv.org/pdf/1710.09412.pdf">MixUp</a><a class="anchor-link" href="#CutMix-&amp;-MixUp"> </a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="https://github.com/noklam/mediumnok/blob/master/_notebooks/nb_img/bengali_3_data_aug.png?raw=true" alt="Example of Augmentation" title="Augmentation Example"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><em>Mixup</em> is simple, if you know about photography, it is similar to have double exposure of your photos. It overlays two images (cat+dog in this case) by sampling weights. So instead of prediction P(dog) = 1, the new target could become P(dog) = 0.8 and P(cat) = 0.2.</p>
<p><em>CutMix</em> shares a similar idea, instead of overlay 2 images, it crops out a certain ratio of the image and replaces it with another one.</p>
<p>It always surprises me that these augmented data does not make much sense to a human, but it is very effective to improve model accuracy and reduce overfitting empirically.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Logging-of-Experiment">Logging of Experiment<a class="anchor-link" href="#Logging-of-Experiment"> </a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I normally just log my experiment with a simple CSV and some printing message. This start to get tedious when there are more than 1 people to work. It is important to communicate the results of experiments. I explore <code>Hydra</code> and <code>wandb</code> in this competition and they are very useful.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Hydra"><a href="https://hydra.cc/">Hydra</a><a class="anchor-link" href="#Hydra"> </a></h2><p><img src="https://github.com/noklam/mediumnok/blob/master/_notebooks/nb_img/bengali_4_hydra.png?raw=true" alt="Hydra for configuration composition"></p>
<p>It is often a good idea to make your experiment configurable. We use <code>Hydra</code> for this purpose and it is useful to compose different configuration group.
By making your hyper-paramters configurable, you can define an experiment by configuration files and run multiple experiments. By logging the configuration with the training statistics, it is easy to do cross-models comparison and find out which configuration is useful for your model.</p>
<p>I have written <a href="https://mediumnok.ml/coding/ml/2020/02/08/Config-Composition-with-Hydra-for-Machine-Learning-Experiments.html">an short example</a> for how to use <strong>Hydra</strong>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Wandb"><a href="https://www.wandb.com/">Wandb</a><a class="anchor-link" href="#Wandb"> </a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>wandb</strong> (Weight &amp; Biases) does a few things. It provides built-in functions that automatically  log all your model statistics, you can also log your custom metrics with simple functions.</p>
<ul>
<li>Compare the configuration of different experiments to find out the model with the best performance.</li>
<li>Built-in function for logging model weights and gradient for debugging purpose.</li>
<li>Log any metrics that you want</li>
</ul>
<p>All of these combined to make collaboration experience better. It is really important to sync the progress frequently and getting everyone results in a single platform makes these conversations easier.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><img src="https://github.com/noklam/mediumnok/blob/master/_notebooks/nb_img/bengali_06.jpg?raw=true" alt="image.png" title="Screenshot of wandb UI for cross model comparison"></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Stochastic-Weight-Averaging"><a href="https://pytorch.org/blog/stochastic-weight-averaging-in-pytorch/">Stochastic Weight Averaging</a><a class="anchor-link" href="#Stochastic-Weight-Averaging"> </a></h1><p>This is a simple yet effective technique which gives about 0.3-0.4% boost to my model. In simple words, it takes <strong>snapshots</strong> of the model weights during training and takes an average at the end. It provides a cheap way to do models ensemble while you are only training 1 model. This is important for this competition as it allows me to keep training time short enough to allow feedback within hours and reduce over-fitting.)</p>
<h1><img src="https://github.com/noklam/mediumnok/blob/master/_notebooks/nb_img/bengali_5_swa.png?raw=true" alt="image.png" title="Stochastic Weight Averaging"></h1>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Larger-is-better-(image-size)">Larger is better (image size)<a class="anchor-link" href="#Larger-is-better-(image-size)"> </a></h1><p>We downsample our image size to 128x128 throughout the competition, as it makes the model train faster and we believe most technique should be transferable to larger image size. It is important to keep your feedback loop short enough (hours if not days). You want your training data as small as possible while keeping them transferable to your full dataset. Once we scale our image to full size, it takes almost 20 hours to train a single model, and we only have little chance to tune the hyper-parameters before the competition end.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Debug-&amp;-Checkpoint">Debug &amp; Checkpoint<a class="anchor-link" href="#Debug-&amp;-Checkpoint"> </a></h1><p>There was a time we develop our model separately and we didn't sync our code for a while. We refactor our code during the time and it was a huge mistake. It turns out our pre-refactor code trains much better model and we introduce some unknown bug. It is almost impossible to find out as we change multiple things. It is so hard to debug a neural network and testing it thoroughly  is important. Injecting a large amount of code may help you to run an experiment earlier, but you may pay much more time to debug it afterwards.</p>
<p>I think this is applicable even if you are working alone.</p>
<ul>
<li>Keep your changes small.</li>
<li>Establish a baseline early, always do a regression test after a new feature introduced (especially after code refactoring)</li>
<li>Create checkpoint to rollback anytime, especially if you are not working on it every day.</li>
</ul>
<p>Implementation is the key of Kaggle competition (in real life too). It does not matter how great your model is, a tiny little bug could have damaged your model silently</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Use-auxiliary-label">Use auxiliary label<a class="anchor-link" href="#Use-auxiliary-label"> </a></h1><p><img src="https://github.com/noklam/mediumnok/blob/master/_notebooks/nb_img/bengali_7.png?raw=true" alt="image.png" title="The extra grapheme label">
As mentioned earlier, this competition requires to predict the <code>root</code>, <code>vowel</code> and the <code>consonant</code> part. In the training data, they actually provide the <code>grapheme</code> too. Lots of people saying that if you train with the <code>grapheme</code>, it improves the model greatly and get the recall &gt;98% easily.</p>
<p>This is something we could not reproduce throughout the competition, we tried it in the very last minute but it does not seem to improve our model. It turns out lots of people are overfitting the data, as the testing dataset has much more unseen character.</p>
<p>But it is still a great remark that training with labels that is not your final desired output could still be very useful.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Weight-loss">Weight loss<a class="anchor-link" href="#Weight-loss"> </a></h1><p>The distribution of the training dataset is very imbalance, but to get a good result, we need to predict every single class accurately (macro recall). To deal with this issue, we choose to use class weights, where a higher weight would be applied to rare samples. We don't have an ablation study for this, but it seems to help close the gap between accuracy &amp; recall and allows us to train the model slightly better.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Find-a-teammate!">Find a teammate!<a class="anchor-link" href="#Find-a-teammate!"> </a></h1><p>Lastly, please go and find a teammate if you can. It is very common to start a Kaggle competition, but not so easy to finish them. I have stopped for a month during the competition due to my job. It is really hard to get back to the competition after you stopped for so long. Getting a teammate helps to motivate you and in the end, it is a great learning experience for both of us.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Pretrain-Model">Pretrain Model<a class="anchor-link" href="#Pretrain-Model"> </a></h1><p>We also tried to use a pretrained model, as it allows shorter training and gives better performance by transfer learning (Using weights learn from a large dataset to as initial weight). It also gives our model a bit of improvement.</p>
<ul>
<li>Finetune the model head, while keeping other layers freeze (except BatchNorm layer).</li>
<li>Unfreeze the model, train all the layers together.</li>
</ul>
<p>I also tried training the model directly with discriminating learning rate while not freezing any layer at all. It performs similarly  to freezing fine-tuning , so I end up just start training the entire model from the beginning.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="If-the-code-works,-don't-touch-it">If the code works, don't touch it<a class="anchor-link" href="#If-the-code-works,-don't-touch-it"> </a></h1><p>This is probably not a good habit usually, but I suggest not to do it for a competition. We spent lots of time for debugging our code after code refactoring and end up just rolling back to an older commit and cherry-picks new features. In a competition, you don't have enough time to test everything. You do not need a nice abstract class for all your features, some refactoring to keep your function/class clean is probably needed, but do not overspend your time on it. It is even common to jump between frameworks (you may find other's Kernel useful), so it is not possible to structure your code perfectly.</p>
<ul>
<li>If someone has create a working submission script, use it!</li>
<li>If someone has create a working pre-processing function, use it!</li>
</ul>
<p>Don't spend time on trying to optimize these code unless it is necessary, it is often not worth it in a competition context. You should focus on adding new features, trying out new model, testing with new augmentation technique instead.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Summary">Summary<a class="anchor-link" href="#Summary"> </a></h1><p>This is a great learning experience and refreshes  some of my outdated computer vision model knowledge. If you have never joined a competition, find a friend and get started. If you have just finished one, try writing it out and share your experience. ????</p>

</div>
</div>
</div>
</div>
 

