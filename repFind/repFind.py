#!/usr/bin/env python
#coding:utf-8
import sys
import os
import argparse

def rep_find(rdseq, max_rep_unit=100):
    '''
    max_rep_unit 为指定最大的重复单元碱基数
    返回  (左端重复单元，左端重复单元重复次数，右端重复单元，右端重复单元重复次数)
    '''
    length = len(rdseq)  
    left,right = {},{}
    for j in range(1,min(max_rep_unit+1,length/2+1)):
        rep = [rdseq[:j],rdseq[-j:]]
        for i in range(0,length-j,j):            
            s = rdseq[i+j:i+j+j]
            if s != rdseq[:j]:              
                break
            rep[0] += s       
        else:                
            left.setdefault(rep[0],j)
            right.setdefault(rep[0],j)
            continue
        for i in range(-j,-length,-j):            
            s = rdseq[i-j:i]
            if s != rdseq[-j:]:
                break
            rep[1] = s + rep[1]
        if len(rep[0]) > j:
            left.setdefault(rep[0],j)
        else:
            left[rdseq[0]] = 1
        if len(rep[1]) > j:
            right.setdefault(rep[1],j)
        else:
            right[rdseq[-1]] = 1
    # print left,right
    o1,o2 = sorted(left.items(),key=lambda x:len(x[0]))[-1],sorted(right.items(),key=lambda x:len(x[0]))[-1]
    return o1[0][:o1[1]],len(o1[0])/o1[1],o2[0][:o2[1]],len(o2[0])/o2[1]
    
def parserArg():
    parser = argparse.ArgumentParser(description= "For finding the tendom repeats in both ends of you sequence.")  
    parser.add_argument("-u","--unit",type=int,help="the length max repeat units, default: 100",metavar="int",default=100)
    parser.add_argument("seqfile",type=str,default=sys.stdin,help="the input seqfile or seqsting, only seq string include. default: sys.stdin")
    parser.add_argument("-o","--outfile",type=argparse.FileType("w"),default=sys.stdout,help="the output file, default: sys.stdout",metavar="outfile")
    args = parser.parse_args()
    return args
    	         
def main():
    args = parserArg()
    args.outfile.write("left_rep_seq\tleft_rep_unit\tleft_rep_num\tright_rep_seq\tright_rep_unit\tright_rep_num\n".upper())
    if os.path.isfile(args.seqfile):
      with open(args.seqfile) as fi:
       for line in fi:
        line = line.strip()
        left,left_u,right,right_u = rep_find(line,args.unit)
        if len(left)==1 and left_u==1 and len(right) == 1 and right_u==1:
            continue
        if len(left) > 1 or left_u > 1:
            args.outfile.write(left*left_u + "\t" + left + "\t" + str(left_u) + "\t")
        else:
            args.outfile.write("-\t-\t-\t")
        if len(right) > 1 or right_u > 1:
            args.outfile.write(right*right_u + "\t" + right + "\t" + str(right_u) + "\n")
        else:
            args.outfile.write("-\t-\t-\n")            
    else:
        line = args.seqfile
        left,left_u,right,right_u = rep_find(line,args.unit)
        args.outfile.write(left*left_u + "\t" + left + "\t" + str(left_u) + "\t")
        args.outfile.write(right*right_u + "\t" + right + "\t" + str(right_u) + "\n")
        
if __name__ == "__main__":
    main()

