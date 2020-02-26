#! /usr/bin/env python
from modules import articles, authors, error_status


def main():
    articles.print_articles()
    authors.print_authors()
    error_status.print_error_status()

#
if __name__ == '__main__':
    main()
