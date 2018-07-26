## 7 reverse
> 反转输出一个数

* 转字符串重排。
* 也可以逐位求余。

## 9 isPalindrome
> 判断给定数字是否为回文数

* 负数不可能是
* 只有一位一定是
* 变成字符串逐位对比即可。

## 67 addBinary
> 给定两个二进制数，求和输出二进制。

* python内置了丰富的进制转换函数。
* 注意输出时要将'0b'去掉。

## 69 mySqrt
> 实现计算平方根整数

## 168 convertToTitle
> 转换成A~Z的26进制。

* 用chr(),ord()转换编码即可。

## 171 titleToNumber
> 168反向实现。

* 168反向计算。

## 172 trailingZeroes
> 求阶乘末尾有多少个0.

* 0的个数= n/5 + n/(5^2)+.......

## 231 isPowerOfTwo
> 确定给定的数是否为2的幂。

* 二进制下，相邻数的按位与可以将大数最后一位的1变0.
* 2的幂在二进制下只有最高位是1，其余皆为0.

## 258 addDigits
> 反复将各个位上的数字相加，直到结果为一位数。

* 既是除9的余数。

## 263 isUgly
> 确定一个数是否只由2，3，5组成。

* 2,3,5皆为素数，彼此之间不相干。

## 292 canWinNim
> 确定先手的情况下是否能够赢得Nim游戏。

* 因为每轮每人只能拿1~3颗石头，所以完全可控范围是每轮两个人加起来一共拿四颗石头。
* 所以只要先手拿起m颗石头，m=n%4即可保证胜利。
* 换而言之，只要石子数n除4有余数，先手即可保证胜利。（不失误）
* 反之，若能整除4，则后手必胜。（不失误）
	
## 367 isPerfectSquare
> 确定一个数是否是个整数的平方数。

* 用牛顿法迭代求解。

## 374 guessNumber
> 提供了判断函数，用二分法来逼近结果。

* 按照二分法思路逼近即可。

## 400 findNthDigit
> 找到数列中第n个字符是什么。

* 1-9每个数字有1个字符，10-99有两个字符，以此类推。

## 441 arrangeCoins
> 给定数字能容纳多大的等差数列。

* 联立等差数列求和公式和一元二次方程求根公式即可。

## 453 minMoves
> 用最小的次数，使数组内全部数字相等，每次可以将其中len-1个数+1.

* n个数，每次n-1个加一，在相对参照系下，既是每次可以将一个数-1.
* 将sum(nums)看做一个山，则海平面就是len(nums)*min(nums)。
* 把山移平只需要进行他们之差次-1。

## 492 constructRectangle
> 找到给定正整数的两个距离最近的正整除数。

* 用math模块下的sqrt定位到中心，以减少时间。

## 504 convertToBase7
> 将给定数字以七进制字符串输出。

* 循环余7除7即可。

## 507 checkPerfectNumber
> 判断一个数是否与其全部正整数因子之和相等。

* 用sqrt减小区间后遍历即可。

## 598 maxCount
> 找到一系列操作后，矩阵中最大数的个数。

* 题中矩阵的每次操作皆从左上角开始。
* 所以只需要寻找到ops中操作的行、列的最小值即可。

## 633 judgeSquareSum
> 确定一个数是否为两个数的平方和。

* 用sqrt确定最大可能值。
* min=0和max值双向逼近中点，若平方和低于n则min++，若高于n则max--，相等return true。

## 728 selfDividingNumbers
> 找到给定上下限内的全部自除数。

* 用range(下限，上限-1)来遍历。
* 转字符串遍历单个数字。

## 836 isRectangleOverlap
> 判断两个矩形是否有重叠

* 纸面推导即可。