# Basic

## 개요

이 Phase는 ROS2 프로젝트를 만들고 실행하는 최소 흐름을 다룬다.

Workspace를 만들고 Package와 Node를 작성한 뒤, Parameter, Logging, Launch, 개발 점검 명령까지 이어서 학습한다. 이후 Phase의 통신 예제는 이 기본 실행 흐름 위에서 진행한다.

## 학습 목표

- Workspace를 만들고 `colcon build`로 빌드할 수 있다.
- Python Package와 Node를 직접 만들 수 있다.
- Parameter, Logging, Launch의 기본 사용법을 설명할 수 있다.
- `colcon test`, `ros2 doctor`, ROS2 CLI로 기본 상태를 확인할 수 있다.

## 포함된 Chapter

1. [ROS2 Overview](01_ros2_overview/README.md)
2. [Workspace](02_workspace/README.md)
3. [Package](03_package/README.md)
4. [Node](04_node/README.md)
5. [Logging](05_logging/README.md)
6. [Parameter](06_parameter/README.md)
7. [Launch](07_launch/README.md)
8. [Development Checks](08_development_checks/README.md)

## 다음 Phase와의 연관성

Phase 2의 Communication은 이 Phase에서 만든 Node 실행, Package 빌드, CLI 점검 흐름을 그대로 사용한다. Topic, Service, Action을 학습하기 전에 이 Phase의 예제를 직접 빌드하고 실행할 수 있어야 한다.

## 정리

Basic Phase를 마치면 ROS2 예제를 만들고 실행하며, 문제가 생겼을 때 기본 CLI로 상태를 확인할 수 있다. 이 흐름이 이후 모든 ROS2 학습의 기준이 된다.
