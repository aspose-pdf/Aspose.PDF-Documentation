---
title: PDF의 개별 페이지 편집
type: docs
weight: 20
url: ko/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: 이 섹션은 PdfPageEditor 클래스를 사용하여 PDF의 개별 페이지를 편집하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/)의 Aspose.Pdf.Facades 네임스페이스는 PDF 파일의 개별 페이지를 조작할 수 있게 합니다. 이 기능은 페이지 디스플레이, 정렬, 전환 등을 다루는 데 도움이 됩니다. PdfPageEditor 클래스는 이 기능을 구현할 수 있도록 도와줍니다. 이 글에서는 이 클래스가 제공하는 속성과 메서드, 그리고 이러한 메서드의 작동 방식을 살펴보겠습니다.

{{% /alert %}}

## 설명

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 클래스는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스 및 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스와 다릅니다. 먼저 차이점을 이해해야 하며, 그런 다음 PdfPageEditor 클래스를 더 잘 이해할 수 있습니다. PdfFileEditor 클래스는 파일의 모든 페이지를 추가, 삭제 또는 연결하는 등의 조작을 가능하게 하고, PdfContentEditor 클래스는 페이지의 내용, 즉 텍스트 및 기타 객체 등을 조작하는 데 도움을 줍니다. 반면에, PdfPageEditor 클래스는 회전, 확대, 정렬 등의 개별 페이지 자체만을 다룹니다.

이 클래스에서 제공하는 기능을 크게 세 가지 범주로 나눌 수 있습니다. 즉, 전환, 정렬, 표시입니다. 아래에서 이러한 범주를 논의할 것입니다:

### Transition

이 클래스는 전환과 관련된 두 가지 속성을 포함하고 있습니다. 즉, [TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) 및 [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration). TransitionType는 프레젠테이션 중에 다른 페이지에서 이 페이지로 이동할 때 사용할 전환 스타일을 지정합니다. TransitionDuration은 페이지의 표시 기간을 지정합니다.

### Alignment

PdfPageEditor 클래스는 수평 및 수직 정렬을 모두 지원합니다. It provides two properties to serve the purpose i.e. [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment) and [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment). Alignment property is used to align the contents horizontally. Alignment property takes a value of AlignmentType, which contains three options i.e. Center, Left, and Right. VerticalAlignment property takes a value of VerticalAlignmentType, which contains three options i.e. Bottom, Center, and Top.

### Display

디스플레이 카테고리에는 PageSize, Rotation, Zoom, DisplayDuration과 같은 속성을 포함할 수 있습니다. PageSize 속성은 파일의 개별 페이지 크기를 지정합니다. 이 속성은 A0, A1, A2, A3, A4, A5, A6, B5, Letter, Ledger 및 P11x17과 같은 미리 정의된 페이지 크기를 캡슐화하는 PageSize 객체를 입력으로 받습니다. Rotation 속성은 개별 페이지의 회전을 설정하는 데 사용됩니다. 0, 90, 180 또는 270의 값을 받을 수 있습니다. Zoom 속성은 페이지의 확대/축소 계수를 설정하며, 부동 소수점 값을 입력으로 받습니다. 이 클래스는 또한 파일 내 개별 페이지의 페이지 크기 및 페이지 회전을 얻기 위한 메서드를 제공합니다.

위에서 언급한 메서드의 샘플은 아래 제공된 코드 스니펫에서 찾을 수 있습니다:

## 결론
{{% alert color="primary" %}}

이 기사에서는 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 클래스에 대해 자세히 살펴보았습니다. We have elaborated the properties and methods provided by this class. It makes the manipulation of individual pages in a class a very easy and simple task.
{{% /alert %}}

우리는 이 클래스에서 제공하는 속성과 메서드를 상세히 설명했습니다. 이는 클래스의 개별 페이지를 조작하는 작업을 매우 쉽고 간단하게 만들어줍니다.