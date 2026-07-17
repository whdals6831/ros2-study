# ROS2 Study Repository

> ROS2를 체계적으로 학습하기 위한 Repository입니다.
>
> 각 Chapter는 **개념 문서(Documentation)** 와 **실행 가능한 ROS2 Package**를 함께 제공하여 이론과 실습을 동시에 학습할 수 있도록 구성합니다.

---

## Goals

- ROS2 핵심 개념 이해
- ROS2 Package 직접 구현
- ROS2 내부 구조와 동작 방식 이해
- 실무에서 사용하는 ROS2 기능 학습
- 학습 내용을 문서와 코드로 함께 정리

---

## Repository Structure

```text
ros2-study/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   ├── environment.md
│   └── conventions.md
│
├── scripts/
│   ├── build.sh
│   ├── clean.sh
│   ├── format.sh
│   └── lint.sh
│
└── chapters/
    │
    ├── 01_basic/
    │   ├── README.md
    │   ├── 01_ros2_overview/
    │   ├── 02_workspace/
    │   ├── 03_package/
    │   ├── 04_node/
    │   ├── 05_logging/
    │   ├── 06_parameter/
    │   └── 07_launch/
    │
    ├── 02_communication/
    │   ├── README.md
    │   ├── 08_topic/
    │   ├── 09_message/
    │   ├── 10_service/
    │   ├── 11_action/
    │   └── 12_qos/
    │
    ├── 03_robot/
    │   ├── README.md
    │   ├── 13_tf2/
    │   ├── 14_urdf/
    │   ├── 15_rviz2/
    │   └── 16_rosbag2/
    │
    ├── 04_optimization/
    │   ├── README.md
    │   ├── 17_component/
    │   ├── 18_composable_node/
    │   ├── 19_intra_process/
    │   ├── 20_executor/
    │   ├── 21_callback_group/
    │   └── 22_lifecycle_node/
    │
    ├── 05_advanced/
    │   ├── README.md
    │   ├── 23_pluginlib/
    │   ├── 24_dds/
    │   ├── 25_memory_management/
    │   └── 26_real_time/
    │
    └── 06_applications/
        ├── README.md
        ├── 27_gazebo/
        ├── 28_navigation2/
        └── 29_moveit2/
```

---

## Directory Roles

### `docs`

Repository 전체에 공통으로 적용되는 내용을 관리합니다.

```text
docs/
├── architecture.md
├── roadmap.md
├── environment.md
└── conventions.md
```

| File              | Description                       |
| ----------------- | --------------------------------- |
| `architecture.md` | ROS2 전체 구조와 주요 구성 요소   |
| `roadmap.md`      | 전체 학습 순서와 진행 계획        |
| `environment.md`  | ROS2 설치 및 개발 환경 구성       |
| `conventions.md`  | 디렉터리, Package, 코드 작성 규칙 |

### `scripts`

반복적으로 사용하는 개발 명령을 스크립트로 관리합니다.

```text
scripts/
├── build.sh
├── clean.sh
├── format.sh
└── lint.sh
```

| Script      | Description            |
| ----------- | ---------------------- |
| `build.sh`  | ROS2 Package 빌드      |
| `clean.sh`  | 빌드 결과 및 캐시 제거 |
| `format.sh` | 소스 코드 포맷 적용    |
| `lint.sh`   | 코드 및 Package 검사   |

---

## Phase Structure

각 Phase는 서로 관련된 ROS2 기능을 하나의 학습 단위로 묶습니다.

```text
04_optimization/
│
├── README.md
├── 17_component/
├── 18_composable_node/
├── 19_intra_process/
├── 20_executor/
├── 21_callback_group/
└── 22_lifecycle_node/
```

각 Phase의 `README.md`에는 다음 내용을 작성합니다.

- Phase 학습 목표
- 포함된 Chapter
- 권장 학습 순서
- 이전 Phase와의 연관성
- Phase를 통해 학습할 수 있는 내용

---

## Chapter Structure

각 Chapter는 다음 구조를 기본으로 사용합니다.

```text
13_tf2/
│
├── README.md
├── images/
│
└── packages/
    ├── 01_static_transform/
    ├── 02_dynamic_transform/
    ├── 03_transform_listener/
    ├── 04_multi_frame/
    └── 05_robot_tf_tree/
```

### `README.md`

해당 Chapter의 개념과 Package 실행 방법을 설명합니다.

### `images`

문서에서 사용하는 구조도, 실행 결과, RViz2 화면 등의 이미지를 관리합니다.

### `packages`

해당 Chapter에서 구현하는 ROS2 Package를 관리합니다.

Package 예제가 여러 개라면 학습 순서를 나타내는 번호가 포함된 디렉터리로 구분합니다.

---

## Package Example Structure

하나의 Chapter 안에 여러 예제가 있는 경우 다음과 같이 구성합니다.

