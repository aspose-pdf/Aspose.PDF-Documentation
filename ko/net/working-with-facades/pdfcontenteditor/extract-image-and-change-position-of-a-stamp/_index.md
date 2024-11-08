---
title: 이미지 추출 및 도장 위치 변경
type: docs
weight: 30
url: /ko/net/extract-image-and-change-position-of-a-stamp/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 이미지 추출 및 도장 위치 변경 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 이미지 스탬프에서 이미지 추출

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스는 PDF 파일의 스탬프에서 이미지를 추출할 수 있게 해줍니다. 먼저, [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음, [GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) 메서드를 호출하여 PDF 파일의 특정 페이지에서 StampInfo 객체 배열을 가져옵니다. 그런 다음 StampInfo.Image 속성을 사용하여 StampInfo에서 이미지를 얻을 수 있습니다. 이미지를 얻은 후, 이미지를 저장하거나 이미지의 다양한 속성을 작업할 수 있습니다. 다음 코드 스니펫은 이미지 스탬프에서 이미지를 추출하는 방법을 보여줍니다.

## PDF 파일에서 스탬프의 위치 변경

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스는 PDF 파일에서 스탬프의 위치를 변경할 수 있게 해줍니다. 먼저, [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) 메서드를 호출하여 특정 페이지의 PDF 파일에서 스탬프 인덱스와 새로운 위치를 지정합니다. 그런 다음, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 파일을 저장할 수 있습니다. 다음 코드 스니펫은 특정 페이지에서 스탬프를 이동하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPosition.cs" >}}

또한, [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) 메서드를 사용하여 StampId를 사용하여 특정 스탬프를 이동할 수 있습니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPositionByID.cs" >}}