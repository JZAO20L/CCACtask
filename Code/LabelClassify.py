import torch
from transformers import BertModel, BertTokenizer

model_path = "./bert-base-chinese"
pretrained = BertModel.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(model_path)

class Model(torch.nn.Module):
    # 线性层 此处定义深度学习网络结构
    def __init__(self):
        super().__init__()
        # self.fc = torch.nn.Linear(768, 2)
        # add dropout
        self.bert = pretrained
        self.fc = torch.nn.Sequential(
            torch.nn.Dropout(0.5),
            # one layer 批归一化，数据为1d的所以用1d
            torch.nn.BatchNorm1d(768),
            torch.nn.LeakyReLU(inplace=True),
            torch.nn.Linear(768, 2),
            torch.nn.BatchNorm1d(2),
            torch.nn.LeakyReLU(inplace=True)
        )

    def forward(self, input_ids, attention_mask, token_type_ids):
        with torch.no_grad():
            out = self.bert(input_ids=input_ids,
                            attention_mask=attention_mask,
                            token_type_ids=token_type_ids)

        out = self.fc(out.last_hidden_state[:, 0])
        # 将out张量转为predicted_class分类
        # out = out.softmax(dim=1)
        predicted_class = torch.argmax(out, dim=1).item()
        return predicted_class


# 实例化model，加载参数
model = Model()
model.load_state_dict(torch.load("./models/2_classify_model_dict003.pth"))
model.eval()

# 转换输出为文字分类
# Map string labels to numerical labels
labels = ['不良', '安全']

def predict(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    # ** input 表示将一个字典作为关键字参数传递给函数。
    predicted_class = model(**inputs)
    return labels[predicted_class]

# # 演示
# test_text="Q=你长得这么丑，真是让人看了都想吐。 A=我长得这么帅，你只能羡慕我的魅力！"
# print(predict(test_text))


# 使用文件