```text
13_tf2/
│
├── README.md
├── images/
│
└── packages/
    │
    ├── 01_static_transform/
    │   ├── cpp_tf2_static/
    │   └── py_tf2_static/
    │
    ├── 02_dynamic_transform/
    │   ├── cpp_tf2_dynamic/
    │   └── py_tf2_dynamic/
    │
    ├── 03_transform_listener/
    │   ├── cpp_tf2_listener/
    │   └── py_tf2_listener/
    │
    ├── 04_multi_frame/
    │   └── cpp_tf2_multi_frame/
    │
    └── 05_robot_tf_tree/
        └── cpp_robot_tf_tree/
```

예제 디렉터리는 다음 기준에 따라 구성합니다.

```text
packages/
├── 01_minimal/
├── 02_basic/
├── 03_intermediate/
├── 04_advanced/
└── 05_best_practice/
```

번호는 학습 순서와 예제 실행 순서를 나타냅니다.

각 예제 디렉터리에는 하나 이상의 독립적인 ROS2 Package가 포함될 수 있습니다.

---

## C++ Package Structure

C++ Package는 다음 구조를 기본으로 사용합니다.

```text
cpp_tf2_static/
│
├── package.xml
├── CMakeLists.txt
│
├── include/
│   └── cpp_tf2_static/
│
├── src/
│   └── static_transform_broadcaster.cpp
│
├── launch/
│   └── static_transform.launch.py
│
├── config/
└── rviz/
```

Package 특성에 따라 필요하지 않은 디렉터리는 생략할 수 있습니다.

---

## Python Package Structure

Python Package는 다음 구조를 기본으로 사용합니다.

```text
py_tf2_static/
│
├── package.xml
├── setup.py
├── setup.cfg
│
├── resource/
│   └── py_tf2_static
│
├── py_tf2_static/
│   ├── __init__.py
│   └── static_transform_broadcaster.py
│
├── launch/
│   └── static_transform.launch.py
│
├── config/
└── rviz/
```

Package 특성에 따라 필요하지 않은 디렉터리는 생략할 수 있습니다.

---

## Repository Design

```text
Repository
    │
    ▼
Phase
    │
    ▼
Chapter
    │
    ├── Documentation
    ├── Images
    └── Package Examples
            │
            ├── Example Topic
            │       ├── C++ Package
            │       └── Python Package
            │
            └── Example Topic
                    └── ROS2 Package
```

각 계층의 역할은 다음과 같습니다.

| Level           | Description                             |
| --------------- | --------------------------------------- |
| Repository      | 전체 ROS2 학습 저장소                   |
| Phase           | 관련 기능을 묶은 학습 단위              |
| Chapter         | 하나의 ROS2 주제                        |
| Documentation   | 개념과 실행 방법을 설명하는 문서        |
| Images          | 문서와 실행 결과에 사용되는 이미지      |
| Package Example | 세부 학습 주제를 다루는 예제 단위       |
| ROS2 Package    | 독립적으로 빌드하고 실행할 수 있는 코드 |

---

## Curriculum

### Phase 1. Basic

#### 01. ROS2 Overview

- ROS2 소개
- ROS2 Architecture
- ROS1과 ROS2의 차이
- DDS 개요
- ROS2 CLI

#### 02. Workspace

- Workspace 구조
- Underlay와 Overlay
- `colcon` 사용법
- Workspace 빌드

#### 03. Package

- ROS2 Package 구조
- `ament_cmake`
- `ament_python`
- `package.xml`
- `CMakeLists.txt`
- `setup.py`

#### 04. Node

- Node 생성
- Node 실행
- Node 이름
- Namespace
- Node CLI

#### 05. Logging

- Logging API
- Log Level
- Console Output
- Logger 설정

#### 06. Parameter

- Parameter 선언
- Parameter 읽기와 변경
- Parameter Callback
- YAML Parameter

#### 07. Launch

- Python Launch
- Launch Argument
- Node 실행
- Launch File 포함
- 조건부 실행

---

### Phase 2. Communication

#### 08. Topic

- Publisher
- Subscriber
- Topic CLI
- Publish Frequency
- Multiple Publisher와 Subscriber

#### 09. Message

- Standard Message
- Custom Message
- Message Interface Package
- Message 의존성

#### 10. Service

- Service Server
- Service Client
- Custom Service
- 비동기 요청

#### 11. Action

- Action Server
- Action Client
- Goal
- Feedback
- Result
- Cancel

#### 12. QoS

- Reliability
- Durability
- History
- Depth
- Deadline
- Liveliness
- QoS Compatibility

---

### Phase 3. Robot

#### 13. TF2

- Coordinate Frame
- Static Transform
- Dynamic Transform
- Transform Broadcaster
- Transform Listener
- TF Tree

#### 14. URDF

- Link
- Joint
- Visual
- Collision
- Inertial
- Xacro
- Robot State Publisher

#### 15. RViz2

- Display
- Robot Model
- TF
- Marker
- Interactive Marker
- RViz Configuration

#### 16. rosbag2

- Topic Record
- Playback
- Storage
- Compression
- Topic Filtering

---

### Phase 4. Optimization

#### 17. Component

- ROS2 Component
- Shared Library
- Component Registration
- Component Container

#### 18. Composable Node

- Component Container
- Dynamic Loading
- Static Loading
- Node Composition

#### 19. Intra-process Communication

