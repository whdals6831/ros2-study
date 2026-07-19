# Workspace

## 개요

이 Chapter는 ROS2 Workspace의 구조와 `colcon` 빌드 흐름을 다룬다.

이 저장소에서는 repository root를 하나의 ROS2 Workspace로 사용한다. 이후 Chapter에서 추가하는 Package는 이 workspace 안에서 빌드하고 실행한다.

## 학습 목표

- ROS2 Workspace의 기본 구조를 설명할 수 있다.
- Underlay와 Overlay의 차이를 이해한다.
- `colcon build`로 workspace를 빌드할 수 있다.
- 빌드 결과를 source 해서 실행 환경에 반영할 수 있다.
- `colcon test`와 기본 CLI로 workspace 상태를 확인할 수 있다.

## 사전 요구사항

- [개발 환경](../../../docs/environment.md)에 따라 ROS2와 `colcon`이 설치되어 있어야 한다.
- 첫 번째 Chapter의 ROS2 CLI 확인이 끝나 있어야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Workspace

Workspace는 여러 ROS2 Package를 함께 빌드하는 작업 공간이다.

일반적인 ROS2 Workspace는 다음 디렉터리를 가진다.

```text
workspace/
├── src/
├── build/
├── install/
└── log/
```

이 저장소는 Chapter별 예제를 관리하기 위해 `src/` 대신 `chapters/` 아래에 Package를 둔다.

```text
ros2-study/
├── docs/
├── chapters/
│   └── 01_basic/
│       └── 02_workspace/
└── README.md
```

`colcon`은 workspace 아래의 Package를 찾아 빌드한다. Package가 생기면 `build/`, `install/`, `log/`가 생성된다.

### Underlay와 Overlay

Underlay는 이미 source 된 기반 환경이고, Overlay는 그 위에 얹는 현재 workspace 환경이다.

보통 ROS2 설치 환경이 Underlay다.

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
```

현재 저장소를 빌드한 뒤 source 하면 이 workspace가 Overlay가 된다.

```bash
source install/setup.bash
```

zsh를 사용한다면 `.zsh` 파일을 source 한다.

```bash
source /opt/ros/$ROS_DISTRO/setup.zsh
source install/setup.zsh
```

### colcon

`colcon`은 ROS2의 기본 빌드 도구다.

자주 쓰는 명령:

```bash
colcon build
colcon test
colcon test-result --verbose
colcon list
```

특정 Package만 빌드할 때는 `--packages-select`를 사용한다.

```bash
colcon build --packages-select <package_name>
```

## 패키지 구조

이 Chapter는 workspace 개념과 명령 흐름을 다루므로 별도 Package 예제를 포함하지 않는다.

```text
02_workspace/
└── README.md
```

## 빌드 방법

저장소 루트에서 빌드한다.

```bash
cd ros2-study
colcon build
```

아직 Package가 없다면 빌드할 대상이 없다는 메시지가 나올 수 있다. 다음 Chapter에서 Package를 추가한 뒤 같은 명령을 다시 사용한다.

빌드 후 현재 터미널에 workspace 환경을 반영한다.

```bash
source install/setup.bash
```

zsh:

```bash
source install/setup.zsh
```

## 실행 방법

현재 workspace에 등록된 Package를 확인한다.

```bash
colcon list
```

ROS2 환경 상태를 확인한다.

```bash
ros2 doctor
```

빌드 결과 경로가 환경에 들어갔는지 확인한다.

```bash
printenv AMENT_PREFIX_PATH
```

## 예상 결과

- `colcon --help`가 정상 출력된다.
- Package가 추가된 뒤 `colcon list`에서 Package 목록이 보인다.
- `colcon build` 후 `build/`, `install/`, `log/` 디렉터리가 생성된다.
- `source install/setup.*` 후 현재 workspace의 Package를 `ros2 run` 또는 `ros2 launch`에서 찾을 수 있다.

## 정리

Workspace는 ROS2 Package를 모아 빌드하고 실행 환경으로 만드는 단위다. ROS2 설치 환경을 Underlay로 source 하고, 현재 저장소를 빌드한 결과를 Overlay로 source 해서 개발한다.

## 참고 자료

- [Development Environment](../../../docs/environment.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
