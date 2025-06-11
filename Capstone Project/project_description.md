## Project Overview

### Build Your Data Science Project

In this capstone project, you will leverage what you’ve learned throughout the program to build a data science project
of your choosing. Your project deliverables are:

1. A Github repository of your work. \
   The repository must have a README.md file that communicates the libraries used, the motivation for the project, the
   files in the repository with a small description of each, a summary of the results.
2. A blog (or other media for a write-up) post written for a technical audience, or a deployed web application powered
   by
   data.

You'll follow the steps of the data science process that we've discussed:

1. You will first define the problem you want to solve and investigate potential solutions.
2. Next, you will analyze the problem through visualizations and data exploration to have a better understanding of what
   algorithms and features are appropriate for solving it.
3. You will then implement the algorithms and metrics of your choice, documenting the preprocessing, refinement, and
   post-processing steps along the way.
4. Afterward, you will collect results about your findings, visualize significant quantities, validate/justify your
   results, and make any concluding remarks about whether your implementation adequately solves the problem.
5. You can choose to: (i) construct a blog post (or another medium for a write-up) to document all of the steps from
   start
   to finish of your project, or (ii) deploy your results into a web application.

#### Capstone Project Report Structure

Writing a clear, concise, and well-structured Data Science report is a critical step to communicate and share your key
findings and processes with your peers. If you choose to provide a blog post (or another medium), your project report
should have the following structure:

1. Section 1: Project Definition
    * Project Overview: state the high-level overview of the project, including the background information such as
      problem
      domain, project origin, and related data sets or input data.
    * Problem Statement: define the problem to be solved.
    * Metrics: define the metrics to measure the results and justifications to use the metrics. For example, if you use
      time-series data sets, what metrics will be appropriate to measure the results.

2. Section 2: Analysis
    * Data Exploration: describe the data sets, including the features, data distributions, and descriptive statistics.
      Identify any abnormalities or specific characteristics inherent in the data sets.
    * Data Visualization: build data visualization based on the data exploration in the previous step.

3. Section 3: Methodology
    * Data Preprocessing: describe the steps taken to preprocess the data and address any abnormalities in the data
      sets. If
      data preprocessing is not needed, please explain why.
    * Implementation: discuss the process using the models, algorithms, and techniques applied to solve the problem. Any
      complications during the implementation should be mentioned.
    * Refinement: describe the process to refine the algorithms and techniques, such as using cross-validation or
      changing the
      parameter settings.

4. Section 4: Results
    * Model Evaluation and Validation: discuss the models and parameters used in the methodology. If no model is used,
      students can discuss the methodology using data visualizations and other means.
    * Justification: discuss the final results in detail and explain why some models, parameters, or techniques perform
      better
      over others. Show and compare the results in tabular forms or charts.

5. Section 5: Conclusion
    * Reflection: summarize the end-to-end problem solution and discuss one or two particular aspects that you find
      interesting or difficult to implement.
    * Improvement: provide suggestions for the next research to improve the experiment.

## Starbuck's Capstone Challenge

### Dataset overview

* The program used to create the data simulates how people make purchasing decisions and how those decisions are
  influenced by promotional offers.
* Each person in the simulation has some hidden traits that influence their purchasing patterns and are associated with
  their observable traits. People produce various events, including receiving offers, opening offers, and making
  purchases.
* As a simplification, there are no explicit products to track. Only the amounts of each transaction or offer are
  recorded.
* There are three types of offers that can be sent: buy-one-get-one (BOGO), discount, and informational. In a BOGO
  offer, a user needs to spend a certain amount to get a reward equal to that threshold amount. In a discount, a user
  gains a reward equal to a fraction of the amount spent. In an informational offer, there is no reward, but neither is
  there a requisite amount that the user is expected to spend. Offers can be delivered via multiple channels.
* The basic task is to use the data to identify which groups of people are most responsive to each type of offer, and
  how best to present each type of offer.

### Data Dictionary

#### profile.json

Rewards program users (17000 users x 5 fields)

* gender: (categorical) M, F, O, or null
* age: (numeric) missing value encoded as 118
* id: (string/hash)
* became_member_on: (date) format YYYYMMDD
* income: (numeric)

#### portfolio.json

Offers sent during 30-day test period (10 offers x 6 fields)

* reward: (numeric) money awarded for the amount spent
* channels: (list) web, email, mobile, social
* difficulty: (numeric) money required to be spent to receive reward
* duration: (numeric) time for offer to be open, in days
* offer_type: (string) bogo, discount, informational
* id: (string/hash)

#### transcript.json

Event log (306648 events x 4 fields)

* person: (string/hash)
* event: (string) offer received, offer viewed, transaction, offer completed
* value: (dictionary) different values depending on event type
* offer id: (string/hash) not associated with any "transaction"
* amount: (numeric) money spent in "transaction"
* reward: (numeric) money gained from "offer completed"
* time: (numeric) hours after start of test