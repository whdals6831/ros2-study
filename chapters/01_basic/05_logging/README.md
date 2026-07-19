# Logging

## 개요

이 Chapter는 ROS2 Node에서 로그를 출력하고, 실행 시 Log Level을 조정하는 방법을 다룬다.

Logging은 Node 상태, 데이터 흐름, 오류 원인을 확인하는 가장 기본적인 관찰 도구다. ROS2에서는 Node별 logger를 사용하며, CLI 옵션으로 출력 수준을 바꿀 수 있다.

## 학습 목표

- ROS2 Logging API의 역할을 설명할 수 있다.
- Node에서 `debug`, `info`, `warn`, `error` 로그를 출력할 수 있다.
- Log Level에 따라 출력되는 로그가 달라지는 것을 확인할 수 있다.
- `--ros-args --log-level`로 실행 시 로그 수준을 바꿀 수 있다.
- Logger 이름이 Node 이름과 어떻게 연결되는지 확인할 수 있다.

## 사전 요구사항

- [Node Chapter](../04_node/README.md)를 완료해야 한다.
- ROS2와 `colcon`이 동작해야 한다.

```bash
ros2 --help
colcon --help
```

## 핵심 개념

### Logger

Logger는 로그 메시지를 출력하는 객체다.

Python Node에서는 `self.get_logger()`로 현재 Node의 logger를 가져온다.

```python
self.get_logger().info('node started')
```

Logger 이름은 기본적으로 Node 이름을 따른다. Node 이름을 remap하면 로그에 보이는 이름도 함께 바뀐다.

### Log Level

Log Level은 메시지의 중요도를 나타낸다.

| Level | 용도 |
| --- | --- |
| `debug` | 상세한 내부 상태 확인 |
| `info` | 정상적인 상태 변화 |
| `warn` | 계속 실행은 가능하지만 주의가 필요한 상태 |
| `error` | 기능 실패나 복구가 필요한 상태 |
| `fatal` | 계속 실행하기 어려운 치명적 상태 |

기본 설정에서는 보통 `info` 이상이 출력된다. `debug` 로그는 Log Level을 낮춰야 보인다.

### Console Output

ROS2 로그는 터미널에 다음 정보와 함께 출력된다.

```text
[INFO] [logger_name]: message
```

출력 형식은 ROS2 배포판과 환경 변수에 따라 조금 달라질 수 있다.

### Logger 설정

실행 시 전체 Log Level을 바꾼다.

```bash
ros2 run py_logging_demo logging_node --ros-args --log-level debug
```

특정 logger만 설정할 수도 있다.

```bash
ros2 run py_logging_demo logging_node --ros-args --log-level logging_node:=debug
```

Node 이름을 바꾸면 logger 이름도 바뀐다.

```bash
ros2 run py_logging_demo logging_node --ros-args -r __node:=renamed_logger --log-level renamed_logger:=debug
```

## 패키지 구조

```text
05_logging/
├── README.md
└── packages/
    └── 01_logging_node/
        └── py_logging_demo/
```

예제 Package:

```text
py_logging_demo/
├── package.xml
├── setup.cfg
├── setup.py
├── resource/
│   └── py_logging_demo
└── py_logging_demo/
    ├── __init__.py
    └── logging_node.py
```

## 빌드 방법

저장소 루트에서 빌드한다.

```bash
colcon build --packages-select py_logging_demo
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

기본 Log Level로 실행한다.

```bash
ros2 run py_logging_demo logging_node
```

`debug` 로그까지 출력한다.

```bash
ros2 run py_logging_demo logging_node --ros-args --log-level debug
```

특정 logger만 `debug`로 설정한다.

```bash
ros2 run py_logging_demo logging_node --ros-args --log-level logging_node:=debug
```

Node 이름을 바꿔 실행한다.

```bash
ros2 run py_logging_demo logging_node --ros-args -r __node:=renamed_logger
```

## 예상 결과

- 기본 실행에서는 `info`, `warn`, `error` 로그가 출력된다.
- `--log-level debug`를 적용하면 `debug` 로그도 출력된다.
- Node 이름을 바꾸면 로그의 logger 이름도 변경된다.
- 터미널에서 로그 Level과 logger 이름을 구분할 수 있다.

## 정리

ROS2 Logging은 Node를 실행하면서 상태를 확인하는 기본 도구다. `get_logger()`로 로그를 출력하고, `--ros-args --log-level`로 실행 시 출력 범위를 조정한다.

## 참고 자료

- [Node Chapter](../04_node/README.md)
- [Repository Conventions](../../../docs/conventions.md)
- [Learning Roadmap](../../../docs/roadmap.md)
