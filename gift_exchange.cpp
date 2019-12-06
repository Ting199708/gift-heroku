#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include <vector>
#define people_num 10
using namespace std;

string name[people_num];
string phonenumber[people_num];
string address[people_num];
int good_list[people_num];
int bad_list[people_num];
void read(string filename, string *arr);
void gift();

int main()
{
    read("./name.txt", name);
    read("./phonenumber.txt", phonenumber);
    read("./address.txt", address);
    gift();

    ofstream outFile("good.txt", ios::app);
    for (int i = 0; i < people_num; i++)
    {
        outFile << name[good_list[i]] << endl;
        outFile << phonenumber[good_list[i]] << endl;
        outFile << address[good_list[i]] << endl;
    }
    ofstream outFile2("bad.txt", ios::app);
    for (int i = 0; i < people_num; i++)
    {
        outFile2 << name[bad_list[i]] << endl;
        outFile2 << phonenumber[bad_list[i]] << endl;
        outFile2 << address[bad_list[i]] << endl;
    }
    
}

void read(string filename, string *arr)
{

    ifstream inFile(filename, ios::in);
    string str;

    for (int i = 0; i < people_num; i++)
    {
        getline(inFile, str);
        arr[i] = str;
    }
}

void gift()
{
    vector<int> random;
    srand(time(NULL));

    //good
    for (int i = 0; i < people_num; i++)
    {
        random.insert(random.end(), i);
    }
    for (int i = 0; i < people_num; i++)
    {
        int x = rand() % random.size();
        int count = 0;
        while (random.at(x) == i)
        {
            x = rand() % random.size();
            count++;
            if (count == 20)
            {
                gift();
                break;
            }
        }
        good_list[i] = random.at(x);
        random.erase(random.begin() + x);
    }

    //bad
    srand(time(NULL));
    for (int i = 0; i < people_num; i++)
    {
        random.insert(random.end(), i);
    }
    for (int i = 0; i < people_num; i++)
    {
        int x = rand() % random.size();
        int count = 0;
        while (random.at(x) == i || random.at(x) == good_list[i])
        {
            x = rand() % random.size();
            count++;
            if (count == 20)
            {
                gift();
                break;
            }
        }
        bad_list[i] = random.at(x);
        random.erase(random.begin() + x);
    }
}