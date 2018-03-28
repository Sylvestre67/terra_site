#!/usr/bin/env bash

cd ./main && yarn run build
cd ..

python manage.py collectstatic --no-input

gsutil rm gs://$GCS_BUCKET_NAME/static/*
gsutil rsync -R staticfiles/ gs://$GCS_BUCKET_NAME/static/

cp app.template.yaml  app.yaml

sed -i -e 's/<gsql_instance_name>/'"$GSQL_INSTANCE_NAME"'/g' app.yaml

sed -i -e 's/<secret_key>/'"$SECRET_KEY"'/g' app.yaml

gcloud app deploy -q

rm ./app.yaml
rm ./app.yaml-e
