---
title: Form Exporter
type: docs
weight: 50
url: /net/plugins/formexpoter/
description: Aspose.PDF Form Exporter 플러그인을 사용하여 폼 필드 값을 CSV 파일로 내보내는 방법
lastmod: "2024-01-24"
draft: false
---

이 기사에서는 PDF 파일에서 CSV 파일로 폼 필드 값을 내보낼 수 있는 [Form Exporter 플러그인](https://products.aspose.org/pdf/net/form-exporter/) 사용 방법을 보여 드리겠습니다.

## 사전 요구 사항

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 21.1 이상
* 일부 폼 필드가 포함된 샘플 PDF 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 Visual Studio의 NuGet 패키지 관리자를 사용하여 설치할 수 있습니다.

## 단계

FormExporter 플러그인을 사용하여 폼 필드 값을 CSV 파일로 내보내는 기본 단계는 다음과 같습니다:

1. `FormExporter` 클래스의 객체를 생성합니다
1. `FormExporterValuesToCsvOptions` 클래스의 객체를 생성하고 조건자 및 구분자를 지정합니다
1.
1.
1. `FormExporter` 객체의 `Process` 메서드를 실행합니다.

C# 코드에서 이 단계를 구현하는 방법을 살펴봅시다.

### 단계 1: FormExporter 클래스의 객체 생성

FormExporter 클래스는 폼 필드 값들을 CSV 파일로 내보내는 기능을 제공하는 주요 클래스입니다. 이를 사용하기 위해서는 기본 생성자를 사용하여 인스턴스를 생성해야 합니다:

```cs
// FormExporter 플러그인의 인스턴스 생성
var plugin = new FormExporter();
```

### 단계 2: FormExporterValuesToCsvOptions 클래스의 객체를 생성하고 조건과 구분자를 지정하세요

FormExporterValuesToCsvOptions 클래스는 내보내기 과정에 대한 다양한 옵션과 매개변수를 지정할 수 있게 해주는 도우미 클래스입니다.
FormExporterValuesToCsvOptions 클래스는 내보내기 프로세스에 대한 다양한 옵션과 매개변수를 지정할 수 있게 해주는 헬퍼 클래스입니다. 예를 들어 조건식과 구분자 등을 지정할 수 있습니다.

```cs
// CSV로 폼 필드 값 내보내기를 위한 옵션 생성
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```

### Step 3: 옵션 객체에 입력 및 출력 데이터 소스 추가

입력 및 출력 데이터 소스는 내보내고자 하는 PDF 파일과 저장하고자 하는 CSV 파일입니다.
입력 및 출력 데이터 소스는 내보내려는 PDF 파일과 저장하려는 CSV 파일입니다.

```cs
// 옵션에 입력 및 출력 파일 추가
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### 4단계: FormExporter 객체의 Process 메소드 실행

마지막 단계는 FormExporter 객체의 Process 메소드를 실행하는 것이며, 매개변수로 옵션 객체를 전달합니다.
마지막 단계는 옵션 객체를 매개 변수로 전달하여 FormExporter 객체의 Process 메서드를 실행하는 것입니다.

```cs
// 플러그인을 사용하여 폼 필드 값을 처리합니다
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

결과에는 입력 파일 경로와 출력 파일 경로와 같은 정보가 포함됩니다.
