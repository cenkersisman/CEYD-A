# CEYD-A 

INTRODUCTION

## What is CEYD?

CEYD language (Cenker.com Artificial Intelligence Language), is a scripting language which enables voice driven chat robot assistant to understand commands (questions) and answers them accordingly (answers) Users can write and develop this script language so that they can use the compiled script in various platform afterwards.CEYD language functions are written inside pure text formatted answers and these functions determine how robot should respond to the question. Writing CEYD functions inside answers is not required. They are used for functionality and productivity of the answer.

What is CEYD-A

CEYD-A is the official assistant of CEYD language. It is currently supported in Android platform and can be downloaded from Google Play Store.


CEYD-A Structure

What is Command?

We can define a command as a chain of question and its answers.
Commands can be defined at: http://ceyd-a.net/komutekle
As CEYD language is free to use and develop, creating your own custom commands is TOTALLY FREE. In fact, developing your own commands are encouraged Note that, after entering this site, English language selection is automatically chosen, otherwise you can also click on English link manually.
After the new command is submitted, it is automatically loaded by the user’s device provided that CEYD-A on the device has the same login information.

STEP 1) Question Words

Question words can be used to help CEYD-A finds its correct command. The words in question words are matched in the sentence spoken. If spoken sentence contains the question word, the command is executed.
Words or sentences are seperated by | sign like: 

Good morning|Hello|Hi

STEP 2) Question Patterns

This is not a required field. If used, it will define parameters of the question. You can use regex to assign groups. For instance if you write,

{HER}make sum of ({SAYI1}) and ({SAYI2}){HERSON}

and you say 

make sum of 4 and 3

4 and 3 will be treated as decimal groups. You can use these groups in response area as {SAYI1} and {SAYI2} , 
In other words groups behave like parameters for responses.

Example 1:

QUESTION PATTERN: {HER}make sum of ({SAYI1}) and ({SAYI2}){HERSON}

QUESTION WORDS: make sum of

RESPONSE: Do you want me to add {SAYI1} to {SAYI2}. I will.

Example 2: (Modified version using CEYD functions inside answer)

QUESTION PATTERN: {HER}make sum of ({SAYI1}) and ({SAYI2}){HERSON}

QUESTION WORDS: make sum of

RESPONSE: Sum of {SAYI1} and {SAYI2} is {!EVAL {SAYI1}+{SAYI2}!}

STEP 3) Response/Add Dialog

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

It is {!RET what is temperature} outside.|It is % {!RET is it cloudy!} percent cloudy outside. 

Television means {!RET what is television} I guess. 

{!SET $temp ={!RET what is temperature!}!}

It is {!GET $temp!} degree.

I think {!IF $temp<=18??it is cold::it is hot!} 

To give a little more complicated example, let’s write a currency calculator. 

QUESTION TEMPLATE: how much ({HER1}) (dollar|euro){HERSON} 

QUESTION WORDS: dollars in euros,10 

RESPONSE: $1 dollars is {!EVAL {HER1}*{!RET euro!}/{!RET dolar!}} 

As we know, the question is in regex format template. Pattern is separated by () groups, they are referred to as the response parameters $1 $2 so on. 

The $1 in the answer corresponds to ({HER1}) group in the pattern. So when how much 5 dollars in euros? is spelled ({HER1}) is the first group. 

Second group is dollar or euro. 

The answer template will be finally transformed to something like 2 dollars is 4.59 TL. 

The answer will be formed and will be reflected on the screen and also will be spoken by CEYD-A. 

STEP 4: Action/Add Action 

You can use this step if you want to add an alternative question sentence to a command already defined. Let’s say you will define a new command B which will behave the same as command A, then you can write command A in this area.

## Syntax Highlighting For NotePad++
Put the ceyd.xml file into the \AppData\Roaming\Notepad++\userDefineLangs folder inside user directory.
