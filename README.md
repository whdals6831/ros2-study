# ROS2 Study Repository

ROS2를 체계적으로 학습하기 위한 저장소입니다.

각 Chapter는 개념 문서와 실행 가능한 ROS2 Package를 함께 제공하여 이론과 실습을 같이 다룹니다.

## Goals

- ROS2 핵심 개념 이해
- ROS2 Package 직접 구현
- ROS2 내부 구조와 동작 방식 이해
- 실무에서 사용하는 ROS2 기능 학습
- 학습 내용을 문서와 코드로 함께 정리

## Documentation

저장소 공통 문서는 `docs/`에서 관리합니다.

| File | Description |
| --- | --- |
| [docs/architecture.md](docs/architecture.md) | ROS2 전체 구조와 주요 구성 요소 |
| [docs/roadmap.md](docs/roadmap.md) | 전체 학습 순서와 진행 계획 |
| [docs/environment.md](docs/environment.md) | ROS2 설치 및 개발 환경 구성 |
| [docs/conventions.md](docs/conventions.md) | 디렉터리, Package, 코드 작성 규칙 |

## Repository Structure

```text
ros2-study/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   ├── environment.md
│   └── conventions.md
├── scripts/
└── chapters/
```

## Study Flow

1. [개발 환경](docs/environment.md)을 준비합니다.
2. [학습 로드맵](docs/roadmap.md)에 따라 Phase와 Chapter를 진행합니다.
3. Chapter README에서 개념과 실행 방법을 확인합니다.
4. 예제 Package를 빌드하고 실행합니다.
5. 새 예제나 문서를 추가할 때는 [작성 규칙](docs/conventions.md)을 따릅니다.

## Design

이 저장소는 다음 계층으로 구성합니다.

```text
Repository
└── Phase
    └── Chapter
        ├── Documentation
        ├── Images
        └── Package Examples
            └── ROS2 Package
```

ROS2 개념 배경은 [architecture.md](docs/architecture.md), 구체적인 Chapter 진행 순서는 [roadmap.md](docs/roadmap.md)를 참고합니다.
