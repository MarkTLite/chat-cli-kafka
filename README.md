# CHAT CLI

[![codecov](https://codecov.io/gh/MarkTLite/chat-cli-kafka/branch/main/graph/badge.svg?token=D1GG1EUSJL)](https://codecov.io/gh/MarkTLite/chat-cli-kafka)
![Test status](https://github.com/MarkTLite/chat-cli-kafka/actions/workflows/testcov.yml/badge.svg)
![Build Status](https://github.com/MarkTLite/landing-page-react/actions/workflows/heroku_deployer.yaml/badge.svg)



## Description

A command-line-driven program that allows message exchange. Uses kafka as a message broker.  

## Usage
With one instance of the program, you can run the command:<br>
    <code>
    python main.py send --channel test-topic --server “localhost:9092” 
    </code>

With a second instance of the same program <br>
<code>
    python main.py receive --channel test-topic --_from start --server “localhost:9092” 
    </code>

### Additional Information
> You can run both instances at the same time in different terminals to test producing and receiving the messages 

## Testing 
Mock testing was applied since a third party service - kafka is involved and to dictate values so as to increase code coverage by touching all decision points of the code.

### To run the tests: 
1. Install coverage<br>
<code>
pip install coverage
</code>

2. Run this:<br>
<code>
coverage run -m unittest
</code>

3. To check code coverage: <br>
<code>
coverage report
</code>


