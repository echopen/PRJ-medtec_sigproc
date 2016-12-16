#ifndef TRANSMITION_H
#define TRANSMITION_H

#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <sys/stat.h>

#include "common.h"

pthread_t transmition_thread;
pthread_cond_t new_data;
pthread_mutex_t mutex;
pthread_cond_t arrived_configuration;
pthread_mutex_t mutex_configuration;
int stop;

typedef struct data_to_send_ {
	int nb_images;
	int buffer_size;
	int decimation;
	char *data;
	int data_length;
	int ramp_size;
	int ramp_position;
}data_to_send;

data_to_send the_data;

void init_transmition();

void end_transmition();

void init_fifos(int* fifo_configuration_fd);

void end_fifos(int fifo_configuration_fd);

void *transmition(void *p_data);

#endif
