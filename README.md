# News Summarization Project

## 프로젝트 개요
이 프로젝트는 Huggingface의 Transformers 라이브러리를 활용하여 뉴스 기사를 요약하는 기능을 제공합니다. `facebook/bart-large-cnn` 모델을 사용하여 긴 문장을 간결하고 핵심적인 내용으로 요약합니다.

## 데모 / 예시
### 원문 예시 (example1.txt)
Scientists have discovered a new species of frog in the Amazon rainforest...

### 요약 결과
New species of frog discovered in Amazon rainforest.

## 실행 화면
![요약 결과 데모](path/to/demo_image.png)

## 사용한 패키지 및 버전
- Python 3.8+
- Huggingface Transformers 4.33.2
- PyTorch 2.0.1

필수 패키지 설치:
```bash
pip install -r requirements.txt
