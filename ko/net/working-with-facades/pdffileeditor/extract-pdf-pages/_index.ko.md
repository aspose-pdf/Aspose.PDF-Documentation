---
title: PDF 페이지 추출
type: docs
weight: 40
url: /net/extract-pdf-pages/
description: 이 섹션은 PdfFileEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 페이지를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 파일 경로를 사용하여 두 숫자 사이의 PDF 페이지 추출

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메소드는 PDF 파일에서 지정된 페이지 범위를 추출할 수 있게 해줍니다. 이 오버로드는 디스크에서 PDF 파일을 조작하면서 페이지를 추출할 수 있게 해줍니다. 이 오버로드는 다음 매개변수가 필요합니다: 입력 파일 경로, 시작 페이지, 종료 페이지 및 출력 파일 경로. 시작 페이지부터 종료 페이지까지의 페이지가 추출되며 출력은 디스크에 저장됩니다. 다음 코드 스니펫은 파일 경로를 사용하여 두 숫자 사이의 PDF 페이지를 추출하는 방법을 보여줍니다.

```csharp
public static void Extract_PDFPages_FilePaths()
{
    // PdfFileEditor 객체 생성
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // 페이지 추출
    pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## 파일 경로를 사용하여 PDF 페이지 배열 추출하기

특정 페이지 집합을 추출하려면 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드를 사용하여 가능합니다. 먼저 추출할 모든 페이지 번호로 정수 배열을 만들어야 합니다. 이 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드의 오버로드는 입력 PDF 파일, 추출할 페이지의 정수 배열 및 출력 PDF 파일을 매개변수로 받습니다. 다음 코드 스니펫은 파일 경로를 사용하여 PDF 페이지를 추출하는 방법을 보여줍니다.

```csharp
public static void Extract_PDFPages_Streams()
{
    // PdfFileEditor 객체 생성
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // 스트림 생성
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        // 페이지 추출
        pdfEditor.Extract(inputStream, 1, 3, outputStream);
}
```

## 두 숫자 사이의 PDF 페이지를 스트림을 사용하여 추출하기

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 클래스의 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메소드는 스트림을 사용하여 페이지 범위를 추출할 수 있게 해줍니다. 이 오버로드에 다음 매개변수를 전달해야 합니다: 입력 스트림, 시작 페이지, 끝 페이지, 출력 스트림. 시작 페이지와 끝 페이지 사이의 범위로 지정된 페이지는 입력 스트림에서 추출되어 출력 스트림에 저장됩니다. 다음 코드 스니펫은 스트림을 사용하여 두 숫자 사이의 PDF 페이지를 추출하는 방법을 보여줍니다.

```csharp
public static void Extract_ArrayPDFPages_FilePaths()
{
    // PdfFileEditor 객체 생성
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // 페이지 추출
    pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## 스트림을 사용하여 PDF 페이지 배열 추출하기

PDF 스트림에서 페이지 배열을 추출하여 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드의 적절한 오버로드를 사용하여 출력 스트림에 저장할 수 있습니다. 페이지 범위를 추출하지 않고 특정 페이지 집합을 추출하려는 경우에도 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드를 사용할 수 있습니다. 먼저 추출해야 할 모든 페이지 번호가 포함된 정수 배열을 만들어야 합니다. 이 [Extract](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 메서드의 오버로드는 다음 매개변수를 사용합니다: 입력 스트림, 추출할 페이지의 정수 배열 및 출력 스트림. 다음 코드 스니펫은 스트림을 사용하여 PDF 페이지를 추출하는 방법을 보여줍니다.

```csharp
public static void Extract_ArrayPDFPages_Streams()
{
    // PdfFileEditor 객체 생성
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // 스트림 생성
    using (FileStream inputStream = new FileStream(_dataDir + "MultiplePages.pdf", FileMode.Open))
    using (FileStream outputStream = new FileStream(_dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
    {
        int[] pagesToExtract = new int[] { 1, 2 };
        // 페이지 추출
        pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
    }
}
```