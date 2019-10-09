# Simple bash script to build the Gnome Shell extension

FILE=docker_integration_fr@faustor21.zip

echo "Zipping the extension..."
rm $FILE
zip -r $FILE . -x@exclude.lst

echo "Done building."

