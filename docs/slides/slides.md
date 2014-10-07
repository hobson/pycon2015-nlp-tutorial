% title: Practical Natural Language Processing
% subtitle: PyCon 2015, Montreal
% subtitle: <i><small>April, 2015</small></i>
% author: <a href="https://github.com/hobson">Hobson Lane</a>
% copyright: Sharp Laboratories of America
% thankyou: Thank you <a href="https://www.sharplabs.com">Sharp Labs!</a>
% thankyou_details: for being <strong>awesome</strong> and contributing to open source...
% contact: PDX Python's <a href="https://github.com/pug/pug">pug</a>
% contact: Steven Skoczen's <a href="http://github.com/skoczen/will">will</a>
% contact: Steven Bird's <a href="https://github.com/nltk">nltk</a>
% contact: Mike Bostock's <a href="http://d3js.org">D3</a>
% favicon: http://hobson.github.io/pycon2015-nlp-tutorial/favicon.ico

---
title: Audience Survey
build_lists: true

* Who has done Natural Language Processing?
    - Stats?  ML?  Parsing?
    - Worked with Large Data Sets? DBs or ORMs?
        + `postgres`, `mysql`, `neo4j`, `sqlite`, `django`
* Used other tools for NLP?
    - grep, sed, awk, cut?
* NLP (Natural Language Processing) using Python?
    - `nltk`, `scrapy`, `numpy`, `fuzzywuzzy`, `collections.Counter`


---
title: What is "natural language"

* System of symbols and utterances developed by humans over millions of years.
* Unstructured text is a generalization of natural language text and the terms are often used interchangeably
* Natural language is often embedded in structured text (formal languages)
* XML, YAML, SQL, and of course **Python**
* variables, elements, names, strings, files, streams
* Example semi-structured, semi-formal language challenges:
* Parse HTML tag contents
* When is PyCon?  "<title>PyCon 2015 in Montréal | April 8th – April 16th</title>""

---
title: What is "natural language" (cont.)

* Parse a textbook or Wikipedia article with headings, page numbers, footnotes, etc
* social network feed (twitter, facebook, ), e.g. "Brushed my teeth today"
* legal contract, license agreement, EULA, annual report, patent
* "By checking this box you sign away your rights to sue us."
* Scrape every other row in an HTML table (e.g. your Facebook page)
* More challenging, less-standardized NLP
* Notes to yourself
* "Don't forget to take Plato for a walk tomorrow"
* Chat room or forum messages

---
title: What is "natural language" (cont.)

* "OMG dont be sucha troll!!!"
* Extract numbers and prices and their "units" of measure
* "200 pythonistas", "$50K per year", "1 GB"
* Nonexamples
* and CSS tags
* python script (but some strings within it may be NL)
* file (but some strings within the fields may be NL)
* mathematical equations (but the integers and fractions within it can be processed as NL)
* a database (but the names of the fields and tables may be processed as NL)

---
title: What is natural language processing

* Computer processing of languages to do something useful or fun
* Story about the genesis of _information theory_ and introduction to concepts Applicable to NLP:
* entropy
* coding
* decoding
* compression
* encryption
* channel capacity

---
title: What is natural language processing (cont.)

* distance metrics
* dimensionality

---
title: Why is natural language processing useful and fun

