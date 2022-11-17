#include <iostream>
using namespace std;
struct node
{
    unsigned dist[20];
    unsigned from[20];
} rt[10];
int main()
{
    int dmat[20][20];
    int n, i, j, k, count = 0;
    // printf("\nEnter the number of nodes : ");
    cout<<"Enter The Number of noted: "<<endl;
    cin>>n;
    // scanf("%d", &n);
    // printf("\nEnter the cost matrix :\n");
    cout<<"Enter the codt matrix: "<<endl;
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
        {
            // scanf("%d", &dmat[i][j]);
            cin>>dmat[i][j];
            dmat[i][i] = 0;
            rt[i].dist[j] = dmat[i][j];
            rt[i].from[j] = j;
        }
    do
    {
        count = 0;
        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++)
                for (k = 0; k < n; k++)
                    if (rt[i].dist[j] > dmat[i][k] + rt[k].dist[j])
                    {
                        rt[i].dist[j] = rt[i].dist[k] + rt[k].dist[j];
                        rt[i].from[j] = k;
                        count++;
                    }
    } while (count != 0);
    for (i = 0; i < n; i++)
    {
        // printf("\n\nState value for router %d is \n", i + 1);
        cout<<"State Value for router "<< i+1 << endl;
        for (j = 0; j < n; j++)
        {
            // printf("\t\nnode %d via %d Distance%d", j + 1, rt[i].from[j] + 1, rt[i].dist[j]);
            cout<<"Node "<< j+1 <<" via " << rt[i].from[j] + 1 << " Distance " <<rt[i].dist[j]<<endl;
        }
    }
    // printf("\n\n");
    cout << endl;
}