# Topic Advanced

## 개요

이 Chapter는 Topic을 실제 시스템에서 더 유연하게 사용하는 방법을 다룬다.

기본 Publisher와 Subscriber 구조는 이전 Chapter와 같지만, 발행 주기, 여러 Publisher와 Subscriber, Custom Message Topic, Topic Remapping을 함께 확인한다. 예제는 `RobotStatus` Custom Message를 사용해서 여러 로봇 상태가 같은 Topic으로 들어오는 상황을 만든다.

## 학습 목표

- Publisher의 발행 주기를 조절할 수 있다.
- 하나의 Topic에 여러 Publisher와 Subscriber가 연결될 수 있음을 확인할 수 있다.
- Custom Message를 Topic으로 주고받을 수 있다.
- CLI remap으로 Node 코드를 바꾸지 않고 Topic 이름을 변경할 수 있다.

## 사전 요구사항

- [Message Chapter](../02_message/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Publish Frequency

Publisher는 timer 주기로 Message를 발행한다.

```python
self.timer = self.create_timer(1.0 / publish_hz, self.publish_status)
```

이 예제는 `publish_hz` Parameter로 발행 주기를 바꾼다.

```bash
ros2 run py_topic_advanced status_publisher --ros-args -p publish_hz:=2.0
```

### Multiple Publisher와 Subscriber

ROS2 Topic은 하나의 Publisher와 하나의 Subscriber만 연결되는 구조가 아니다.

```text
Publisher A ─┐
             ├── /topic_advanced/status ──> Subscriber A
Publisher B ─┘                         └──> Subscriber B
```

같은 Topic 이름과 Message 타입을 쓰면 여러 Node가 같은 데이터 흐름에 참여할 수 있다.

### Custom Message Topic

이 Chapter는 이전 Chapter에서 만든 `message_demo_interfaces/msg/RobotStatus`를 재사용한다.

```python
from message_demo_interfaces.msg import RobotStatus
```

Topic 타입은 다음 CLI로 확인한다.

```bash
ros2 topic info /topic_advanced/status
```

### Topic Remapping

Remapping은 Node 코드를 수정하지 않고 Topic 이름을 바꾸는 기능이다.

예제 Node는 상대 Topic 이름 `status`를 사용한다. 기본 namespace가 `topic_advanced`이므로 기본 Topic은 `/topic_advanced/status`가 된다.

```bash
ros2 run py_topic_advanced status_publisher --ros-args -r status:=robot_status
```

위 명령은 Topic을 `/topic_advanced/robot_status`로 바꾼다.

`-r`은 Topic, Service, Action 같은 ROS graph 이름을 remap한다. 같은 이름의 Parameter가 있어도 Parameter 이름은 바뀌지 않는다. Parameter 값을 바꾸려면 `-p`를 사용한다.

```bash
ros2 run py_topic_advanced status_publisher --ros-args -p robot_name:=alpha
```

## 패키지 구조

```text
03_topic_advanced/
├── README.md
└── packages/
    └── 01_status_topic/
        └── py_topic_advanced/
```

예제 Package:

```text
py_topic_advanced/
├── package.xml
├── setup.cfg
├── setup.py
├── resource/
│   └── py_topic_advanced
└── py_topic_advanced/
    ├── __init__.py
    ├── status_publisher_node.py
    └── status_subscriber_node.py
```

## 빌드 방법

저장소 루트에서 Interface Package와 예제 Package를 함께 빌드한다.

```bash
colcon build --packages-select message_demo_interfaces py_topic_advanced
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

터미널 1에서 Subscriber를 실행한다.

```bash
ros2 run py_topic_advanced status_subscriber
```

터미널 2에서 Publisher를 실행한다.

```bash
source install/setup.bash
ros2 run py_topic_advanced status_publisher
```

zsh:

```bash
source install/setup.zsh
ros2 run py_topic_advanced status_publisher
```

터미널 3에서 Topic 상태와 발행 주기를 확인한다.

```bash
source install/setup.bash
ros2 topic info /topic_advanced/status
ros2 topic echo /topic_advanced/status
ros2 topic hz /topic_advanced/status
```

zsh:

```bash
source install/setup.zsh
ros2 topic info /topic_advanced/status
ros2 topic echo /topic_advanced/status
ros2 topic hz /topic_advanced/status
```

발행 주기를 2Hz로 바꿔 실행한다.

```bash
ros2 run py_topic_advanced status_publisher --ros-args -p publish_hz:=2.0
```

다른 로봇 이름으로 두 번째 Publisher를 실행한다.

```bash
ros2 run py_topic_advanced status_publisher --ros-args -r __node:=status_publisher_alpha -p robot_name:=alpha
ros2 run py_topic_advanced status_publisher --ros-args -r __node:=status_publisher_beta -p robot_name:=beta
```

두 번째 Subscriber를 실행한다.

```bash
ros2 run py_topic_advanced status_subscriber --ros-args -r __node:=status_subscriber_monitor
```

Topic 이름을 remap해서 실행한다.

```bash
ros2 run py_topic_advanced status_subscriber --ros-args -r status:=robot_status
ros2 run py_topic_advanced status_publisher --ros-args -r status:=robot_status
ros2 topic echo /topic_advanced/robot_status
```

## 예상 결과

- `status_publisher`가 `/topic_advanced/status`에 `RobotStatus` Message를 발행한다.
- `publish_hz` 값을 바꾸면 `ros2 topic hz` 결과가 함께 바뀐다.
- Publisher를 여러 개 실행하면 `ros2 topic info /topic_advanced/status`의 Publisher 수가 증가한다.
- Subscriber를 여러 개 실행하면 Subscriber 수가 증가하고, 각 Subscriber가 같은 Message를 받는다.
- Remapping을 적용하면 `/topic_advanced/status` 대신 `/topic_advanced/robot_status`로 통신한다.

## 정리

Topic은 하나의 데이터 스트림에 여러 Node가 참여할 수 있는 다대다 통신 방식이다. Node 코드는 상대 Topic 이름과 Message 타입에 집중하고, 실행 시점에는 Parameter와 Remapping으로 발행 주기, Node 이름, Topic 이름을 조절할 수 있다.

## 참고 자료

- [Topic Chapter](../01_topic/README.md)
- [Message Chapter](../02_message/README.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