* Example applications
* a. sentiment analysis of customer service data (SAP)
* b. sentiment analysis for trend and finance prediction on twitter and other news feeds (Thomson Reuters)
* Reuters provides a low-latency feed to hedge funds containing a single bit associated with a stock symbol -- positive or negative impact on price
* c. hardware performance trends based on technician inspection comments (Sharp Electronics Corporation)
* d. enable artificial intelligence agents to train/teach themselves (CMU's NELL)
* e. data migration (ETL) between bodies of structured text like CSV, HTML tables to save the planet (DOE and Building Energy)
* f. example processing of memoirs for psychoanalysis: Stephen Fry's autobiography and its [open API + metadata](http://yourfry.com/)

---
title: Is NLP related to AI?

* Turing defined it as being able to imitate a human's ability to converse in  natural language text
* In some ways coding languages, structured text, and data structures, are just a subset or specialization of natural languages (because they are meant to be written and read by humans *AND* machines)
* semantic processing (state of the art NLP) extracts knowledge or meaning from text
* Speech recognition + NLP can often produce effective AI (e.g. Liza 2.0)

---
title: Context:

* What is _context_?
* Why is it important?
* Some common layers of context and meaning
* word (the "meaning" of syllables depends on the word they are used in)
* compound word ("boot" means something different in "bootstrap" and "boot up")
* phrase (noun-phrases are particularly "atomic")
* sentence (a sentence can often be presumed to have some grammatically-required elements like a noun and a verb)
* paragraph (paragraphs often have an intro, body, conclusion with different word usage assumptions)

---
title: Context: (cont.)

* passage (quotes, excerpts)
* page (text often will refer to images or quotes on the same page, like "see above")
* section (topics are changed between sections of an article or book)
* chapter (authors change viewpoint/location/subject between chapters)
* book (terms and symbols used in a dictionary may only be relevant there)
* corpus (a subset of language usages will always have sample biases)
* language ("taco" means something different in English than in Spanish)
* tribe/city/region ("Zoobombing" means something completely different in Portland than in a war zone)
* nation (culture)

---
title: Context: (cont.)

* planet (yes, projects like SETI are very concerned with NLP of ET languages)

---
title: Teasers: Algorithms Behind Some Popular NLP Packages

* sluggify.sluggify
* Foundation: str.split(), str.strip(), str.replace()
* Uses: Django url composition
* slugify(u"Awesome:*lol*resume'=B", max_length=15, word_boundary=True)
* 'awesome-lol-b'
* dateutils.parser.parse
* Foundation: Regular expressions
* Uses: Google Calendar, Remember The Milk

---
title: Teasers: Algorithms Behind Some Popular NLP Packages (cont.)

* parse('fri')
* datetime.datetime(2015, 4, 10, 0, 0)
* fuzzywuzzy.process
* Foundation: Levenshtein Edit Distance, `difflib`
* Uses: Building Energy data ETL
* process.extractOne("mess with", ["nuke", "talk", "surrender"])[0]
* ('talk', 29)

---
title: Break

* Available to help "offline"

---
title: Tools and techniques for identifying "style" or "context"

* Sentiment and mood metrics
* Style distance metrics for comparison of a text to that of famous authors like Hemmingway, Shakespeare, US presidents,
* Techniques
* vocabulary breadth
* vocabulary statistics relative to "standard vocabularies" or age-group vocabularies from education material
* vacabulary evolution over the course of a document
* structure (vocabulary shifts within a document for each of the context layers discussed previously)

---
title: Acquiring a Corpus

* using `nltk` to download text corpora (text documents or strings)
* extracting text and semi-structure text (tables) from web pages using Scrapy and Beautiful Soup
* encoding issues and python 2 vs 3: what has changed and how to use the best of python 3 with python 2 NLP tools
* `unicode()` vs `str()` vs `repr()`
* `from __future__ import unicode_literals`
* check user-supplied corpus  with some common tools for "quantifying" and structuring unstructured text

---
title: Frequency analysis of US President inaugural speeches

* segmentation/tokenization/parsing
* characters (encoding issues, some natural languages like Japanese Kanji and Chinese don't have "letters")
* words
* digits and symbols and unicode as part of words
* punctuation at the end of sentences and word
* hyphenation
* typos
* spelling variations (British English)

---
title: Frequency analysis of US President inaugural speeches (cont.)

* language variations (Spanish, French, slang)
* bag-of-words counting (frequency analysis) ignores context at any layer above the "documents"
* agnostic counting
* stemming
* nltk stemmers
* counting
* Data structures like `collections.Counter` that discard context/order
* Can `collections.OrderedDict` be used to preserve context and order? (not easily)
* normalization of counts/frequencies/probabilities

---
title: Frequency analysis of US President inaugural speeches (cont.)

* occurrence matrices ("word space" or "word vector space" in information theory)
* uses for word-word, word-document, document-word, and document-document matrices
* "word space" is a way of giving words a distance metric, from each other as individuals and as collections of words (documents)
* Leventshtein distance
* Distance
* statistical (frequency) word space
* `nltk.metrics.distance.jaccard_distance`
* `nltk.metrics.distance.masi_distance`
* `nltk.metrics.distance.presence`

---
title: Frequency analysis of US President inaugural speeches (cont.)

* direct semantic word space (we'll talk about WordNet later)
* syntactic/gramatical word space (we'll talk about POS tagging later)
* statistical nltk distance measures/metrics:
* complexity/entropy/information measures for unstructured text
* a. compression ratio
* b. entropy
* c. predictability (human trials by Claude Shannon et al.)

---
title: Dimension reduction

* occurrence matrices will grow to become impractical
* 100k words/tokens counted across 10k documents = 1 GB of data, if stored efficiently
* ignoring "stop words" and low-information-content words won't significantly reduce the dimensions
* many machine learning algorithms are impractical at this scale:
* decision trees
* KNN
* K-means
* Support vector machines

---
title: Dimension reduction (cont.)

* can reduce the dimensions and enable many powerful machine learning algorithms to be employed
* When SVD is impractical (e.g. 100k x 100k matrices or larger), dimension reduction can be based on the entropy found in each word and document independent of the others
* ntlk US inaugural presidential speech word-frequency example
* raw occurrence matrices
* reduced-dimension occurrence matrices
* d3 visualizations of occurrence matrices
* as "checkerboard" grids or heat-maps
* as graphs or networks (D3 force-directed graph)

---
title: Break

* Available to help "offline"

---
title: Getting Fuzzy

* regular expressions
* examples for use in a chat bot
* examples for use in a crawler for financial information
* what they're good at (semi-structured text) and what their not good for (not robust/reliable)
* `fuzzywuzzy` (uses "quick" Levenshtein distance)
* examples for matching database table/column names
* when you need the "best" match and you need it fast
* fuzzy regular expressions (`regex` package)

---
title: Getting Fuzzy (cont.)

* example use in a chatbot (`will`)
* when you want the very "best match" and you can wait

---
title: Jargon and typo consolidation

* Tell a story about the need for word consolidation (vocab dimension reduction) at Sharp Electronics to interpret multilingual, jargony, and abbreviation-filled natural language repair technician notes
* word distance metrics (Levenshtein)
* which word is the "canonical" form among a list of typos
* sorting by frequency
* sorting by word length
* iterative loosening of fuzziness threshold
* use of dictionaries and word graphs (WordNet, ConceptNet) to find the "root" of a word
* example usages o

---
title: Parsing structured data to create small , context-specific databases of knowledge for use in NLP information extraction from unstructured text

* extracting tabular data automatically from a web page (using Scrapy)
* automatic-identification of table "schema" using frequency analysis
* parsing a natural language database table query and producing a natural language response (i.e. how Wolfram Alpha does it)

---
title: Natural language processing of search queries

* composing logical statements from natural language
* state of the art in semantic parsing of sentences
* word order to tag words with POS and context

---
title: Break

* Available to help "offline"

---
title: Knowledge extraction

* date/time information using python-dateutil
* `will` example "remind me to knock off at 5"
* regexes to extract prices

---
title: Sentiment analysis to gauge chat room "mood"

* Applications of sentiment analysis
* financial analytic forecasting
* social network research and traffic/mood manipulation
* advertising
* consumer feedback processing
* movie, music, book review processing and triage
* will` chatbot example using nltk
* gage the mood and civility of your chat room

---
title: Sentiment analysis to gauge chat room "mood" (cont.)

* long term "culture" tracking
* identifying the mood of individual chatroom members

---
title: Sentence structure

* `nltk` POS tagging tools and examples
* grammar analysis and checking
* using POS to aid in information/knowledge extraction

---
title: Semantic processing

* `nltk` <-> `WordNet` interface
* analyze and visualize the semantic network for the participant-supplied text
* use NLTK to populate a simple knowledge base about you based on your hard drive contents

---
title: Metadata


* Lines: 222
* Pages: 34
* Tokens: 2275
* Sentences: 27
* Vocabulary: 788
* Time: 4:25

---
title: Contributors

* Hobson Lane <pugauthors@totalgood.com>
* LiZhong Zheng <lizhong@MIT.edu>
* Your Name Here ;) <pugauthors@totalgood.com>



