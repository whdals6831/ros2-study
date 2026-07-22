# Action

## 개요

이 Chapter는 ROS2 Action으로 오래 걸리는 작업을 요청하고, 진행 상태와 최종 결과를 받는 방법을 다룬다.

Service는 짧은 요청과 응답에 적합하다. Action은 이동, 충전, 탐색처럼 시간이 걸리고 중간 진행률이나 취소가 필요한 작업에 적합하다. 예제는 `MoveRobot` Custom Action으로 목표 거리만큼 이동하는 Server와 Client를 만든다.

## 학습 목표

- Action Server와 Action Client의 역할을 설명할 수 있다.
- `.action` 파일로 Goal, Result, Feedback을 정의할 수 있다.
- Python Node에서 Action Goal을 처리할 수 있다.
- Client에서 Feedback과 Result를 받을 수 있다.
- 실행 중인 Goal을 취소할 수 있다.
- `ros2 action` CLI로 Action 목록, 타입, 호출을 확인할 수 있다.

## 사전 요구사항

- [Service Chapter](../04_service/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Action Server

Action Server는 Goal을 받은 뒤 작업을 수행하고, 중간 상태를 Feedback으로 보낸다.

```python
self.action_server = ActionServer(self, MoveRobot, 'move_robot', self.execute_callback)
```

### Action Client

Action Client는 Goal을 보내고, Feedback callback과 Result future로 진행 상태와 결과를 받는다.

```python
send_goal_future = self.action_client.send_goal_async(
    goal,
    feedback_callback=self.feedback_callback,
)
```

### Custom Action

Action 타입은 `.action` 파일에 Goal, Result, Feedback을 `---`로 나눠 정의한다.

```text
float32 target_distance
---
bool success
float32 final_distance
string message
---
float32 current_distance
float32 remaining_distance
```

이 Chapter는 `message_demo_interfaces/action/MoveRobot`을 사용한다.

```python
from message_demo_interfaces.action import MoveRobot
```

### Goal, Feedback, Result

- Goal: Client가 Server에 요청하는 목표다.
- Feedback: Server가 작업 중간에 보내는 진행 상태다.
- Result: 작업이 끝난 뒤 Server가 보내는 최종 결과다.

일반적인 Action 완료 흐름은 다음과 같다.

```text
Action Client                 Action Server
     |                              |
     | send_goal_async()            |
     |----------------------------->|
     | Goal accepted                |
     |<-----------------------------|
     | Feedback                     |
     |<-----------------------------|
     | Feedback                     |
     |<-----------------------------|
     |                              | goal_handle.succeed()
     | Result success=True          |
     |<-----------------------------|
```

### Cancel

Action은 실행 중인 Goal을 취소할 수 있다. Server는 취소 요청을 확인하고 취소된 Result를 반환한다.

Client는 `GoalHandle`을 받은 뒤 `cancel_goal_async()`로 취소를 요청한다.

```python
goal_handle.cancel_goal_async()
```

Server는 취소 요청을 받을지 결정하는 callback에서 `CancelResponse.ACCEPT`를 반환해야 한다.

```python
def cancel_callback(self, goal_handle):
    return CancelResponse.ACCEPT
```

실제 작업 loop에서는 취소 요청이 들어왔는지 반복해서 확인한다.

```python
if goal_handle.is_cancel_requested:
    goal_handle.canceled()
```

작업 callback이 오래 실행되면 cancel 요청도 함께 처리할 수 있도록 `MultiThreadedExecutor`와 `ReentrantCallbackGroup`을 사용한다.

취소는 즉시 모터를 멈추는 비상 정지와 다르다. 실제 로봇에서는 먼저 모터 정지 명령이나 하드웨어 E-stop으로 로봇을 안전 상태로 만들고, 그 다음 진행 중인 Action Goal을 취소한다.

취소 흐름은 다음과 같다.

```text
Action Client                 Executor                 Action Server
     |                            |                          |
     | send_goal_async()          |                          |
     |------------------------------------------------------>|
     | Goal accepted              |                          |
     |<------------------------------------------------------|
     | Feedback                   |                          |
     |<------------------------------------------------------|
     | cancel_goal_async()        |                          |
     |------------------------------------------------------>|
     |                            | cancel_callback()        |
     |                            |------------------------->|
     |                            | CancelResponse.ACCEPT    |
     |                            |<-------------------------|
     |                            |                          | is_cancel_requested 확인
     |                            |                          | goal_handle.canceled()
     | Result success=False       |                          |
     |<------------------------------------------------------|
```

## 패키지 구조

```text
05_action/
├── README.md
└── packages/
    └── 01_move_robot/
        └── py_action_demo/
```

예제 Package:

```text
py_action_demo/
├── package.xml
├── setup.cfg
├── setup.py
├── resource/
│   └── py_action_demo
└── py_action_demo/
    ├── __init__.py
    ├── move_client_node.py
    └── move_server_node.py
```

Custom Action은 Message Chapter의 Interface Package에 추가되어 있다.

```text
message_demo_interfaces/
└── action/
    └── MoveRobot.action
```

## 빌드 방법

저장소 루트에서 Interface Package와 예제 Package를 함께 빌드한다.

```bash
colcon build --packages-select message_demo_interfaces py_action_demo
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

Custom Action 타입을 확인한다.

```bash
ros2 interface show message_demo_interfaces/action/MoveRobot
```

터미널 1에서 Server를 실행한다.

```bash
ros2 run py_action_demo move_server
```

터미널 2에서 Client를 실행한다.

```bash
source install/setup.bash
ros2 run py_action_demo move_client 5.0
```

zsh:

```bash
source install/setup.zsh
ros2 run py_action_demo move_client 5.0
```

취소 흐름을 확인하려면 `cancel` 인자를 추가한다.

```bash
ros2 run py_action_demo move_client 5.0 cancel
```

취소가 정상 처리되면 최종 Result가 실패로 출력된다.

```text
success=False, final_distance=1.0m, message="move canceled at 1.0m"
```

취소가 되지 않고 끝까지 완료된다면 다음을 확인한다.

- Server 코드가 `cancel_callback`에서 `CancelResponse.ACCEPT`를 반환하는지 확인한다.
- Server가 `MultiThreadedExecutor`와 `ReentrantCallbackGroup`으로 실행되는지 확인한다.
- 같은 이름의 Action Server가 여러 개 떠 있지 않은지 확인한다.

터미널 3에서 Action 상태를 확인한다.

```bash
source install/setup.bash
ros2 action list
ros2 action info /action_demo/move_robot
ros2 action send_goal /action_demo/move_robot message_demo_interfaces/action/MoveRobot "{target_distance: 3.0}" --feedback
```

zsh:

```bash
source install/setup.zsh
ros2 action list
ros2 action info /action_demo/move_robot
ros2 action send_goal /action_demo/move_robot message_demo_interfaces/action/MoveRobot "{target_distance: 3.0}" --feedback
```

## 예상 결과

- `ros2 interface show`에서 Goal, Result, Feedback 필드가 출력된다.
- `move_server`가 `/action_demo/move_robot` Action을 제공한다.
- `move_client 5.0`은 1m 단위 Feedback을 받고 `success=True` Result를 출력한다.
- `move_client 5.0 cancel`은 첫 Feedback 뒤 Goal을 취소하고 `success=False` Result를 출력한다.
- `ros2 action send_goal --feedback`으로도 같은 Action을 호출할 수 있다.

## 정리

Action은 오래 걸리는 작업을 Goal, Feedback, Result로 나눠 표현한다. 요청과 응답만 있으면 Service가 더 단순하고, 계속 흐르는 데이터는 Topic이 맞다. 작업 중간 상태와 취소가 필요할 때 Action을 사용한다.

## 참고 자료

- [Service Chapter](../04_service/README.md)
- [Message Chapter](../02_message/README.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
