# PyFest

A repository for hacktoberfest 2022

## Problem Statement

Music festivals have huge lineups, many with multiple stages for multiple days. Once you've seen the bands you know you love, how do you find the bands you didn't know you love?

## Available tools and data sources

Lineups are published months ahead of time in many formats. Many festivals have a dedicated Lineup Page.

Many bands have very public information available aout them, including thier top songs, genres, and associated acts. Wikipedia also contains information about the artists `influences` in some cases.

Many music streaming services have apis that allow playlists to be made through a programtic call.

## Solution statement

By processing the information on a festivals lineup page, a data set of the `artists` can be constructed automatically.

By using this `artists` data set information can be associated to each artist describing their acts, such as genre, associatate acts, and record labels to make `artist description` data sets.

By using the `artists description` data sets a first pass of likley good artists can be made according to criteria set by the user e.g. genre, number of albums, associated acts, influences to create a `suggested artists` data set.

By using the `suggested artists` data set you can curate a list of artists that might be a good fit for your music taste that you do not alredy know to create a `top songs` data set.

By using the `top songs` data set and a connection to a music streaming service you can create a `top songs playlist` in the streaming service.
