#!/bin/bash

echo''

while true; do
    read -p "${nl}Would you like to delete previously built docker image? (Y/n/v):${nl}(HINT: To view current images, press 'v'): " yn
    case $yn in
        [Y]* )
            echo -e "\nDeleting previous build image..."
            docker kill $(sudo docker ps -q --filter "name=autosave_songmoana")
            docker rmi -f $(sudo docker images -q --filter "reference=autosave_songmoana")
            echo -e "\nDONE"
            break;;
        [n]* )
            echo -e "Keeping the previously built image, moving on...\n"
            break;;

        [v]* )
            echo ""
            docker image ls
            echo ""
            ;;
        *) echo "Please answer either Y or n, input: '$REPLY'";;
    esac
done



PS3="${nl}--------------- Select your choice? ¯\_( ツ)_/¯ ${nl}(1 : Build Image / 2 : Run Server / 3 : View Docker Images / 4 : Quit): "
options=("Build Image" "Run Server" "View Docker Images" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Build Image")
            echo -e "\nCreating image...\n"
            docker build -f Dockerfile -t autosave_songmoana .
            echo ""
            ;;

        "Run Server")
        echo -e "\nRunning server...\n"
        docker run -it --name autosave_songmoana --env-file=.env -v /home/mark16/workspace/src/sprint1/auto_save/:/app/ --rm -p $port:9999 autosave_songmoana
        ;;

        "View Docker Images")
            echo ""
            sudo docker image ls
            echo ""
            ;;

        "Quit")
            break
            ;;
        *) echo "invalid option '$REPLY'"
    esac
done