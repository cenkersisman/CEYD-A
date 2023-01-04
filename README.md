FORMAT: 1A
HOST: https://beta.ceyd-a.com/

# CEYD-A

# What is CEYD?
CEYD language (Cenker.com Artificial Intelligence Language), is a scripting language which enables voice-driven chat robot assistant to understand commands (questions) and answers them accordingly (response) Users can write and develop this scripting language so that they can use the compiled script in various platform afterwards.

CEYD language functions are written inside pure text formatted answers and these functions determine how a robot or chatbot should respond to the question. Writing CEYD functions inside answers is not required. They are used for functionality and productivity of the answer.

# What is CEYD-A
CEYD-A is the official assistant of CEYD language. It is currently supported in the Android platform and can be downloaded from Google Play Store. It has more than 4 million users in Turkey and will spread worldwide soon
English version of CEYD-A is also available and can be downloaded from https://play.google.com/store/apps/details?id=com.cenker.ceydasistan.app.en&hl=en_US

<b>Features:</b>
* It is a voice assistant that can be developed by users.
* Unlike other digital assistants, it performs what you say on the device.
* It has its own interpreter, its own development language.
* The commands you develop are accumulated in the pool, when approved, all CEYD-As benefit from them.
* It does not send your private information to the server, but keeps it in the database on your own device. The server is only for updating the command repository.
* As it works on the device, the performance is directly proportional to the speed of the device.
* Since it works on the device, it can work without the need for internet except for voice detection.

# For Developers
## Webservice API
As of August 2017, CEYD-A contains more than <b>300.000 commands</b> created by <b>200.000 developers</b>. These developers generally create commands orally using CEYD-A application. Commands can also be created in written form for more complicated usage. 
You may assume CEYD-A as a voice enabled semantic search engine which answers your questions. So the use of this API, is to get the answer of your question.
### Sample usage of this API
API URL is at https://beta.ceyd-a.com/jsonengine.jsp
You can set the following POST parameters as

``` 
"username": "test",
"token": "aaa28b4089101057d2b026adf9c68da1",
"code": "bayram ne zaman",
"type": "text",
"lang": "tr-TR"

``` 
  
When you call this service, you can expect the following response

``` 
"username": "test",
"question": "bayram ne zaman",
"answer": "Zafer Bayramı 30 Ağustos 2017,Çarşamba"
``` 


### Is this service free ?
You can use this service freely provided that your quota will not be exceeded. If you use this service for academic purposes, you may ask for free usage.

