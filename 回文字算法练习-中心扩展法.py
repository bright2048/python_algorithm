#寻找最长回文串
def getHuiwen(s):
	if len(s)<2:
		return s
	start,end=0,0
	max_len=0
	def getLength(left,right):
		while left>=0 and right<len(s) and s[left]==s[right]:
			left-=1
			right+=1
		return right-left-1
	for x in range(len(s)):
		len1=getLength(x,x)
		len2=getLength(x,x+1)
		max_len=max(len1,len2)
		if max_len>(end-start):
			start=x-(max_len-1)//2  #这里减1，主要是针对双字母对称结构。max_len最终一定为偶数，比如len为8（双字母对称回文，长度必偶数），8除以2等于4，而x为3,3-4变成-1了。
			end=x+(max_len)//2
	return s[start:end+1]


def main():
	print(getHuiwen("abcddcba"))
if __name__ == '__main__':
	main()
