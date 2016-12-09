#include "../inc/transmition.h"

int main() {
	/* Variable Declaration and Initialization */
	int i = 0, j = 0;
	int nb_tirs = 128;
	char *pixel_buffer = NULL;

	/* Initialization */
	init_transmition();

	pthread_mutex_lock(&mutex_configuration);
	pthread_cond_wait(&arrived_configuration, &mutex_configuration);
	pthread_mutex_unlock(&mutex_configuration);

	if((pixel_buffer = malloc(the_data.data_length * sizeof(char))) == NULL)
		exit(-1);

	for(i = 0; i < the_data.data_length; i++)
		pixel_buffer[i] = 66;

	/* Main routine */
	for(j = 0; j < the_data.nb_images; j++) {
		for(i = 0; i < nb_tirs; i++) {
			pixel_buffer[0] = 65;
			pthread_mutex_lock(&mutex);
			fprintf(stdout, "Acquiring\n");
			fflush(stdout);
			sprintf(the_data.data, "%s", pixel_buffer);
			pthread_cond_signal(&new_data);
			pthread_mutex_unlock(&mutex);
			usleep(300);
		}
	}

	end_transmition();

	free(pixel_buffer);

	return EXIT_SUCCESS;
}
