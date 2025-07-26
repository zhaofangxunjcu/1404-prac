class Band:
    """Band class for storing details of a band."""

    def __init__(self, name=""):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of the band with its members and their instruments."""
        if not self.members:
            return f"{self.name} (no members)"
        member_strs = ', '.join(str(m) for m in self.members)
        return f"{self.name} ({member_strs})"

    def __repr__(self):
        """Return detailed representation of the band."""
        return f"Band(name={self.name!r}, members={self.members!r})"

    def add(self, musician):
        """Add a Musician to the band."""
        self.members.append(musician)

    def play(self):
        """Return the result of each musician playing."""
        if not self.members:
            return f"{self.name} has no members!"
        # Each musician plays; join results by newline
        return '\n'.join(m.play() for m in self.members)
