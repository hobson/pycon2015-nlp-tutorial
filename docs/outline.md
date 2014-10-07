1. (10 min) What is "natural language"

    1. System of symbols and utterances developed by humans over millions of years.
    2. Unstructured text is a generalization of natural language text and the terms are often used interchangeably
    3. Natural language is often embedded in structured text (formal languages)
        * HTML, XML, YAML, SQL, and of course **Python**
        * variables, elements, names, strings, files, streams
    4. Example semi-structured, semi-formal language challenges:
        * Parse HTML tag contents
            * When is PyCon?  "<title>PyCon 2015 in Montréal | April 8th – April 16th</title>""
        * Parse a textbook or Wikipedia article with headings, page numbers, footnotes, etc
        * A social network feed (twitter, facebook, ), e.g. "Brushed my teeth today"
        * A legal contract, license agreement, EULA, annual report, patent
            * "By checking this box you sign away your rights to sue us."
        * Scrape every other row in an HTML table (e.g. your Facebook page)
    5. More challenging, less-standardized NLP
        * Notes to yourself
            * "Don't forget to take Plato for a walk tomorrow"
        * Chat room or forum messages
            * "OMG dont be sucha troll!!!"
        * Extract numbers and prices and their "units" of measure
            *  "200 pythonistas", "$50K per year", "1 GB"
    6. Nonexamples
        * HTML and CSS tags
        * python script (but some strings within it may be NL)
        * A CSV file (but some strings within the fields may be NL)
        * mathematical equations (but the integers and fractions within it can be processed as NL)
        * a database (but the names of the fields and tables may be processed as NL)

2. (10 min) what is natural language processing 
    1. Computer processing of languages to do something useful or fun
    2. Story about the genesis of _information theory_ and introduction to concepts Applicable to NLP:
        * entropy
        * coding
        * decoding
        * compression
        * encryption
        * channel capacity
        * distance metrics
        * dimensionality

