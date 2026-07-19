# Communication

## 개요

이 Phase는 ROS2의 기본 통신 방식인 Topic, Service, Action을 다룬다.

Phase 1에서 Node를 만들고 실행하는 흐름을 익혔다면, Phase 2에서는 Node가 서로 데이터를 주고받는 방법을 학습한다. Topic은 지속적인 데이터 흐름, Service는 짧은 요청과 응답, Action은 오래 걸리는 작업의 진행 상태와 결과를 표현할 때 사용한다.

## 학습 목표

- Topic, Service, Action의 사용 시점을 구분할 수 있다.
- Publisher와 Subscriber로 데이터를 주고받을 수 있다.
- 표준 Message와 Custom Message를 사용할 수 있다.
- QoS 설정이 통신 결과에 주는 영향을 확인할 수 있다.

## 포함된 Chapter

1. [Topic](01_topic/README.md)
2. Message
3. Topic Advanced
4. Service
5. Action
6. QoS

## 이전 Phase와의 연관성

Phase 1의 Node, Parameter, Launch, Development Checks를 기반으로 한다. 특히 Topic 실습에서는 여러 터미널에서 Node를 실행하고 `ros2 topic` CLI로 통신 상태를 확인한다.

## 정리

ROS2 시스템은 여러 Node가 graph 위에서 통신하며 동작한다. 이 Phase를 마치면 데이터 흐름의 성격에 따라 Topic, Service, Action 중 적절한 방식을 선택할 수 있다.
