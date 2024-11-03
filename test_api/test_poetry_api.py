import pytest
from api.api_controller import ApiController


# Test Case 1: Retrieve a Random Poem
def test_retrieve_random_poem():
    """
    Test retrieving a random poem and verify that the response contains the
    necessary poem data.
    """
    api = ApiController()

    # Step 1: Send a GET request to retrieve a random poem
    response = api.get_random_poem()

    # Step 2: Verify the response status code is 200
    assert response.status_code == 200, "Expected status code 200"

    # Step 3: Verify the response body structure
    poem_data = response.json()
    assert isinstance(poem_data, list) and len(poem_data) > 0, "Expected a list with at least one poem"
    poem = poem_data[0]

    # Check that the necessary fields are present
    assert "title" in poem, "Expected 'title' field in poem data"
    assert "author" in poem, "Expected 'author' field in poem data"
    assert "lines" in poem, "Expected 'lines' field in poem data"

    # Check that 'lines' is a list of strings
    assert isinstance(poem["lines"], list), "'lines' should be a list"
    assert all(isinstance(line, str) for line in poem["lines"]), "All items in 'lines' should be strings"


# Test Case 2: Search for Poems by Author
@pytest.mark.parametrize("author_name", ["Emily Dickinson"])
def test_search_poems_by_author(author_name):
    """
    Test searching for poems by a specific author and verify that all returned
    poems are by the specified author.
    """
    api = ApiController()

    # Step 1: Send a GET request to search poems by author
    response = api.get_poem_by_author(author_name)

    # Step 2: Verify the response status code is 200
    assert response.status_code == 200, "Expected status code 200"

    # Step 3: Verify the response body structure
    poems_data = response.json()
    assert isinstance(poems_data, list) and len(poems_data) > 0, "Expected a list with at least one poem"

    for poem in poems_data:
        # Check that the 'author' field matches the specified author
        assert poem.get("author") == author_name, f"Expected author '{author_name}'"

        # Check that each poem has 'title' and 'lines' fields
        assert "title" in poem, "Expected 'title' field in poem data"
        assert "lines" in poem, "Expected 'lines' field in poem data"

        # Check that 'lines' is a list of strings
        assert isinstance(poem["lines"], list), "'lines' should be a list"
        assert all(isinstance(line, str) for line in poem["lines"]), "All items in 'lines' should be strings"


# Test Case 3: Retrieve a Poem by Title
@pytest.mark.parametrize("title, expected_author", [
    ("The Raven", "Edgar Allan Poe")
])
def test_retrieve_poem_by_title(title, expected_author):
    """
    Test retrieving a specific poem by title and verify that the returned data
    matches the requested title.
    """
    api = ApiController()

    # Step 1: Send a GET request to retrieve a poem by title
    response = api.get_poem_by_title(title)

    # Step 2: Verify the response status code is 200
    assert response.status_code == 200, "Expected status code 200"

    # Step 3: Verify the response body structure and content
    poem_data = response.json()
    assert isinstance(poem_data, list) and len(poem_data) > 0, "Expected a list with at least one poem"
    poem = poem_data[0]

    # Check that the title and author match the expected values
    assert poem.get("title") == title, f"Expected title '{title}'"
    assert poem.get("author") == expected_author, f"Expected author '{expected_author}'"

    # Check that 'lines' is a list of strings
    assert "lines" in poem, "Expected 'lines' field in poem data"
    assert isinstance(poem["lines"], list), "'lines' should be a list"
    assert all(isinstance(line, str) for line in poem["lines"]), "All items in 'lines' should be strings"


# Test Case 4: Error Handling for Non-Existent Author
@pytest.mark.parametrize("non_existent_author", ["Unknown Author"])
def test_non_existent_author(non_existent_author):
    """
    Test searching for poems by a non-existent author and verify that the API
    returns an appropriate error response.
    """
    api = ApiController()

    # Step 1: Send a GET request to search for poems by a non-existent author
    response = api.get_poem_by_author(non_existent_author)

    # Step 2: Verify the response status code is 200 but contains a 404 error in the content
    assert response.status_code == 200, "Expected status code 200"

    # Step 3: Verify the content of the response indicates a 404 error
    error_data = response.json()
    assert error_data.get("status") == 404, "Expected status 404 in response content"
    assert "Not found" in error_data.get("reason", ""), "Expected 'Not found' message in response content"