#!/usr/bin/bash
echo "Value to be entered into the test database: "
read test

printf "insert into walnut_bams(entry_id) values(\"$test\");" | sqlite3 test.sqlite 
