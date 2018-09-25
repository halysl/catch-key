# 捕捉键盘输入

主要目的：
- 捕捉键盘输入
- 将键盘输入记录文件持久保存
- 统计击打键盘数
- 同步在桌面显示击打键盘数


@time: 2018-09-21 19:32  完成键盘记录功能
@time: 2018-09-22 19:32  完成输入记录文件功能
@time: 2018-09-25 21:00  完成统计击打键盘数目并根据频次进行输出


@todo
- thing： 再次需求分析
- time： 2018-09-26 20:00
- who：light

@todo
- thing：补全单元测试
- time： 2018-09-26 22:00
- who： light

@todo
- thing：根据日期统计击打键盘数目，并输出
- time： 2018-09-27 22:00
- who： light


@当前统计结果显示：

```python
当前输入字符统计：

<backspace>:78
i:67
<enter>:58
n:48
a:46
space:44
1:41
h:38
e:33
u:31
s:30
o:28
t:28
left_shift:26
d:25
left_ctrl:23
w:22
<tab>:21
left_alt:20
g:20
m:16
::15
c:14
j:13
l:13
.:13
p:12
k:11
2:10
-:10
y:8
q:8
x:8
v:7
z:6
b:6
@:5
r:4
;:4
<esc>:3
3:3
f:3
E:2
:1
right_shift:1
=:1
4:1
,:1
L:1
R:1
A:1
D:1
M:1
```

可见打错字还是蛮多的（逃。


@error
- 当前发现一个error，可能和ctypes模块有关系，显示是Segmentation fault in Linux。具体排查放在功能完成后。