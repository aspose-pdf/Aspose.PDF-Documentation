---
title: Splitter
type: docs
weight: 120
url: /ko/net/plugins/splitter/
description: PDF 문서를 개별 페이지로 분할
lastmod: "2024-01-24"
draft: false
---

큰 PDF 문서를 더 작고 관리하기 쉬운 파일로 나누고 싶으신가요? [Aspose.PDF Splitter for .NET](https://products.aspose.org/pdf/net/splitter/)를 사용하면 이 작업을 쉽게 수행할 수 있습니다. 이 글에서는 Aspose.PDF 플러그인을 사용하여 PDF 문서를 여러 파일로 분할하는 과정을 탐색해 보겠습니다. 코드를 살펴보고 단계를 따라가 보겠습니다.

## 사전 요구 사항

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* 샘플 PDF 파일

또한, `SplitOptions` 클래스와 그 속성에 익숙해지세요. 이 클래스에 대한 자세한 정보는 [API 참조](https://reference.aspose.com/pdf/net/aspose.pdf/SplitOptions/)에서 찾을 수 있습니다. 각 출력 `FileDataSource`는 분할 PDF 파일의 단일 페이지를 나타냅니다.

이제 제공된 코드를 살펴보고 PDF 문서를 분할하는 방법을 이해해 보겠습니다.
이제 제공된 코드를 탐색하고 PDF 문서를 분할하는 방법을 이해해 보겠습니다.

## 코드 분석

아래 코드는 Aspose.PDF.Plugins를 사용한 PDF 분할 데모를 보여줍니다:

```csharp
using Aspose.Pdf.Plugins;
// ...........

// 분할할 PDF 문서의 입력 경로를 설정합니다.
using var inputStream = File.OpenRead(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Splitter의 새 인스턴스를 생성합니다.
var splitter = new Splitter();

// 문서를 분할하기 위한 옵션을 생성합니다.
var options = new SplitOptions();

// 옵션에 입력 및 출력 데이터 소스를 추가합니다.
options.AddInput(new StreamDataSource(inputStream));

var document = new Aspose.Pdf.Document(inputStream);

for (int i = 1; i <= document.Pages.Count; i++)
{
   var pageNum = string.Format("{0,3}", i.ToString("D3"));
   options.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", $"splitter_{pageNum}.pdf")));
}

// 옵션을 처리하여 문서를 분할합니다.
var result = splitter.Process(options);
Console.WriteLine(result);
```

핵심 단계를 분해해 보겠습니다:
1. **입력 PDF 설정**

   코드는 분할할 입력 PDF 문서의 경로를 지정하는 것으로 시작됩니다. 이는 `File.OpenRead` 메서드를 사용하여 수행됩니다.

2. **객체 생성 (분할기 및 분할 옵션)**

   코드는 분할 프로세스를 처리하기 위해 `Splitter` 클래스의 인스턴스를 생성합니다. 추가로, 분할 작업을 구성하기 위해 `SplitOptions` 클래스의 인스턴스도 생성됩니다.

3. **데이터 소스 추가 (입력 및 출력)**

   입력 PDF 문서는 `SplitOptions`에 입력 데이터 소스로 `AddInput` 메서드를 사용하여 추가됩니다. 문서의 각 페이지에 대해, 출력 파일 경로는 출력 데이터 소스로 `AddOutput` 메서드를 사용하여 추가됩니다.

4. **프로세스 메서드 실행**

   `Splitter` 클래스에서 구성된 `SplitOptions`를 전달하여 분할 프로세스가 `Process` 메서드 호출로 시작됩니다. 작업의 결과는 `result` 변수에 저장됩니다.

5. **결과 처리**

   코드는 콘솔에 결과를 출력하여 분할 프로세스에 대한 정보를 제공합니다.
코드는 콘솔에 결과를 출력하여 분할 과정에 대한 정보를 제공합니다.
