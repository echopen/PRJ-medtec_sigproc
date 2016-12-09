clear all;
close all;

%sig=load('../test/moyt0.txt');
sig=load('../data/raw_data.txt');
sig=sig(:,2:end);


fe=125;  %sampling rate in MHz
N=16384; %number of data in each line
nint=32; %nomber of data on which we integrate
xf=10;   %data set to 0 form x=0 to x=xf
nbrLine = 61;  %number of line in the

t=0:1:N-1;
x=1.5*t/fe/2;


for temp=1:nbrLine
  sig(temp,:)=sig(temp,:)-mean(sig(temp,:));
endfor

temp=1;
while (x(temp)<xf)
  sig(:,temp)=0;
  temp=temp+1;
end

figure(10)
plot(sig(43,:));

data=zeros(nbrLine,512);
% boucle sur les lignes
for counter=1:nbrLine

  sigLine = transpose(sig(counter,:));
  sigpt=filtsigsq(sigLine,fe,N,5.5,9.5);

 S1=(sigpt).^2;
 [Xi,S1i]=intsignotsafe(x,S1,nint);
 
 data(counter,:) = S1i;
end

maxdata = max(max(data));
data=data/maxdata;
data=10*log(data);

max(max(data))
min(min(data))

line=0:60;

figure(1)
surf(Xi,line,data)
shading interp;
colormap bone;
view ([0 90]);
caxis([-80 0]);
xlim([Xi(1) Xi(end)]);
xlabel('x (mm)');
ylabel('line number');