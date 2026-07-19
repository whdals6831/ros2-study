# Node

## 개요

이 Chapter는 ROS2 Node의 생성, 실행, 이름, Namespace, CLI 확인 방법을 다룬다.

Node는 ROS2 애플리케이션의 기본 실행 단위다. 이후 Topic, Service, Action, Parameter, Launch는 모두 Node를 기준으로 연결된다.

## 학습 목표

- ROS2 Node의 역할을 설명할 수 있다.
- C++ 또는 Python Package 안에 Node 실행 파일을 구성할 수 있다.
- `ros2 run`으로 Node를 실행할 수 있다.
- Node 이름과 Namespace가 ROS graph에 어떻게 보이는지 확인할 수 있다.
- `ros2 node list`, `ros2 node info`로 실행 중인 Node를 점검할 수 있다.

## 사전 요구사항

- [Package Chapter](../03_package/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Node

Node는 ROS2에서 실행되는 독립적인 기능 단위다.

한 Node는 보통 하나의 책임만 가진다.

예:

- 센서 값을 읽는 Node
- 모터 명령을 보내는 Node
- 상태를 계산하는 Node
- 다른 Node를 감시하는 Node

### Node 생성

C++에서는 `rclcpp::Node`, Python에서는 `rclpy.node.Node`를 사용한다.

권장 패키지 이름:

```text
cpp_node_minimal
py_node_minimal
```

### Node 실행

빌드와 source가 끝난 뒤 `ros2 run`으로 실행한다.

```bash
ros2 run <package_name> <executable_name>
```

예:

```bash
ros2 run cpp_node_minimal minimal_node
ros2 run py_node_minimal minimal_node
```

### Node 이름

Node 이름은 ROS graph에서 Node를 구분하는 이름이다.

CLI에서 실행 시 이름을 바꿀 수 있다.

```bash
ros2 run py_node_minimal minimal_node --ros-args -r __node:=renamed_node
```

### Namespace

Namespace는 Node와 Topic, Service 이름을 그룹화한다.

```bash
ros2 run py_node_minimal minimal_node --ros-args -r __ns:=/robot1
```

Namespace가 적용되면 Node는 `/robot1/<node_name>` 형태로 보인다.

### Node CLI

실행 중인 Node 목록:

```bash
ros2 node list
```

Node 상세 정보:

```bash
ros2 node info /minimal_node
```

Namespace가 있으면 전체 이름을 사용한다.

```bash
ros2 node info /robot1/minimal_node
```

## 패키지 구조

이 Chapter에서는 문서와 디렉터리 구조만 제공한다. Package 소스코드는 `01_minimal_node` 아래에 직접 구성한다.

```text
04_node/
├── README.md
├── images/
└── packages/
    └── 01_minimal_node/
```

권장 Package 배치:

```text
packages/
└── 01_minimal_node/
    ├── cpp_node_minimal/
    └── py_node_minimal/
```

## 빌드 방법

Package 소스코드를 추가한 뒤 저장소 루트에서 빌드한다.

```bash
colcon build
```

특정 Package만 빌드한다.

```bash
colcon build --packages-select cpp_node_minimal py_node_minimal
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

최소 Node 실행:

```bash
ros2 run py_node_minimal minimal_node
```

다른 터미널에서 Node 목록 확인:

```bash
ros2 node list
```

Node 정보 확인:

```bash
ros2 node info /minimal_node
```

같은 실행 파일로 Node 이름 변경:

```bash
ros2 run py_node_minimal minimal_node --ros-args -r __node:=renamed_node
```

같은 실행 파일로 Namespace 적용:

```bash
ros2 run py_node_minimal minimal_node --ros-args -r __ns:=/robot1
```

## 예상 결과

- 실행 중인 Node가 `ros2 node list`에 표시된다.
- 이름을 remap하면 변경된 Node 이름으로 표시된다.
- Namespace를 적용하면 `/robot1/<node_name>` 형태로 표시된다.
- `ros2 node info`에서 Node의 Publisher, Subscriber, Service, Action 정보가 출력된다.

## 정리

Node는 ROS2 graph의 기본 실행 단위다. Package 안에 실행 파일을 설치하고 `ros2 run`으로 실행한 뒤, `ros2 node` CLI로 graph에 등록된 상태를 확인한다.

## 참고 자료

- [ROS2 Architecture](../../../docs/architecture.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
