# 捕捉键盘输入

主要目的：
- 捕捉键盘输入
- 将键盘输入记录文件持久保存
- 统计击打键盘数
- 同步在桌面显示击打键盘数


@time: 2018-09-21 19:32  完成键盘记录功能
@time: 2018-09-22 19:32  完成输入记录文件功能
@time: 2018-09-25 21:00  完成统计击打键盘数目并根据频次进行输出
@time: 2018-09-26 20:00  完成再次需求分析
@time: 2018-09-26 22:00  完成单元测试补充

@todo
- thing：根据日期统计击打键盘数目，并输出
- time： 2018-09-28 22:00
- who： light


@当前统计结果显示：

```python
当前输入字符统计：

<backspace>:173
<enter>:135
i:134
n:116
a:112
left_ctrl:90
e:86
s:85
1:81
space:80
h:71
left_shift:61
t:61
o:60
u:60
c:53
d:48
<tab>:48
g:45
left_alt:41
p:29
r:28
x:28
w:27
m:27
j:23
v:22
.:20
y:19
::19
k:18
z:18
l:16
2:15
q:12
-:12
b:10
@:10
\:9
E:8
=:7
f:6
`:6
3:5
A:5
M:5
(:5
<esc>:4
,:4
;:4
R:4
D:4
':4
4:2
9:2
V:2
:1
right_shift:1
L:1
5:1
):1
W:1
```

可见打错字还是蛮多的（逃。


@error
- 当前发现一个error，可能和ctypes模块有关系，显示是Segmentation fault in Linux。具体排查放在功能完成后。
- 当前发现一个error，报错信息为：symbol not found，可能和x11有关系。具体排查无限期拖延。

@使用测试
将该脚本作为系统启动项，循环测试。