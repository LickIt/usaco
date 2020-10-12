/*
ID: giliev91
LANG: C++
TASK: stamps
*/
#include <iostream>
#include <fstream>
using namespace std;
#define MAXM 10000000

int main()
{
    ifstream fin("stamps.in");
    ofstream fout("stamps.out");

    int K, N;
    fin >> K >> N;

    int *stamps = new int[N];
    for (int i = 0; i < N; i++)
        fin >> stamps[i];

    unsigned char *s = new unsigned char[MAXM];
    s[0] = 0;
    int m = 0, min;

    while (s[m++] <= K)
    {
        min = MAXM;
        for (int i = 0; i < N; i++)
            if (m >= stamps[i] && s[m - stamps[i]] < min)
                min = s[m - stamps[i]];

        s[m] = min + 1;
    }

    fout << (m - 2) << "\n";
    return 0;
}