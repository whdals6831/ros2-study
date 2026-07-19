# Repository Conventions

이 문서는 새 Chapter와 ROS2 Package를 추가할 때 지킬 규칙만 다룬다.

## Directory Roles

`docs/`는 저장소 전체에 공통으로 적용되는 내용을 관리한다.

```text
docs/
├── architecture.md
├── roadmap.md
├── environment.md
└── conventions.md
```

`scripts/`는 반복적으로 사용하는 개발 명령을 관리한다.

| Script | Description |
| --- | --- |
| `build.sh` | ROS2 Package 빌드 |
| `clean.sh` | 빌드 결과 및 캐시 제거 |
| `format.sh` | 소스 코드 포맷 적용 |
| `lint.sh` | 코드 및 Package 검사 |

## Phase Structure

각 Phase는 서로 관련된 ROS2 기능을 하나의 학습 단위로 묶는다.

```text
04_optimization/
├── README.md
├── 17_component/
├── 18_composable_node/
├── 19_intra_process/
├── 20_executor/
├── 21_callback_group/
└── 22_lifecycle_node/
```

각 Phase의 `README.md`에는 다음 내용을 작성한다.

- Phase 학습 목표
- 포함된 Chapter
- 권장 학습 순서
- 이전 Phase와의 연관성
- Phase를 통해 학습할 수 있는 내용

## Chapter Structure

각 Chapter는 다음 구조를 기본으로 사용한다.

```text
13_tf2/
├── README.md
├── images/        # README에서 이미지 파일을 사용할 때만 생성
└── packages/
    ├── 01_static_transform/
    ├── 02_dynamic_transform/
    ├── 03_transform_listener/
    ├── 04_multi_frame/
    └── 05_robot_tf_tree/
```

- `README.md`: 해당 Chapter의 개념과 Package 실행 방법
- `images/`: README에서 구조도, 실행 결과, RViz2 화면 같은 이미지 파일을 실제로 사용할 때만 생성
- `packages/`: 해당 Chapter에서 구현하는 ROS2 Package

Package 예제가 여러 개라면 학습 순서를 나타내는 번호가 포함된 디렉터리로 구분한다.

## Package Example Structure

하나의 Chapter 안에 여러 예제가 있는 경우 다음과 같이 구성한다.

```text
13_tf2/
├── README.md
├── images/        # README에서 이미지 파일을 사용할 때만 생성
└── packages/
    ├── 01_static_transform/
    │   ├── cpp_tf2_static/
    │   └── py_tf2_static/
    ├── 02_dynamic_transform/
    │   ├── cpp_tf2_dynamic/
    │   └── py_tf2_dynamic/
    ├── 03_transform_listener/
    │   ├── cpp_tf2_listener/
    │   └── py_tf2_listener/
    ├── 04_multi_frame/
    │   └── cpp_tf2_multi_frame/
    └── 05_robot_tf_tree/
        └── cpp_robot_tf_tree/
```

예제 디렉터리 이름은 학습 순서와 예제 실행 순서를 나타낸다.

```text
packages/
├── 01_minimal/
├── 02_basic/
├── 03_intermediate/
├── 04_advanced/
└── 05_best_practice/
```

## Naming

Phase 디렉터리:

```text
<order>_<phase_name>
```

예:

```text
01_basic
02_communication
03_robot
04_optimization
05_advanced
06_applications
```

Chapter 디렉터리:

```text
<order>_<topic_name>
```

예:

```text
01_ros2_overview
02_workspace
03_package
18_composable_node
29_moveit2
```

Example 디렉터리:

```text
<order>_<example_name>
```

예:

```text
01_minimal_publisher
02_minimal_subscriber
03_pub_sub
04_custom_message
05_qos
```

C++ Package:

```text
cpp_<feature>_<role>
```

예:

```text
cpp_topic_publisher
cpp_service_server
cpp_tf2_listener
```

Python Package:

```text
py_<feature>_<role>
```

예:

```text
py_topic_publisher
py_service_server
py_tf2_listener
```

이름은 소문자와 underscore만 사용한다.

## Chapter README

Chapter README는 필요한 항목만 포함한다.

기본 순서:

1. 개요
2. 학습 목표
3. 사전 요구사항
4. 핵심 개념
5. 패키지 구조
6. 빌드 방법
7. 실행 방법
8. 예상 결과
9. 정리
10. 참고 자료

실행 예제가 없는 순수 개념 Chapter가 아니라면 빌드와 실행 방법은 반드시 적는다.

## Package Rules

- 각 ROS2 Package는 독립적으로 빌드 가능해야 한다.
- Package 이름은 저장소 안에서 중복하지 않는다.
- 의존성은 `package.xml`에 명시한다.
- 예제 Package에는 copyright linter(`ament_copyright`, `test_copyright.py`)를 적용하지 않는다.
- C++ 실행 파일과 라이브러리는 `CMakeLists.txt`에서 install한다.
- Python entry point는 `setup.py`에 명시한다.
- Launch, config, rviz, urdf 파일은 패키지 install 대상에 포함한다.

## C++ Style

C++ Package는 다음 구조를 기본으로 사용한다.

```text
cpp_tf2_static/
├── package.xml
├── CMakeLists.txt
├── include/
│   └── cpp_tf2_static/
├── src/
│   └── static_transform_broadcaster.cpp
├── launch/
│   └── static_transform.launch.py
├── config/
└── rviz/
```

Package 특성에 따라 필요하지 않은 디렉터리는 생략할 수 있다.

- Node 구현은 `src/`에 둔다.
- 공개 header가 필요할 때만 `include/<package_name>/`를 만든다.
- 실행 파일 이름은 기능을 드러내는 snake_case를 사용한다.
- ROS2 API는 `rclcpp` 기본 패턴을 따른다.

## Python Style

Python Package는 다음 구조를 기본으로 사용한다.

```text
py_tf2_static/
├── package.xml
├── setup.py
├── setup.cfg
├── resource/
│   └── py_tf2_static
├── py_tf2_static/
│   ├── __init__.py
│   └── static_transform_broadcaster.py
├── launch/
│   └── static_transform.launch.py
├── config/
└── rviz/
```

Package 특성에 따라 필요하지 않은 디렉터리는 생략할 수 있다.

- Python module 디렉터리는 package 이름과 같게 둔다.
- 실행 가능한 Node는 `console_scripts` entry point로 노출한다.
- `setup.cfg`로 script 설치 경로를 맞춘다.
- ROS2 API는 `rclpy` 기본 패턴을 따른다.

## Launch Files

- Launch 파일은 `launch/`에 둔다.
- 파일명은 `<purpose>.launch.py` 형식을 사용한다.
- Node가 2개 이상이거나 parameter, namespace, remapping이 필요하면 launch 파일을 추가한다.

## Config Files

- Parameter YAML은 `config/`에 둔다.
- RViz2 설정은 `rviz/`에 둔다.
- URDF/Xacro는 `urdf/`에 둔다.

## Documentation

- README에는 실행 가능한 명령을 넣는다.
- 개념 설명은 예제 코드와 연결해서 쓴다.
- 스크린샷이나 구조도는 해당 Chapter의 `images/`에 둔다.
- README의 전체 커리큘럼을 Chapter 문서에 반복하지 않는다.

## Commit Hygiene

커밋 전 확인:

```bash
git status --porcelain
```

빌드 산출물과 rosbag 파일은 커밋하지 않는다.
