---
title: 이미지 추출기
type: docs
weight: 80
url: ko/net/plugins/imageextractor/
description: ImageExtractor 플러그인으로 PDF에서 이미지 추출하기
lastmod: "2024-01-24"
draft: false
---

.NET을 사용하여 PDF 파일에서 이미지를 추출해야 하는 경우, Aspose.PDF for .NET은 강력하고 간단한 솔루션을 제공합니다. 이 가이드에서는 객체를 생성하고 데이터 소스를 추가하며 프로세스 메소드를 실행하는 기본 단계를 안내합니다. [Aspose.PDF 이미지 추출기](https://products.aspose.org/pdf/net/image-extractor/).

## 필수 조건

다음이 필요합니다:

* 비주얼 스튜디오 2019 이상
* Aspose.PDF for .NET 21.1 이상
* 샘플 PDF 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 비주얼 스튜디오의 NuGet 패키지 관리자를 사용하여 설치할 수 있습니다.
이제 코드로 들어가서 ImageExtractor 플러그인 사용 방법을 알아봅시다.

## 단계

제공된 코드는 PDF 파일에서 이미지를 추출하기 위해 `ImageExtractor` 플러그인의 사용 방법을 보여줍니다.
제공된 코드는 PDF 파일에서 이미지를 추출하기 위해 `ImageExtractor` 플러그인의 사용 방법을 보여줍니다.

### 1. 객체 생성 (ImageExtractor)

첫 번째 단계는 `ImageExtractor` 플러그인의 인스턴스를 생성하는 것입니다. 다음 코드를 사용하여 이를 달성합니다:

```csharp
using var plugin = new ImageExtractor();
```

여기서 `using` 문은 작업이 완료될 때 리소스가 적절하게 해제되도록 보장합니다.

### 2. 데이터 소스 추가

다음으로, 이미지 추출 과정을 구성하기 위해 `ImageExtractorOptions` 클래스의 인스턴스를 생성합니다. `AddInput` 메서드를 사용하여 옵션에 입력 파일 경로를 추가합니다:

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

`"C:\Samples\"` 및 `"sample.pdf"`를 귀하의 PDF 파일의 적절한 경로 및 파일 이름으로 교체하십시오.

### 3. 프로세스 메서드 실행

마지막 단계는 플러그인과 옵션을 사용하여 이미지 추출을 처리하는 것입니다:

```csharp
plugin.Process(imageExtractorOptions);
```

이 코드는 지정된 PDF 파일에서 이미지를 추출하고 관련 정보를 처리합니다.
```csharp
var resultContainer = plugin.Process(imageExtractorOptions);
```

결과는 `resultContainer`에 저장되며, 추출된 이미지를 포함합니다.

### 4. 추출된 이미지 처리하기

프로세스 실행 후, 결과 컨테이너에서 추출된 이미지를 검색할 수 있습니다. 아래 코드는 첫 번째 추출된 이미지를 임시 위치에 저장하는 방법을 보여줍니다:

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

목적지 경로 및 파일 이름을 선호에 따라 맞춤 설정하세요.

아래 전체 예제를 복사할 수 있습니다:

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // PDF 파일에서 이미지를 추출하기 위한 ImageExtractor 플러그인 사용법을 보여줍니다.
    // </summary>
    internal static void Run()
    {
        // ImageExtractor 플러그인의 인스턴스를 생성합니다.
        using var plugin = new ImageExtractor();

        // ImageExtractorOptions 클래스의 인스턴스를 생성합니다.
        var imageExtractorOptions = new ImageExtractorOptions();

        // 옵션에 입력 파일 경로를 추가합니다.
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // 플러그인과 옵션을 사용하여 이미지 추출을 처리합니다.
        var resultContainer = plugin.Process(imageExtractorOptions);

        // 결과 컨테이너에서 추출된 이미지를 가져옵니다.
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```

