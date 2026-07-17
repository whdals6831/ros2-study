# ROS2 Architecture

이 문서는 ROS2 학습 중 반복해서 등장하는 구조를 한곳에서 정리한다.

## System Layers

ROS2 애플리케이션은 보통 다음 계층으로 나뉜다.

1. Application: 사용자가 작성하는 Node, Launch, Parameter, 로봇 로직
2. Client Library: `rclcpp`, `rclpy`
3. ROS Client Library Core: `rcl`, executor, wait set, graph API
4. Middleware Interface: `rmw`
5. DDS/RTPS: discovery, publish/subscribe transport, QoS

각 Chapter의 예제는 Application 계층에서 시작하되, 통신과 실행 모델을 설명할 때 아래 계층까지 내려간다.

## Core Concepts

### Node

Node는 ROS2에서 실행 단위가 되는 프로세스 또는 구성 요소다. 하나의 프로세스에 하나의 Node만 둘 수도 있고, Component와 Composition을 사용해 여러 Node를 같은 프로세스에 올릴 수도 있다.

### Topic

Topic은 비동기 publish/subscribe 통신에 사용한다. 센서 데이터, 상태 스트림, 주기적 이벤트처럼 지속적으로 흐르는 데이터에 적합하다.

### Service

Service는 요청과 응답이 한 쌍인 동기 또는 비동기 호출에 사용한다. 설정 조회, 단발성 명령, 즉시 결과가 필요한 작업에 적합하다.

### Action

Action은 오래 걸리는 목표 지향 작업에 사용한다. Goal, Feedback, Result, Cancel 흐름을 가지며 Navigation2나 MoveIt2 같은 고수준 작업에서 자주 사용한다.

### Parameter

Parameter는 Node 실행 중 조정 가능한 설정값이다. 예제에서는 하드코딩 대신 YAML Parameter 또는 Launch Argument를 우선 사용한다.

### Launch

Launch 파일은 여러 Node, Parameter, Namespace, 조건부 실행을 함께 관리한다. 실행 방법이 두 줄 이상으로 늘어나면 Launch 파일을 추가한다.

## Execution Model

Executor는 callback을 언제 어떤 thread에서 실행할지 결정한다.

- Single-threaded Executor: 기본 학습 예제에 사용한다.
- Multi-threaded Executor: callback 병렬 실행이나 blocking 작업 비교가 필요할 때 사용한다.
- Callback Group: 같은 Node 안에서 callback 간 동시 실행 가능 여부를 제어한다.

성능이나 동시성 Chapter가 아니라면 가장 단순한 Executor 구성을 사용한다.

## Communication Model

ROS2 통신은 DDS QoS의 영향을 받는다. 기본 예제는 ROS2 기본 QoS를 사용하고, QoS 자체를 학습하는 Chapter에서만 reliability, durability, history, depth를 명시적으로 바꾼다.

## Package Boundary

각 ROS2 Package는 독립적으로 빌드 가능해야 한다.

- 의존성은 `package.xml`에 둔다.
- C++ 빌드 규칙은 `CMakeLists.txt`에 둔다.
- Python 패키징 규칙은 `setup.py`와 `setup.cfg`에 둔다.
- 실행에 필요한 launch, config, rviz, urdf 파일은 install 대상에 포함한다.

## Study Direction

처음에는 Node, Topic, Service, Action의 사용법을 익히고, 이후 Executor, Component, DDS, Real-Time으로 내부 구조를 확장해서 본다.

## Repository Design

저장소는 문서와 실행 가능한 예제를 함께 유지하는 구조를 따른다.

```text
Repository
└── Phase
    └── Chapter
        ├── Documentation
        ├── Images
        └── Package Examples
            ├── Example Topic
            │   ├── C++ Package
            │   └── Python Package
            └── Example Topic
                └── ROS2 Package
```

각 계층의 역할:

| Level | Description |
| --- | --- |
| Repository | 전체 ROS2 학습 저장소 |
| Phase | 관련 기능을 묶은 학습 단위 |
| Chapter | 하나의 ROS2 주제 |
| Documentation | 개념과 실행 방법을 설명하는 문서 |
| Images | 문서와 실행 결과에 사용되는 이미지 |
| Package Example | 세부 학습 주제를 다루는 예제 단위 |
| ROS2 Package | 독립적으로 빌드하고 실행할 수 있는 코드 |

## Repository Philosophy

이 저장소는 문서와 코드가 함께 존재하는 ROS2 학습 저장소를 목표로 한다.

각 Chapter는 하나의 ROS2 기능을 다루며, 개념을 설명하는 문서와 직접 실행할 수 있는 ROS2 Package를 함께 제공한다.

Chapter 내부의 예제는 학습 주제와 난이도에 따라 분리하며, 각 예제에는 독립적으로 빌드하고 실행할 수 있는 ROS2 Package를 배치한다.

전체 커리큘럼을 순차적으로 따라가면 ROS2의 기본 구조부터 통신, 로봇 모델링, 성능 최적화, 내부 구조 및 응용 기능까지 단계적으로 학습할 수 있도록 구성한다.
