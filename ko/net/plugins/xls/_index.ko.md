---
title: XLS 변환기
type: docs
weight: 20
url: /net/plugins/xls/
description: Aspose.Pdf 플러그인을 사용하여 PDF를 Excel 스프레드시트로 변환하는 방법
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

이 글에서는 [PdfXls 플러그인](https://products.aspose.org/pdf/net/xls-converter/)을 사용하여 PDF 파일을 고도의 정확성과 충실도로 Excel 형식으로 변환하는 방법을 보여 드리겠습니다.

{{% /alert %}}

## 필수 조건

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* Excel 형식으로 변환하고자 하는 샘플 PDF 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 Visual Studio의 NuGet 패키지 관리자를 사용하여 설치할 수 있습니다.

## 단계

PdfXls 플러그인을 사용하여 PDF 파일을 Excel 형식으로 변환하는 기본 단계는 다음과 같습니다:

1. PdfXls 클래스의 객체를 생성합니다
1. 입력 및 출력 데이터 소스를 PdfToXlsOptions 객체에 추가합니다
1. PdfXls 객체의 Process 메소드를 실행합니다

이제 C# 코드에서 이러한 단계를 구현하는 방법을 살펴보겠습니다.
### 1단계: PdfXls 클래스의 객체 생성

PdfXls 클래스는 PDF를 Excel로 변환하는 기능을 제공하는 주요 클래스입니다. 이를 사용하려면 기본 생성자를 사용하여 인스턴스를 생성해야 합니다:

```csharp
// PdfXls 플러그인의 인스턴스 생성
var plugin = new PdfXls();
```

### 2단계: PdfToXlsOptions 객체에 입력 및 출력 데이터 소스 추가

PdfToXlsOptions 클래스는 변환 프로세스에 대한 다양한 옵션과 매개변수를 지정할 수 있는 도우미 클래스입니다. 이를 사용하려면 인스턴스를 생성하고 `AddInput` 및 `AddOutput` 메소드를 사용하여 입력 및 출력 데이터 소스를 추가해야 합니다. 데이터 소스는 파일 경로 또는 스트림일 수 있습니다. 예를 들어, `C:\Samples` 폴더에 있는 `sample.pdf` 파일을 같은 폴더에 있는 `sample.xlsx` 파일로 변환하려면 다음 코드를 사용할 수 있습니다:

```csharp
// 입력 및 출력 파일 경로 지정
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// PdfToXlsOptions 클래스의 인스턴스 생성
var options = new PdfToXlsOptions();

// 옵션에 입력 및 출력 파일 경로 추가
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```
출력 형식, 페이지 범위, 워크시트 이름 등의 다른 옵션도 PdfToXlsOptions 클래스의 속성을 사용하여 설정할 수 있습니다. 예를 들어, PDF 파일을 XLSX 형식으로 변환하고 첫 번째 위치에 빈 열을 삽입하고 워크시트의 이름을 "MySheet"로 지정하려면 다음 코드를 사용할 수 있습니다.

```csharp
// 출력 형식을 XLSX로 설정
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// 첫 번째 위치에 빈 열 삽입
options.InsertBlankColumnAtFirst = true;
```

### Step 3: PdfXls 객체의 Process 메소드 실행

마지막 단계는 PdfToXlsOptions 객체를 매개변수로 전달하여 PdfXls 객체의 Process 메소드를 실행하는 것입니다.
마지막 단계는 PdfXls 객체의 Process 메소드를 실행하는 것이며, 매개변수로 PdfToXlsOptions 객체를 전달합니다.

```csharp
// PDF를 Excel로 변환하는 프로세스를 플러그인 및 옵션을 사용하여 수행
var resultContainer = plugin.Process(options);

// 결과 컬렉션에서 첫 번째 결과를 가져옵니다
var result = resultContainer.ResultCollection[0];

// 결과를 출력합니다
Console.WriteLine(result);
```

결과에는 출력 파일 경로와 같은 정보가 포함됩니다.

