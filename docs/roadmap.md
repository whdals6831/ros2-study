# Learning Roadmap

이 문서는 README의 Curriculum을 실제 학습 순서로 압축한 진행 계획이다.

## Phase 1. Basic

목표: ROS2 프로젝트를 만들고 실행하는 최소 흐름을 익힌다.

완료 기준:

- Workspace를 만들고 `colcon build`로 빌드할 수 있다.
- `colcon test`, `ros2 doctor`, ROS2 CLI로 기본 상태를 확인할 수 있다.
- C++ 또는 Python Package를 직접 만들 수 있다.
- Node, Parameter, Logging, Launch의 기본 사용법을 설명할 수 있다.

권장 순서:

1. ROS2 Overview
   - ROS2 소개
   - Architecture
   - ROS1과 ROS2의 차이
   - DDS 개요
   - ROS2 CLI
2. Workspace
   - Workspace 구조
   - Underlay와 Overlay
   - `colcon` 사용법
   - Workspace 빌드
3. Package
   - ROS2 Package 구조
   - `ament_cmake`
   - `ament_python`
   - `package.xml`
   - `CMakeLists.txt`
   - `setup.py`
4. Node
   - Node 생성
   - Node 실행
   - Node 이름
   - Namespace
   - Node CLI
5. Logging
   - Logging API
   - Log Level
   - Console Output
   - Logger 설정
6. Parameter
   - Parameter 선언
   - Parameter 읽기와 변경
   - Parameter Callback
   - YAML Parameter
7. Launch
   - Python Launch
   - Launch Argument
   - Node 실행
   - Namespace
   - Remapping
   - Parameter YAML 적용
   - 여러 Node 동시 실행
   - Launch File 포함
   - 조건부 실행
8. Development Checks
   - `ros2 doctor`
   - `ros2 node list/info`
   - `ros2 topic list/info/echo/hz`
   - `rqt_graph`
   - `colcon test`
   - Lint 실행

## Phase 2. Communication

목표: ROS2의 주요 통신 방식을 구분해서 사용한다.

완료 기준:

- Topic, Service, Action을 언제 써야 하는지 구분할 수 있다.
- 표준 Message와 Custom Message를 작성하고 빌드할 수 있다.
- QoS 설정이 통신 결과에 주는 영향을 재현할 수 있다.

권장 순서:

1. Topic
   - Publisher
   - Subscriber
   - Topic CLI
2. Message
   - Standard Message
   - Custom Message
   - Message Interface Package
   - Message 의존성
3. Topic Advanced
   - Publish Frequency
   - Multiple Publisher와 Subscriber
   - Custom Message Topic
   - Topic Remapping
4. Service
   - Service Server
   - Service Client
   - Custom Service
   - 비동기 요청
5. Action
   - Action Server
   - Action Client
   - Goal
   - Feedback
   - Result
   - Cancel
6. QoS
   - Reliability
   - Durability
   - History
   - Depth
   - Deadline
   - Liveliness
   - QoS Compatibility

## Phase 3. Robot

목표: 로봇 모델과 좌표계, 시각화, 데이터 기록 흐름을 익힌다.

완료 기준:

- TF tree를 만들고 RViz2에서 확인할 수 있다.
- URDF/Xacro로 간단한 로봇 모델을 표현할 수 있다.
- rosbag2로 Topic을 기록하고 재생할 수 있다.

권장 순서:

1. TF2
   - Coordinate Frame
   - Static Transform
   - Dynamic Transform
   - Transform Broadcaster
   - Transform Listener
   - TF Tree
2. URDF
   - Link
   - Joint
   - Visual
   - Collision
   - Inertial
   - Xacro
   - Robot State Publisher
3. RViz2
   - Display
   - Robot Model
   - TF
   - Marker
   - Interactive Marker
   - RViz Configuration
4. rosbag2
   - Topic Record
   - Playback
   - Storage
   - Compression
   - Topic Filtering

