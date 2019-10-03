#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

int main()
{
   int A=10;
   int B=5;
   vector<vector<int> >v;
   vector<int>v2;
   int minn=min(A,B);
   minn--;
   int val=A+B-2;
   v2.push_back(1);
   v.push_back(v2);
   v2.clear();
   v2.push_back(1);
   v2.push_back(1);
   v.push_back(v2);
  
int temp1;
int temp2;
   for(int i=2;i<=val;i++)
   {
        v2.clear();
        v2.push_back(1);
        int x=min(i,minn);
       for(int j=1;j<=x;j++)
       {	
			if((i-1)<j)
			temp1=0;
			else 
			temp1 = v[i-1][j];
		
			if((i-1)<(j-1))
			temp2=0;
			
			else
			temp2 = v[i-1][j-1];

           cout<<(temp1+temp2)<<" ";
           v2.push_back(temp1+temp2);
           
       }
      
       v.push_back(v2);
       cout<<endl;
       
   }
   

	
}