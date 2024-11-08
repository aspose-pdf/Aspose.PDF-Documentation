---
title: ToC Generator
type: docs
weight: 150
url: /ko/net/plugins/tocgenerator/
description: Aspose.PDF ToC Generator를 사용하여 목차 생성
lastmod: "2024-01-24"
draft: false
---

PDF 문서에 동적으로 [목차(ToC)를 추가](https://products.aspose.org/pdf/net/toc-generator/)하고 싶으신가요? Aspose.PDF for .NET은 간편하게 TOC를 생성할 수 있는 강력한 `TocGenerator` 클래스를 제공합니다. 이 가이드에서는 Aspose.PDF를 사용하여 PDF 문서에 TOC를 생성하는 기본 단계를 소개하겠습니다. `TocGenerator` 객체 생성, 입력/출력 경로 추가 및 TOC 생성 프로세스 실행을 다루게 됩니다.

## Prerequisites

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* 샘플 PDF 파일

또한, `TocOptions` 클래스와 그 기능에 대해 익숙해지세요. 자세한 정보는 [Aspose.PDF API Reference](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/)에서 확인할 수 있습니다.

이제 코드를 살펴보고 PDF 문서에 목차를 생성하는 방법을 탐구해 보겠습니다.
이제 코드로 들어가서 PDF 문서의 목차를 생성하는 방법을 탐구해 보겠습니다.

## 코드 설명

`TocGeneratorDemo` 클래스와 `Run` 메소드를 사용하여 목차 생성 방법을 시연할 것입니다. 주요 단계를 살펴보겠습니다:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // TOC 생성 데모를 실행합니다.
        internal static void Run()
        {
            // TocGenerator 클래스의 새 인스턴스를 생성합니다.
            TocGenerator generator = new();

            // TocOptions 클래스의 새 인스턴스를 생성합니다.
            TocOptions options = new();
            // TocOptions에 입력 및 출력 경로를 추가합니다.
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // TOC 생성을 처리하고 결과 컨테이너를 가져옵니다.
            var resultContainer = generator.Process(options);

            // 결과 컨테이너에서 결과를 가져옵니다.
            var result = resultContainer.ResultCollection[0];

            // 결과를 콘솔에 출력합니다.
            Console.WriteLine(result);
        }
    }
}
```
### 1. TocGenerator 객체 생성

코드는 `TocGenerator` 클래스의 새 인스턴스를 생성하여 시작합니다. 이 클래스는 PDF 문서에 대한 목차(TOC)를 생성하는 메서드를 제공합니다.

```csharp
TocGenerator generator = new();
```

### 2. TocOptions 생성

다음으로, TOC 생성 프로세스를 구성하기 위해 `TocOptions` 클래스의 새 인스턴스가 생성됩니다. 입력 및 출력 파일 경로가 옵션에 추가됩니다.

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. TOC 생성 프로세스 실행

구성된 옵션을 전달하면서 `TocGenerator` 객체에 `Process` 메서드가 호출됩니다. 결과 컨테이너는 생성된 TOC를 보유하고 있으며, 콘솔에 출력됩니다.

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```
