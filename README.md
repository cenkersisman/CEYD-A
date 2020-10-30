FORMAT: 1A
HOST: https://beta.ceyd-a.com/

# CEYD-A

# What is CEYD?
CEYD language (Cenker.com Artificial Intelligence Language), is a scripting language which enables voice driven chat robot assistant to understand commands (questions) and answers them accordingly (answers)
Users can write and develop this script language so that they can use the compiled script in various platform afterwards. 

CEYD language functions are written inside pure text formatted answers and these functions determine how robot should respond to the question. CEYD functions are not required to be included in the answer.  They are used for functionality and productivity of the answer.
# What is CEYD-A
CEYD-A is the official assistant of CEYD language. It is currently supported in Android platform and can be downloaded from Google Play Store. It has more than <b>2.2 million users in Turkey</b> and will spread worldwide soon
# For Developers
## Webservice API
As of August 2017, CEYD-A contains more than <b>300.000 commands</b> created by <b>200.000 developers</b>. These developers generally create commands orally using CEYD-A application. Commands can also be created in written form for more complicated usage. 
You may assume CEYD-A as a voice enabled semantic search engine which answers your questions. So the use of this API, is to get the answer of your question.
### Sample usage of this API
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
Your login information is the same as your CEYD-A account. You can take free support from https://ceyd-a.net/
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

## STEP 4: Action/Add Action

You can use this step if you want to add an alternative question sentence to a command already defined. Let’s say you will define a new command B which will behave the same as command A, then you can write command A in this area.
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


## Code Syntax Highlighting For NotePad++
Put the ceyd.xml file into the \AppData\Roaming\Notepad++\userDefineLangs folder inside user directory.
