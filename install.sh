clear
echo "                                                         "
echo "Preparing environment ... "
echo "_________________________________________________________"
virtualenv env
echo "_________________________________________________________"
echo "                                                         "
echo "Installing required packages ..."
echo "_________________________________________________________"
./env/bin/pip install -r requirements.txt
echo "Done"