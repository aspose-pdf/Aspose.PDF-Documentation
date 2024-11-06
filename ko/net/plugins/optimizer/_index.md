---
title: Optimizer
type: docs
weight: 80
url: ko/net/plugins/optimizer/
description: Aspose.PDF Optimizer를 사용하여 PDF 파일 최적화 및 조작 방법
lastmod: "2024-01-24"
---

이 장에서는 [Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/)를 사용하여 C# 애플리케이션에서 PDF 파일을 최적화하고 크기를 조정하며 회전하는 방법을 알아봅니다.
이제 단계별로 이 작업을 수행하는 방법을 알아보겠습니다.

## Prerequisites

다음이 필요합니다:

* Visual Studio 2019 이상
* Aspose.PDF for .NET 24.1 이상
* 일부 양식 필드가 포함된 샘플 PDF 파일

## Optimizing PDF Files

PDF 파일을 최적화하는 것은 파일 크기를 줄이고 성능을 향상시키는 것을 포함합니다. 다음 스니펫은 이 작업을 수행하는 방법을 보여줍니다. PDF 파일을 최적화하는 방법은 다음과 같습니다:

* 입력 PDF 파일을 위한 새 파일 데이터 소스를 생성합니다.
* 최적화된 출력 PDF 파일을 위한 새 파일 데이터 소스를 생성합니다.
* `OptimizeOptions` 인스턴스를 생성합니다.
* 입력 및 출력 데이터 소스를 최적화 옵션에 추가합니다.
* 최적화 옵션에 입력 및 출력 데이터 소스를 추가합니다.
* `Optimizer` 인스턴스를 생성하고 최적화 옵션을 사용하여 최적화를 처리합니다.

```cs
// 입력 PDF 파일에 대한 새 파일 데이터 소스를 생성합니다.
var inputDataSource = new FileDataSource(inputPath);

// 최적화된 출력 PDF 파일에 대한 새 파일 데이터 소스를 생성합니다.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// OptimizeOptions의 새 인스턴스를 생성합니다.
var options = new OptimizeOptions();

// 최적화 옵션에 입력 및 출력 데이터 소스를 추가합니다.
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);


// Optimizer의 새 인스턴스를 생성합니다.
var optimizer = new Optimizer();

// 최적화 옵션을 사용하여 최적화를 처리합니다.
optimizer.Process(options);
```

## PDF 파일 크기 조정

PDF 파일의 크기를 조정하려면 페이지 크기를 변경해야 합니다. 다음 코드는 이 작업을 수행하는 방법을 보여줍니다. PDF 파일의 크기를 조정하려면 다음 단계를 따르십시오:

* 입력 PDF 파일에 대한 새 파일 데이터 소스를 생성합니다.
* 입력 PDF 파일에 대한 새 파일 데이터 소스 생성
* 크기가 조정된 출력 PDF 파일에 대한 새 파일 데이터 소스 생성
* `ResizeOptions` 인스턴스를 생성하고 원하는 페이지 크기를 설정
* 입력 및 출력 데이터 소스를 리사이즈 옵션에 추가
* `Optimizer` 인스턴스를 생성하고 리사이즈 옵션을 사용하여 리사이징 처리

```cs
// 입력 PDF 파일에 대한 새 파일 데이터 소스 생성
var inputDataSource = new FileDataSource("sample.pdf");

// 크기가 조정된 출력 PDF 파일에 대한 새 파일 데이터 소스 생성
var outputDataSource = new FileDataSource("sample_resized.pdf");

// ResizeOptions의 새 인스턴스를 생성하고 원하는 페이지 크기를 설정
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// 리사이즈 옵션에 입력 및 출력 데이터 소스를 추가
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Optimizer의 새 인스턴스를 생성
var optimizer = new Optimizer();

// 리사이즈 옵션을 사용하여 리사이징 처리
optimizer.Process(opt);
```

## PDF 페이지 회전
## PDF 페이지 회전

PDF 페이지를 회전하면 PDF 문서 내 페이지의 방향을 변경할 수 있습니다. PDF 페이지를 회전하는 방법은 다음과 같습니다:

* 입력 PDF 파일을 위한 새 파일 데이터 소스를 생성합니다.
* 출력 PDF 파일을 위한 새 파일 데이터 소스를 생성합니다.
* `RotateOptions`의 인스턴스를 생성하고 회전 값을 설정합니다.
* 회전 옵션에 입력 및 출력 데이터 소스를 추가합니다.
* `Optimizer`의 인스턴스를 생성하고 회전 옵션을 사용하여 회전을 처리합니다.

```cs
// 입력 PDF 파일을 위한 새 파일 데이터 소스를 생성합니다.
var inputDataSource = new FileDataSource(inputPath);

// 최적화된 출력 PDF 파일을 위한 새 파일 데이터 소스를 생성합니다.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// OptimizeOptions의 새 인스턴스를 생성합니다.
var opt = new RotateOptions();

// 최적화 옵션에 입력 및 출력 데이터 소스를 추가합니다.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// 회전 값 설정
opt.Rotation = Rotation.on180;

// Optimizer의 새 인스턴스를 생성합니다.
var optimizer = new Optimizer();

// 최적화 옵션을 사용하여 최적화를 처리합니다.
optimizer.Process(opt)
```
## 결론

Aspose.PDF Optimizer 플러그인을 사용하여 C#에서 PDF 파일을 최적화하고, 크기를 조정하며, 회전하는 방법을 배웠습니다. 이 기술들을 여러분의 애플리케이션에 통합하여 요구사항에 맞게 PDF 문서를 효율적으로 조작하세요.
