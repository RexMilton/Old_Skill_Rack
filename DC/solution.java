class Node implements Pair{
        public long getHCF(int a, int b){
            if(a==0) return b;
            else return getHCF(b%a,a);
        }
        public boolean areCoPrime(int a, int b){
            if(getHCF(a,b)==1) return true;
            return false;
        }
    }
