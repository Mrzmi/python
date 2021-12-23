```python
from locust import HttpLocust,TaskSet,task

#locust是一种测试框架，用于生产蝗虫进行群攻击（压力测试）
#TaskSet相当于测试场景，制定蝗虫攻击总方案
#task：任务，是TaskSet的最小单位，制定单个任务
#client:攻击方法，类似于魔法攻击
#HttpLocust全部魔法，魔法书
# min_wait、max_wait：每个任务执行后到下一个任务执行前的最小/最大等待时间（注：是每个任务间的等待时间！！！）
# host：客户端发送消息的主机地址
# wait_function：一个用于获取任务间等待时长的函数，默认是min_wait和max_wait中的随机值

'''案例一'''
 class UserBehavior(TaskSet):
   on_start方法会在每个任务集开始的时候执行
     def on_start(self):
         """ on_start is called when a Locust start before any task is scheduled """
         self.login()

   on_stop方法会在框架的网页上点击了stop时执行
     def on_stop(self):
         """ on_stop is called when the TaskSet is stopping """
         self.logout()

     def login(self):
         self.client.post("/login", {"username": "ellen_key", "password": "education"})

     def logout(self):
         self.client.post("/logout", {"username": "ellen_key", "password": "education"})

    #每个带注解@task的方法，都是一个最基本的任务，数字代表攻击比重
     @task(2)
     def index(self):
         self.client.get("/")

     @task(1)
     def profile(self):
         self.client.get("/profile")

#兵工厂授权魔法HttpLocust
 class WebsituUser(HttpLocust):
     task_set = UserBehavior
    
    #用于确定模拟用户在执行任务之间应等待多长时间。如果没有[`wait_time`] 指定，下一个任务将在完成后立即执行。
    #constant在固定的时间内
	#between:在最小值和最大值之间的随机时间
	#constant_pacing: 确保任务每 X 秒运行一次（最多）的自适应时间
    
     wait_time = between(1, 5)
        
     #min_wait = 5000
     #max_wait = 9000

'''案例二'''
#可以有多个兵工厂，生产不同兵种
 from locust import TaskSet, HttpLocust, task, TaskSequence, seq_task, InterruptTaskSet
 class HangOutTaskSet(TaskSet):
     @task
     def hang_out(self):
         print("the player is hanging out")
 class PlayGameTaskSet(TaskSet):
     @task
     def play(self):
         print("the player is playing game")

 class PlayerOwn(HttpLocust):
     weight = 10
     task_set = HangOutTaskSet
     host = "http://www.baidu.com"
     min_wait = 10000
     max_wait = 10000

 class PlayerTwo(HttpLocust):
     weight = 90
     task_set = PlayGameTaskSet
     host = "http://www.baidu.com"
     min_wait = 10000
     max_wait = 10000

'''案例三'''
# Locust setup # 第一次启动Locust的时候执行
# TaskSet setup # 第一次实例化任务集时执行
# TaskSet on_start # 每一次开始一个任务时执行
# 。。。
# TaskSet tasks…
# 。。。
# TaskSet on_stop # 点击页面stop时，当前所有在执行中的TaskSet执行
# TaskSet teardown # 停止locust运行时执行
# Locust teardown # 停止locust运行时执行

 class MyTaskSet(TaskSet):
     def setup(self):
         print("task set_up")

     def on_start(self):
         print("start")
     @task
     def one(self):
         print("one")

     @task(3)
     def two(self):
         print("two")

     def on_stop(self):
         print("stop")

     def teardown(self):
         print("task tear_down")

 class WebSiteUser(HttpLocust):
     task_set = MyTaskSet
     host = "http://www.baidu.com"
     min_wait = 10000
     max_wait = 10000

     def setup(self):
         print("locust set_up")

     def teardown(self):
         print("locust tear_down")

'''案例四'''
# 使用@seq_task指定执行顺序，如果没有该注解，默认顺序是1；相同的order，会根据字母顺序排序
# @task不再代表权重，而是代表执行次数（！！！），由于不再是随机选择任务执行，框架会直接使用task的权重作为执行次数，如果没有该注解，默认执行1次
 class PlayGameTaskSet(TaskSequence):
     tasks = [play_one, play_two]

     @seq_task(1)
     def login(self):
         print("login")

     @seq_task(2)
     @task(5)
     def play_game(self):
         print("the player is playing game")

     @seq_task(3)
     @task
     def end_game(self):
         print("game end")
```

