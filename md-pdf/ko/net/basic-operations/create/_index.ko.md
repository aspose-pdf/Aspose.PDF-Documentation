---
title: 프로그래밍 방식으로 PDF 문서 생성
linktitle: PDF 생성
type: docs
weight: 10
url: /net/create-document/
description: 이 페이지는 Aspose.PDF 라이브러리를 사용하여 처음부터 PDF 문서를 생성하는 방법을 설명합니다.
---

Aspose.PDF for .NET API는 C# 및 VB.NET을 사용하여 PDF 파일을 생성하고 읽을 수 있습니다. 이 API는 WinForms, ASP.NET 및 기타 여러 .NET 애플리케이션에서 사용할 수 있습니다. 이 글에서는 .NET 애플리케이션에서 Aspose.PDF for .NET API를 사용하여 PDF 파일을 쉽게 생성하고 읽는 방법을 보여줍니다.

## C#을 사용하여 PDF 파일 생성 방법

C#을 사용하여 PDF 파일을 생성하기 위해 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 객체 생성
1. 문서 객체의 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) 컬렉션에 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체 추가
1.
1.
1. 결과 PDF 문서를 저장하세요.

다음 코드 스니펫은 새로운 그래픽 [Aspose.Drawing](/pdf/net/drawing/) 인터페이스와 함께 작동합니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// 문서 객체 초기화
Document document = new Document();
// 페이지 추가
Page page = document.Pages.Add();
// 새 페이지에 텍스트 추가
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// 업데이트된 PDF 저장
document.Save(dataDir + "HelloWorld_out.pdf")
```

이 경우, 우리는 A4 페이지 크기, 세로 방향의 PDF 단일 페이지 문서를 만듭니다. 우리의 페이지는 페이지 상단 왼쪽 부분에 "Hello, World"를 포함할 것입니다.
