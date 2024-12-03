# 뉴스 요약 프로젝트

주어진 텍스트 파일의 내용을 Huggingface Transformers를 활용해 요약합니다.  
Python으로 구현된 간단하고 강력한 텍스트 요약 도구입니다.

---

## 주요 내용

### 수행 단계:
1. 입력 텍스트 파일을 불러옵니다.
2. Huggingface의 `pipeline`과 `facebook/bart-large-cnn` 모델을 사용합니다.
3. 지정된 길이 조건에 따라 간결한 요약문을 생성합니다.
4. 생성된 요약 결과를 터미널에 출력합니다.

---

### 가정:
1. 입력 텍스트는 `.txt` 형식의 일반 텍스트 파일입니다.
2. 사전 학습된 모델을 사용해 요약문을 생성합니다.
3. `facebook/bart-large-cnn` 모델은 뉴스와 같은 형식의 텍스트에 적합합니다.

---

## 요구사항:
**다음 버전에서 테스트되었습니다**:
- **Python**: 3.8+
- **Transformers**: 4.33.2
- **PyTorch**: 2.0.1

필수 패키지 설치 방법:
```bash
pip install -r requirements.txt
