
# PoetryDB API Testing Framework

This repository contains a testing framework for the [PoetryDB API](https://github.com/thundercomb/poetrydb), 
which allows users to retrieve and search for poems by various criteria such as title and author.

## Framework Overview

The testing framework is built using `pytest` and `requests`, making it easy to run automated API tests. 
The framework includes various test cases that validate the API responses for functionality and error handling.

### Key Tests

1. **Retrieve a Random Poem**: Tests the `/random` endpoint to ensure a random poem is returned with required fields.
2. **Search for Poems by Author**: Tests the `/author/{author}` endpoint to confirm that poems are returned for a specified author.
3. **Retrieve a Poem by Title**: Tests the `/title/{title}` endpoint to validate that the correct poem is returned by title.
4. **Error Handling for Non-Existent Author**: Verifies that an error response is given when searching for a non-existent author.

## Getting Started

### Prerequisites

Ensure you have Python installed. Then install the necessary packages:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
pytest
requests
```

### Running the Tests

To run the tests, simply execute:

```bash
pytest
```

This will run all test cases and display the results in the terminal.

## Test Details

### 1. Retrieve a Random Poem

- **Description**: Tests the `/random` endpoint to verify that a random poem is returned with required fields.
- **Expected Result**: The response should have a `200` status code and include `title`, `author`, and `lines` fields.

### 2. Search for Poems by Author

- **Description**: Tests the `/author/{author}` endpoint to confirm that poems by a specified author are returned.
- **Expected Result**: The response should have a `200` status code, and each returned poem should have the correct `author`, `title`, and `lines` fields.

### 3. Retrieve a Poem by Title

- **Description**: Tests the `/title/{title}` endpoint to validate that the correct poem is returned by title.
- **Expected Result**: The response should have a `200` status code, and the returned poem should match the requested title and include `author` and `lines` fields.

### 4. Error Handling for Non-Existent Author

- **Description**: Verifies that an error response is given when searching for a non-existent author.
- **Expected Result**: The response should have a `200` status code, but the content should include `status: 404` and `reason: "Not found"`.

## Additional Information

For more details on the PoetryDB API and endpoints, visit the [PoetryDB GitHub page](https://github.com/thundercomb/poetrydb).

