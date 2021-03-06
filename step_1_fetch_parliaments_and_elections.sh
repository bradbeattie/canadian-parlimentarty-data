#!/bin/bash
./manage.py check && \
flake8 --ignore E501 parliaments proceedings elections localsite && \
mysql parliamentary_data < after-step-0.sql && \
./manage.py fetch_parliaments && \
./manage.py fetch_provinces && \
./manage.py fetch_sessions && \
./manage.py fetch_elections && \
./manage.py fetch_ridings && \
./manage.py fetch_parliamentarians && \
./manage.py fetch_election_ridings riding-populations-electors-and-rejected-ballots.ods && \
mysqldump parliamentary_data > after-step-1.sql
