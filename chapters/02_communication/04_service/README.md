# Service

## 개요

이 Chapter는 ROS2 Service로 짧은 요청과 응답을 주고받는 방법을 다룬다.

Topic은 계속 흐르는 데이터를 보내는 데 적합하고, Service는 한 번 요청하고 한 번 응답받는 작업에 적합하다. 예제는 `SetRobotMode` Custom Service로 로봇 모드를 바꾸는 Server와 비동기 Client를 만든다.

## 학습 목표

- Service Server와 Service Client의 역할을 설명할 수 있다.
- `.srv` 파일로 Custom Service를 정의할 수 있다.
- Python Node에서 Service 요청을 처리할 수 있다.
- 비동기 Client로 요청을 보내고 응답을 받을 수 있다.
- `ros2 service` CLI로 Service 목록, 타입, 호출을 확인할 수 있다.

## 사전 요구사항

- [Message Chapter](../02_message/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Service Server

Service Server는 요청을 기다리다가 callback에서 응답을 채운다.

```python
self.create_service(SetRobotMode, 'set_mode', self.set_mode_callback)
```

요청과 응답 타입은 `.srv` 파일의 `---` 위아래로 나뉜다.

```text
string mode
---
bool success
string message
```

### Service Client

Service Client는 Service가 준비될 때까지 기다린 뒤 요청을 보낸다.

```python
future = self.client.call_async(request)
```

`call_async()`는 즉시 반환한다. 응답은 `Future`가 완료된 뒤 확인한다.

### Custom Service

이 Chapter는 `message_demo_interfaces/srv/SetRobotMode`를 사용한다.

```python
from message_demo_interfaces.srv import SetRobotMode
```

Service 타입은 CLI로 확인한다.

```bash
ros2 interface show message_demo_interfaces/srv/SetRobotMode
```

### 비동기 요청

Service 요청은 네트워크와 Server 처리 시간 때문에 바로 끝난다고 가정하면 안 된다. Python Client는 `call_async()`로 요청을 보내고, `rclpy.spin_until_future_complete()`로 응답 완료를 기다린다.

```python
rclpy.spin_until_future_complete(node, future)
```

## 패키지 구조

```text
04_service/
├── README.md
└── packages/
    └── 01_set_mode/
        └── py_service_demo/
```

예제 Package:

```text
py_service_demo/
├── package.xml
├── setup.cfg
├── setup.py
├── resource/
│   └── py_service_demo
└── py_service_demo/
    ├── __init__.py
    ├── mode_client_node.py
    └── mode_server_node.py
```

Custom Service는 Message Chapter의 Interface Package에 추가되어 있다.

```text
message_demo_interfaces/
└── srv/
    └── SetRobotMode.srv
```

## 빌드 방법

저장소 루트에서 Interface Package와 예제 Package를 함께 빌드한다.

```bash
colcon build --packages-select message_demo_interfaces py_service_demo
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

Custom Service 타입을 확인한다.

```bash
ros2 interface show message_demo_interfaces/srv/SetRobotMode
```

터미널 1에서 Server를 실행한다.

```bash
ros2 run py_service_demo mode_server
```

터미널 2에서 Client를 실행한다.

```bash
source install/setup.bash
ros2 run py_service_demo mode_client auto
```

zsh:

```bash
source install/setup.zsh
ros2 run py_service_demo mode_client auto
```

터미널 3에서 Service 상태를 확인한다.

```bash
source install/setup.bash
ros2 service list
ros2 service type /service_demo/set_mode
ros2 service call /service_demo/set_mode message_demo_interfaces/srv/SetRobotMode "{mode: manual}"
```

zsh:

```bash
source install/setup.zsh
ros2 service list
ros2 service type /service_demo/set_mode
ros2 service call /service_demo/set_mode message_demo_interfaces/srv/SetRobotMode "{mode: manual}"
```

잘못된 모드로 요청하면 실패 응답을 확인할 수 있다.

```bash
ros2 run py_service_demo mode_client invalid
```

## 예상 결과

- `ros2 interface show`에서 `mode`, `success`, `message` 필드가 출력된다.
- `mode_server`가 `/service_demo/set_mode` Service를 제공한다.
- `mode_client auto`는 `success=True` 응답을 받는다.
- `mode_client invalid`는 `success=False` 응답을 받는다.
- `ros2 service call`로도 같은 Service를 호출할 수 있다.

## 정리

Service는 요청과 응답이 명확한 짧은 작업에 사용한다. 계속 변하는 센서값이나 상태 흐름은 Topic이 맞고, 오래 걸리며 중간 진행률과 취소가 필요한 작업은 Action이 맞다.

## 참고 자료

- [Message Chapter](../02_message/README.md)
- [Topic Advanced Chapter](../03_topic_advanced/README.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
