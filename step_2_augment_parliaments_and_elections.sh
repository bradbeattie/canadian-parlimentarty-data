#!/bin/bash
./manage.py check && \
flake8 --ignore E501 parliaments proceedings elections localsite && \
mysql parliamentary_data < after-step-1.sql && \
./manage.py augment_elections_wiki && \
./manage.py augment_ridings_lop && \
./manage.py augment_ridings_ec && \
./manage.py augment_parties_lop_parliament && \
./manage.py augment_parties_lop_party && \
./manage.py augment_parties_wiki && \
./manage.py augment_parties_ec && \
./manage.py augment_parliamentarians_op && \
./manage.py augment_parliamentarians_hoc && \
./manage.py augment_ridings_fsas && \
mysqldump parliamentary_data > after-step-2.sql
