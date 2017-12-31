# -*- coding: utf-8 -*-
import time
start1 = time.clock()
print ([m * 100 + n * 10 + q for m in range(1, 10) for n in range(10) for q in range(1, 10) if m == q])
end1 = time.clock()
# 或者可以这样写
start2 = time.clock()
print ([m * 100 + n * 10 + m for m in range(1, 10) for n in range(10)])
end2 = time.clock()
print (end1 - start1, ':', end2 - start2)

# 运行结果:
# 0.0004983750166709952 : 0.00013066820588773667
# 很明显可以看出第二种方法的运行时间更短
