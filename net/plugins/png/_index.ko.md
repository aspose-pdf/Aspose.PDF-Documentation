---
title: PNG 변환기
type: docs
weight: 110
url: /net/plugins/png/
description: Aspose.PDF PNG 플러그인으로 PDF를 PNG 이미지로 변환
lastmod: "2024-01-24"
---

.NET을 사용하여 [PDF 문서를 PNG 이미지로 변환](https://products.aspose.org/pdf/net/png-converter/)하려는 경우, Aspose.PDF for .NET은 견고한 해결책을 제공합니다. 이 글에서는 Aspose.PDF 라이브러리를 사용하여 객체를 생성하고 데이터 소스를 추가하며 프로세스 메서드를 실행하는 필수 단계를 설명합니다.

## 필수 조건

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* 샘플 PDF 파일

## 코드 개요

아래 코드는 Aspose.PDF PNG 플러그인을 사용한 PNG 변환 데모를 보여줍니다:

```csharp
using Aspose.Pdf.Plugins;

//....

// PngOptions 클래스의 새 인스턴스를 생성합니다.
var convertorOptions = new PngOptions();

// PngOptions에 입력 및 출력 경로를 추가합니다.
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// 출력 해상도를 300 DPI로 설정합니다.
convertorOptions.OutputResolution = 300;

// Png 클래스의 새 인스턴스를 생성합니다.
Png converter = new ();

// PNG 변환을 처리하고 결과 컨테이너를 가져옵니다.
ResultContainer resultContainer = converter.Process(convertorOptions);

// 결과를 콘솔에 출력합니다.
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```
핵심 단계를 분석해 봅시다:

1. **객체 생성 (PngOptions 및 Png)**

   코드는 PNG 변환을 설정하기 위해 `PngOptions` 클래스의 인스턴스를 생성합니다. 추가적으로, 처리를 위해 `Png` 클래스의 인스턴스도 생성됩니다.

2. **데이터 소스 추가**

   입력 PDF 파일 경로를 `PngOptions`에 `AddInput` 메서드를 사용하여 추가합니다. 마찬가지로, PNG 이미지의 출력 경로는 `AddOutput` 메서드를 사용하여 추가됩니다.

3. **출력 해상도 설정**

   코드는 `PngOptions` 클래스의 `OutputResolution` 속성을 사용하여 출력 해상도를 300 DPI로 설정합니다.

4. **프로세스 메서드 실행**

   `Png` 클래스에서 `Process` 메서드를 호출하여 구성된 `PngOptions`를 전달함으로써 PNG 변환을 시작합니다. 결과는 `resultContainer`에 저장됩니다.

5. **결과 처리**

   코드는 콘솔에 결과를 출력하여 변환된 파일 경로를 보여줍니다.
