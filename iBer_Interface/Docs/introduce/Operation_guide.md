markdown常用操作：换行：用2个空格+回车，代码段注释： ``` 来包裹代码段，添加空格：&nbsp;

# 常用安装包
    安装方法：pip install xxxx
    1、requests  
    2、logs  
    3、config
    4、email
    5、xlwt
    
    
# 框架介绍

## -Common
--gol：全局变量的通用方法封装  
--HTMLtestrunner：调用的第三方测试报告模板  
--logs：log的打印日志包  

## -configuration
--host_header.yaml：共用请求域名、请求头的共用参数的出处  

## -docs
--operation_guide:对框架及如何使用的介绍  

## -result
--report：测试报告的存放  
--run_logs:控制台打印log日志的存放，方便后期排查定位问题，直接打开此文件进行搜索即可  

## -Test

--Case:测试用例  
---login：有关login的用例全部写在此文件夹  
---todo：有关login的用例全部写在此文件夹  
---........  
---Z_Case_collects：用例的集合。所有的测试用例将在此处进行集合。  

--Module:业务模块    
---login:有关此模块的所有业务接口  
---todo:有关此模块的所有业务接口，分不同的接口可新建不同的def方法编写  

说明：  
&nbsp;每个module的class前均需要写入如下内容：  
 ```
import yaml,sys,os  
#导入yaml中的host  
reload(sys)  
sys.setdefaultencoding("utf-8")  
with open(os.getcwd()[:-5] + "/Configuration/host_header.yaml", 'rb') as f:  
    data = yaml.load(f)  
host = data["host"]   #获取到url  
header = data["headers"]  #获取到host  
 ```
&nbsp;在类中的写法：  
 ```
url = host+"todo-report/get-share-code"   #这将会组成一个完成的url链接  
headers = header   #获取请求头  
 ```
&nbsp;reponse结果的判断  
 ```  
'''判断：根据reponse中的某个值来判断接口返回是否成功'''
if str(r.json()["msg"]) == "SUCCESS":
    self.log.info("获取分享码成功：%s"%(str(r.json()["data"]["share_code"])))
else:
    self.log.error("获取分享码失败")
    raise False
  ```  
  
--run_test:运行的执行文件。 

# 测试API接口的请求时长
1、requests.post中加timeout  
2、添加：times = str(r.elapsed.total_seconds())  # 获取到响应时间temeout  
 ```  
r  = requests.post(url=url, data=data, headers=headers, verify=False, timeout=100000)  
times = str(r.elapsed.total_seconds())   
print times   
  ``` 


