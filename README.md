# RedstoneCPUTest
红石CPU试水

## CPU架构
+ ALU: 8位，包含加、减、与、或非、同或、逻辑左移、逻辑右移和一个累加器
+ 寄存器: 8字节，其中R0为零寄存器
+ 标志位与分支逻辑: 共设三个标志位: 非空、负数、奇数
+ 控制单元: 对操作码(5位)解码，控制CPU运行
+ 程序计数器: 可以自增、跳转，前者由1t脉冲触发，后者由2t脉冲触发
+ 时钟: 每周期给出2t脉冲，周期为54t(5.4s)，频率约0.185Hz
+ 指令ROM: 大小32B，只读
+ I/O端口: 共两个，一个用于输入，一个用于输出

## 指令集
+ 单/双字节指令
+ 共17条

## 外置编译器
+ 使用Python的mcschematic库编写
+ 可以直接根据.txt文件中存储的汇编生成机器码并生成.schem文件，使之可以直接被WorldEdit加载粘贴
+ .schem文件结构只针对本CPU使用的ROM设计
+ 每8字节需要分开独自编译
