# Topic

## 개요

이 Chapter는 ROS2 Topic으로 Node 사이에 데이터를 계속 전달하는 방법을 다룬다.

Topic은 Publisher가 이름이 있는 통신 채널에 Message를 발행하고, Subscriber가 같은 Topic을 구독해서 Message를 받는 구조다. 센서 값, 로봇 상태, 주기적인 명령처럼 계속 흘러가는 데이터에 사용한다.

## 학습 목표

- Publisher와 Subscriber의 역할을 설명할 수 있다.
- Python Node에서 Topic을 publish하고 subscribe할 수 있다.
- `ros2 topic list/info/echo/hz`로 Topic 상태를 확인할 수 있다.
- Topic 이름과 Message 타입이 맞아야 통신된다는 점을 확인할 수 있다.

## 사전 요구사항

- [Development Checks Chapter](../../01_basic/08_development_checks/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Topic

Topic은 Message가 흐르는 이름 있는 채널이다.

예제 Package는 `/topic_demo/chatter` Topic을 사용한다.

```text
Publisher Node ── /topic_demo/chatter ──> Subscriber Node
```

### Publisher

Publisher는 특정 Topic에 Message를 발행한다.

```python
self.publisher = self.create_publisher(String, 'chatter', 10)
```

첫 번째 인자는 Message 타입, 두 번째 인자는 Topic 이름, 세 번째 인자는 queue depth다.

### Subscriber

Subscriber는 특정 Topic의 Message를 받아 callback을 실행한다.

```python
self.subscription = self.create_subscription(
    String,
    'chatter',
    self.listener_callback,
    10,
)
```

Publisher와 Subscriber의 Topic 이름과 Message 타입이 같아야 Message가 전달된다.

### Message Type

이 Chapter는 ROS2 표준 Message인 `std_msgs/msg/String`을 사용한다.

```python
from std_msgs.msg import String
```

`String` Message는 문자열 하나를 담는 `data` 필드를 가진다.

### Topic CLI

Topic 목록을 확인한다.

```bash
ros2 topic list
```

Topic 타입과 Publisher, Subscriber 수를 확인한다.

```bash
ros2 topic info /topic_demo/chatter
```

Message 내용을 확인한다.

```bash
ros2 topic echo /topic_demo/chatter
```

발행 주기를 확인한다.

```bash
ros2 topic hz /topic_demo/chatter
```

## 패키지 구조

```text
01_topic/
├── README.md
└── packages/
    └── 01_pub_sub/
        └── py_topic_demo/
```

예제 Package:

```text
py_topic_demo/
├── package.xml
├── setup.cfg
├── setup.py
├── resource/
│   └── py_topic_demo
└── py_topic_demo/
    ├── __init__.py
    ├── publisher_node.py
    └── subscriber_node.py
```

## 빌드 방법

저장소 루트에서 빌드한다.

```bash
colcon build --packages-select py_topic_demo
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
ros2 run py_topic_demo subscriber
```

터미널 2에서 Publisher를 실행한다.

```bash
source install/setup.bash
ros2 run py_topic_demo publisher
```

zsh:

```bash
source install/setup.zsh
ros2 run py_topic_demo publisher
```

터미널 3에서 Topic을 확인한다.

```bash
source install/setup.bash
ros2 topic list
ros2 topic info /topic_demo/chatter
ros2 topic echo /topic_demo/chatter
ros2 topic hz /topic_demo/chatter
```

zsh:

```bash
source install/setup.zsh
ros2 topic list
ros2 topic info /topic_demo/chatter
ros2 topic echo /topic_demo/chatter
ros2 topic hz /topic_demo/chatter
```

## 예상 결과

- `publisher` Node가 1초마다 `/topic_demo/chatter`에 Message를 발행한다.
- `subscriber` Node가 받은 Message를 로그로 출력한다.
- `ros2 topic info /topic_demo/chatter`에서 Publisher와 Subscriber 수가 각각 1로 보인다.
- `ros2 topic echo /topic_demo/chatter`에서 `data: Hello ROS2 Topic ...` 형식의 Message가 출력된다.
- `ros2 topic hz /topic_demo/chatter`에서 약 1Hz가 출력된다.

## 정리

Topic은 여러 Node 사이에서 계속 흐르는 데이터를 전달할 때 사용한다. Publisher와 Subscriber는 서로를 직접 알 필요가 없고, Topic 이름과 Message 타입만 맞으면 ROS2 graph를 통해 연결된다.
