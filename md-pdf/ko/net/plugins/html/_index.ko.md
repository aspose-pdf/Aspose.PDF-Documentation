---
title: HTML 변환기
type: docs
weight: 70
url: /net/plugins/html/
description: Aspose.PDF PdfHtml 플러그인을 사용하여 PDF 파일을 HTML 파일로 변환하는 방법
lastmod: "2024-01-24"
draft: false
---

이 글에서는 PDF 파일을 HTML 파일로 변환할 수 있는 [PdfHtml 플러그인](https://products.aspose.org/pdf/net/html-converter/)을 사용하는 방법을 보여 드리겠습니다.

## 필수 조건

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 21.1 이상
* 샘플 PDF 파일과 샘플 HTML 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 Visual Studio의 NuGet 패키지 매니저를 사용하여 설치할 수 있습니다.

## 단계

PdfHtml 플러그인을 사용하여 PDF 파일을 HTML 파일로 변환하는 기본 단계는 다음과 같습니다:

1. PdfHtml 클래스의 객체를 생성합니다
2. 변환 방향에 따라 PdfToHtmlOptions 또는 HtmlToPdfOptions 클래스의 객체를 생성합니다
3. 옵션 객체에 입력 및 출력 데이터 소스를 추가합니다
4.
### 1단계: PdfHtml 클래스의 객체 생성

PdfHtml 클래스는 PDF 파일을 HTML 파일로 변환하는 기능을 제공하는 주요 클래스입니다. 사용하려면 기본 생성자를 사용하여 인스턴스를 생성해야 합니다:

```cs
// PdfHtml 플러그인의 인스턴스 생성
var plugin = new PdfHtml();
```

### 2단계: 변환 방향에 따라 PdfToHtmlOptions 또는 HtmlToPdfOptions 클래스의 객체 생성

PdfToHtmlOptions 및 HtmlToPdfOptions 클래스는 출력 형식, 페이지 범위, 인코딩, 글꼴 등 변환 과정에 대한 다양한 옵션과 매개변수를 지정할 수 있게 해주는 도우미 클래스입니다. 이 클래스들을 사용하려면 기본 생성자를 사용하거나 일부 매개변수를 전달하여 적절한 클래스의 인스턴스를 생성해야 합니다. 예를 들어, PDF 파일을 임베디드 리소스가 포함된 HTML 파일로 변환하려면 다음 코드를 사용할 수 있습니다:

```cs
```

```cs
// PdfToHtmlOptions 클래스의 새 인스턴스를 생성합니다.
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);
```

HTML 파일을 기본 설정으로 PDF 파일로 변환하려면 다음 코드를 사용할 수 있습니다:

```cs
// HtmlToPdfOptions 클래스의 새 인스턴스를 생성합니다
var options = new HtmlToPdfOptions();
```

출력 형식, 페이지 범위, 인코딩, 폰트 등 다른 옵션도 options 클래스의 속성을 사용하여 설정할 수 있습니다. 예를 들어, PDF 파일을 UTF-8 인코딩과 Arial 폰트를 사용하여 HTML 파일로 변환하려면 다음 코드를 사용할 수 있습니다:

```cs
// PdfToHtmlOptions 클래스의 새 인스턴스를 생성합니다.
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);

// 인코딩을 UTF-8로 설정합니다.
options.Encoding = Encoding.UTF8;

// 폰트를 Arial로 설정합니다.
options.Font = "Arial";
```

### 3단계: 입력 및 출력 데이터 소스를 옵션 객체에 추가합니다.

입력 및 출력 데이터 소스는 변환하고 저장하려는 PDF 또는 HTML 파일입니다.
입력 및 출력 데이터 소스는 변환하고 저장하려는 PDF 또는 HTML 파일입니다.

```cs
// 입력 및 출력 파일 경로 지정
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.html");

// 옵션에 입력 및 출력 파일 경로 추가
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

### Step 4: PdfHtml 객체의 Process 메소드 실행

마지막 단계는 options 객체를 매개변수로 전달하여 PdfHtml 객체의 Process 메소드를 실행하는 것입니다. 이 메소드는 변환을 수행하고 ResultContainer 객체를 반환합니다. 이 객체에는 변환의 결과, 상태, 메시지, 출력 데이터 소스 등이 포함되어 있습니다. ResultContainer 클래스의 속성 및 메소드를 사용하여 결과를 액세스할 수 있습니다. 예를 들어, 결과 컬렉션에서 첫 번째 결과를 가져와 콘솔에 출력하려면 다음 코드를 사용할 수 있습니다:

```cs
// 변환을 처리하고 결과 컨테이너 가져오기
var resultContainer = plugin.Process(options);

// 결과 컬렉션에서 첫 번째 결과 가져오기
var result = resultContainer.ResultCollection[0];

// 콘솔에 결과 출력
Console.WriteLine(result);
```
결과는 출력 파일 경로와 같은 정보를 포함하게 됩니다.