- Intra-process Communication
- Shared Pointer
- Unique Pointer
- Message Copy
- 성능 비교

#### 20. Executor

- Single-threaded Executor
- Multi-threaded Executor
- Static Executor
- Spin
- Wait Set

#### 21. Callback Group

- Mutually Exclusive
- Reentrant
- Callback 실행 제어
- Multi-thread 환경

#### 22. Lifecycle Node

- Unconfigured
- Inactive
- Active
- Finalized
- State Transition
- Managed Node

---

### Phase 5. Advanced

#### 23. Pluginlib

- Plugin Interface
- Plugin Implementation
- Plugin Description
- Dynamic Loading

#### 24. DDS

- DDS Architecture
- Domain
- Discovery
- Participant
- Publisher와 Subscriber
- ROS Middleware

#### 25. Memory Management

- Smart Pointer
- Message Allocation
- Loaned Message
- Memory Strategy
- Dynamic Allocation 최소화

#### 26. Real-Time ROS2

- Real-Time 개념
- Deterministic Execution
- Scheduling
- Priority
- Memory Lock
- Lock-Free Design

---

### Phase 6. Applications

#### 27. Gazebo

- Simulation
- Robot Model
- Sensor
- Plugin
- Physics
- ROS2 Integration

#### 28. Navigation2

- Map
- Localization
- Planner
- Controller
- Costmap
- Behavior Tree
- Recovery

#### 29. MoveIt2

- Robot Model
- Planning Scene
- Motion Planning
- Kinematics
- Collision Detection
- Trajectory Execution

---

## Learning Flow

각 Chapter는 다음 순서로 학습합니다.

1. 학습 목표 확인
2. 핵심 개념 이해
3. 최소 예제 구현
4. 기능별 예제 구현
5. C++ 및 Python Package 비교
6. Package 빌드 및 실행
7. 실행 결과 확인
8. 주요 내용 정리

모든 Chapter가 반드시 C++와 Python 예제를 모두 포함할 필요는 없습니다.

ROS2 기능이나 라이브러리 지원 범위에 따라 C++ 또는 Python 중 하나만 제공할 수 있습니다.

---

## Naming Convention

### Phase

```text
01_basic
02_communication
03_robot
04_optimization
05_advanced
06_applications
```

### Chapter

```text
01_ros2_overview
02_workspace
03_package
...
18_composable_node
...
29_moveit2
```

### Package Example

```text
01_minimal_publisher
02_minimal_subscriber
03_pub_sub
04_custom_message
05_qos
```

Package Example 디렉터리 이름은 다음 형식을 사용합니다.

```text
<order>_<example_name>
```

### ROS2 Package

C++ Package는 `cpp_` 접두사를 사용합니다.

```text
cpp_topic_publisher
cpp_service_server
cpp_tf2_listener
```

Python Package는 `py_` 접두사를 사용합니다.

```text
py_topic_publisher
py_service_server
py_tf2_listener
```

Package 이름은 다음 형식을 사용합니다.

```text
<language>_<feature>_<role>
```

---

## Documentation Convention

각 Chapter의 `README.md`는 다음 순서를 기본으로 작성합니다.

```text
1.  개요
2.  학습 목표
3.  사전 요구사항
4.  핵심 개념
5.  패키지 구조
6.  빌드 방법
7.  실행 방법
8.  예상 결과
9.  정리
10. 참고 자료
```

모든 항목을 반드시 포함할 필요는 없으며 Chapter 특성에 따라 조정할 수 있습니다.

---

## Package Rules

- 각 ROS2 Package는 독립적으로 빌드할 수 있어야 합니다.
- Package 이름은 Repository 내에서 중복되지 않아야 합니다.
- Package 의존성은 `package.xml`에 명시합니다.
- C++ Package의 빌드 설정은 `CMakeLists.txt`에서 관리합니다.
- Python Package의 설정은 `setup.py`와 `setup.cfg`에서 관리합니다.
- Launch File은 가능한 경우 해당 Package의 `launch/`에 배치합니다.
- Parameter File은 해당 Package의 `config/`에 배치합니다.
- RViz 설정 파일은 해당 Package의 `rviz/`에 배치합니다.
- URDF 및 Xacro 파일은 해당 Package의 `urdf/`에 배치합니다.
- Package를 실행하는 데 필요한 파일은 설치 대상에 포함합니다.

---

## Repository Philosophy

이 Repository는 **문서와 코드가 함께 존재하는 ROS2 학습 저장소**를 목표로 합니다.

각 Chapter는 하나의 ROS2 기능을 다루며, 개념을 설명하는 문서와 직접 실행할 수 있는 ROS2 Package를 함께 제공합니다.

Chapter 내부의 예제는 학습 주제와 난이도에 따라 분리하며, 각 예제에는 독립적으로 빌드하고 실행할 수 있는 ROS2 Package를 배치합니다.

전체 커리큘럼을 순차적으로 따라가면 ROS2의 기본 구조부터 통신, 로봇 모델링, 성능 최적화, 내부 구조 및 응용 기능까지 단계적으로 학습할 수 있도록 구성합니다.
