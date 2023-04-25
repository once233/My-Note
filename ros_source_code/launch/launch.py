def generate_launch_description():        # 自动生成launch文件的函数
    bringup_dir = get_package_share_directory('nav2_bringup') # 获取nav2_bringup文件夹下的share文件夹的路径
    
    
    container_name = LaunchConfiguration('container_name') # 用于在变量中存储启动参数的值并将它们传递给所需的变量（声明一个变量）
    declare_params_file_cmd = DeclareLaunchArgument( # 用于定义可以从上述启动文件或控制台传递的启动参数（给变量赋值）
        'params_file', # 定义的名称
        default_value=os.path.join(bringup_dir, 'params', 'nav2_params.yaml'), # 默认值
        description='Full path to the ROS2 parameters file to use for all launched nodes')
    
        configured_params = RewrittenYaml( # 根据参数文件， 以及替换更新的部分参数，生成新的yaml文件对象
        source_file=params_file,
        root_key=namespace,
        param_rewrites={},
        convert_types=True)
        
   load_nodes = GroupAction(
    condition=IfCondition(PythonExpression(['not ', use_composition])), # 未定义宏时执行
    actions = [
    Node(
        condition= LaunchConfigurationEquals('map', ''),
        package='nav2_map_server' , # 工程名
        executable='map_server', # 可执行文件名
        name='map_server' , # 显示出来的节点名称
        output='screen' , # 打印输出到屏幕
        respawn=use_respawn, # 节点崩溃是否重启节点
        respawn_delay=2.0 ,# 延迟n秒后重启节点
        parameters=[configured_params], # ros系统使用的数值，存放在参数服务器，可用rosparam获取
        arguments=['--ros-args', '--log-level', log_level],# 只在launch文件内部有意义
        remappings=remappings ), # 资源重映射表
        )]
   )

load_composable_nodes = GroupAction(
        condition=IfCondition(use_composition), # 设置多个节点当一组,放container里
        actions=[
            SetParameter('use_sim_time', use_sim_time),
            LoadComposableNodes( # 多个节点放一组的形式，要用这个load来加载
                target_container=container_name_full, # 装该节点的容器名
                condition=LaunchConfigurationEquals('map', ''), # 未设置地图参数时执行
                composable_node_descriptions=[  # 列表中的ComposableNode放上面设置的容器里
                    ComposableNode(
                        package='nav2_map_server', 
                        plugin='nav2_map_server::MapServer',
                        name='map_server',
                        parameters=[configured_params],
                        remappings=remappings), 
                ],
            ),
        ]
)
 
ld = LaunchDescription()  # 返回launch文件的描述信息
ld.add_action(load_nodes)
ld.add_action(load_composable_nodes)
return ld   


有关LifecycleNode
如果需要使用节点生命周期管理机制，类必须继承于LifecycleNode

有关节点启动流程
加载动态库->实例节点->configure节点-> Activate节点->(create bond)
