import pytest
from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""
@pytest.mark.skip
def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"

"""
We can format artists to strings nicely
"""
@pytest.mark.skip
def test_artists_format_nicely():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
@pytest.mark.skip
def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist", "Test Genre")
    artist2 = Artist(1, "Test Artist", "Test Genre")
    assert artist1 == artist2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
