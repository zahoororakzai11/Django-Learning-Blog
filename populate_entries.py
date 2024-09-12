from datetime import date
from authentications.models import Blog, Author, Entry

# Insert multiple Blog records
blogs = [
    Blog(name="Tech Trends", tagline="The latest in tech news and trends."),
    Blog(name="Healthy Living", tagline="Tips and advice for a healthier lifestyle."),
    Blog(
        name="Travel Diaries", tagline="Exploring the world one destination at a time."
    ),
]

Blog.objects.bulk_create(blogs)

# Insert multiple Author records
authors = [
    Author(name="Alice Smith", email="alice@example.com"),
    Author(name="Bob Johnson", email="bob@example.com"),
    Author(name="Charlie Brown", email="charlie@example.com"),
]

Author.objects.bulk_create(authors)

# Insert multiple Entry records with associated Blog and Author relationships
entries = [
    Entry(
        blog=blogs[0],  # Associate with the first blog
        headline="The Future of AI",
        body_text="Exploring the potential of artificial intelligence in various industries...",
        pub_date=date(2024, 9, 1),
        mod_date=date.today(),
        number_of_comments=10,
        number_of_pingbacks=2,
        rating=5,
    ),
    Entry(
        blog=blogs[1],  # Associate with the second blog
        headline="10 Tips for a Balanced Diet",
        body_text="Learn how to maintain a healthy and balanced diet with these simple tips...",
        pub_date=date(2024, 9, 2),
        mod_date=date.today(),
        number_of_comments=5,
        number_of_pingbacks=1,
        rating=4,
    ),
    Entry(
        blog=blogs[2],  # Associate with the third blog
        headline="Top 5 Destinations for 2024",
        body_text="Discover the top travel destinations for the upcoming year...",
        pub_date=date(2024, 9, 3),
        mod_date=date.today(),
        number_of_comments=8,
        number_of_pingbacks=3,
        rating=5,
    ),
]

Entry.objects.bulk_create(entries)

# Associate authors with entries
entry_1 = entries[0]
entry_2 = entries[1]
entry_3 = entries[2]

entry_1.authors.add(authors[0], authors[1])  # Add Alice and Bob to the first entry
entry_2.authors.add(authors[1], authors[2])  # Add Bob and Charlie to the second entry
entry_3.authors.add(authors[0], authors[2])  # Add Alice and Charlie to the third entry
