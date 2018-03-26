#!/usr/bin/env bash

echo $GSQL_INSTANCE_NAME

./cloud_sql_proxy -instances="$GSQL_INSTANCE_NAME"=tcp:3306
