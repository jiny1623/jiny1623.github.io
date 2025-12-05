---
permalink: /
title: "About Me"#"Academic Pages is a ready-to-fork GitHub Pages template for academic personal websites"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hello! I am a first-year Ph.D. student in Computer Science and Engineering at the University of Michigan, where I'm advised by Prof. [Lu Wang](https://web.eecs.umich.edu/~wangluxy/). Previously, I was an undergraduate researcher at the [Vision & Learning Lab](https://vision.snu.ac.kr/) at Seoul National University, advised by Prof. [Gunhee Kim](https://vision.snu.ac.kr/gunhee/). 

My primary research interests lie in natural language processing and machine learning, with a focus on developing adaptive and trustworthy AI systems that can operate reliably in dynamic environments. I work on:
  * Learning-to-critique with reinforcement learning for improving non-verifiable and long-horizon reasoning
  * Retrieval-augmented and data-centric adaptation for models facing evolving knowledge
  * Fine-grained evaluation frameworks that enable continual improvement and robust generalization

## CV
Here is my CV:
<a class="btn btn--primary" href="https://drive.google.com/file/d/1C44hPamECTSzpB5sXOgVjaMKfYzvm9-Y/view?usp=sharing" target="_blank" rel="noopener">Download CV (PDF)</a>
<span style="font-size:0.9em; margin-left:8px;">Updated {{ site.time | date: "%b %Y" }}</span>

## Current Research Projects   

### 1. Learning-to-Critique with Reinforcement Learning  
I explore reinforcement learning methods that enable models to *critique, revise, and refine* their own reasoning, especially in non-verifiable tasks where correctness is difficult to judge. My work investigates how models can generate structured feedback, self-evaluate intermediate steps, and improve through iterative critique loops, with the goal of building more reliable and interpretable reasoning systems.   

### 2. Retrieval-Augmented and Data-Centric Adaptation  
I study how AI systems can incorporate new or evolving knowledge through retrieval and data-centric methods. This includes understanding when models should rely on external information, how to handle shifting or conflicting sources, and how retrieval affects downstream reasoning. My research aims to improve robustness as real-world knowledge changes, without requiring expensive retraining.   

### 3. Fine-Grained Evaluation for Continual Improvement  
I develop evaluation frameworks that diagnose model behavior at a detailed level, capturing nuances in reasoning quality, factuality, and robustness across domains. These frameworks support continual model improvement by revealing where models struggle, what types of errors they make, and how their performance evolves under distribution shift.   