### What is my token for my account ?
Please login <a href="https://beta.ceyd-a.com/">https://beta.ceyd-a.com/</a> . After login, you will see your username and token info as well as your current quota.
Your login information is the same as your CEYD-A account. You can take free support from https://en.ceyd-a.com
## Offline Library
For offline usage, you may use CEYD Java library in your code project. CEYD Java library is referenced at: [Using CEYD-A Services in Java Projects](https://en.ceyd-a.com/en/2020/08/java-projelerinde-ceyd-a-hizmetlerini-kullanmak/)

## How can I create my own custom commands ?
Commands can be created freely at:

<a href=https://kodla.ceyd-a.com>https://kodla.ceyd-a.com</a> 

## Where can I find a command sample which fetches data from a remote web service ?
This example shows how to fetch json data from remote server using CEYD language:

<a href="https://en.ceyd-a.com/2016/10/json-web-servislerinden-bilgi-cekme/">https://en.ceyd-a.com/2016/10/json-web-servislerinden-bilgi-cekme/</a>
## Where can I find more command samples ?
<a href="https://en.ceyd-a.com/category/ozel-komutlar/">https://en.ceyd-a.com/category/ozel-komutlar/</a>
## Can I develop commands without coding, simply using block patterns?
Yes, you can find resources from the following page: 

<a href="https://en.ceyd-a.com/2019/11/ceyd-a-ile-kurgu-gelistirmeleri/">https://en.ceyd-a.com/2019/11/ceyd-a-ile-kurgu-gelistirmeleri/</a>
## Can I code my command samples using CEYD language without block patterns? 
<a href="https://en.ceyd-a.com/2019/11/ceyd-a-ile-kurgu-gelistirmeleri/">https://en.ceyd-a.com/2018/09/komut-ekleme-nasil-yapilir/</a>
# CEYD Structure


## What is Command?

We can define a command as a chain of question and its answers.

![ceyd editor](https://github.com/cenkersisman/CEYD-A/blob/master/images/fiction.png)

Commands can be defined at:
<a href=https://kodla.ceyd-a.com>https://kodla.ceyd-a.com</a>

As CEYD language is free to use and develop, creating your own custom commands is TOTALLY FREE. In fact, developing your own commands are encouraged
Note that, after entering this site, English language selection is automatically chosen, otherwise you can also click on English link manually .
After the new command is submitted, it is automatically loaded by the user’s device provided that CEYD-A on the device has the same login information.

## STEP 1) Question Words
Question words can be used to help CEYD-A finds its correct command. The words in question words are matched in the sentence spoken. If spoken sentence contains the question word, the command is executed.

Words or sentences are seperated by | sign like:
Good morning|Hello|Hi

## STEP 2) Question Patterns

This is not a required field. If used, it will define the parameters of the question. You can use regex to assign groups.

For instance, if you write,

```
{ANY}make sum of ({NUM1}) and ({NUM2}){ANY}
```

and you say to make the sum of 4 and 3, 4 and 3 will be treated as decimal groups. You can use these groups in the response area as {NUM1} and {NUM2}, In other words, groups behave like parameters for responses.
Example 1:
```
WORDS: make sum of
PATTERN: {ANY}make sum of ({NUM1}) and ({NUM2}){ANY}
RESPONSE:
Do you want me to add {NUM1} to {NUM2}. I will.
```

Example 2: (Modified version using CEYD functions inside answer)
```
WORDS: make sum of
PATTERN: {ANY}make sum of ({NUM1}) and ({NUM2}){ANY}
RESPONSE: Sum of {NUM1} and {NUM2} is {!EVAL {NUM1}+{NUM2}!}
``` 

 

## STEP 3) Response/Add Dialog

It is the response of the command. They must be seperated by | signs

No, I am not a student|I am a robot not human

Also, CEYD functions can be embedded into the answer. The parameter passed from the question may also be used in the sentence.

I do not know what $1 is|Unfortunately I do not have any information about $1

CEYD functions are encapsulated in {! and !}

CEYD functions are

RET, IF, SET, GET, EVAL, FOR functions

RET function returns the result of a command.

IF function compares two values and returns a value or execute a block of command depending on the comparison.

SET function assigns a value to a variable. This value is stored in memory even if the device is restarted.

GET function returns the variable value.

EVAL makes mathematical function and returns its value

FOR is a control flow statement for specifying iteration, which allows code to be executed repeatedly.
Some examples, provided that temperature and cloudy commands are created before:

```
It is {!RET what is temperature} outside.|It is % {!RET is it cloudy!} percent cloudy outside.
```

Television means {!RET what is television} I guess.

```
{!SET $temp={!RET what is temperature!}!}It is {!GET $temp!} degree.I think {!IF $temp<=18??it is cold::it is hot!}
```

To give a little more complicated example, let’s write a currency calculator.

```
WORDS: dollars in euros,10
PATTERN: how much ({PAR1}) (dollar|euro){ANY}
RESPONSE:
$1 euro is {!EVAL {PAR1}*{!RET euro!}/{!RET dollar!}!} dollars
``` 

```
5 euro is {!EVAL 5*{!RET euro!}/{!RET dollar!}!} dollars
```
As we know, the question is in regex format template. The pattern is separated by () groups, they are referred to as the response parameters $1 $2 so on. The $1 in the answer corresponds to ({PAR1}) group in the pattern. So when <b>how much 5 euros in dollars?</b> is spelt
({PAR1}) is the first group. The second group is dollar or euro.
The answer template will be finally transformed into something like
5 dollars is 4.59 Euros.
The answer will be formed and will be reflected on the screen and also will be spoken by CEYD-A.

# Information
These are simple APIs allowing consumers to view answers to the questions asked and CEYD codes to be executed. Questions are referred to commands

## Questions Collection [/jsonengine.jsp]


### Ask a Question [POST]

You may ask your question using this action. It takes a JSON
object containing a question, username and token. .

+ Request (application/json)

        {
            "username":"test",
            "token":"aaa28b4089101057d2b026adf9c68da1",
            "code": "bayram ne zaman",
            "type": "text",
            "lang": "tr-TR"
        }

+ Response 201 (application/json)

    + Headers

            Location: /jsonengine.jsp

    + Body
    
            {
                "username": "test",
                "question": "bayram ne zaman",
                "answer": "Zafer Bayramı 30 Ağustos 2017,Çarşamba",
                "priority": 10,
                "commandname","ne zaman"
            }


### Ask a Question (English) [POST]

You may ask your question using this action. It takes a JSON
object containing a question, username and token. .

+ Request (application/json)

        {
            "username":"test",
            "token":"aaa28b4089101057d2b026adf9c68da1",
            "code": "hello",
            "type": "text",
            "lang": "en-US"
        }

+ Response 201 (application/json)

    + Headers

            Location: /jsonengine.jsp

    + Body
    
            {
                "username": "test",
                "question": "hello",
                "answer": "",
                "priority": 10,
                "commandname",""
            }



### Execute a CEYD Code [POST]

You may execute your own CEYD code using this action. It takes a JSON
object containing a CEYD codes, username and token.

+ Request (application/json)

        {
            "username":"test",
            "token":"aaa28b4089101057d2b026adf9c68da1",
            "code": "{!SET i={!RET random 10!}!}{!GET i!}",
            "lang": "tr-TR"
        }

+ Response 201 (application/json)

    + Headers
    
            Location: /jsonengine.jsp

    + Body
    
            {
                "username": "test",
                "question": "",
                "answer": "5",
                "priority": 1
                
            }


[](codehighlight)
## Code Syntax Highlighting For NotePad++
Put the [ceyd.xml](https://github.com/cenkersisman/CEYD-A/blob/master/ceyd.xml) file into the %UserProfile%\AppData\Roaming\Notepad++\userDefineLangs folder for Windows System

![ceyd editor](https://github.com/cenkersisman/CEYD-A/blob/master/images/image_2020_10_30T14_39_54_411Z.png)

Using Notepad ++, you can code fictions (commands) for CEYD-A with the syntax highlighting feature. You can easily check the brackets of IF THEN ELSE blocks and brackets of other functions (RET,SET,GET,FOR,EVAL). 
The code will work for your command which you can enter on https://kodla.ceyd-a.com. 
After you login this site, you must add this code to the RESPONSE field of your new command. After the commands are updated, they will be reflected in your own environment, mobile, tv and web..

![ceyd editor](https://github.com/cenkersisman/CEYD-A/blob/master/images/chrome_XqpRlramm2.png)

You can see the RESPONSE field inside the red rectangle. You must also fill in the Question word and Question Pattern for the command to be created properly.

![ceyd editor](https://github.com/cenkersisman/CEYD-A/blob/master/images/chrome_XoL3m607d6.png)

Also, you can select any lines and test its response before updating.

After updating the command, you can use it in your CEYD-A clients.
You can use this command using sentence like 
cmdenwikipedia book
and you will see the definition of book from wikipedia.

You can test your updated commands at https://beta.ceyd-a.com

![ceyd editor](https://github.com/cenkersisman/CEYD-A/blob/master/images/cmdenwikipedia_test.png?raw=true)

## Telegram Bot
You can use this Python code below to create a Telegram bot. You must change the required fields in the code. 
That way, people can talk to your bot like chatting with another person. I would like you to inform me after creating the bot.
[ceyd-a_telegrambot.py](https://github.com/cenkersisman/CEYD-A/blob/master/ceyd-a_telegrambot.py)

## CEYD-A Proxy
With this application running on Windows, you can communicate with your Windows computer via bluetooth from CEYD-A installed on your Android device. CEYD-A will be able to send codes and files to be processed on Windows and receive the results again via bluetooth.

The exe application is the executable version of the Java jar file. Once it's running, you should be able to see the CEYD-A logo in the Windows system tray. This means that you can now get Windows to work through CEYD-A.
[Ceyd-a Proxy](https://github.com/cenkersisman/CEYD-A/blob/master/ceyd-a_proxy.exe)

