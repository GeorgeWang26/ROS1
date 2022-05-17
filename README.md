# **ROS 1**

#### **Install new ROS package**
* Clone repo to "workspace/src"
* Install dependencies -> `rosdep install --from-paths src --ignore-src -r -y`
* Build in "workspace/" -> `catkin_make`
* Reload ros launch files -> `source devel/setup.bash`

#### **Catkin commands**
`catkin_make` (in "workspace/") \
`catkin_create_pkg` (in "workspace/src")

#### **ROS CLI commands**
`roscore` \
`rosnode` \
`rostopic` \
`rosservice` \
`rosparam` 

#### **Message formats**
.msg for publish/subscribe \
.srv for services (converted into Python class)

#### **Pass data through publishers and service clients**
* explicit
* inplicit
    * in order
    * parameter/keyword (ommited parameters are set to 0)
    
---

### **Catkin workspace for ROS**
Only need one workspace as it can contain multiple packages
```
cd ./workspace
mkdir src (this is a MUST for catkin_make)
catkin_make
cd devel
source setup.bash
```

### **ROS Package**
Stored under "workspace/src" \
Package consist of nodes that share **similar** functionalities
```
cd src
catkin_create_pkg <new_package> roscpp rospy std_msgs
cd ..
catkin_make     #(build in "workspace/" after adding new packages)
```

### **ROS Node**
Every ROS node should be stored in a package under "workspace/src/package/src" \
Initialized with `rospy.init_node("node_name")`. \
Every program must have one and only one ROS node, but it can have multiple publishers, subsribers, service servers and service clients

---

### **Publisher**
A ROS Publisher is a node that publishes a specific type of ROS message at a given ROS topic
```
pub = rospy.Publisher("topic_name", data_type, que_size)`
publish with `pub.publish()`
```

### **Subscriber**
Subscriber is also a ROS node that it listens to a given topic of specific data type. When recieve new data, it will triger the callback function to process the data
```
sub = rospy.Subscriber("topic_name", data_type, callback)
rospy.spin()
```
`spin()` keeps the node alive until ROS is shutdown. Withought `spin()`, the callback functons will **never** be triggered \
It is only used for subscribers & service servers because they require callbacks \
Publishers run at regular interval within while loop, and service clients are either used only one time or stay connected by using persistent connection. Neither require callbacks, so `spin()` is not needed

---

### **Service Server**
A ROS node that listen to topic of given message format (.srv) \
Process recieved messages, then the server will send a response back to the client
```
server = rospy.Service("service_name", message_type, callback)
spin()
```

### **Service Client**
A ROS node that create a service proxy to the topic with given .srv format. \
It sends data to the server and wait for responce.
```
client = rospy.ServiceProxy("service name", message_type)
response = client(input_parameters)
```
Uses `rospy.wait_for_service("service_name")` to block until service server is available

---

### **Parameter server**
Used to store parameters
* /abs_path
* relative_path_under_program_namespace
* ~private_path (path under node namespace)

Program namespace is set to "/" by default, so it acts like root path. Use `os.environ["ROS_NAMESPACE"] = "/namespace"` before `import rospy` to set a different namespace. \
Note that this will affect node name as well since it is relative to namespace of the program. Because `rospy.init_node("/abs_node_name")` with absolute path is **NOT** allowed.

The best option now is to keep namespace of the program as it is being "/", and when using parameter server, just use either absolute path or private path, avoid using "relative_path_under_program_namespace" and setting it with `os.environ["ROS_NAMESPACE"]`

---

### **Logging**
`rospy.log*()` for different types of log \
ROS logs are stored under "~/.ros/log" or "ROS_ROOT/log" (ROS_ROOT is env variable, get its value with `env|grep` or `$ROS_ROOT`)

### **Time**
`rospy.Time(secs = 0, nsecs = 0)` mainly used to get current time with `rospy.Time.now()` \
`rospy.Duration(secs = 0, nsecs = 0)` \
`rospy.sleep(duration)` maintains the rate of loops (ex: publisher)
```
r = rospy.Rate(hz)
r.sleep()
```
`rospy.Timer(rospy.Duration(), callback, oneshot=False)` allows regular callback withought having loop

Timer and Rate sleep can be used in the same program \
ex: use Timer to update parameters from paramserver and use Rate sleep to keep publisher running

### **ROS launch**
.launch file in XML format for launching multiple ros nodes together
