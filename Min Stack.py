class MinStack:
    '''
    requires:
        -
    ensures:
        -
    algo:
        st: tuple[int] = []
        push := 
            if stack is empty: append (x, x)
            else:
                append (x, min(x, st.top().[1]))
        pop :=
            st.pop()[0]
        top :=
            st[-1][0]
        getMin :=
            st[-1][1]
    '''

    def __init__(self):
        self.st: list[int] = []

    def push(self, val: int) -> None:
        if self.st:
            self.st.append( (val, min(val, self.getMin())) )
        else:
            self.st.append( (val, val) )

    def pop(self) -> None:
        self.st.pop()
        return

    def top(self) -> int: 
        return self.st[-1][0]
        
    def getMin(self) -> int:
        return self.st[-1][1]