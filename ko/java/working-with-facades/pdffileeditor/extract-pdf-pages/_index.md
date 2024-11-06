---
title: PDF 페이지 추출
type: docs
weight: 20
url: ko/java/extract-pdf-pages/
description: 이 섹션에서는 PdfFileEditor 클래스를 사용하여 com.aspose.pdf.facades로 PDF 페이지를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 파일 경로를 사용하여 두 숫자 사이의 PDF 페이지 추출

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 클래스의 [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 메서드를 사용하면 PDF 파일에서 지정된 범위의 페이지를 추출할 수 있습니다. 이 오버로드를 사용하면 디스크에서 PDF 파일을 조작하면서 페이지를 추출할 수 있습니다. 이 오버로드는 다음 매개 변수를 필요로 합니다: 입력 파일 경로, 시작 페이지, 끝 페이지, 그리고 출력 파일 경로. 시작 페이지에서 끝 페이지까지의 페이지가 추출되며 출력은 디스크에 저장됩니다. 다음 코드 스니펫은 파일 경로를 사용하여 두 숫자 사이의 PDF 페이지를 추출하는 방법을 보여줍니다.

```java
  public static void Extract_PDFPages_FilePaths() {
        // PdfFileEditor 객체 생성
        PdfFileEditor pdfEditor = new PdfFileEditor();

        // 페이지 추출
        pdfEditor.Extract(_dataDir + "MultiplePages.pdf", 1, 3, _dataDir + "ExtractPagesBetweenNumbers_out.pdf");
    }
```


## PDF 페이지 배열 추출

일련의 페이지가 아니라 특정 페이지 집합을 추출하려는 경우, [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 메서드를 사용하여 가능합니다. 먼저 추출할 모든 페이지 번호로 정수 배열을 생성해야 합니다. 이 [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 메서드의 오버로드는 다음과 같은 매개변수를 사용합니다: 입력 PDF 파일, 추출할 페이지의 정수 배열, 출력 PDF 파일. 다음 코드 스니펫은 파일 경로를 사용하여 PDF 페이지를 추출하는 방법을 보여줍니다.

```java
 public static void Extract_ArrayPDFPages_FilePaths() {
        // PdfFileEditor 객체 생성
        PdfFileEditor pdfEditor = new PdfFileEditor();
        int[] pagesToExtract = new int[] { 1, 2 };
        // 페이지 추출
        pdfEditor.Extract(_dataDir + "Extract.pdf", pagesToExtract, _dataDir + "ExtractArrayOfPages_out.pdf");
    }
```


## 스트림을 사용하여 두 숫자 사이의 PDF 페이지 추출

[PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) 클래스의 [추출](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 메서드를 사용하면 스트림을 사용하여 페이지 범위를 추출할 수 있습니다. 이 오버로드에 다음 매개변수를 전달해야 합니다: 입력 스트림, 시작 페이지, 끝 페이지 및 출력 스트림. 시작 페이지와 끝 페이지 사이의 범위에 의해 지정된 페이지가 입력 스트림에서 추출되어 출력 스트림에 저장됩니다. 다음 코드 스니펫은 스트림을 사용하여 두 숫자 사이의 PDF 페이지를 추출하는 방법을 보여줍니다.

```java
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


## 스트림을 사용하여 PDF 페이지 배열 추출하기

페이지 배열은 PDF 스트림에서 추출되어 [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 메서드의 적절한 오버로드를 사용하여 출력 스트림에 저장될 수 있습니다. 페이지 범위를 추출하지 않고 특정 페이지를 추출하려면, [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 메서드를 사용하여 그렇게 할 수 있습니다. 먼저 추출할 모든 페이지 번호를 포함하는 정수 배열을 만들어야 합니다. 이 [Extract](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#extract-java.io.InputStream-int:A-java.io.OutputStream-) 메서드의 오버로드는 입력 스트림, 추출할 페이지의 정수 배열 및 출력 스트림과 같은 매개변수를 받습니다. 아래의 코드 스니펫은 스트림을 사용하여 PDF 페이지를 추출하는 방법을 보여줍니다.

```java
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