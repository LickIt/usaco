/*
ID: giliev91
LANG: C++
TASK: ariprog
*/
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int N, M;
    ofstream fout("ariprog.out");
    ifstream fin("ariprog.in");
    fin >> N >> M;

    int max_bisq = M * M * 2 + 1;
    bool *is_bisq = new bool[max_bisq];
    fill(is_bisq, is_bisq + sizeof(is_bisq), false);

    for (int i = 0; i <= M; i++)
        for (int j = i; j <= M; j++)
            is_bisq[i * i + j * j] = true;

    int max_a = 0;
    int *bisq = new int[max_bisq];
    for (int i = 0; i < max_bisq; i++)
        if (is_bisq[i])
            bisq[max_a++] = i;

    int total = 0;
    int max_b = max_bisq / (N - 1) + 2;
    for (int b = 1; b <= max_b; b += 1)
        for (int a = 0; a < max_a; a++)
        {
            int x = bisq[a];
            int i = 0;
            for (i = 0; i < N; i++)
            {
                if (x >= max_bisq || !is_bisq[x])
                    break;
                x += b;
            }

            if (i == N)
            {
                fout << bisq[a] << " " << b << "\n";
                total++;
            }
        }

    if (total == 0)
        fout << "NONE\n";
    return 0;
}