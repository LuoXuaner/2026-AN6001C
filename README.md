# AN6001C · DBS 股价预测

这个 Flask 网页用于演示线性回归。输入 1 美元可兑换的新加坡元数（例如 `1.28`），网页用课程历史数据训练的模型估算 DBS 股票价格，单位为新加坡元。输入页和结果页是独立页面。模型只使用汇率这一项特征，结果反映课程样本里的统计关系，没有实时行情或预测日期。

## 运行网页

在项目根目录用 Python 3.12 执行下列命令，然后打开 [本地网页](http://127.0.0.1:5000/)。

```text
python -m pip install -r requirements.txt
python app.py
```

在 Linux 或 GitHub Codespaces 中，可用以下命令运行 Gunicorn，并在 Codespaces 的 Ports 面板打开端口 8000。

```text
gunicorn --bind 0.0.0.0:8000 app:app
```

## 重跑训练

完整课程包包含 `6001 W1 DBS.ipynb` 和 `DBS_SingDollar.csv`。在项目根目录运行全部单元，或在 Colab 打开 Notebook 后把 CSV 上传到当前会话。Notebook 会用 `SGD` 列拟合 `DBS` 列、计算训练集 RMSE，并输出 `DBS_SGD.pkl`。网页已附课程提供的模型，直接启动即可。
