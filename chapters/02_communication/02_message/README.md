# Message

## 개요

이 Chapter는 ROS2 Message 타입을 읽고, 직접 정의하고, Python Node에서 사용하는 방법을 다룬다.

Message는 Topic, Service, Action이 주고받는 데이터의 형식이다. Topic 이름이 같아도 Message 타입이 다르면 통신되지 않는다. 간단한 문자열은 `std_msgs/msg/String` 같은 표준 Message로 충분하지만, 로봇 상태처럼 여러 필드를 함께 보내야 하면 Custom Message를 정의한다.

## 학습 목표

- 표준 Message와 Custom Message의 차이를 설명할 수 있다.
- `.msg` 파일로 Custom Message를 정의할 수 있다.
- Message Interface Package와 사용 Package의 의존성을 구분할 수 있다.
- Python Node에서 Custom Message를 publish하고 subscribe할 수 있다.
- `ros2 interface`와 `ros2 topic` CLI로 Message 타입을 확인할 수 있다.

## 사전 요구사항

- [Topic Chapter](../01_topic/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Standard Message

표준 Message는 ROS2가 제공하는 재사용 가능한 Message 타입이다.

Topic Chapter에서는 `std_msgs/msg/String`을 사용했다.

```python
from std_msgs.msg import String
```

설치된 Message 목록은 CLI로 확인한다.

```bash
ros2 interface list
```

특정 Message의 필드는 `show`로 확인한다.

```bash
ros2 interface show std_msgs/msg/String
```

### Custom Message

Custom Message는 Package 안의 `msg/` 디렉터리에 `.msg` 파일로 정의한다.

이 Chapter의 예제 Message는 `RobotStatus.msg`다.

```text
string name
uint8 battery_percent
float32 temperature
bool is_active
```

각 줄은 `타입 필드명` 형식이다. Message 이름은 파일 이름에서 결정되고, 빌드 후에는 `message_demo_interfaces/msg/RobotStatus` 타입으로 사용할 수 있다.

### Message Interface Package

Custom Message는 보통 별도 Interface Package에 둔다.

```text
message_demo_interfaces
└── msg
    └── RobotStatus.msg
```

Interface Package는 Message 코드를 생성하는 역할만 한다. Node 실행 코드는 별도 Package에서 작성한다.

### Message Dependency

Message를 정의하는 Package는 `rosidl_default_generators`로 코드를 생성하고, 런타임에는 `rosidl_default_runtime`을 내보낸다.

Message를 사용하는 Package는 Interface Package에 의존한다.

```xml
<depend>message_demo_interfaces</depend>
```

Python 코드에서는 생성된 Message를 import해서 사용한다.

```python
from message_demo_interfaces.msg import RobotStatus
```

### Custom Message Topic

Publisher는 Custom Message 객체를 만들고 필드를 채운 뒤 발행한다.

```python
message = RobotStatus()
message.name = 'rover'
message.battery_percent = 95
message.temperature = 36.5
message.is_active = True
```

Subscriber는 같은 Message 타입으로 Topic을 구독한다.

```python
self.create_subscription(RobotStatus, 'status', self.listener_callback, 10)
```

## 패키지 구조

```text
02_message/
├── README.md
└── packages/
    ├── 01_custom_message/
    │   └── message_demo_interfaces/
    └── 02_message_topic/
        └── py_message_demo/
```

Interface Package:

```text
message_demo_interfaces/
├── CMakeLists.txt
├── package.xml
└── msg/
    └── RobotStatus.msg
```

Python 예제 Package:

```text
py_message_demo/
├── package.xml
├── setup.cfg
├── setup.py
├── resource/
│   └── py_message_demo
└── py_message_demo/
    ├── __init__.py
    ├── status_publisher_node.py
    └── status_subscriber_node.py
```

## 빌드 방법

저장소 루트에서 두 Package를 함께 빌드한다.

```bash
colcon build --packages-select message_demo_interfaces py_message_demo
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

Custom Message 타입을 확인한다.

```bash
ros2 interface show message_demo_interfaces/msg/RobotStatus
```

터미널 1에서 Subscriber를 실행한다.

```bash
ros2 run py_message_demo status_subscriber
```

터미널 2에서 Publisher를 실행한다.

```bash
source install/setup.bash
ros2 run py_message_demo status_publisher
```

zsh:

```bash
source install/setup.zsh
ros2 run py_message_demo status_publisher
```

터미널 3에서 Topic을 확인한다.

```bash
source install/setup.bash
ros2 topic info /message_demo/status
ros2 topic echo /message_demo/status
```

zsh:

```bash
source install/setup.zsh
ros2 topic info /message_demo/status
ros2 topic echo /message_demo/status
```

## 예상 결과

- `ros2 interface show`에서 `RobotStatus.msg`의 네 필드가 출력된다.
- `status_publisher` Node가 1초마다 `/message_demo/status`에 `RobotStatus` Message를 발행한다.
- `status_subscriber` Node가 `name`, `battery_percent`, `temperature`, `is_active` 값을 로그로 출력한다.
- `ros2 topic info /message_demo/status`에서 타입이 `message_demo_interfaces/msg/RobotStatus`로 보인다.
- `ros2 topic echo /message_demo/status`에서 네 필드가 YAML 형태로 출력된다.

## 정리

Message는 ROS2 통신의 데이터 계약이다. 표준 Message로 표현할 수 없는 데이터는 Interface Package에 Custom Message로 정의하고, Node Package는 그 Interface Package에 의존해서 생성된 타입을 사용한다.

## 참고 자료

- [Topic Chapter](../01_topic/README.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
