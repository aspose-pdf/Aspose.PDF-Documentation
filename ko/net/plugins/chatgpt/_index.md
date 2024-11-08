---
title: ChatGPT
type: docs
weight: 30
url: /ko/net/plugins/chatGPT/
description: AI-파워드 ChatGPT 응답을 생성하고 PDF에 저장하는 방법
lastmod: "2024-02-24"
---

## ChatGpt 플러그인을 사용한 AI-파워드 채팅 응답 생성

PDF 문서를 AI 생성 채팅 응답으로 향상시키고 싶으셨나요? 더 이상 찾지 마세요! 이 가이드에서는 C# 애플리케이션에 강력한 [ChatGpt 플러그인](https://products.aspose.org/pdf/net/chat-gpt/)을 통합하는 과정을 안내합니다. 몇 가지 간단한 단계만으로 매력적인 채팅 응답을 쉽게 생성할 수 있습니다.

## 필수 조건

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* 샘플 PDF 파일

## 단계

### 1. 객체 생성

채팅 생성 작업을 위한 객체를 만드는 것부터 시작합시다. 제공된 C# 코드 스니펫은 PdfChatGpt 플러그인을 위한 옵션 설정 방법을 보여줍니다.

```csharp
// ChatGPT 플러그인을 위한 옵션 생성.
var options = new PdfChatGptRequestOptions();
```
### 2. 데이터 소스 추가하기

다음으로, 데이터 소스를 추가해야 하는데, 이 경우에는 AI 생성 채팅 응답으로 향상시키고 싶은 텍스트가 포함된 입력 PDF 파일입니다.

```csharp
// 입력 PDF 파일을 옵션에 추가합니다.
options.AddInput(new FileDataSource("c:\\Samples\\sample.pdf"));

// 출력 PDF 파일을 옵션에 추가합니다.
options.AddOutput(new FileDataSource("c:\\Samples\\chat_results.pdf"));
```

위 코드 조각에서는 입력 PDF 파일 경로와 향상된 채팅 응답이 저장될 출력 경로를 지정하고 있습니다.

### 3. 프로세스 메소드 실행하기

이제 모든 것을 실행에 옮기기 위해 프로세스 메소드를 실행합시다. 이곳에서 마법과 같은 일이 일어나게 됩니다 – AI 기반의 ChatGPT 모델이 제공된 쿼리와 텍스트를 바탕으로 채팅 응답을 생성합니다.

```csharp
// 인증을 위한 API 키를 설정합니다.
options.ApiKey = "sk-******";

// ChatGPT 모델의 최대 토큰 수를 설정합니다.
options.MaxTokens = 1000;

// ChatGPT 모델의 쿼리를 설정합니다.
options.Query = "What are the best keywords for this text?";

// PdfChatGpt 플러그인의 인스턴스를 생성합니다.
var plugin = new PdfChatGpt();

// ChatGPT 플러그인을 사용하여 PDF 문서를 처리합니다.
var result = await plugin.ProcessAsync(options);
```
이 코드 라인들을 통해 인증을 설정하고, ChatGPT 모델의 매개변수를 설정하며, 채팅 생성 프로세스를 시작합니다.
