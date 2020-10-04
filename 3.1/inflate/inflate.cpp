/*
ID: giliev91
LANG: C++
TASK: inflate
*/
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("inflate.in");
    ofstream fout("inflate.out");

    int M, N;
    fin >> M >> N;

    int *points = new int[N];
    int *time = new int[N];
    for (int i = 0; i < N; i++)
    {
        fin >> points[i] >> time[i];
    }

    int *best = new int[M + 1];
    fill(best, best + sizeof(best), 0);
    for (int i = 0; i <= M; i++)
        for (int j = 0; j < N; j++)
            if (i >= time[j])
                if (best[i] < best[i - time[j]] + points[j])
                    best[i] = best[i - time[j]] + points[j];

    fout << best[M] << "\n";
    return 0;
}