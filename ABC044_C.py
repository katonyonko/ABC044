from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="044"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc060_a".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,A=map(int,input().split())
  x=list(map(int,input().split()))
  dp=[0]*5001
  dp[2500]=1
  for i in range(N):
    tmp=dp.copy()
    for j in range(min(5001-x[i]+A,5001)):
      tmp[j+x[i]-A]+=dp[j]
    dp=tmp
  print(dp[2500]-1)
  """ここから上にコードを記述"""

  print(test_case[__+1])