# CHAT Cli

[![codecov](https://codecov.io/gh/MarkTLite/WebScraper/branch/main/graph/badge.svg?token=KS779CNL3Z)](https://app.codecov.io/gh/MarkTLite/chat-cli-kafka)
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

## Additional Information
> You can run both instances at the same time in different terminals to test producing and receiving the messages 

