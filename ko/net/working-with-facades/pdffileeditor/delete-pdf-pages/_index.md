---
title: PDF 페이지 삭제
type: docs
weight: 70
url: ko/net/delete-pdf-pages/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 페이지를 삭제하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

디스크에 있는 PDF 파일에서 여러 페이지를 삭제하려면 다음 세 가지 매개변수를 사용하는 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) 메서드의 오버로드를 사용할 수 있습니다: 입력 파일 경로, 삭제할 페이지 번호 배열, 출력 PDF 파일 경로. 두 번째 매개변수는 삭제해야 할 모든 페이지를 나타내는 정수 배열입니다. 지정된 페이지는 입력 파일에서 제거되고 결과는 출력 파일로 저장됩니다. 다음 코드 스니펫은 파일 경로를 사용하여 PDF 페이지를 삭제하는 방법을 보여줍니다.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}


## 스트림을 사용하여 PDF 페이지 삭제

The [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 오버로드를 제공하여 입력 및 출력 파일이 스트림에 있을 때 입력 PDF 파일에서 페이지를 삭제할 수 있습니다. 이 오버로드는 다음 세 가지 매개변수를 받습니다: 삭제할 PDF 페이지의 정수 배열, 입력 스트림 및 출력 스트림. 다음 코드 스니펫은 스트림을 사용하여 PDF 페이지를 삭제하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingStream-DeletePagesUsingStream.cs" >}}