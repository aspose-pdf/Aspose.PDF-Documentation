```
---
title: PDF 페이지 분할
type: docs
weight: 60
url: /net/split-pdf-pages/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 페이지를 분할하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 파일 경로를 사용하여 처음부터 PDF 페이지 분할

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 클래스의 [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) 메소드는 PDF 파일을 첫 페이지부터 지정된 페이지 번호까지 분할할 수 있게 해줍니다. 디스크에서 PDF 파일을 조작하려면 입력 및 출력 PDF 파일의 파일 경로를 이 메소드에 전달할 수 있습니다. 다음 코드 조각은 파일 경로를 사용하여 처음부터 PDF 페이지를 분할하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## 파일 스트림을 사용하여 처음부터 PDF 페이지 분할
```

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 클래스의 첫 페이지부터 지정된 페이지 번호까지 PDF 파일을 분할할 수 있습니다. 스트림에서 PDF 파일을 조작하려면 이 메서드에 입력 및 출력 PDF 스트림을 전달할 수 있습니다. 다음 코드 스니펫은 파일 스트림을 사용하여 처음부터 PDF 페이지를 분할하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## 파일 경로를 사용하여 대량으로 PDF 페이지 분할

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) 메서드는 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 클래스의 PDF 파일을 여러 페이지 세트로 분할할 수 있습니다. 이 예제에서는 두 세트의 페이지 (1, 2) 및 (5, 6)가 필요합니다. 디스크에서 PDF 파일에 액세스하려면 입력 PDF를 파일 경로로 전달해야 합니다. 이 메서드는 MemoryStream 배열을 반환합니다. 이 배열을 반복하여 개별 페이지 세트를 별도의 파일로 저장할 수 있습니다. 다음 코드 조각은 파일 경로를 사용하여 PDF 페이지를 대량으로 분할하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## 스트림을 사용하여 PDF 페이지를 대량으로 분할

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) 메서드를 사용하면 PDF 파일을 여러 세트의 페이지로 분할할 수 있습니다. 이 예제에서는 두 세트의 페이지 (1, 2) 및 (5, 6)가 필요합니다. 이 메서드에 파일을 디스크에서 액세스하는 대신 스트림을 전달할 수 있습니다. 이 메서드는 MemoryStream 배열을 반환합니다. 이 배열을 반복하여 개별 페이지 세트를 별도의 파일로 저장할 수 있습니다. 다음 코드 조각은 스트림을 사용하여 PDF 페이지를 대량으로 분할하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## 파일 경로를 사용하여 PDF 페이지 끝까지 분할

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) 메서드는 지정된 페이지 번호부터 PDF 파일의 끝까지 PDF를 분할하고 새 PDF로 저장할 수 있습니다. 이 작업을 수행하려면 파일 경로를 사용하여 입력 및 출력 파일 경로와 분할을 시작할 페이지 번호를 전달해야 합니다. 출력 PDF는 디스크에 저장됩니다. 다음 코드 스니펫은 파일 경로를 사용하여 PDF 페이지를 끝까지 분할하는 방법을 보여줍니다.

## 스트림을 사용하여 PDF 페이지 끝까지 분할

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) 메서드를 사용하면 지정된 페이지 번호부터 PDF 파일의 끝까지 PDF를 분할하고 이를 새로운 PDF로 저장할 수 있습니다. 이 작업을 수행하려면 스트림을 사용하여 입력 및 출력 스트림과 분할을 시작할 페이지 번호를 전달해야 합니다. 출력 PDF는 출력 스트림에 저장됩니다. 다음 코드 스니펫은 스트림을 사용하여 PDF 페이지를 끝까지 분할하는 방법을 보여줍니다.

## 파일 경로를 사용하여 PDF를 개별 페이지로 분할

PDF 문서를 분할하고 결과를 온라인으로 확인하려면 다음 링크를 시도해 보세요:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

PDF 파일을 개별 페이지로 분할하려면 PDF를 파일 경로로 [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) 메서드에 전달해야 합니다. 이 메서드는 PDF 파일의 개별 페이지를 포함하는 MemoryStream 배열을 반환합니다. 이 MemoryStream 배열을 반복하여 개별 페이지를 디스크에 개별 PDF 파일로 저장할 수 있습니다. 다음 코드 스니펫은 파일 경로를 사용하여 PDF를 개별 페이지로 분할하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## 스트림을 사용하여 PDF를 개별 페이지로 분할

PDF 파일을 개별 페이지로 분할하려면 [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) 메서드에 PDF를 스트림으로 전달해야 합니다. 이 메서드는 PDF 파일의 개별 페이지를 포함하는 MemoryStream 배열을 반환합니다. 이 MemoryStream 배열을 통해 반복하고 개별 페이지를 디스크에 개별 PDF 파일로 저장하거나, 이러한 개별 페이지를 메모리 스트림에 보관하여 애플리케이션에서 나중에 사용할 수 있습니다. 다음 코드 스니펫은 스트림을 사용하여 PDF를 개별 페이지로 분할하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingStreams-SplitToIndividualPagesUsingStreams.cs" >}}