function [xb,sb] = intsignotsafe (x,s,N)
%function that return a signal sb wich values are the integration of s over each N points
%pgcd(Nb,N) must be equal to N so N is 2^n

Nb=length(x);

Nnew=floor(Nb/N);

dx=x(N+1)-x(1);
xb=x(1):dx:x(end);

sb=zeros(Nnew,1);

for (temp=0:Nnew-1)
  sb(temp+1)=sum(s(N*temp+1:N*(temp+1)));
end

end