## Publications
<!-- ============== -->
* ### When Should Dense Retrievers Be Updated in Evolving Corpora? Detecting Out-of-Distribution Corpora Using GradNormIR   
  Dayoon Ko, **Jinyoung Kim**, Sohyeon Kim, Jinhyuk Kim, Jaehoon Lee, Seonghak Song, Minyoung Lee, Gunhee Kim   
  **ACL 2025 Findings**   
  [[paper]](https://arxiv.org/abs/2506.01877) [[code]](https://github.com/dayoon-ko/gradnormir)

* ### DynamicER: Resolving Emerging Mentions to Dynamic Entities for RAG   
  **Jinyoung Kim**, Dayoon Ko, Gunhee Kim   
  **EMNLP 2024**   
  [[paper]](https://arxiv.org/abs/2410.11494) [[code]](https://github.com/jiny1623/DynamicER)

* ### GrowOVER: How Can LLMs Adapt to Growing Real-World Knowledge?   
  Dayoon Ko, **Jinyoung Kim**, Hahyeon Choi, Gunhee Kim   
  **ACL 2024**   
  [[paper]](https://arxiv.org/abs/2406.05606) [[code]](https://github.com/dayoon-ko/GrowOVER)

<!-- * ### GradNormIR: Unsupervised Prediction of Document Retrieval Failure
  Dayoon Ko, **Jinyoung Kim**, Jinhyuk Kim, Jaehoon Lee, Seonghak Song, Minyoung Lee, Gunhee Kim   
  Submitted to ACL Rolling Review -->


## Education

* ### University of Michigan <span style="font-size:0.9em;">(Aug. 2025 - Present)</span>   
  **Ph.D.** student in Computer Science and Engineering

* ### Seoul National University <span style="font-size:0.9em;">(Mar. 2018 - Aug. 2024)</span>   
  <!-- <span style="font-size:0.9em;">(Leave of absence for military service: Jul. 2020 - Jan. 2022)</span>    -->
  Leave of absence for military service: Jul. 2020 - Jan. 2022   
  **B.S.** in Computer Science and Engineering & **B.A.** in Economics   
  Graduated with **Summa Cum Laude**   


  
## Experiences
* ### [Vision & Learning Lab](https://vision.snu.ac.kr/), SNU <span style="font-size:0.9em;">(Sep. 2023 - Present)</span>
  Research Intern
  * Conducted research on evolving knowledge and retrieval-augmented generation
  * Published 3 papers in top-tier conferences
  
* ### [CLOVA Voice & Avatar Team](https://clova.ai/speech/en), NAVER <span style="font-size:0.9em;">(Jan. 2023 - Feb. 2023)</span>     
  Machine Learning Researcher
  * Topic: Unified Accent Estimation for Speech Synthesis
  * Achieved 7.8% improvement in Accent Phrase (AP) prediction accuracy by unifying estimation for AP and Accent Nucleus (AN) boundaries
  * Designed and implemented novel AN decoder framework to address challenges in the long-tail distribution of accent estimation
* ### [Music & Audio Research Group](https://snu-marg.notion.site/MARG-091390162ca941f4b88f64d47d2c4e87), SNU <span style="font-size:0.9em;">(Jul. 2022 - Aug. 2022)</span> 
  Research Intern
  * Conducted research on personalized symbolic music generation
  * Developed contrastive learning-based encoder and holistic frameworks for emotion and style conditioning in music generation

## Leadership Experiences

* ### Squad Leader, [Korean Augmentation to the US Army](https://en.wikipedia.org/wiki/Korean_Augmentation_to_the_United_States_Army) <span style="font-size:0.9em;">(Jul. 2020 - Jan. 2022)</span> 
  Sergeant, 176th Financial Management Support Unit, Eight Army

<!-- ### Devsisters
*Machine Learning Engineer*  
<span style="font-size:0.9em;">Sep 2018 - Sep 2020</span>  
&nbsp;&nbsp;&nbsp;&nbsp;Worked as part of the mandatory military service in the Republic of Korea

### Ace Project
*Software Engineer*  
<span style="font-size:0.9em;">Sep 2017 - Aug 2018</span>  
&nbsp;&nbsp;&nbsp;&nbsp;Worked as part of the mandatory military service in the Republic of Korea -->


<!-- This is the front page of a website that is powered by the [Academic Pages template](https://github.com/academicpages/academicpages.github.io) and hosted on GitHub pages. [GitHub pages](https://pages.github.com) is a free service in which websites are built and hosted from code and data stored in a GitHub repository, automatically updating when a new commit is made to the respository. This template was forked from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/) created by Michael Rose, and then extended to support the kinds of content that academics have: publications, talks, teaching, a portfolio, blog posts, and a dynamically-generated CV. You can fork [this repository](https://github.com/academicpages/academicpages.github.io) right now, modify the configuration and markdown files, add your own PDFs and other content, and have your own site for free, with no ads! An older version of this template powers my own personal website at [stuartgeiger.com](http://stuartgeiger.com), which uses [this Github repository](https://github.com/staeiou/staeiou.github.io).

A data-driven personal website
======
Like many other Jekyll-based GitHub Pages templates, Academic Pages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
2. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
3. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
4. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
5. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
6. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful. -->
