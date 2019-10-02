class point:
    p1=(1,2,3)
    p2=(6,7,8)
    def __init__(self, dim, data):
        self.dim=dim
        self.data=[]
        for i in range(dim):
            self.data.append(float(data[i]))
    def __repr__(self):
        output=""
        for i in self.data:
            output+=str(i)+" "
        return output
    def __add__(self,p2):
        max_len=len(self.data)
        if len(p2.data)>max_len:
            max_len=len(p2.data)
        data=[]
        for i in range(max_len):
            total=0
            if i < len(self.data):
                total+=self.data[i]
                if i < len(p2.data):
                    total+=p2.data[i]
                data.append(total)
            return Point(max_len, data)

    def __sqmag__(self):
        total=0
        for i in self.data:
            total+=i*i
        return total


    j=list(p1.add(p2))
    k=list(p1.sqmag())
print(j,k)