# N-life 

## 简介

* N-life 前端框架Materialize 后端django驱动
* 方便学生查询课表和成绩(主要为iphone用户服务）
* 暂时有三个功能在运行，查看课表,成绩以及查询自习室，以后会加上考试查询

## ubuntu下配置

### 安装pip
```
sudo apt-get install python-pip
```
### 通过pip安装
#### 安装django
```
pip install Django==1.9
```
#### 安装requests
```
pip install requests
```
#### 安装mysql-python
```
pip install Mysql-python
```
#### 如果安装MySQL-python失败请执行
```
sudo apt-get install libmysqlclient-dev
```
### clone 项目
```
git clone https://github.com/Liewithen/N-life.git
```
### New 自习室信息导入数据库

#### 记得修改setting.py中的数据库密码
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nlife',
        'USER': 'root',
        'PASSWORD': '******',
    }
}
```
#### 获取自习室信息
```
cd Room_Info
python getclassroom.py
//会提示输入学号密码
```

#### 导入数据库
```
python insertdata.py
//数据成功导入后会有提示成功信息
```
