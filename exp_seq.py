class fastafile:
    def __init__(self,filelocation):
        self.filelocation = filelocation
        self.data = {}

    def read(self):
        self.data = {}
        with open(self.filelocation,'r') as file:
            curr_head,curr_seq='',''
            for line in file:
                if line.startswith('>'):
                    if not(curr_head==''):
                        self.data[curr_head]=curr_seq
                    curr_head=line.rstrip()[1:]
                    curr_seq = ''
                else:
                    curr_seq+=line.rstrip()
        if not(curr_head==''):
            self.data[curr_head]=curr_seq

    def write(self,location):
        with open(location,'w') as file:
            for seqs in list(self.data.keys()):
                file.write('>'+str(seqs)+'\n')
                file.write(str(self.data[seqs]))
