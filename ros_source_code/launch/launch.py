def generate_launch_description():        # 自动生成launch文件的函数
    return LaunchDescription([            # 返回launch文件的描述信息
Node(
     condition= LaunchConfigurationEquals('map', ''),
     package='nav2_map_server'(工程名),
     executable='map_server'（可执行文件名）,
     name='map_server'（显示出来的节点名称）,
     output='screen'（打印输出到屏幕）,
     respawn=use_respawn（节点崩溃是否重启节点）,
     respawn_delay=2.0（延迟n秒后重启节点）,
     parameters=[configured_params]（ros系统使用的数值，存放在参数服务器，可用rosparam获取）,
     arguments=['--ros-args', '--log-level', log_level]（只在launch文件内部有意义）,
     remappings=remappings（资源重映射表）)，
    ])