3. (10 min) why is natural language processing useful and fun 
    2. Example applications
        a. sentiment analysis of customer service data (SAP)
        b. sentiment analysis for trend and finance prediction on twitter and other news feeds (Thomson Reuters)
           * Reuters provides a low-latency feed to hedge funds containing a single bit associated with a stock symbol -- positive or negative impact on price
        c. hardware performance trends based on technician inspection comments (Sharp Electronics Corporation)
        d. enable artificial intelligence agents to train/teach themselves (CMU's NELL)
        e. data migration (ETL) between bodies of structured text like CSV, HTML tables to save the planet (DOE and Building Energy)
        f. example processing of memoirs for psychoanalysis: Stephen Fry's autobiography and its [open API + metadata](http://yourfry.com/)

5. (5 min) Is NLP related to AI? 
    1. Turing defined it as being able to imitate a human's ability to converse in  natural language text
    2. In some ways coding languages, structured text, and data structures, are just a subset or specialization of natural languages (because they are meant to be written and read by humans *AND* machines)
    3. semantic processing (state of the art NLP) extracts knowledge or meaning from text
    4. Speech recognition + NLP can often produce effective AI (e.g. Liza 2.0)

6. (10 min) Context:
    1. What is _context_?
    2. Why is it important?
    3. Some common layers of context and meaning
        1. word (the "meaning" of syllables depends on the word they are used in)
        2. compound word ("boot" means something different in "bootstrap" and "boot up")
        3. phrase (noun-phrases are particularly "atomic")
        4. sentence (a sentence can often be presumed to have some grammatically-required elements like a noun and a verb)
        5. paragraph (paragraphs often have an intro, body, conclusion with different word usage assumptions)
        6. passage (quotes, excerpts)
        7. page (text often will refer to images or quotes on the same page, like "see above")
        8. section (topics are changed between sections of an article or book)
        8. chapter (authors change viewpoint/location/subject between chapters)
        9. book (terms and symbols used in a dictionary may only be relevant there)
        10. corpus (a subset of language usages will always have sample biases)
        11. language ("taco" means something different in English than in Spanish)
        12. tribe/city/region ("Zoobombing" means something completely different in Portland than in a war zone)
        12. nation (culture)
        13. planet (yes, projects like SETI are very concerned with NLP of ET languages)

7. (10 min) Teasers: Algorithms Behind Some Popular NLP Packages
    1. sluggify.sluggify
        * Foundation: str.split(), str.strip(), str.replace()
        * Uses: Django url composition

    >>> slugify(u"Awesome:*lol*resume'=B", max_length=15, word_boundary=True)
    'awesome-lol-b'

    2. dateutils.parser.parse 
        * Foundation: Regular expressions
        * Uses: Google Calendar, Remember The Milk
        
    >>> parse('fri')
    datetime.datetime(2015, 4, 10, 0, 0)

    3. fuzzywuzzy.process
        * Foundation: Levenshtein Edit Distance, `difflib`
        * Uses: Building Energy data ETL

    >>> process.extractOne("mess with", ["nuke", "talk", "surrender"])[0]
    ('talk', 29)

8. --- (10 min) Coffee Break ---
    * Available to help "offline"

9. (15 min) Tools and techniques for identifying "style" or "context"
    1. Sentiment and mood metrics
    2. Style distance metrics for comparison of a text to that of famous authors like Hemmingway, Shakespeare, US presidents,
    3. Techniques
        * vocabulary breadth 
        * vocabulary statistics relative to "standard vocabularies" or age-group vocabularies from education material
        * vacabulary evolution over the course of a document
        * structure (vocabulary shifts within a document for each of the context layers discussed previously) 

9. (10 min) Acquiring a Corpus
    1. using `nltk` to download text corpora (text documents or strings)
    2. extracting text and semi-structure text (tables) from web pages using Scrapy and Beautiful Soup
    3. encoding issues and python 2 vs 3: what has changed and how to use the best of python 3 with python 2 NLP tools
        * `unicode()` vs `str()` vs `repr()`
        * `from __future__ import unicode_literals`
    4. check user-supplied corpus  with some common tools for "quantifying" and structuring unstructured text

10.  (20 min) Frequency analysis of US President inaugural speeches ()
    1. segmentation/tokenization/parsing
        * characters (encoding issues, some natural languages like Japanese Kanji and Chinese don't have "letters")
        * words
            * digits and symbols and unicode as part of words
            * punctuation at the end of sentences and word
            * hyphenation
            * typos
            * spelling variations (British English)
            * language variations (Spanish, French, slang)
        * bag-of-words counting (frequency analysis) ignores context at any layer above the "documents"
        * agnostic counting
    2. stemming
        * nltk stemmers
    3. counting 
        * Data structures like `collections.Counter` that discard context/order 
        * Can `collections.OrderedDict` be used to preserve context and order? (not easily)
    4. normalization of counts/frequencies/probabilities
    5. occurrence matrices ("word space" or "word vector space" in information theory)
        * uses for word-word, word-document, document-word, and document-document matrices
        * "word space" is a way of giving words a distance metric, from each other as individuals and as collections of words (documents)
            * Leventshtein distance
                * Distance
            * statistical (frequency) word space
                * `nltk.metrics.distance.jaccard_distance`
                * `nltk.metrics.distance.masi_distance`
                * `nltk.metrics.distance.presence`
            * direct semantic word space (we'll talk about WordNet later)
            * syntactic/gramatical word space (we'll talk about POS tagging later)
            * statistical nltk distance measures/metrics:
    2. complexity/entropy/information measures for unstructured text
        a. compression ratio
        b. entropy
        c. predictability (human trials by Claude Shannon et al.)

11. (15 min) Dimension reduction (PCA or SVG)
    1. occurrence matrices will grow to become impractical
        * 100k words/tokens counted across 10k documents = 1 GB of data, if stored efficiently
        * ignoring "stop words" and low-information-content words won't significantly reduce the dimensions
        * many machine learning algorithms are impractical at this scale:
            * decision trees
            * KNN
            * K-means
            * Support vector machines
        * SVD (PCA) can reduce the dimensions and enable many powerful machine learning algorithms to be employed
        * When SVD is impractical (e.g. 100k x 100k matrices or larger), dimension reduction can be based on the entropy found in each word and document independent of the others
    2. ntlk US inaugural presidential speech word-frequency example
        * raw occurrence matrices
        * reduced-dimension occurrence matrices
    3. d3 visualizations of occurrence matrices
        * as "checkerboard" grids or heat-maps
        * as graphs or networks (D3 force-directed graph)

9. -- (10 min) Coffee Break ---
    * Available to help "offline"

10. (15 min) Getting Fuzzy
    1. regular expressions
        * examples for use in a chat bot
        * examples for use in a crawler for financial information
        * what they're good at (semi-structured text) and what their not good for (not robust/reliable)
    2. `fuzzywuzzy` (uses "quick" Levenshtein distance)
        * examples for matching database table/column names
        * when you need the "best" match and you need it fast
    3. fuzzy regular expressions (`regex` package)
        * example use in a chatbot (`will`)
        * when you want the very "best match" and you can wait
11. (15 min) Jargon and typo consolidation
    * Tell a story about the need for word consolidation (vocab dimension reduction) at Sharp Electronics to interpret multilingual, jargony, and abbreviation-filled natural language repair technician notes
    * word distance metrics (Levenshtein)
    * which word is the "canonical" form among a list of typos
        * sorting by frequency
        * sorting by word length
        * iterative loosening of fuzziness threshold
        * use of dictionaries and word graphs (WordNet, ConceptNet) to find the "root" of a word
    * example usages o
12. (15 min) Parsing structured data to create small , context-specific databases of knowledge for use in NLP information extraction from unstructured text
    1. extracting tabular data automatically from a web page (using Scrapy)
    2. automatic-identification of table "schema" using frequency analysis
    3. parsing a natural language database table query and producing a natural language response (i.e. how Wolfram Alpha does it)
13. (15 min) Natural language processing of search queries
    1. composing logical statements from natural language
    2. state of the art in semantic parsing of sentences
    3. word order to tag words with POS and context

14. -- (10 min) Coffee Break ---
    * Available to help "offline"

15. (15 min) Knowledge extraction
    1. date/time information using python-dateutil
        * `will` example "remind me to knock off at 5"
    2. regexes to extract prices
16. (15 min) sentiment analysis to gauge chat room "mood"
    1.  Applications of sentiment analysis
        * financial analytic forecasting
        * social network research and traffic/mood manipulation
        * advertising
        * consumer feedback processing
        * movie, music, book review processing and triage
    2. will` chatbot example using nltk
       * gage the mood and civility of your chat room
       * long term "culture" tracking
       * identifying the mood of individual chatroom members
17. (15 min) sentence structure
    1. `nltk` POS tagging tools and examples
    2. grammar analysis and checking
    3. using POS to aid in information/knowledge extraction
18. (15 min) Semantic processing
    1. `nltk` <-> `WordNet` interface
    2. analyze and visualize the semantic network for the participant-supplied text 
    3. use NLTK to populate a simple knowledge base about you based on your hard drive contents
