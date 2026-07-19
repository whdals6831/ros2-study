# Launch

## 개요

이 Chapter는 ROS2 Launch 파일로 Node를 실행하고, 실행 옵션을 한 곳에서 관리하는 방법을 다룬다.

Launch는 여러 Node를 같은 명령으로 시작하고, 이름, Namespace, Remapping, Parameter를 실행 시점에 적용하는 도구다. 단일 Node는 `ros2 run`으로 충분하지만, Node가 2개 이상이거나 설정이 길어지면 launch 파일로 실행 흐름을 고정하는 편이 낫다.

## 학습 목표

- Python Launch 파일의 기본 구조를 설명할 수 있다.
- Launch Argument로 실행 값을 바꿀 수 있다.
- Launch 파일에서 Node를 실행할 수 있다.
- Namespace와 Remapping이 Node 실행 결과에 주는 영향을 확인할 수 있다.
- Parameter YAML을 Launch에서 적용할 수 있다.
- 여러 Node를 동시에 실행하고 다른 Launch 파일을 포함할 수 있다.
- 조건부 실행으로 일부 Node를 켜거나 끌 수 있다.

## 사전 요구사항

- [Parameter Chapter](../06_parameter/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Python Launch

ROS2 Python Launch 파일은 보통 `generate_launch_description()` 함수를 제공한다.

```python
from launch import LaunchDescription


def generate_launch_description():
    return LaunchDescription([])
```

이 함수가 반환하는 `LaunchDescription` 안에 실행할 Node, Argument, Include 같은 action을 넣는다.

### Launch Argument

Launch Argument는 launch 실행 시 바꿀 수 있는 입력값이다.

```python
DeclareLaunchArgument('robot_name', default_value='launch_rover')
robot_name = LaunchConfiguration('robot_name')
```

실행할 때 값을 덮어쓴다.

```bash
ros2 launch py_launch_demo demo.launch.py robot_name:=scout
```

### Node 실행

Launch 파일에서는 `launch_ros.actions.Node`로 Node를 실행한다.

```python
Node(
    package='py_launch_demo',
    executable='launch_demo_node',
    name='main',
    output='screen',
)
```

`package`는 ROS2 Package 이름이고, `executable`은 `setup.py`의 `console_scripts`에 등록한 실행 이름이다.

### Namespace

Namespace는 Node와 Topic 이름 앞에 붙는 실행 범위다.

```python
Node(
    package='py_launch_demo',
    executable='launch_demo_node',
    namespace='demo',
)
```

위 설정으로 실행하면 Node 이름은 `/demo/launch_demo_node` 형태가 된다. 같은 실행 파일을 여러 번 띄울 때 Namespace를 나누면 이름 충돌을 줄일 수 있다.

### Remapping

Remapping은 Node 코드 안의 이름을 실행 시점에 다른 이름으로 바꾼다.

```python
Node(
    package='py_launch_demo',
    executable='launch_demo_node',
    remappings=[('status', 'main_status')],
)
```

예제 Node는 `status` Topic 이름을 resolve해서 로그로 출력한다. Launch에서 remap하면 로그에 `main_status` 또는 `worker_status`가 보인다.

### Parameter YAML 적용

Launch에서도 Parameter YAML 파일을 적용할 수 있다.

```python
Node(
    package='py_launch_demo',
    executable='launch_demo_node',
    parameters=['config/launch_parameters.yaml'],
)
```

예제에서는 install된 package share 경로에서 YAML 파일을 찾아 적용한다. 같은 Parameter를 뒤쪽 딕셔너리에서 다시 지정하면 뒤쪽 값이 우선한다.

```python
parameters=[parameter_file, {'robot_name': robot_name}]
```

### 여러 Node 동시 실행

`LaunchDescription`에 `Node` action을 여러 개 넣으면 한 번의 `ros2 launch`로 여러 Node가 실행된다.

```python
return LaunchDescription([
    Node(...),
    Node(...),
])
```

이 Chapter의 `demo.launch.py`는 `main` Node를 실행하고, 포함된 `worker.launch.py`가 `worker` Node를 추가로 실행한다.

### Launch File 포함

Launch 파일은 다른 Launch 파일을 포함할 수 있다.

```python
IncludeLaunchDescription(
    PythonLaunchDescriptionSource(str(worker_launch)),
    launch_arguments={'robot_name': robot_name}.items(),
)
```

반복되는 실행 묶음은 작은 launch 파일로 나누고, 상위 launch 파일에서 포함한다.

### 조건부 실행

조건부 실행은 특정 Node나 Include를 켜고 끌 때 사용한다.

```python
Node(
    package='py_launch_demo',
    executable='launch_demo_node',
    condition=IfCondition(enable_worker),
)
```

실행 시 `enable_worker:=false`를 주면 worker Node는 시작되지 않는다.

## 패키지 구조

```text
07_launch/
├── README.md
└── packages/
    └── 01_launch_node/
        └── py_launch_demo/
```

예제 Package:

```text
py_launch_demo/
├── config/
│   └── launch_parameters.yaml
├── launch/
│   ├── demo.launch.py
│   └── worker.launch.py
├── package.xml
├── setup.cfg
├── setup.py
├── resource/
│   └── py_launch_demo
└── py_launch_demo/
    ├── __init__.py
    └── launch_demo_node.py
```

## 빌드 방법

저장소 루트에서 빌드한다.

```bash
colcon build --packages-select py_launch_demo
```

빌드 결과를 현재 터미널에 반영한다.

```bash
source install/setup.bash
```

zsh:

```bash
source install/setup.zsh
```

## 실행 방법

Launch 파일로 main Node와 worker Node를 함께 실행한다.

```bash
ros2 launch py_launch_demo demo.launch.py
```

Launch Argument를 바꿔 실행한다.

```bash
ros2 launch py_launch_demo demo.launch.py robot_name:=scout namespace:=robot1
```

worker Node를 끄고 main Node만 실행한다.

```bash
ros2 launch py_launch_demo demo.launch.py enable_worker:=false
```

다른 터미널에서 실행 중인 Node를 확인한다.

```bash
ros2 node list
```

Node 정보를 확인한다.

```bash
ros2 node info /demo/main
ros2 node info /demo/worker
```

직접 Node만 실행해서 launch 적용 전 값을 확인할 수도 있다.

```bash
ros2 run py_launch_demo launch_demo_node
```

## 예상 결과

- 기본 launch 실행에서는 `/demo/main`, `/demo/worker` Node가 실행된다.
- `main` Node 로그에는 `status_topic=/demo/main_status`가 출력된다.
- `worker` Node 로그에는 `status_topic=/demo/worker_status`가 출력된다.
- `robot_name:=scout`을 주면 두 Node 로그의 `robot_name` 값이 `scout`으로 바뀐다.
- `namespace:=robot1`을 주면 Node와 Topic 이름 앞에 `/robot1`이 붙는다.
- `enable_worker:=false`를 주면 worker Node는 실행되지 않는다.

## 정리

Launch는 여러 Node와 실행 설정을 하나의 재사용 가능한 실행 파일로 묶는다. Python Launch 파일에서 Argument, Node, Namespace, Remapping, Parameter, Include, Condition을 조합하면 반복 실행 명령을 짧고 일관되게 관리할 수 있다.

## 참고 자료

- [Parameter Chapter](../06_parameter/README.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
