# Development Environment

이 문서는 저장소 실습에 필요한 ROS2 개발 환경 기준을 정리한다.

## Target Environment

기본 기준은 Ubuntu LTS와 ROS2 LTS 배포판이다.

- OS: Ubuntu 22.04 또는 24.04
- ROS2: Humble, Iron, Jazzy 중 사용 환경에 맞는 배포판
- Shell: bash 또는 zsh
- Build tool: `colcon`

Chapter에서 특정 배포판 기능이 필요하면 해당 Chapter README에 별도로 적는다.

## Required Tools

```bash
sudo apt update
sudo apt install -y build-essential git python3-colcon-common-extensions
```

ROS2 설치는 공식 문서를 따른다. 설치 후 새 터미널에서 아래 명령이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## Workspace Setup

저장소 루트가 ROS2 workspace 역할을 한다.

```bash
cd ros2-study
colcon build
source install/setup.bash
```

zsh를 쓰면 다음을 사용한다.

```bash
source install/setup.zsh
```

## Package Creation

패키지는 각 Chapter의 `packages/<example>/` 아래에서 생성한다.

C++ 패키지:

```bash
ros2 pkg create cpp_<feature>_<role> --build-type ament_cmake --dependencies rclcpp
```

Python 패키지:

```bash
ros2 pkg create py_<feature>_<role> --build-type ament_python --dependencies rclpy
```

예:

```bash
mkdir -p chapters/01_basic/04_node/packages/01_minimal
cd chapters/01_basic/04_node/packages/01_minimal
ros2 pkg create cpp_node_minimal --build-type ament_cmake --dependencies rclcpp
ros2 pkg create py_node_minimal --build-type ament_python --dependencies rclpy
```

패키지 이름과 디렉터리 규칙은 [conventions.md](conventions.md)를 따른다.

## Common Commands

전체 빌드:

```bash
colcon build
```

특정 패키지만 빌드:

```bash
colcon build --packages-select <package_name>
```

테스트:

```bash
colcon test
colcon test-result --verbose
```

환경 적용:

```bash
source install/setup.bash
```

## Clean Build

빌드 결과를 지우고 다시 빌드할 때만 사용한다.

```bash
rm -rf build install log
colcon build
```

## Environment Checks

문제가 생기면 먼저 아래를 확인한다.

```bash
which ros2
ros2 doctor
printenv ROS_DISTRO
printenv ROS_DOMAIN_ID
printenv RMW_IMPLEMENTATION
printenv AMENT_PREFIX_PATH
```

`source install/setup.*`를 하지 않으면 방금 빌드한 패키지를 `ros2 run` 또는 `ros2 launch`에서 찾지 못한다.

`ros2 node list`, `ros2 topic list` 같은 graph 명령이 비어 있는데 `--no-daemon`을 붙이면 출력된다면 ROS2 CLI daemon 상태가 오래되었을 수 있다.

```bash
ros2 daemon stop
ros2 daemon start
ros2 node list
```

계속 다르게 보이면 Node를 실행한 터미널과 CLI를 실행한 터미널의 `ROS_DOMAIN_ID`, `RMW_IMPLEMENTATION`, workspace source 상태가 같은지 확인한다.

## Git Ignore Policy

다음 파일과 디렉터리는 커밋하지 않는다.

- `build/`
- `install/`
- `log/`
- `.colcon/`
- `__pycache__/`
- `.pytest_cache/`
- rosbag output
