---
title: 텍스트 추출기
type: docs
weight: 140
url: ko/net/plugins/textextractor/
description: PDF 문서에서 텍스트 내용을 추출합니다.
lastmod: "2024-01-24"
---

PDF 문서에서 [프로그래밍 방식으로 텍스트를 추출](https://products.aspose.org/pdf/net/text-extractor/)하려고 하나요? Aspose.PDF for .NET을 사용하면 TextExtractor 클래스를 사용하여 이 작업을 쉽게 수행할 수 있습니다. 이 글에서는 .NET에서 텍스트 추출 애플리케이션을 만드는 기본 단계를 살펴보겠습니다. TextExtractor 객체 생성, 데이터 소스 추가, 텍스트 추출 프로세스 실행을 다룹니다.

## 필수 조건

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* 샘플 PDF 파일

또한, `TextExtractorOptions` 클래스와 그 기능에 익숙해지세요. 자세한 정보는 [Aspose.PDF API 참조](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/)에서 찾을 수 있습니다.

이제 코드를 살펴보고 PDF 문서에서 텍스트를 추출하는 방법을 탐색해 보겠습니다.
이제 코드를 살펴보고 PDF 문서에서 텍스트를 추출하는 방법을 탐구해 보겠습니다.

## 코드 분석

다음 코드는 텍스트 추출 기능을 보여줍니다. 핵심 단계를 살펴보겠습니다:

### 1. TextExtractor 객체 생성

코드는 `TextExtractor` 클래스의 새 인스턴스를 생성하여 시작합니다. 이 클래스는 PDF 문서에서 텍스트를 추출하는 메서드를 제공합니다.

```csharp
using TextExtractor extractor = new();
```

### 2. 데이터 소스 추가

다음으로, 입력 PDF 파일을 위한 `FileDataSource`가 생성됩니다. 이 파일에서 텍스트가 추출될 것입니다.

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. TextExtractorOptions 생성

텍스트 추출 과정을 구성하기 위해 `TextExtractorOptions` 객체가 생성됩니다. 입력 파일 소스가 옵션에 추가됩니다.

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. 텍스트 추출 과정 실행

구성된 옵션을 전달하면서 `TextExtractor` 객체에 `Process` 메서드가 호출됩니다.
`Process` 메소드는 `TextExtractor` 객체에 설정된 옵션을 전달하면서 호출됩니다.

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

전체 코드는 아래와 같습니다:

``````cs
using Aspose.Pdf.Plugins;
// ...

// TextExtractor의 새 인스턴스를 생성합니다.
using TextExtractor extractor = new();

// 입력 PDF 파일을 위한 FileDataSource를 생성합니다.
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

// TextExtractorOptions를 생성합니다.
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);

// 텍스트 추출을 처리합니다.
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;

// 추출된 텍스트를 출력합니다.
Console.WriteLine(results[0]);

```

