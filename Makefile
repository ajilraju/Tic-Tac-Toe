build:
	# Build the container from the source
	sudo docker build -t tictactoe .
run:
	# Run the container as read-only
	sudo docker run --name tictactoe --rm --read-only -i tictactoe
pull-run:
	# Pull the image from the docker hub and run it.
	sudo docker run --rm --read-only ajilraju/tictactoe

clean:
	# clean the images for the tictactoe
	sudo docker rmi tictactoe
