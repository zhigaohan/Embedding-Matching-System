# Embedding-Matching-System

This example shows how to build an end-to-end real-time text semantic search:
1. Extract text embeddings of Wikipedia titles from BigQuery, 
using the [Universal Sentence Encoder](https://tfhub.dev/google/universal-sentence-encoder/2) module,
via Cloud Dataflow. 
2. Build an approximate similarity matching index using Spotify’s [Annoy](https://github.com/spotify/annoy)
library, via Cloud ML Engine.
3. Serve the index for real-time search queries in a [Flask](http://flask.pocoo.org/)
web application, via Google AppEngine.

To run the end-to-end example, we need to execute the following script files,
after setting following configuration parameters:
1. embedding extraction/run.sh
2. index/submit.sh
3. semantic_search/deploy.sh

## Requirements
1. Have your [GCP Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).
2. Use [Cloud Shell](https://cloud.google.com/shell/docs/quickstart) 
or [gcloud CLI](https://cloud.google.com/sdk/) to run all the commands in this
guideline.



## Setup python environment and sample code

Follow commands below to install required python packages and download a
Dataflow pipeline code.

```bash
git clone [this-repo]
cd [this-repo]

pip install -r requirements.txt
```

## 1. Run the Dataflow pipeline for embedding extraction

With configuration file embedding extraction/run.sh, run the pipeline by executing the **run.sh** script file

```bash
bash embedding extraction/run.sh
```

## 2. Use Cloud ML Engine job to build the index

Use Cloud ML engine to submit the job by executing the **submit.sh** script file:

```bash
bash index/submit.sh
```

## 3. Deploy semantic search app to AppEngine 

Deploy the app to AppEngine by executing the **deploy.sh**
script file:

```bash
bash semantic_search/deploy.sh
```
