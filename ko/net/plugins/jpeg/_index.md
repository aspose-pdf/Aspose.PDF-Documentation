---
title: JPEG 변환기
type: docs
weight: 90
url: ko/net/plugins/jpeg/
description: Aspose.PDF JPEG 변환기를 사용하여 PDF 페이지를 JPEG 이미지로 변환하는 방법
lastmod: "2024-01-24"
draft: false
---

이 글에서는 [JPEG 변환기](https://products.aspose.org/pdf/net/jpeg-converter/)를 사용하여 PDF 페이지를 JPEG 이미지로 변환하고 별도의 파일로 저장하는 방법을 보여드릴 것입니다.

## 준비 사항

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* 몇 페이지가 포함된 샘플 PDF 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 Visual Studio의 NuGet 패키지 관리자를 사용하여 설치할 수 있습니다.

## 단계

JPEG 변환기를 사용하여 PDF 페이지를 JPEG 이미지로 변환하는 기본 단계는 다음과 같습니다:

1. Jpeg 클래스의 객체를 생성합니다
1. JpegOptions 클래스의 객체를 생성하고 입력 및 출력 파일 경로를 추가합니다
1. Jpeg 객체의 Process 메서드를 실행하고 결과 컨테이너를 가져옵니다
1.
1.

C# 코드에서 이 단계들을 구현하는 방법을 살펴봅시다.

### 단계 1: Jpeg 클래스의 객체 생성

Jpeg 클래스는 PDF 페이지를 JPEG 이미지로 변환하는 기능을 제공하는 주요 클래스입니다. 사용하려면 기본 생성자를 사용하여 인스턴스를 생성해야 합니다:

```cs
// Jpeg의 새 인스턴스 생성
var converter = new Jpeg();
```

### 단계 2: JpegOptions 클래스의 객체를 생성하고 입력 및 출력 파일 경로 추가

JpegOptions 클래스는 출력 해상도, 페이지 범위, 이미지 품질 등 변환 과정에 대한 다양한 옵션과 매개변수를 지정할 수 있게 해주는 도우미 클래스입니다.
JpegOptions 클래스는 출력 해상도, 페이지 범위, 이미지 품질 등 변환 과정에 대한 다양한 옵션과 매개변수를 지정할 수 있도록 돕는 헬퍼 클래스입니다.

```cs
// 입력 및 출력 파일 경로 지정
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "images");

// JpegOptions 클래스의 인스턴스 생성
var converterOptions = new JpegOptions();

// 옵션에 입력 및 출력 파일 경로 추가
converterOptions.AddInput(new FileDataSource(inputPath));
converterOptions.AddOutput(new FileDataSource(outputPath));
```

출력 해상도, 페이지 범위, 이미지 품질 등의 다른 옵션도 JpegOptions 클래스의 속성을 사용하여 설정할 수 있습니다. 예를 들어, PDF 파일의 첫 페이지만 JPEG 이미지로 변환하려면 300 dpi 해상도로 다음 코드를 사용할 수 있습니다:

```cs
// 출력 해상도를 300 dpi로 설정
converterOptions.OutputResolution = 300;

// 페이지 범위를 첫 페이지로 설정
converterOptions.PageRange = new PageRange(1);
```
### 3단계: Jpeg 객체의 Process 메소드 실행 및 결과 컨테이너 가져오기

마지막 단계는 Jpeg 객체의 Process 메소드를 실행하는 것이며, 여기에 converterOptions 객체를 매개변수로 전달합니다. 이 메소드는 변환을 수행하고 결과 컨테이너인 ResultContainer 객체를 반환합니다. 이 객체는 변환의 상태, 메시지, 출력 파일 경로 등 변환 결과를 포함하고 있습니다. ResultContainer 클래스의 속성 및 메소드를 사용하여 결과를 접근할 수 있습니다. 예를 들어, 결과 컨테이너를 가져와 변환 상태를 출력하려면 다음 코드를 사용할 수 있습니다:

```cs
// 변환을 처리하고 결과 컨테이너를 가져옵니다
ResultContainer resultContainer = converter.Process(converterOptions);

// 변환의 상태를 출력합니다
Console.WriteLine(resultContainer.Status);
```

변환의 상태는 변환이 성공적으로 완료되었는지 여부에 따라 성공 또는 실패일 수 있습니다.

### 4단계: 변환된 JPEG 이미지의 경로 출력

결과 컨테이너는 각 출력 파일 경로에 대한 결과 컬렉션을 포함합니다.
결과 컨테이너는 각 출력 파일 경로마다 결과 컬렉션을 포함하고 있습니다.

```cs
// 변환된 JPEG 이미지의 경로를 출력합니다
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
  Console.WriteLine(operationResult.Data.ToString());
}
```

출력 파일 경로는 {outputPath}{pageNumber}.jpg 형식을 가집니다. 여기서 {outputPath}는 출력 디렉토리이고 {pageNumber}는 PDF 파일의 페이지 번호입니다. 예를 들어, 출력 디렉토리가 C:\Samples\images이고 PDF 파일이 세 페이지인 경우, 출력 파일 경로는 다음과 같습니다:

```text
C:\Samples\images\1.jpg
C:\Samples\images\2.jpg
C:\Samples\images\3.jpg
```
