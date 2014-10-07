
---
title: What is natural language
footer: (10.0 min)
* a system of utterances invented by humans "spontaneously" over millions of years.* unstructured text is a generalization of natural language text and the terms are often used interchangeably* natural language is often embedded in structure text (formal languages), like HTML, XML, YAML, SQL, and of course Python as the content of variables, elements, or strings* Examples (why NLP is challenging):* HTML tag contents, e.g. the "PyCon 2015..." in <title>PyCon 2015 in Montréal | April 8th – April 16th</title>* A textbook, encyclopedia or Wikipedia articles with headings, page numbers, footnotes, etc* A social network feed (twitter, facebook, ), e.g. "Brushed my teeth today"* A legal contract, license agreement (EULA), annual report, patent "By checking this box you sign away your rights to sue us."* Notes to yourself: "Don't forget to take Plato for a walk"* Chat room correspondence: "OMG dont be sucha troll!!!"* Numbers and prices (e.g. "200 pythonistas", "$50K per year", "1 GB")* Nonexamples* HTML and CSS tags* python script (but some strings within it may be NL)* A CSV file (but some strings within the fields may be NL)* mathematical equations (but the integers and fractions within it can be processed as NL)* a database (but the names of the fields and tables may be processed as NL)
---
title: What is natural language processing
footer: (15.0 min)
* Computer processing of languages to do something useful or fun* Story about the genesis of _information theory_ and introduction to concepts Applicable to NLP:* entropy* coding* decoding* compression* encryption* channel capacity
---
title: Why is natural language processing useful and fun
footer: (15.0 min)
* Example applications* a. sentiment analysis of customer service data (SAP)* b. sentiment analysis for trend and finance prediction on twitter and other news feeds (Thomson Reuters)* Reuters provides a low-latency feed to hedge funds containing a single bit associated with a stock symbol -- positive or negative impact on price* c. hardware performance trends based on technician inspection comments (Sharp Electronics Corporation)* d. enable artificial intelligence agents to train/teach themselves (CMU's NELL)* e. data migration (ETL) between bodies of structured text like CSV, HTML tables to save the planet (DOE and Building Energy)* f. example processing of memoirs for psychoanalysis: Stephen Fry's autobiography and its [open API + metadata](http://yourfry.com/)
---
title: What does artificial intelligence have to do with NLP
footer: (5.0 min)
* Turing defined it as being able to imitate a human's ability to converse in  natural language text* In some ways coding languages, structured text, and data structures, are just a subset or specialization of natural languages (because they are meant to be written and read by humans *AND* machines)* semantic processing (state of the art NLP) extracts knowledge or meaning from text
---
title: Context:
footer: (5.0 min)
* what is context* why is it important?* Some common layers of context and meaning* word (the "meaning" of syllables depends on the word they are used in)* compound word ("boot" means something different in "bootstrap" and "boot up")* phrase (noun-phrases are particularly "atomic")* sentence (a sentence can often be presumed to have some grammatically-required elements like a noun and a verb)* paragraph (paragraphs often have an intro, body, conclusion with different word usage assumptions)* passage (quotes, excerpts)* page (text often will refer to images or quotes on the same page, like "see above")* section (topics are changed between sections of an article or book)* chapter (authors change viewpoint/location/subject between chapters)* book (terms and symbols used in a dictionary may only be relevant there)* corpus (a subset of language usages will always have sample biases)* language ("taco" means something different in English than in Spanish)* tribe/city/region ("Zoobombing" means something completely different in Portland than in a war zone)* nation (culture)* planet (yes, projects like SETI are very concerned with NLP of ET languages)
---
title: Tools and techniques for identifying "style" or "context"
footer: (15.0 min)
* Sentiment and mood metrics* Style distance metrics for comparison of a text to that of famous authors like Hemmingway, Shakespeare, US presidents,* Techniques* vocabulary breadth* vocabulary statistics relative to "standard vocabularies" or age-group vocabularies from education material* vacabulary evolution over the course of a document* structure (vocabulary shifts within a document for each of the context layers discussed previously)
---
title: Break
footer: (10 min)
* Will help those having trouble getting the examples so far to work in their environment
---
title: Acquiring a Corpus
footer: (14.0 min)
* using `nltk` to download text corpora (text documents or strings)* extracting text and semi-structure text (tables) from web pages using Scrapy and Beautiful Soup* encoding issues and python 2 vs 3: what has changed and how to use the best of python 3 with python 2 NLP tools* `unicode()` vs `str()` vs `repr()`* `from __future__ import unicode_literals`* check user-supplied corpus  with some common tools for "quantifying" and structuring unstructured text
---
title: Frequency analysis of US President inaugural speeches
footer: (20.0 min)
* segmentation/tokenization/parsing* characters (encoding issues, some natural languages like Japanese Kanji and Chinese don't have "letters")* words* digits and symbols and unicode as part of words* punctuation at the end of sentences and word* hyphenation* typos* spelling variations (British English)* language variations (Spanish, French, slang)* bag-of-words counting (frequency analysis) ignores context at any layer above the "documents"* agnostic counting* stemming* nltk stemmers* counting* Data structures like `collections.Counter` that discard context/order* Can `collections.OrderedDict` be used to preserve context and order? (not easily)* normalization of counts/frequencies/probabilities* occurrence matrices ("word space" or "word vector space" in information theory)* uses for word-word, word-document, document-word, and document-document matrices* "word space" is a way of giving words a distance metric, from each other as individuals and as collections of words (documents)* Leventshtein distance* Distance* statistical (frequency) word space* nltk.metrics.distance.jaccard_distance* nltk.metrics.distance.masi_distance* nltk.metrics.distance.presence* direct semantic word space (we'll talk about WordNet later)* syntactic/gramatical word space (we'll talk about POS tagging later)* statistical nltk distance measures/metrics:* complexity/entropy/information measures for unstructured text* a. compression ratio* b. entropy* c. predictability (human trials by Claude Shannon et al.)
---
title: Dimension reduction
footer: (15.0 min)
* occurrence matrices will grow to become impractical* 100k words/tokens counted across 10k documents = 1 GB of data, if stored efficiently* ignoring "stop words" and low-information-content words won't significantly reduce the dimensions* many machine learning algorithms are impractical at this scale:* decision trees* KNN* K-means* Support vector machines* SVD (PCA) can reduce the dimensions and enable many powerful machine learning algorithms to be employed* When SVD is impractical (e.g. 100k x 100k matrices or larger), dimension reduction can be based on the entropy found in each word and document independent of the others* ntlk US inaugural presidential speech word-frequency example* raw occurrence matrices* reduced-dimension occurrence matrices* d3 visualizations of occurrence matrices* as "checkerboard" grids or heat-maps* as graphs or networks (D3 force-directed graph)
---
title: Getting Fuzzy
footer: (15.0 min)
* regular expressions* examples for use in a chat bot* examples for use in a crawler for financial information* what they're good at (semi-structured text) and what their not good for (not robust/reliable)* fuzzywuzzy (uses "quick" Levenshtein distance)* examples for matching database table/column names* when you need the "best" match and you need it fast* fuzzy regular expressions (`regex` package)* example use in a chatbot (`will`)* when you want the very "best match" and you can wait
---
title: Break
footer: (10 min)

---
title: Jargon and typo consolidation
footer: (15.0 min)
* Tell a story about the need for word consolidation (vocab dimension reduction) at Sharp Electronics to interpret multilingual, jargony, and abbreviation-filled natural language repair technician notes* word distance metrics (Levenshtein)* which word is the "canonical" form among a list of typos* sorting by frequency* sorting by word length* iterative loosening of fuzziness threshold* use of dictionaries and word graphs (WordNet, ConceptNet) to find the "root" of a word* example usages o
---
title: Parsing structured data to create small , context-specific databases of knowledge for use in NLP information extraction from unstructured text
footer: (15.0 min)
* extracting tabular data automatically from a web page (using Scrapy)* automatic-identification of table "schema" using frequency analysis* parsing a natural language database table query and producing a natural language response (i.e. how Wolfram Alpha does it)
---
title: Natural language processing of search queries
footer: (15.0 min)
* composing logical statements from natural language* state of the art in semantic parsing of sentences* word order to tag words with POS and context
---
title: Break
footer: (10 min)

---
title: Knowledge extraction
footer: (15.0 min)
* date/time information using python-dateutil* `will` example "remind me to knock off at 5"* regexes to extract prices
---
title: Sentiment analysis to gage chat room "mood"
footer: (15.0 min)
* Applications of sentiment analysis* financial analytic forecasting* social network research and traffic/mood manipulation* advertising* consumer feedback processing* movie, music, book review processing and triage* will` chatbot example using nltk* gage the mood and civility of your chat room* long term "culture" tracking* identifying the mood of individual chatroom members
---
title: Sentence structure
footer: (15.0 min)
* `nltk` POS tagging tools and examples* grammar analysis and checking* using POS to aid in information/knowledge extraction
---
title: Semantic processing
footer: (15.0 min)
* nltk WordNet interface\* analyze and visualize the semantic network for the participant-supplied text* use NLTK to populate a simple knowledge base about you based on your hard drive contents
---
title: Metadata


* Lines: 58
* Pages: 21
* Tokens: 2069
* Sentences: 12
* Vocabulary: 735
* Time: 4:24
