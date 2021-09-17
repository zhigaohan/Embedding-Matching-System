

# Configurable parameter
PROJECT=""

[[ -z "${PROJECT}" ]] && echo "PROJECT not set" && exit 1

echo "App Engine deployment started..."

# Command to deploy an app to AppEngine
gcloud --verbosity=info -q app deploy app.yaml --project="${PROJECT}"

echo "App Engine Deployment Finished."
