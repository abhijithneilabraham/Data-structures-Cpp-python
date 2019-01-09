#include<iostream>

using namespace std;
  class creditcard{
  private :
    string customer;
    string bank;
    string account;
    int limit;
 int balance;
public:
 creditcard(): customer("Abhijith"),account("12002100"),bank("SBI"),limit(10000),balance(500){}

 int charge(int pay){
 balance=balance-pay;
 return balance;
 }
};

int main(){

creditcard c1;

  int bal;
  bal=c1.charge(100);
  cout<<"balance"<<bal;
  return 0;
}
