# twinkle-storage
트윙클 한국어 번역 저장소

# 스토리 번역만 이용하는 방법
- `BepInEx\plugins\TwinkleTranslator` 폴더 제거

<br><br><br>

# AI 번역 설정 방법
## 공통 설정
- `BatchMaxTexts` : 1회 요청당 배치 갯수
- `BatchWindowSeconds` : 배치 모으는 시간(시간이 길 수록 API 요청수 Down)

## 번역 이용시 OpenAI(또는 호환) API 설정 방법
1. `BepInEx\config\Twinkle.Translator.Fallback.cfg` 열기
2. `OpenAiApiKey`에 API 키 입력하기(API키 불필요시 아무 글자나 입력)
3. `OpenAiModel`에 모델 이름 입력하기
4. (호환 또는 로컬 API 이용시)`OpenAiBaseUrl`에 API URL 입력하기
5. `OpenAiReasoningEffort` 설정하기(로컬API 사용시 대부분 공백)
6. `FallbackProvider`를 OpenAI로 설정하기

## 번역 이용시 Gemini API 설정 방법
1. `BepInEx\config\Twinkle.Translator.Fallback.cfg` 열기
2. `GeminiApiKey`에 API 키 입력하기
3. `GeminiModel`에 모델 이름 입력하기
5. `GeminiThinkingLevel` 모델에 따라 설정하기(3.7-flash 3.1-pro는 LOW, 그 외 모델 minimal 권장)
6. `FallbackProvider`를 Gemini로 설정하기