#include "test_client_web.h"

#include<signal.h>
#include<math.h>

#define Port 9000 
#define Nset 8

static int sock;

void ctrlc(int signum)
{
	printf("oquin\n");
	close(sock);
	exit(signum);
}

int main(int arg, char *argv[])
{
	signal(SIGINT,ctrlc);

	int nsample, i, j, k;
	SOCKADDR_IN sin={0};
	struct hostent *hostinfo=NULL;
	const char *IP="92.243.29.92";

	//buffers parameters
	char buff[Nset], rep[Nset];	
	int *intbuff=(int *)malloc(Nset*sizeof(int));

	//Create socket
	sock=socket(AF_INET, SOCK_STREAM, 0);
	if (sock==INVALID_SOCKET)
	{
		perror("socket()");
		exit(errno);
	}

	sin.sin_addr.s_addr=inet_addr(IP);
	sin.sin_family=AF_INET;
	sin.sin_port=htons(Port);

	if (connect(sock, (SOCKADDR *) &sin, sizeof(SOCKADDR))==SOCKET_ERROR)

	{
		perror("connect()");
		exit(errno);
	}

	printf("Connected\n");

	int tmp=0;
	char ctmp;
	while(1)
	{

		printf("waiting for settings...\n");
		if(recv(sock, buff, Nset, MSG_WAITALL)==0)
		{
			printf("Server closed\n");
			break;
		}
		printf("done\n");
		printf("%s\n",buff);

		for (i=0 ; i<Nset ; i++)
		{
			ctmp=buff[i];
			intbuff[i]=(int)(ctmp);
			rep[i]=(char)intbuff[i];
			printf("intbuff[%d]=%d\n",i,intbuff[i]);
		}

		nsample=(int)(2.0*(double)(intbuff[2]-intbuff[1])*125.0/1.48/(double)(intbuff[0]));
		if (nsample>16384){nsample=16384;}
		printf("nsample=%i\n",nsample);

		//send(sock,rep,Nset,0);
			
		char ** tmpbuff=(char **)malloc(intbuff[6]*sizeof(char *));
		for (i=0 ; i<intbuff[6] ; i++)
		{
			tmpbuff[i]=(char *)malloc(nsample*sizeof(char));
		}

		for (k=0 ; k<intbuff[7] ; k++)
		{
			for (j=0 ; j<intbuff[6] ; j++)
			{
				for (i=0 ; i<nsample ; i++)
				{
					//fscanf(fmat,"%c ",&tmpbuff[j][i]);
					tmp=(k+1)*(j+1)%256;
					tmpbuff[j][i]=(char)(tmp);
					//printf("tmpbuff[%i][%i]=:%i\n",j,i,tmp);
				}
			send(sock,tmpbuff[j],nsample,0);
			printf("line %i, image %i\n",j,k);
			}
		}

		free(tmpbuff);
	}

	close(sock);
	free(intbuff);
	return 0;
}
