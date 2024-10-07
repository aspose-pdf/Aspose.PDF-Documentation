---
title: Form Exporter
type: docs
weight: 60
url: /net/plugins/formflattener/
description: Aspose.PDF FormFlattener 플러그인을 사용하여 PDF 파일의 양식 필드를 평탄화하는 방법
lastmod: "2024-01-24"
---

이 글에서는 PDF 파일의 양식 필드를 평탄화할 수 있는 [FormFlattener 플러그인](https://products.aspose.org/pdf/net/form-flattener/) 사용 방법을 보여 드리겠습니다.

## 사전 요구 사항

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 21.1 이상
* 양식 필드가 포함된 샘플 PDF 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 Visual Studio의 NuGet 패키지 관리자를 사용하여 설치할 수 있습니다.

## 단계

FormFlattener 플러그인을 사용하여 PDF 파일의 양식 필드를 평탄화하는 기본 단계는 다음과 같습니다:

1. FormFlattener 클래스의 객체를 생성합니다
1. 모든 필드를 평탄화하고자 하는지 일부 필드만 평탄화하고자 하는지에 따라 FormFlattenAllFieldsOptions 클래스 또는 FormFlattenSelectedFieldsOptions 클래스의 객체를 생성합니다
1.
1.
1. FormFlattener 객체의 Process 메소드를 실행합니다.

C# 코드로 이 단계를 구현하는 방법을 살펴봅시다.

### 단계 1: FormFlattener 클래스의 객체를 생성합니다.

FormFlattener 클래스는 PDF 파일의 폼 필드를 평탄화하는 기능을 제공하는 주요 클래스입니다. 이를 사용하려면 기본 생성자를 사용하여 인스턴스를 생성해야 합니다:

```cs
// FormFlattener 플러그인의 인스턴스를 생성합니다
var plugin = new FormFlattener();
```

### 단계 2: 모든 필드를 평탄화하고자 하는 경우 FormFlattenAllFieldsOptions 클래스의 객체를 생성하거나 일부 필드만 평탄화하고자 하는 경우 FormFlattenSelectedFieldsOptions 클래스의 객체를 생성합니다.

FormFlattenAllFieldsOptions 및 FormFlattenSelectedFieldsOptions 클래스는 평탄화 과정에 대한 다양한 옵션과 매개변수를 지정할 수 있도록 도와주는 도우미 클래스입니다.
FormFlattenAllFieldsOptions 및 FormFlattenSelectedFieldsOptions 클래스는 평탄화 프로세스에 대한 다양한 옵션과 매개변수를 지정할 수 있는 도우미 클래스입니다.

```cs
// 모든 필드를 평탄화하기 위한 옵션 생성
var options = new FormFlattenAllFieldsOptions();
```

하단 왼쪽 x 좌표가 300보다 큰 양식 필드만 평탄화하려면 다음 코드를 사용할 수 있습니다:

```cs
// 선택된 필드를 평탄화하기 위한 옵션 생성
var options = new FormFlattenSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Step 3: 옵션 객체에 입력 및 출력 데이터 소스 추가

입력 및 출력 데이터 소스는 평탄화하고 저장하려는 PDF 파일입니다.
입력 및 출력 데이터 소스는 평면화하고 저장하려는 PDF 파일입니다.

```cs
// 옵션에 입력 및 출력 데이터 소스 추가
options.Inputs.Add(new FileDataSource("sample.pdf"));
options.Outputs.Add(new FileDataSource("sample-flat.pdf"));
```

### Step 4: FormFlattener 객체의 Process 메서드 실행

마지막 단계는 FormFlattener 객체의 Process 메서드를 실행하는 것입니다. 이 메서드는 옵션 객체를 매개변수로 전달받아 평면화 과정을 수행하며, 결과 상태, 메시지, 출력 데이터 소스 등을 포함하는 ResultContainer 객체를 반환합니다. ResultContainer 클래스의 속성과 메서드를 사용하여 결과를 액세스할 수 있습니다. 예를 들어, 결과 컬렉션에서 첫 번째 결과를 가져와 콘솔에 출력하려면 다음 코드를 사용할 수 있습니다:

```cs
// 옵션을 처리하고 결과 컨테이너를 가져옵니다
var resultContainer = plugin.Process(options);

// 결과 컨테이너에서 첫 번째 결과를 가져옵니다
var result = resultContainer.ResultCollection[0];

// 결과를 출력합니다
Console.WriteLine(result);
```
결과는 출력 파일 경로와 같은 정보를 포함할 것입니다.
