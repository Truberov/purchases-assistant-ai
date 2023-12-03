# purchases-assistant-ai
This is an interactive assistant for a participant in public procurement. The assistant is integrated into an existing business process automation service for bidders and is a recommendation system that helps the user navigate the legislation of public procurement.

## Built With
* Python
* GigaChain
* GigaChat
* FastApi
* ElasticSearch

## Getting Started

* docker-compose
  ```sh
  docker-compose up -d --build
  ```
## Usage 
`POST http:localhost:8080/`

`{"question": "Your question"}`

## Chain architecture
row_documents -> split -> summary -> split -> embed -> retrieve -> compress -> reorder -> prompt -> gigaChat
