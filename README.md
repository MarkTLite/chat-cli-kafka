# CHAT Cli

[![codecov](https://codecov.io/gh/MarkTLite/WebScraper/branch/main/graph/badge.svg?token=KS779CNL3Z)](https://codecov.io/gh/MarkTLite/WebScraper)
![Test status](https://github.com/MarkTLite/WebScraper/actions/workflows/pytester.yml/badge.svg)
[![Build Status](https://app.travis-ci.com/MarkTLite/WebScraper.svg?branch=main&status=unknown)](https://app.travis-ci.com/MarkTLite/WebScraper.svg?branch=main)


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

