function [sigfilter] = filtsigsq (sig,fe,N,fmin,fmax)
%filtsig2 give the choice to choose the windows apply for filtering,
%and return envelop of the signal

%frequential step
df=fe/N;

%size of the window
Nmin=floor(fmin/df)+1;
Nmax=floor(fmax/df)+1;
Np=Nmax-Nmin+1;

wint=zeros(N,1);
wint(Nmin:Nmax)=1;
%filtering routhly
SIG=fft(sig).*wint;

sigfilter=abs(ifft(SIG));  

end
