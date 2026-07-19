# ROS2 Overview

## 개요

이 Chapter는 ROS2를 본격적으로 사용하기 전에 전체 구조와 기본 명령 흐름을 훑는다.

ROS2는 여러 Node가 DDS 기반 통신으로 데이터를 주고받는 로봇 소프트웨어 프레임워크다. 이후 Chapter에서는 이 구조를 Workspace, Package, Node, Topic, Service, Action 순서로 직접 구현한다.

## 학습 목표

- ROS2가 해결하려는 문제를 설명할 수 있다.
- ROS2의 주요 계층을 구분할 수 있다.
- ROS1과 ROS2의 큰 차이를 이해한다.
- DDS가 ROS2 통신에서 맡는 역할을 설명할 수 있다.
- 기본 ROS2 CLI로 설치 상태와 graph 정보를 확인할 수 있다.

## 사전 요구사항

- [개발 환경](../../../docs/environment.md)에 따라 ROS2와 `colcon`이 설치되어 있어야 한다.
- 새 터미널에서 ROS2 환경이 source 되어 있어야 한다.

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
```

zsh를 사용한다면 다음을 사용한다.

```bash
source /opt/ros/$ROS_DISTRO/setup.zsh
```

## 핵심 개념

### ROS2

ROS2는 로봇 애플리케이션을 여러 실행 단위로 나누고, 그 사이의 통신과 실행을 관리한다.

주요 구성 요소:

| 구성 요소 | 역할 |
| --- | --- |
| Node | ROS2에서 실행되는 기본 단위 |
| Topic | 지속적으로 흐르는 데이터 publish/subscribe |
| Service | 요청과 응답이 한 쌍인 통신 |
| Action | 오래 걸리는 목표 기반 작업 |
| Parameter | Node 실행 중 조정 가능한 설정 |
| Launch | 여러 Node와 설정을 한 번에 실행 |

### Architecture

ROS2 애플리케이션은 보통 다음 계층으로 이해한다.

```text
Application
Client Library: rclcpp, rclpy
ROS Client Library Core: rcl
Middleware Interface: rmw
DDS/RTPS
```

상세 구조는 [architecture.md](../../../docs/architecture.md)를 참고한다.

### ROS1과 ROS2의 차이

| 항목 | ROS1 | ROS2 |
| --- | --- | --- |
| 중앙 관리 | ROS Master 필요 | DDS discovery 사용 |
| 통신 기반 | 자체 TCPROS/UDPROS | DDS/RTPS |
| QoS | 제한적 | reliability, durability, history 등 지원 |
| 실시간성 | 제한적 | 실시간 시스템을 고려한 구조 |
| 보안 | 기본 기능 부족 | DDS-Security 기반 확장 가능 |

### DDS

DDS는 ROS2의 기본 통신 계층이다. ROS2 Node는 직접 DDS API를 다루지 않고 `rclcpp`, `rclpy`, `rmw`를 통해 DDS 기능을 사용한다.

DDS가 맡는 대표 역할:

- 같은 ROS Domain 안의 Node 발견
- Publisher와 Subscriber 연결
- QoS 정책 적용
- 네트워크 전송 처리

### ROS2 CLI

ROS2 CLI는 현재 환경과 graph 상태를 확인하는 기본 도구다.

자주 쓰는 명령:

```bash
ros2 --help
ros2 doctor
ros2 node list
ros2 topic list
ros2 service list
ros2 action list
```

## 패키지 구조

이 Chapter는 개념 정리용 Chapter라 ROS2 Package 예제를 포함하지 않는다.

```text
01_ros2_overview/
└── README.md
```

## 빌드 방법

빌드할 Package가 없다.

다음 Chapter부터 `colcon build`를 사용한다.

## 실행 방법

설치와 환경 설정을 확인한다.

```bash
ros2 --help
ros2 doctor
```

터미널 두 개를 열고 ROS2 데모 Node를 실행해 graph를 확인할 수 있다.

터미널 1:

```bash
ros2 run demo_nodes_cpp talker
```

터미널 2:

```bash
ros2 run demo_nodes_cpp listener
ros2 node list
ros2 topic list
ros2 topic echo /chatter
```

데모 패키지가 없다면 설치한다.

```bash
sudo apt install ros-$ROS_DISTRO-demo-nodes-cpp
```

## 예상 결과

- `ros2 doctor`가 ROS2 환경 상태를 출력한다.
- `talker`는 `/chatter` Topic으로 문자열을 publish한다.
- `listener`는 `/chatter` Topic 메시지를 받아 출력한다.
- `ros2 node list`에서 talker와 listener Node를 확인할 수 있다.

## 정리

ROS2는 Node를 실행 단위로 두고 DDS 기반 통신으로 graph를 구성한다. 이 Chapter에서는 전체 구조만 확인하고, 다음 Chapter부터 Workspace와 Package를 직접 만든다.

## 참고 자료

- [ROS2 Architecture](../../../docs/architecture.md)
- [Development Environment](../../../docs/environment.md)
- [Learning Roadmap](../../../docs/roadmap.md)
