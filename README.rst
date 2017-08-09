Micro-library to quickly clean up text for textmining purposes.  Mostly devoted to getting rid of unicode punctuation, random extra spaces, etc. etc.

This is meant as a very quick and dirty cleanup process (hence the name). It throws out numbers, currency symbols, math, punctuation, superscripts and subscripts etc. The objective is primarily to eliminate an annoying step in bag-of-words style textmining.

Usage is really simple::

    from dirtyclean import clean
    clean("some string full of punctuation and stuff")

Right now, the only options given are to convert combined letters (letters with accent marks, umlats, etc.) into their unicode primitives or not.  Default behavior is to not do so, and hence retain all characters that might actually distinguish different words.  

If you want to get rid of umlats and such, you can try ``clean("somestring", simplify_letters = True)`` However, I don't guarantee that letter simplification will work.  If it breaks, please file an issue, or, better yet, a PR.

This micro-library just tries to take a string with arbitrary unicode in it and emit a string with all the words, separated by single spaces, where "word" is defined as "continuous sequence of letters" and "letter" is defined as "stuff in the `unicode categories<http://www.fileformat.info/info/unicode/category/index.htm>`_ Lu, Ll, Lt, and Lo." Does not lowercase or anything like that; that's a single method call you can do it yourself (also, I don't want to throw away case information for users who need it). 

One known problem is that hyphenated words and contractions will be split up.  In view of the fact that in natural language English as actually used (at least, not sure about other languages) uses "-", "'" and various other characters with similar shapes to split words and to serve as ordinary punctuation, there's no simple and quick way to detect the difference between these uses, at least not without some kind of dictionary. So I just let stuff like "don't" be two words.  If this is a problem for your use case, maybe try a fancy `NLTK tokenizer<<http://www.nltk.org/api/nltk.tokenize.html>`_?

One possible heuristic solution would be to replace the punctuation and such with a placeholder on the translation pass, and then on the regular expression pass, replace the with a space iff there's a space (but not newline, because of line-break hyphenation) on either side. This could work, but would involve making the regex a bit more convoluted + would smush together rather than separate compound constructions that are normally hyphenated. For example, "injury-prone" would become "injuryprone" rather than the more sensible "injury prone."  Nonetheless, it's worth a try as an alternative implementation, perhaps under a flag like `heuristic-hyphens = True`.  I might implement this down the line, but I'd welcome a PR to do it before I get there.

In general, this is a work in progress, pull requests very much desired.  Please add a test for any functionality you add, and please keep the default behavior the same (except for bugfixed) without any new arguments (i.e., for new functionality, just add another optional argument).

Tests are bare unittest; I use nose2 for testing, but you can use whatever. Run tests from the test directory so it can find the text file in there.

MIT license.
