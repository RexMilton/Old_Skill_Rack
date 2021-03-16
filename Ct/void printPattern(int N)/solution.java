private static void printPattern(int N) {
    int l=1,n=1;
    while(l<=N){
        if(l%2!=0)
        for(int i=0;i<l;i++)
        System.out.print(n+++" ");
        else
        for(int i=0;i<l;i++)
        System.out.print(l-1-i-i+n+++" ");
        System.out.println();
        l++;
    }
}
