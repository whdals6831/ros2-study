# Parameter

## 개요

이 Chapter는 ROS2 Node에서 Parameter를 선언하고, 읽고, 실행 중 변경하는 방법을 다룬다.

Parameter는 Node의 동작을 코드 수정 없이 조정하는 설정값이다. 실행 옵션이나 YAML 파일로 초기값을 바꿀 수 있고, 실행 중 `ros2 param` CLI로 값을 확인하거나 변경할 수 있다.

## 학습 목표

- Node에서 Parameter를 선언할 수 있다.
- 선언한 Parameter 값을 읽어 Node 동작에 사용할 수 있다.
- `ros2 param get/set/list`로 실행 중인 Node의 Parameter를 확인하고 변경할 수 있다.
- Parameter Callback으로 잘못된 값을 거부할 수 있다.
- YAML 파일로 Parameter 초기값을 적용할 수 있다.

## 사전 요구사항

- [Logging Chapter](../05_logging/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Parameter 선언

Parameter는 사용하기 전에 Node에서 선언한다.

```python
self.declare_parameter('robot_name', 'turtlebot')
self.declare_parameter('max_speed', 1.0)
```

선언된 Parameter는 기본값을 가지며, 실행 시 CLI나 YAML 파일로 덮어쓸 수 있다.

### Parameter 읽기

Python Node에서는 `get_parameter()`로 값을 읽는다.

```python
robot_name = self.get_parameter('robot_name').value
```

Parameter 값은 Node의 이름, 속도, 임계값 같은 실행 설정에 사용한다.

### Parameter 변경

실행 중인 Node의 Parameter는 CLI로 확인하고 변경할 수 있다.

```bash
ros2 param list
ros2 param get /parameter_node robot_name
ros2 param set /parameter_node robot_name rover
```

### Parameter Callback

Parameter Callback은 값이 변경되기 전에 호출된다. 허용할 수 없는 값이면 변경을 거부한다.

예:

- 빈 문자열인 `robot_name` 거부
- 0 이하인 `max_speed` 거부

Callback은 실행 중 변경되는 값을 검증한다. CLI나 YAML 파일로 들어온 초기값은 Parameter를 선언한 직후 따로 확인한다.

```python
self.declare_parameter('robot_name', 'turtlebot')
self.declare_parameter('max_speed', 1.0)

if not self.get_parameter('robot_name').value:
    raise ValueError('robot_name must not be empty')

if self.get_parameter('max_speed').value <= 0.0:
    raise ValueError('max_speed must be greater than 0')
```

초기값 검증과 실행 중 변경 검증은 같은 기준을 사용한다. 이 예제에서는 `robot_name`이 빈 문자열이거나 `max_speed`가 0 이하이면 잘못된 값으로 판단한다.

### YAML Parameter

여러 Parameter 초기값은 YAML 파일로 관리할 수 있다.

```yaml
parameter_node:
  ros__parameters:
    robot_name: rover
    max_speed: 2.0
```

실행 시 YAML 파일을 적용한다.

```bash
ros2 run py_parameter_demo parameter_node --ros-args --params-file config/parameters.yaml
```

## 패키지 구조

```text
06_parameter/
├── README.md
└── packages/
    └── 01_parameter_node/
        └── py_parameter_demo/
```

예제 Package:

```text
py_parameter_demo/
├── config/
│   └── parameters.yaml
├── package.xml
├── setup.cfg
├── setup.py
├── resource/
│   └── py_parameter_demo
└── py_parameter_demo/
    ├── __init__.py
    └── parameter_node.py
```

## 빌드 방법

저장소 루트에서 빌드한다.

```bash
colcon build --packages-select py_parameter_demo
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

기본 Parameter로 실행한다.

```bash
ros2 run py_parameter_demo parameter_node
```

CLI로 Parameter를 덮어쓴다.

```bash
ros2 run py_parameter_demo parameter_node --ros-args -p robot_name:=rover -p max_speed:=2.0
```

YAML 파일을 사용한다.

```bash
ros2 run py_parameter_demo parameter_node --ros-args --params-file install/py_parameter_demo/share/py_parameter_demo/config/parameters.yaml
```

다른 터미널에서 Parameter를 확인한다.

```bash
ros2 param list /parameter_node
ros2 param get /parameter_node robot_name
ros2 param get /parameter_node max_speed
```

실행 중 값을 변경한다.

```bash
ros2 param set /parameter_node robot_name scout
ros2 param set /parameter_node max_speed 0.5
```

잘못된 값이 거부되는지 확인한다.

```bash
ros2 param set /parameter_node max_speed 0.0
ros2 param set /parameter_node robot_name ""
```

잘못된 초기값도 확인한다.

```bash
ros2 run py_parameter_demo parameter_node --ros-args -p max_speed:=0.0
ros2 run py_parameter_demo parameter_node --ros-args -p robot_name:=""
```

## 예상 결과

- 기본 실행에서는 `robot_name=turtlebot`, `max_speed=1.0`으로 로그가 출력된다.
- CLI나 YAML로 실행하면 지정한 초기값이 적용된다.
- `ros2 param set`으로 값을 바꾸면 이후 로그에 변경된 값이 반영된다.
- 초기값이 잘못되면 Node가 시작되지 않는다.
- 실행 중 `max_speed`가 0 이하이거나 `robot_name`이 빈 문자열이면 변경이 거부된다.

## 정리

Parameter는 Node의 실행 설정을 외부에서 바꾸는 기본 방법이다. Node는 필요한 Parameter를 선언하고, CLI나 YAML 파일은 환경별 초기값을 주입한다. Callback은 잘못된 설정값이 Node에 적용되는 것을 막는다.

## 참고 자료

- [Logging Chapter](../05_logging/README.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
