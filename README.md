# python-flask-template

基于 Python 的 Flask 项目模板

## 依赖要求


- python >=3.6

## 安装依赖

```sh
pip install -r requirements.txt
```

## 开发环境运行

```sh
# 默认为开发环境
python app.py
```

## 生产环境运行

```sh
# 设置环境变量
export PYTHON_ENV='production'  # Linux 
gunicorn app:app -p app.pid -b 0.0.0.0:80 -w 2
```

## 作者


👤 **CaoMeiYouRen**

* Website: [https://blog.cmyr.ltd/](https://blog.cmyr.ltd/)
* GitHub: [@CaoMeiYouRen](https://github.com/CaoMeiYouRen)