## Phase 4. Optimization

목표: ROS2 실행 구조와 성능 관련 선택지를 이해한다.

완료 기준:

- Component와 Composable Node의 차이를 설명할 수 있다.
- Intra-process Communication의 copy 감소 효과를 확인할 수 있다.
- Executor와 Callback Group이 callback 실행에 주는 영향을 재현할 수 있다.
- Lifecycle Node의 상태 전이를 사용할 수 있다.

권장 순서:

1. Component
   - ROS2 Component
   - Shared Library
   - Component Registration
   - Component Container
2. Composable Node
   - Component Container
   - Dynamic Loading
   - Static Loading
   - Node Composition
3. Intra-process Communication
   - Intra-process Communication
   - Shared Pointer
   - Unique Pointer
   - Message Copy
   - 성능 비교
4. Executor
   - Single-threaded Executor
   - Multi-threaded Executor
   - Static Executor
   - Spin
   - Wait Set
5. Callback Group
   - Mutually Exclusive
   - Reentrant
   - Callback 실행 제어
   - Multi-thread 환경
6. Lifecycle Node
   - Unconfigured
   - Inactive
   - Active
   - Finalized
   - State Transition
   - Managed Node

## Phase 5. Advanced

목표: ROS2 내부 구조와 실무 제약을 다룬다.

완료 기준:

- pluginlib로 런타임 확장 구조를 만들 수 있다.
- DDS와 `rmw`의 역할을 설명할 수 있다.
- 메모리 할당과 Real-Time 제약을 고려한 예제를 작성할 수 있다.

권장 순서:

1. Pluginlib
   - Plugin Interface
   - Plugin Implementation
   - Plugin Description
   - Dynamic Loading
2. DDS
   - DDS Architecture
   - Domain
   - Discovery
   - Participant
   - Publisher와 Subscriber
   - ROS Middleware
3. Memory Management
   - Smart Pointer
   - Message Allocation
   - Loaned Message
   - Memory Strategy
   - Dynamic Allocation 최소화
4. Real-Time ROS2
   - Real-Time 개념
   - Deterministic Execution
   - Scheduling
   - Priority
   - Memory Lock
   - Lock-Free Design

## Phase 6. Applications

목표: 대표 ROS2 응용 스택을 실행하고 구조를 파악한다.

완료 기준:

- Gazebo에서 로봇과 센서를 시뮬레이션할 수 있다.
- Navigation2의 주요 구성 요소를 실행할 수 있다.
- MoveIt2의 planning scene과 motion planning 흐름을 설명할 수 있다.

권장 순서:

1. Gazebo
   - Simulation
   - Robot Model
   - Sensor
   - Plugin
   - Physics
   - ROS2 Integration
2. Navigation2
   - Map
   - Localization
   - Planner
   - Controller
   - Costmap
   - Behavior Tree
   - Recovery
3. MoveIt2
   - Robot Model
   - Planning Scene
   - Motion Planning
   - Kinematics
   - Collision Detection
   - Trajectory Execution

## Learning Flow

각 Chapter는 다음 순서로 학습한다.

1. 학습 목표 확인
2. 핵심 개념 이해
3. 최소 예제 구현
4. 기능별 예제 구현
5. C++ 및 Python Package 비교
6. Package 빌드 및 실행
7. 실행 결과 확인
8. 주요 내용 정리

모든 Chapter가 반드시 C++와 Python 예제를 모두 포함할 필요는 없다.

ROS2 기능이나 라이브러리 지원 범위에 따라 C++ 또는 Python 중 하나만 제공할 수 있다.

## Chapter Completion Checklist

각 Chapter는 다음을 만족하면 완료로 본다.

- 개념 README가 있다.
- 최소 실행 예제가 있다.
- 빌드 명령과 실행 명령이 문서화되어 있다.
- 예상 출력 또는 RViz2 확인 방법이 있다.
- 불필요한 build/install/log 산출물이 커밋되지 않았다.
