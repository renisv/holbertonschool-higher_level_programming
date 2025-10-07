#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder and saves to CSV file"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts_data = response.json()
        structured_posts = []

        for post in posts_data:
            post_dict = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(post_dict)

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)

        print("Posts have been saved to posts.csv")
        print(f"Total posts saved: {len(structured_posts)}")

    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
