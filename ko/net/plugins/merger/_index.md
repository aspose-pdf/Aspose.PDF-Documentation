---
title: Merger
type: docs
weight: 100
url: /ko/net/plugins/merger/
description: Aspose.PDF Merger 플러그인을 사용하여 여러 PDF 파일을 하나로 병합하는 방법
lastmod: "2024-01-24"
---

이 글에서는 여러 PDF 파일을 하나로 병합하고 새 파일로 저장할 수 있는 [Merger 플러그인](https://products.aspose.org/pdf/net/merger/) 사용 방법을 보여 드리겠습니다.

## 필수 조건

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 21.1 이상
* 병합하려는 세 개의 샘플 PDF 파일

Aspose.PDF for .NET 라이브러리는 공식 웹사이트에서 다운로드하거나 Visual Studio의 NuGet 패키지 관리자를 사용하여 설치할 수 있습니다.

## 단계

Merger 플러그인을 사용하여 여러 PDF 파일을 하나로 병합하는 기본 단계는 다음과 같습니다:

1. Merger 클래스의 객체를 생성합니다.
2. MergeOptions 클래스의 객체를 생성하고 입력 및 출력 파일 경로를 추가합니다.
3. Merger 객체의 Process 메소드를 실행합니다.

C# 코드에서 이 단계들을 구현하는 방법을 살펴보겠습니다.

### 단계 1: Merger 클래스의 객체를 생성합니다.
### 1단계: Merger 클래스의 객체 생성

Merger 클래스는 여러 PDF 파일을 하나로 병합하는 기능을 제공하는 주요 클래스입니다. 사용하려면 기본 생성자를 사용하여 인스턴스를 생성해야 합니다:

```cs
// Merger의 새 인스턴스 생성
var pdfMerger = new Merger();
```

### 2단계: MergeOptions 클래스의 객체를 생성하고 입력 및 출력 파일 경로 추가

MergeOptions 클래스는 병합 과정에 대한 다양한 옵션과 매개변수를 지정할 수 있는 도우미 클래스입니다. 페이지 범위, 순서, 보안 등을 지정할 수 있습니다.
MergeOptions 클래스는 페이지 범위, 순서, 보안 등 병합 과정에 대한 다양한 옵션과 매개변수를 지정할 수 있는 헬퍼 클래스입니다.

```cs
// 입력 및 출력 파일 경로 지정
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// MergeOptions 클래스의 인스턴스 생성
var mergeOptions = new MergeOptions();

// 옵션에 입력 및 출력 파일 경로 추가
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

### Step 3: Run the Process method of the Merger object

마지막 단계는 Merger 객체의 Process 메소드를 실행하는 것이며, mergeOptions 객체를 매개변수로 전달합니다.
최종 단계는 Merger 객체의 Process 메소드를 실행하는 것이며, 매개변수로 mergeOptions 객체를 전달합니다.

```cs
// 병합을 처리하고 병합된 파일을 저장합니다.
pdfMerger.Process(mergeOptions);

// 확인 메시지를 출력합니다.
Console.WriteLine("PDF 파일이 성공적으로 병합되었습니다.");
```
