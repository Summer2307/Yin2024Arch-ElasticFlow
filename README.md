# ElasticFlow-复现

## 模拟器实验复现

## 主要文件
- `ElasticFlow/` 包含模拟器的主要代码，参考 [Tiresias](https://github.com/SymbioticLab/Tiresias)。
	- `chronus-scheduler/` 包含Chronus调度算法的源代码实现，由 [this repo](https://github.com/S-Lab-System-Group/ChronusArtifact)提供。
	- `scheduler/` 包含ElasticFlow算法的实现和baseline算法的实现
		- `cluster_spec/` 包含配置文件
		- `runtime/` 包含用于调度、节点等联系的gRPC源代码
		- `throughputs_A100/` 包含各模型在A100 GPU上的运行数据
		- `throughputs_T4/` 包含各模型在T4 GPU上的运行数据（由 [adaptdl](https://github.com/petuum/adaptdl/tree/osdi21-artifact)提供)
		- `trace_generator/` 包含生成job traces的文件
	
## 复现步骤

### conda虚拟环境创建、需要的包安装
```Bash
# create conda env
conda create -n elasticflow python=3.8
conda activate elasticflow
# install dependencies
cd ElasticFlow
python -m pip install --upgrade pip
pip install -r requirements.txt
# make gRPC
cd chronus-scheduler
make
cd ../scheduler
make
```
Chronus需要的Gurobi optimizer配置： [official website](https://www.gurobi.com) 。

### 具体步骤

0. 准备好Job Traces 
从10个Microsoft internal ITP 集群获取 [job traces](https://github.com/microsoft/elasticflow-traces) ，解压到相应文件夹

```Bash
tar -xvzf elasticflow-traces/data/elasticflow-traces.tar.gz -C ElasticFlow/traces_for_ElasticFlow/
```

1. 运行对应的实验（对应原文中的Figure）
```Bash
cd scheduler
```
- Figure 8(a): `source run_fig8a.sh`. （约30分钟）
- Figure 8(b): `source run_fig8b.sh`. （运行了2天左右，结果未放在报告中）This might take a few days to finish the simulation of all of the traces!
- Figure 9: `bash run_fig9.sh`. （约10分钟）
- Figure 10: `source run_fig10.sh`. （约2分钟）

结果储存在`<repo>/plot_figure/logs/` 文件夹

2. 绘图

主要参考 `<repo>/plot_figure/README.md`
