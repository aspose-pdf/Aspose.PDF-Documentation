---
title: 양식 편집기
type: docs
weight: 40
url: /ko/net/plugins/formeditor/
description: Aspose.PDF 플러그인을 사용하여 PDF 파일에서 양식 필드 추가, 업데이트 및 제거하는 방법
lastmod: "2024-01-24"
draft: false
---

이 문서에서는 PDF 파일에서 양식 필드를 추가, 업데이트 및 제거할 수 있는 [양식 편집기 플러그인](https://products.aspose.org/pdf/net/form-editor/) 사용 방법을 보여 드리겠습니다.

## 필수 조건

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* 일부 양식 필드가 포함된 샘플 PDF 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 Visual Studio의 NuGet 패키지 관리자를 사용하여 설치할 수 있습니다.

## 단계

FormEditor 플러그인을 사용하여 PDF 파일에서 양식 필드를 추가, 업데이트 및 제거하는 기본 단계는 다음과 같습니다:

1. FormEditor 클래스의 객체를 생성합니다.
1. 수행하려는 작업에 따라 FormEditorAddOptions, FormEditorSetOptions 또는 FormRemoveSelectedFieldsOptions 클래스의 객체를 생성합니다.
1. FormEditor 객체의 Process 메소드 실행

각 작업에 대해 C# 코드로 구현하는 방법을 알아봅시다.

### 1단계: FormEditor 클래스의 객체 생성

FormEditor 클래스는 PDF 파일에서 폼 필드를 추가, 업데이트, 제거하는 기능을 제공하는 주요 클래스입니다. 이를 사용하려면 기본 생성자를 사용하여 인스턴스를 생성해야 합니다:

```cs
// FormEditor 플러그인의 인스턴스 생성
var plugin = new FormEditor();
```

### 2단계: 수행하려는 작업에 따라 FormEditorAddOptions, FormEditorSetOptions 또는 FormRemoveSelectedFieldsOptions 클래스의 객체 생성

`FormEditorAddOptions`, `FormEditorSetOptions`, `FormRemoveSelectedFieldsOptions` 클래스는 폼 필드 유형, 값, 속성, 조건 등 다양한 옵션과 매개변수를 지정할 수 있게 해주는 도우미 클래스입니다.
`FormEditorAddOptions`, `FormEditorSetOptions`, 및 `FormRemoveSelectedFieldsOptions` 클래스는 폼 필드 유형, 값, 속성, 조건 등과 같은 폼 편집 작업에 대한 다양한 옵션과 매개 변수를 지정할 수 있도록 하는 헬퍼 클래스입니다.

```cs
    // 폼 필드를 추가하기 위한 옵션 생성
    var options = new FormEditorAddOptions(
        [
            // 체크박스 폼 필드 생성
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CheckBoxField 1",
                PartialName = "CheckBoxField_1",
                Color = Color.Blue,
            },
            // 콤보 박스 폼 필드 생성
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["option1", "option2", "option3"],
                Selected = 2
            },
            // 텍스트박스 폼 필드 생성
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Some text",
                Color = Color.Chocolate
            }
        ]);
```
"값이" 또는 "또 다른 값"인 양식 필드의 값을 "새 값"으로 변경하려면 다음 코드를 사용할 수 있습니다:

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "값이" || field.Value == "또 다른 값"; },
    new FormFieldSetOptions()
    {
        Value = "새 값"
    });
```

왼쪽 아래 x좌표가 300보다 큰 양식 필드를 제거하려면 다음 코드를 사용할 수 있습니다:

```cs
// 양식 필드 제거를 위한 옵션 생성
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### 단계 3: 옵션 객체에 입력 및 출력 데이터 소스 추가

입력 및 출력 데이터 소스는 편집하고 저장하고자 하는 PDF 파일입니다.
입력 및 출력 데이터 소스는 편집 및 저장하려는 PDF 파일입니다.

```cs
// 입력 및 출력 파일 경로 지정
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// 입력 및 출력 파일에 대한 FileDataSource 클래스의 새 인스턴스 생성
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// 옵션에 입력 및 출력 데이터 소스 추가
options.AddInput(inputData);
options.AddOutput(outputData);
```

### 4단계: FormEditor 객체의 Process 메소드 실행

마지막 단계는 options 객체를 매개변수로 전달하여 FormEditor 객체의 Process 메소드를 실행하는 것입니다.
마지막 단계는 옵션 객체를 매개 변수로 전달하여 FormEditor 객체의 Process 메소드를 실행하는 것입니다.

```cs
// 플러그인과 옵션을 사용하여 폼 편집 작업 처리
ResultContainer result = plugin.Process(options);

// 결과 컬렉션에서 첫 번째 결과 가져오기
var result = resultContainer.ResultCollection[0];

// 결과 출력
Console.WriteLine(result);
```

결과에는 출력 파일 경로와 같은 정보가 포함됩니다.
