#include "../inc/transmition.h"

/* Initialize everything (The RP and all the configurations) */
void init_transmition(){
	pthread_cond_init(&new_data,NULL);
	pthread_mutex_init(&mutex,NULL);
	pthread_cond_init(&arrived_configuration,NULL);
	pthread_mutex_init(&mutex_configuration,NULL);

	stop = 0;

	/* Launch the transmission protocol */
	pthread_create(&transmition_thread, NULL, transmition, NULL);
}

/* Init the fifos */
void init_fifos(int* fifo_configuration_fd) {
	if (mkfifo("/tmp/FIFOCONFIGURATION", S_IRUSR|S_IWUSR|S_IRGRP|S_IWGRP) != 0) {
		if (errno != EEXIST) {
			perror("Creating the fifo FIFOCONFIGURATION. Error");
			exit(1);
		}
	}

	// Open the fifo configuration for reading
	if ((*fifo_configuration_fd = open("/tmp/FIFOCONFIGURATION", O_RDONLY)) < 0) {
		perror("Opening the fifo for reading. Error");
		exit(2);
	}
}

/* Close the fifos */
void end_fifos(int fifo_configuration_fd) {
	close(fifo_configuration_fd);
}

/* End the transmition */
void end_transmition() {
	stop = 1;
	pthread_join(transmition_thread, NULL);
	pthread_cond_destroy(&new_data);
    	pthread_mutex_destroy(&mutex);
	pthread_cond_destroy(&arrived_configuration);
    	pthread_mutex_destroy(&mutex_configuration);
}

void *transmition(void *p_data) {
	int fifo_configuration_fd = 0;
	char buffer = '0';
	int bufferRead[5] = {0};
	FILE* file = NULL;

	if( (file = fopen("/tmp/imageTemp.txt", "w")) == NULL) {
		exit(-2);
	}

	init_fifos(&fifo_configuration_fd);

	pthread_mutex_lock(&mutex_configuration);
	for(int i = 0; i < 5; i++) {
		for(int j = 0; j < 5; j++) {
			bufferRead[i] *= 10;
			if(!read(fifo_configuration_fd, &buffer, sizeof(char))) {
				fprintf(stdout, "Couldn't read\n");
				fflush(stdout);
			}
			bufferRead[i] += buffer-48;
		}
	}
	the_data.nb_images = bufferRead[0];
	the_data.ramp_size = bufferRead[1];
	the_data.ramp_position = bufferRead[2];
	the_data.buffer_size = bufferRead[3];
	the_data.decimation = bufferRead[4];
	the_data.data_length = the_data.buffer_size+1;
	the_data.data = malloc(the_data.data_length*sizeof(char));
	pthread_cond_signal(&arrived_configuration);
	pthread_mutex_unlock(&mutex_configuration);

	while(!stop) {
		pthread_mutex_lock(&mutex);
		pthread_cond_wait(&new_data, &mutex);
		fprintf(file, "%s\n", the_data.data);
		fflush(stdout);
		pthread_mutex_unlock(&mutex);
	}

	end_fifos(fifo_configuration_fd);
	free(the_data.data);
	fprintf(stdout, "Everything was closed\n");
	fflush(stdout);

	pthread_exit(NULL);
}
