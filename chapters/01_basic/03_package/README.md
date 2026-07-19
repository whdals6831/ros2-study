# Package

## 개요

이 Chapter는 ROS2 Package의 기본 구조와 빌드 설정 파일을 다룬다.

ROS2 Package는 Node, Launch, 설정 파일, 메시지 정의처럼 하나의 기능 단위를 담는 빌드 가능한 묶음이다. C++ Package는 보통 `ament_cmake`, Python Package는 `ament_python`을 사용한다.

## 학습 목표

- ROS2 Package의 기본 파일 구조를 설명할 수 있다.
- `ros2 pkg create`로 C++ 또는 Python Package를 만들 수 있다.
- `package.xml`의 역할을 이해한다.
- C++ Package의 `CMakeLists.txt` 역할을 이해한다.
- Python Package의 `setup.py` 역할을 이해한다.
- `colcon build --packages-select`로 특정 Package만 빌드할 수 있다.

## 사전 요구사항

- [Workspace Chapter](../02_workspace/README.md)를 완료해야 한다.
- ROS2와 `colcon` 명령이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### ROS2 Package

Package는 ROS2에서 코드를 배포하고 빌드하는 기본 단위다.

Package 안에는 보통 다음 파일이 들어간다.

| 파일 | 역할 |
| --- | --- |
| `package.xml` | Package 이름, 버전, 의존성, 빌드 타입 |
| `CMakeLists.txt` | C++ Package 빌드 규칙 |
| `setup.py` | Python Package 설치 규칙 |
| `setup.cfg` | Python 실행 파일 설치 경로 |
| `resource/<package_name>` | `ament_python` Package marker |

### ament_cmake

`ament_cmake`는 C++ Package에서 주로 사용하는 빌드 타입이다.

생성 명령:

```bash
ros2 pkg create cpp_package_basic --build-type ament_cmake --dependencies rclcpp
```

기본 구조:

```text
cpp_package_basic/
├── CMakeLists.txt
├── include/
├── package.xml
└── src/
```

### ament_python

`ament_python`은 Python Package에서 사용하는 빌드 타입이다.

생성 명령:

```bash
ros2 pkg create py_package_basic --build-type ament_python --dependencies rclpy
```

기본 구조:

```text
py_package_basic/
├── package.xml
├── py_package_basic/
│   └── __init__.py
├── resource/
│   └── py_package_basic
├── setup.cfg
├── setup.py
└── test/
```

### package.xml

`package.xml`은 Package metadata와 의존성을 정의한다.

자주 보는 항목:

```xml
<name>cpp_package_basic</name>
<version>0.0.0</version>
<description>TODO: Package description</description>
<maintainer email="user@example.com">user</maintainer>
<license>TODO: License declaration</license>
<depend>rclcpp</depend>
<buildtool_depend>ament_cmake</buildtool_depend>
```

Package를 추가한 뒤에는 `description`, `maintainer`, `license`, `depend`를 실제 값에 맞게 정리한다.

### CMakeLists.txt

`CMakeLists.txt`는 C++ 소스 빌드와 설치 규칙을 정의한다.

기본 흐름:

```cmake
cmake_minimum_required(VERSION 3.8)
project(cpp_package_basic)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

ament_package()
```

실행 파일을 추가하는 Chapter부터 `add_executable`, `ament_target_dependencies`, `install`을 사용한다.

### setup.py

`setup.py`는 Python Package 설치와 실행 entry point를 정의한다.

기본 흐름:

```python
from setuptools import setup

package_name = 'py_package_basic'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [],
    },
)
```

Python Node를 실행 파일로 등록하는 Chapter부터 `console_scripts`를 사용한다.

## 패키지 구조

이 Chapter에서는 생성 명령과 구조만 확인한다. 예제 Package를 남기지 않으려면 실습 후 삭제해도 된다.

권장 실습 위치:

```text
03_package/
└── packages/
    └── 01_basic/
        ├── cpp_package_basic/
        └── py_package_basic/
```

## 빌드 방법

저장소 루트에서 실습 디렉터리를 만든다.

```bash
mkdir -p chapters/01_basic/03_package/packages/01_basic
cd chapters/01_basic/03_package/packages/01_basic
```

C++ Package와 Python Package를 생성한다.

```bash
ros2 pkg create cpp_package_basic --build-type ament_cmake --dependencies rclcpp
ros2 pkg create py_package_basic --build-type ament_python --dependencies rclpy
```

저장소 루트로 돌아가 빌드한다.

```bash
cd ../../../../../
colcon build --packages-select cpp_package_basic py_package_basic
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

이 Chapter에서 만든 Package는 아직 Node 실행 파일이 없다. Package가 workspace에 인식되는지만 확인한다.

```bash
colcon list | grep package_basic
ros2 pkg list | grep package_basic
```

Package 정보를 확인한다.

```bash
ros2 pkg prefix cpp_package_basic
ros2 pkg prefix py_package_basic
```

## 예상 결과

- `colcon list`에서 `cpp_package_basic`, `py_package_basic`이 보인다.
- `colcon build --packages-select ...`가 성공한다.
- `source install/setup.*` 후 `ros2 pkg prefix`가 각 Package의 install 경로를 출력한다.
- 아직 Node를 만들지 않았으므로 `ros2 run`으로 실행할 대상은 없다.

## 정리

ROS2 Package는 `package.xml`로 metadata와 의존성을 선언하고, 빌드 타입에 따라 `CMakeLists.txt` 또는 `setup.py`로 빌드와 설치 규칙을 정의한다. 다음 Chapter에서는 Package 안에 실제 Node를 추가한다.

## 참고 자료

- [Development Environment](../../../docs/environment.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
