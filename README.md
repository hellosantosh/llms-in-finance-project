# llms-in-finance-project
PROBLEM:
Analyst ratings from different analysts are available as independent PDFs. To get a wholistic view of an equity, one has to go through several PDFs to get an overview of the stock's current performance and future outlook. 

SOLUTION:
Using Agentic Doc Extractor, read analyst ratings pdfs from different analysts and print out a side-by-side data for each of them. The data could be price target, buy/sell ratings, summary of the recommendation, etc. 

The Agentic Document Extractor is located at: https://github.com/landing-ai/agentic-doc 

PRE-REQUISITE:
- Create a virtual conda env, activate it:
``` 
    conda create -n condavenv python=3.13.5
    conda activate condavenv
```
- To deactivate
```
    conda deactivate
```

TO RUN:
-- pip install -r requirements.txt
-- python app.py

RESULTS:
This uses the agentic-doc API from landing.ai to parse and extract a bunch of PDF documents recursively from a top level folder. In this case, the top-level folder is "analyst_reports". I have included analyst reports for two stocks - AMD and NVDA. The results are stored in the "results" folder. The grounding is stored in the "groundings" folder. 

NEXT STEPS:
We now have a comprehensive set of parsed output data in markdown format from PDF documents. This can easily be fed to an LLM using RAG. The goal is to create a UI that takes a stock ticker as input and show the analyst ratings side-by-side from different "sell side" companies like Argus, ISS-EVA, Jefferson Research, LSEG, McLean Equity Research, and Zacks. The UI will show useful information from each analyst report like price target, buy/sell recommendation, company outlook, strengths, weaknesses, etc. The grounding data in the "grounding" directly will be used for evaluating the LLM Outputs. 

