---
title: PDF 페이지 삽입
type: docs
weight: 50
url: /ko/net/insert-pdf-pages/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 페이지를 삽입하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 파일 경로를 사용하여 두 숫자 사이에 PDF 페이지 삽입

특정 페이지 범위는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 메서드를 사용하여 한 PDF에서 다른 PDF로 삽입할 수 있습니다. 그렇게 하려면, 페이지를 삽입하려는 입력 PDF 파일, 삽입할 페이지를 가져와야 하는 포트 파일, 페이지를 삽입할 위치, 입력 PDF 파일에 삽입해야 하는 포트 파일의 페이지 범위가 필요합니다. 이 범위는 시작 페이지와 종료 페이지 매개변수로 지정됩니다. 마지막으로, 출력 PDF 파일은 입력 파일에 지정된 범위의 페이지가 삽입된 상태로 저장됩니다. 다음 코드 스니펫은 파일 스트림을 사용하여 두 숫자 사이에 PDF 페이지를 삽입하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbers-InsertPagesBetweenNumbers.cs" >}}

## 파일 경로를 사용하여 PDF 페이지 배열 삽입

특정 페이지를 다른 PDF 파일에 삽입하려는 경우, 페이지의 정수 배열이 필요한 [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 메서드의 오버로드를 사용할 수 있습니다. 이 배열에서는 입력 PDF 파일에 삽입하고자 하는 특정 페이지를 지정할 수 있습니다. 이를 위해서는 페이지를 삽입할 입력 PDF 파일, 삽입할 페이지를 가져올 포트 파일, 페이지가 삽입될 위치, 입력 PDF 파일에 삽입해야 할 포트 파일의 페이지 정수 배열이 필요합니다. 이 배열에는 입력 PDF 파일에 삽입하고자 하는 특정 페이지 목록이 포함되어 있습니다. 마지막으로, 출력 PDF 파일은 입력 파일에 삽입된 페이지 배열과 함께 저장됩니다.
다음 코드 스니펫은 파일 경로를 사용하여 PDF 페이지 배열을 삽입하는 방법을 보여줍니다.

## 스트림을 사용하여 두 숫자 사이에 PDF 페이지 삽입

스트림을 사용하여 페이지 범위를 삽입하려면, [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 메서드의 적절한 오버로드를 사용하기만 하면 됩니다. 문서를 그렇게 하기 위해서는 삽입하고자 하는 페이지를 포함한 입력 PDF 스트림, 삽입을 위해 페이지를 가져와야 하는 포트 스트림, 페이지가 삽입될 위치, 입력 PDF 스트림에 삽입해야 할 포트 스트림의 페이지 범위가 필요합니다. 이 범위는 시작 페이지와 종료 페이지 매개변수로 지정됩니다. 마지막으로, 출력 PDF 스트림은 입력 스트림에 삽입된 페이지 범위가 지정되어 저장됩니다. 다음 코드 스니펫은 스트림을 사용하여 두 숫자 사이에 PDF 페이지를 삽입하는 방법을 보여줍니다.

## 스트림을 사용하여 PDF 페이지 배열 삽입

또한, 페이지의 정수 배열이 필요한 Insert 메서드의 적절한 오버로드를 사용하여 스트림을 통해 다른 PDF 파일에 페이지 배열을 삽입할 수도 있습니다. 이 배열에서는 입력 PDF 스트림에 삽입하고자 하는 특정 페이지를 지정할 수 있습니다. 이를 위해서는 페이지를 삽입하고자 하는 입력 PDF 스트림, 삽입을 위해 페이지를 가져와야 하는 포트 스트림, 페이지가 삽입될 위치, 입력 PDF 파일에 삽입되어야 하는 포트 스트림의 페이지 정수 배열이 필요합니다. 이 배열은 입력 PDF 스트림에 삽입하고자 하는 특정 페이지 목록을 포함하고 있습니다. 마지막으로, 출력 PDF 스트림은 입력 파일에 삽입된 지정된 페이지 배열과 함께 저장됩니다. 다음 코드 스니펫은 스트림을 사용하여 PDF 페이지 배열을 삽입하는 방법을 보여줍니다.