```python
# locust是一种测试框架，用于生产蝗虫进行群攻击（压力测试）
# TaskSet相当于测试场景，制定蝗虫攻击总方案
# task：任务，是TaskSet的最小单位，制定单个任务
# client:攻击方法，类似于魔法攻击
# HttpLocust全部魔法，魔法书
# min_wait、max_wait：每个任务执行后到下一个任务执行前的最小/最大等待时间（注：是每个任务间的等待时间！！！）
# host：客户端发送消息的主机地址
# wait_function：一个用于获取任务间等待时长的函数，默认是min_wait和max_wait中的随机值

'''案例一'''
# class UserBehavior(TaskSet):
#   on_start方法会在每个任务集开始的时候执行
#     def on_start(self):
#         """ on_start is called when a Locust start before any task is scheduled """
#         self.login()

#   on_stop方法会在框架的网页上点击了stop时执行
#     def on_stop(self):
#         """ on_stop is called when the TaskSet is stopping """
#         self.logout()
#
#     def login(self):
#         self.client.post("/login", {"username": "ellen_key", "password": "education"})
#
#     def logout(self):
#         self.client.post("/logout", {"username": "ellen_key", "password": "education"})
#
# 每个带注解@task的方法，都是一个最基本的任务，数字代表攻击比重
#     @task(2)
#     def index(self):
#         self.client.get("/")
#
#     @task(1)
#     def profile(self):
#         self.client.get("/profile")
#
# 兵工厂授权魔法HttpLocust
# class WebsituUser(HttpLocust):
#     task_set = UserBehavior
#     min_wait = 5000
#     max_wait = 9000

'''案例二'''
# 可以有多个兵工厂，生产不同兵种
# from locust import TaskSet, HttpLocust, task, TaskSequence, seq_task, InterruptTaskSet
# class HangOutTaskSet(TaskSet):
#     @task
#     def hang_out(self):
#         print("the player is hanging out")
# class PlayGameTaskSet(TaskSet):
#     @task
#     def play(self):
#         print("the player is playing game")
#
# class PlayerOwn(HttpLocust):
#     weight = 10
#     task_set = HangOutTaskSet
#     host = "http://www.baidu.com"
#     min_wait = 10000
#     max_wait = 10000
#
# class PlayerTwo(HttpLocust):
#     weight = 90
#     task_set = PlayGameTaskSet
#     host = "http://www.baidu.com"
#     min_wait = 10000
#     max_wait = 10000

'''案例三'''
# Locust setup # 第一次启动Locust的时候执行
# TaskSet setup # 第一次实例化任务集时执行
# TaskSet on_start # 每一次开始一个任务时执行
# 。。。
# TaskSet tasks…
# 。。。
# TaskSet on_stop # 点击页面stop时，当前所有在执行中的TaskSet执行
# TaskSet teardown # 停止locust运行时执行
# Locust teardown # 停止locust运行时执行

# class MyTaskSet(TaskSet):
#     def setup(self):
#         print("task set_up")
#
#     def on_start(self):
#         print("start")
#     @task
#     def one(self):
#         print("one")
#
#     @task(3)
#     def two(self):
#         print("two")
#
#     def on_stop(self):
#         print("stop")
#
#     def teardown(self):
#         print("task tear_down")
#
# class WebSiteUser(HttpLocust):
#     task_set = MyTaskSet
#     host = "http://www.baidu.com"
#     min_wait = 10000
#     max_wait = 10000
#
#     def setup(self):
#         print("locust set_up")
#
#     def teardown(self):
#         print("locust tear_down")

'''案例四'''
# 使用@seq_task指定执行顺序，如果没有该注解，默认顺序是1；相同的order，会根据字母顺序排序
# @task不再代表权重，而是代表执行次数（！！！），由于不再是随机选择任务执行，框架会直接使用task的权重作为执行次数，如果没有该注解，默认执行1次
# class PlayGameTaskSet(TaskSequence):
#     tasks = [play_one, play_two]
#
#     @seq_task(1)
#     def login(self):
#         print("login")
#
#     @seq_task(2)
#     @task(5)
#     def play_game(self):
#         print("the player is playing game")
#
#     @seq_task(3)
#     @task
#     def end_game(self):
#         print("game end")
```

