---
title: DOC 변환기
type: docs
weight: 10
url: /net/plugins/doc/
description: PdfDoc 플러그인을 사용하여 PDF를 Word로 변환하는 방법
lastmod: "2024-01-24"
---

이 기사는 [Aspose.Pdf DOC 변환기 for .NET](https://products.aspose.org/pdf/net/doc-converter/)을 사용하여 PDF 문서를 Microsoft Word 형식(.doc / .docx)으로 변환하는 방법을 안내합니다.

## 필수 조건

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* 일부 양식 필드가 포함된 샘플 PDF 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 Visual Studio의 NuGet 패키지 관리자를 사용하여 설치할 수 있습니다.

## 단계

### 1. 변환 설정하기 (FileDataSource 클래스의 스크린샷)

변환 과정은 세 가지 주요 단계를 포함합니다: 입력 및 출력 파일 정의, `PdfDoc` 객체 생성, 변환 옵션 지정.

#### 1.1. 데이터 소스 정의

* **입력 파일:** 우리는 `FileDataSource` 클래스를 사용하여 변환하려는 PDF 파일의 위치를 지정할 것입니다.
* **입력 파일:** `FileDataSource` 클래스를 사용하여 변환할 PDF 파일의 위치를 지정합니다.

```csharp
  FileDataSource inputDataSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

  * `"C:\Samples\sample.pdf"`를 실제 PDF 파일 경로로 교체하세요.

* **출력 파일:** 마찬가지로 다른 `FileDataSource` 객체를 사용하여 결과 Word 문서의 위치와 파일 이름을 정의합니다.

```csharp
  FileDataSource outputDataSource = new(Path.Combine(@"C:\Samples\", "sample.docx"));
```

* `"C:\Samples\sample.docx"`를 원하는 출력 경로와 파일 이름으로 교체하세요.

### 2. PdfDoc 플러그인 객체 생성 (PdfDoc 클래스의 스크린샷)

다음으로, 변환을 수행할 `PdfDoc` 클래스의 인스턴스를 생성합니다.

```csharp
  var plugin = new PdfDoc();
```

이 객체는 변환 프로세스의 엔진 역할을 합니다.

### 3. 변환 옵션 구성

`PdfToDocOptions` 클래스를 사용하여 변환 프로세스를 미세 조정할 수 있습니다.
`PdfToDocOptions` 클래스는 변환 프로세스를 미세 조정할 수 있습니다.

* **저장 형식:** 워드 문서의 원하는 출력 형식을 지정합니다. 이 경우, Microsoft Word 2007 이후와 호환되는 문서(.docx)를 생성하기 위해 `SaveFormat.DocX`를 사용합니다.

* **변환 모드:** 플러그인이 PDF 구조를 변환하는 동안 해석하는 방법을 정의합니다. 우리는 레이아웃과 포맷을 최적화하기 위해 `ConversionMode.EnhancedFlow`를 사용할 것입니다.

다음은 옵션을 구성하기 위한 코드 스니펫입니다:

```csharp
  PdfToDocOptions options = new()
  {
      SaveFormat = SaveFormat.DocX,
      ConversionMode = ConversionMode.EnhancedFlow
  };
```

**입력 및 출력 추가:**

마지막으로, 이전에 정의된 데이터 소스를 `AddInput` 및 `AddOutput` 메소드를 사용하여 변환 옵션과 연결합니다:

```csharp
  options.AddInput(inputDataSource);
  options.AddOutput(outputDataSource);
```

이렇게 하면 입력 PDF와 원하는 출력 워드 문서가 변환 프로세스에 연결됩니다.

### 4.
### 4.

모든 설정이 완료되었으므로, 구성된 옵션을 전달하면서 `PdfDoc` 플러그인의 `Process` 메소드를 호출하여 변환을 시작합시다:

```csharp
  var resultContainer = plugin.Process(options);
```

이 메소드는 변환을 실행하고 프로세스에 대한 세부 정보가 포함된 `ResultContainer` 객체를 반환합니다.

**결과 검색:**

기본 변환에 필수는 아니지만, `ResultContainer` 객체의 `ResultCollection` 속성을 통해 결과에 접근할 수 있습니다. 이는 디버깅이나 특정 변환 세부 정보 추적에 유용할 수 있습니다.

```csharp
  var result = resultContainer.ResultCollection[0];

  // 결과 출력 (시연 목적으로 선택적)
  Console.WriteLine(result);
```

이 마지막 단계로, PDF 문서가 지정된 Word 형식으로 변환되어 정의된 출력 위치에 저장됩니다.
