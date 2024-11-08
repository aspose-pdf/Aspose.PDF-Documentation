```
---
title: 페이지 속성 조작
type: docs
weight: 80
url: /ko/net/manipulate-page-properties/
description: 이 섹션에서는 PdfPageEditor 클래스를 사용하여 Aspose.PDF Facades로 페이지 속성을 조작하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일에서 PDF 페이지 속성 가져오기

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor)를 사용하면 PDF 파일의 개별 페이지를 작업할 수 있습니다.
``` 개별 페이지의 속성(다양한 페이지 박스 크기, 페이지 회전, 페이지 확대/축소 등)을 가져오는 데 도움이 됩니다. 이러한 속성을 얻으려면 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음, [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) 등과 같은 다양한 메서드를 사용하여 페이지 속성을 가져올 수 있습니다.

다음 코드 스니펫은 기존 PDF 파일에서 PDF 페이지 속성을 가져오는 방법을 보여줍니다. 

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-GetPageProperties-GetPageProperties.cs" >}}
## 기존 PDF 파일에서 PDF 페이지 속성 설정

페이지 회전, 확대 또는 원점과 같은 페이지 속성을 설정하려면 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 클래스를 사용해야 합니다. 이 클래스는 이러한 페이지 속성을 설정할 수 있는 다양한 메서드와 속성을 제공합니다. 먼저, [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음, 이러한 메서드와 속성을 사용하여 페이지 속성을 설정할 수 있습니다. 마지막으로, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 기존 PDF 파일에서 PDF 페이지 속성을 설정하는 방법을 보여줍니다.

## 특정 페이지의 PDF 파일 내용 크기 조정

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 클래스의 ResizeContents 메서드를 사용하여 PDF 파일의 페이지 내용을 크기 조정할 수 있습니다. [ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) 클래스는 페이지의 크기를 조정하기 위해 사용할 매개변수를 지정하는 데 사용됩니다. 예를 들어, 퍼센트 또는 단위로 여백 등을 지정할 수 있습니다. ResizeContents 메서드를 사용하여 모든 페이지의 크기를 조정하거나 크기를 조정할 페이지의 배열을 지정할 수 있습니다.

다음 코드 스니펫은 PDF 파일의 특정 페이지 내용의 크기를 조정하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-ResizePageContents-ResizePageContents.cs" >}}