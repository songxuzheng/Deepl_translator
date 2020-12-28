# Deepl_translator
Get translation from Deepl.com using Selenium.   
deepl翻译！运用Selenium 的Chromedriver 进行网络爬虫获取翻译！
## Dependencies
- selenium
> pip install selenium
- chromewebdriver
> https://chromedriver.chromium.org/downloads

## How to use!   

from Deepl_trans import deepl_translator  

sentence = 'Give me a star please!'  
to_lang = 'zh-ZH'. 

translation = deepl_translator(sentence, to_lang).translation  

print(translation). 

----->'请给我一颗星！'

**The input language is auto-detected**, and the input language should be also one of the following output language

## To_language
 
            'en-US':American English,  
            'en-GB':Britisch English,  
            'fr-FR':French,  
            'es-ES':Spanish,  
            'pt-PT': Portuguese (Portugal),
            'pt-BR': Portuguese (Brazil),
            'it-IT': Italian,
            'nl-NL': Dutch,
            'pl-PL': Polish,
            'ru-RU': Russian,
            'ja_JA': Japanese,
            'zh-ZH': Chinese(simplified),
## Problem 
The translation process is rather slow, might take a few seconds.
### Only for study, do not use it for commercial purposes!  
I am open to any suggestions! Thank you!
