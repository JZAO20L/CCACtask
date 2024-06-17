各文件夹介绍：
Data：
	包含源数据（jsonl），之后转为保留三个域的test_data.csv，和只有两个域（text、label）的dataset_raw.csv，后续7：3分割为training_set和testing_set
Code：
	SparkPython：调用大模型API，读取源数据，包含了所使用的所有prompt，最后输出的结果保存在Result文件夹下（一开始想着jsonl转csv，后面直接读jsonl，这部分代	码删了，要是想jsonl转csv可以补充下）
	Reformat：用于调整数据格式、分割数据集，使用csv主要是为了符合之前的现成代码（懒得改json）
	BERTClassify：训练基于BERT的分类器，模型参数保存在Models文件夹下
	LabelClassify：实例化分类器，加载参数，进行预测（时间原因这版还没写读写文件，可自行补充）
其他不太重要的文件夹：
	bert-base-chinese，使用的预训练模型，为了避免连不上huggingface直接下了一份，可以修改BERTClassify和LabelClassify的路径然后就不需要本地的bert了；
	Models：保存的分类器参数，附表记录了训练过程中的评测结果
	Result：大模型API的结果，scoring_table统计了结果