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

- Make changes to `csv_to_db.py` file to generate a SQLite .db file that is used to generate a Datasette
- Run `csv_to_db.py` from the command line
- Run `datasette pdx_inmates_data.db --open` from the command line

## Deploying

- Run `vercel login` to login to Vercel account
- Run `datasette publish vercel`