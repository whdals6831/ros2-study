# Development Checks

## 개요

이 Chapter는 ROS2 개발 중 자주 사용하는 점검 명령을 한 번에 정리한다.

Node를 만들고 Launch로 실행할 수 있어도, 실제 개발에서는 실행 상태를 확인하고 문제가 생긴 위치를 좁히는 일이 반복된다. `ros2 doctor`, ROS2 graph CLI, `rqt_graph`, `colcon test`, lint 명령은 이때 사용하는 기본 점검 도구다.

## 학습 목표

- `ros2 doctor`로 ROS2 환경 상태를 확인할 수 있다.
- `ros2 node list/info`로 실행 중인 Node를 확인할 수 있다.
- `ros2 topic list/info/echo/hz`로 Topic 상태와 메시지 흐름을 확인할 수 있다.
- `rqt_graph`로 Node와 Topic 연결을 시각적으로 확인할 수 있다.
- `colcon test`로 Package 테스트를 실행할 수 있다.
- Python lint 테스트 결과를 확인할 수 있다.

## 사전 요구사항

- [Launch Chapter](../07_launch/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.
- `py_launch_demo` Package가 빌드되어 있어야 한다.
- Topic 점검에는 ROS2 기본 데모 Package인 `demo_nodes_cpp`를 사용한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### ros2 doctor

`ros2 doctor`는 ROS2 설치, 환경 변수, 네트워크 설정, middleware 상태를 점검한다.

```bash
ros2 doctor
```

상세 보고서를 보려면 `--report`를 붙인다.

```bash
ros2 doctor --report
```

문제가 생겼을 때는 먼저 이 명령으로 환경 자체가 깨졌는지 확인한다.

### Node 점검

실행 중인 Node 목록은 `ros2 node list`로 확인한다.

```bash
ros2 node list
```

특정 Node의 Publisher, Subscriber, Service, Action 정보는 `ros2 node info`로 확인한다.

```bash
ros2 node info /demo/main
```

Node가 목록에 없다면 보통 다음 중 하나다.

- Node가 실행되지 않았다.
- 다른 터미널에서 workspace setup을 source하지 않았다.
- 다른 `ROS_DOMAIN_ID`를 사용하고 있다.
- Node 이름이나 Namespace가 예상과 다르다.

### Topic 점검

Topic 목록은 `ros2 topic list`로 확인한다. 이 Chapter에서는 실제 메시지를 publish하는 `demo_nodes_cpp`의 `talker`를 Topic 점검에 사용한다.

```bash
ros2 topic list
```

Topic 타입과 Publisher, Subscriber 수는 `ros2 topic info`로 확인한다.

```bash
ros2 topic info /chatter
```

메시지 내용을 직접 보려면 `ros2 topic echo`를 사용한다.

```bash
ros2 topic echo /chatter
```

메시지 publish 주기는 `ros2 topic hz`로 확인한다.

```bash
ros2 topic hz /chatter
```

`echo`나 `hz`가 아무것도 출력하지 않으면 Topic 이름, 메시지 publish 여부, QoS 설정을 먼저 확인한다.

### rqt_graph

`rqt_graph`는 ROS2 graph를 그림으로 보여준다.

```bash
rqt_graph
```

CLI는 정확한 값을 확인하기 좋고, `rqt_graph`는 전체 연결 구조를 빠르게 보기 좋다. Node나 Topic이 많아질수록 시각화 도구로 연결 방향을 먼저 확인하는 편이 빠르다.

### colcon test

`colcon test`는 Package의 테스트를 실행한다.

```bash
colcon test --packages-select py_launch_demo
```

테스트 결과는 다음 명령으로 확인한다.

```bash
colcon test-result --verbose
```

테스트가 실패하면 실패한 Package와 테스트 파일을 먼저 확인한다.

### Lint 실행

이 저장소의 Python 예제 Package는 `ament_flake8`, `ament_pep257` 테스트를 포함한다.

```text
test/
├── test_flake8.py
└── test_pep257.py
```

따라서 별도 lint 명령을 만들지 않아도 `colcon test`가 lint를 함께 실행한다.

Python 파일만 빠르게 확인하고 싶다면 Package 디렉터리에서 직접 실행할 수도 있다.

```bash
python3 -m flake8 py_launch_demo test
python3 -m pydocstyle py_launch_demo
```

직접 실행은 도구가 설치되어 있을 때만 가능하다. 저장소 기준 점검은 `colcon test`를 기본으로 둔다.

## 패키지 구조

이 Chapter는 점검 명령을 다루므로 새 ROS2 Package를 추가하지 않는다. 이전 Chapter의 `py_launch_demo` Package를 사용한다.

```text
08_development_checks/
└── README.md
```

사용하는 예제 Package:

```text
07_launch/
└── packages/
    └── 01_launch_node/
        └── py_launch_demo/
```

## 빌드 방법

저장소 루트에서 예제 Package를 빌드한다.

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

터미널 1에서 Launch 예제를 실행한다.

```bash
ros2 launch py_launch_demo demo.launch.py
```

터미널 2에서 ROS2 기본 talker를 실행한다.

```bash
source install/setup.bash
ros2 run demo_nodes_cpp talker
```

zsh:

```bash
source install/setup.zsh
ros2 run demo_nodes_cpp talker
```

`demo_nodes_cpp`가 없다면 설치한다.

```bash
sudo apt install ros-$ROS_DISTRO-demo-nodes-cpp
```

터미널 3에서 환경을 source하고 점검 명령을 실행한다.

```bash
source install/setup.bash
```

zsh:

```bash
source install/setup.zsh
```

환경 상태를 확인한다.

```bash
ros2 doctor
```

Node를 확인한다.

```bash
ros2 node list
ros2 node info /demo/main
ros2 node info /demo/worker
```

Topic을 확인한다.

```bash
ros2 topic list
ros2 topic info /chatter
ros2 topic echo /chatter
ros2 topic hz /chatter
```

graph를 시각적으로 확인한다.

```bash
rqt_graph
```

테스트와 lint를 실행한다.

```bash
colcon test --packages-select py_launch_demo
colcon test-result --verbose
```

## 예상 결과

- `ros2 doctor`가 ROS2 환경 점검 결과를 출력한다.
- `ros2 node list`에서 `/demo/main`, `/demo/worker`를 확인할 수 있다.
- `ros2 node info /demo/main`에서 Node의 통신 정보를 확인할 수 있다.
- `ros2 topic list`에서 `/chatter`를 확인할 수 있다.
- `ros2 topic echo /chatter`가 publish되는 메시지를 출력한다.
- `ros2 topic hz /chatter`가 메시지 주기를 출력한다.
- `rqt_graph`에서 Node와 Topic 연결을 확인할 수 있다.
- `colcon test-result --verbose`가 lint와 테스트 결과를 출력한다.

## 정리

Development Checks는 코드를 더 쓰는 작업이 아니라 현재 ROS2 graph와 Package 상태를 확인하는 반복 절차다. 실행 문제는 `ros2 doctor`로 환경을 확인하고, `ros2 node`, `ros2 topic`, `rqt_graph`로 graph를 좁힌 뒤, `colcon test`로 Package 품질을 확인한다.

## 참고 자료

- [Launch Chapter](../07_launch/README.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
