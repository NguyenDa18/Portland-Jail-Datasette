# Portland Inmates Datasette

[Website](https://pdx-inmates-database.vercel.app/)

Analysis of [Portland Inmates data scraped](https://github.com/NguyenDa18/Portland-Jail-Data-Crawler)

Creates SQLite database with `inmate_details` and `inmate_charges` tables
[Datasette](https://datasette.io/) publishes the data as explorable tables

## Prerequisites

- `datasette`
- `datasette-publish-vercel`

## Running

- [Install Datasette](https://docs.datasette.io/en/stable/installation.html#installation)

- Run `datasette inmate_details.db --open` from the command line