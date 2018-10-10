<img src="http://geeko.lesoir.be/wp-content/uploads/sites/58/2017/04/08446114-photo-twitter-logo.jpg" title="Twitter"/>
<h2 align="center">Twitter text mining</h2>
Text Mining is a branch of Data Mining that allows you to analyze the content of a text in order to extract knowledge from it. It is based on a semantic research based on the analysis of natural language.

Text Mining allows you to search for information for a specific context, to compare several documents and deduce an adapted operation from them. It then allows the realization of tasks such as architecting the information extracted in such a way that it can be reused
quickly.

With the advent of social networks, sources and data contents have continued to grow exponentially. 

<h3>1. Create Twitter API keys </h3>

You can follow this link <a href="http://docs.inboundnow.com/guide/create-twitter-application/" >How to create a Twitter application</a>


<h3>2. Collecting data </h3>

The code is in <a href="https://github.com/Khoumzy/twitter/blob/master/twitter_streaming.py">twitter_streaming.py</a>.
You have to run this file in your terminal.

$ python twitter_streaming.py > dataset/datas.txt

In my part i run the code 10h et i have collected 280 Mb.

<h3>3. Understanding the data</h3>

You have to explore my notebook <a href="https://github.com/Khoumzy/twitter/blob/master/text_mining.ipynb">text_mining.ipynb</a> . The code is well documented.
