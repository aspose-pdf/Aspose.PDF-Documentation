---
title: 헤더 및 푸터 관리
type: docs
weight: 40
url: /java/manage-header-and-footer/
description: 이 섹션에서는 PdfFileStamp 클래스를 사용하여 Aspose.PDF Facades로 헤더 및 푸터를 관리하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일에 헤더 추가

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일에 헤더를 추가할 수 있게 해줍니다.
 In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.  
헤더를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 객체를 생성해야 합니다. 헤더 텍스트를 포맷하려면 [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) 클래스를 사용하세요. 파일에 헤더를 추가할 준비가 되면 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) 메서드를 호출해야 합니다. 또한 [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) 메서드에서 최소한 상단 여백을 지정해야 합니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 메서드를 사용하여 출력 PDF 파일을 저장하세요. 다음 코드 스니펫은 PDF 파일에 헤더를 추가하는 방법을 보여줍니다.

```java
 public static void AddHeader() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 페이지 번호를 위한 포맷된 텍스트 생성
        FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!", java.awt.Color.YELLOW,
                java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // 헤더 추가
        fileStamp.addHeader(formattedText, 20);

        // 업데이트된 PDF 파일 저장
        fileStamp.save(_dataDir + "AddHeader_out.pdf");

        // fileStamp 닫기
        fileStamp.close();
    }
```

## PDF 파일에 바닥글 추가

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일에 바닥글을 추가할 수 있게 해줍니다.
 In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.  
푸터를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 객체를 생성해야 합니다. [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) 클래스를 사용하여 바닥글 텍스트를 포맷할 수 있습니다. 파일에 바닥글을 추가할 준비가 되면, [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) 메서드를 호출해야 합니다. 또한, [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) 메서드에서 적어도 하단 여백을 지정해야 합니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 메서드를 사용하여 출력 PDF 파일을 저장하세요. 다음 코드 스니핏은 PDF 파일에 바닥글을 추가하는 방법을 보여줍니다.

```java
 public static void AddFooter() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 페이지 번호에 대한 포맷된 텍스트 생성
        FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // 바닥글 추가
        fileStamp.addFooter(formattedText, 10);

        // 업데이트된 PDF 파일 저장
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // fileStamp 닫기
        fileStamp.close();
    }
```

## 기존 PDF 파일의 헤더에 이미지 추가

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일의 헤더에 이미지를 추가할 수 있게 해줍니다.
 헤더에 이미지를 추가하기 위해서는 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 객체를 생성해야 합니다. 그 후, [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) 메서드를 호출해야 합니다. 이 메서드에 이미지를 전달할 수 있습니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 헤더에 이미지를 추가하는 방법을 보여줍니다.

```java
public static void AddImageHeader() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // 헤더 추가
            fileStamp.addHeader(fs, 10);

            // 업데이트된 PDF 파일 저장
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // fileStamp 닫기
        fileStamp.close();
    }
```

## 기존 PDF 파일의 바닥글에 이미지 추가하기

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일의 바닥글에 이미지를 추가할 수 있게 해줍니다.
 이미지를 푸터에 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 객체를 만들어야 합니다. 그 후, [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) 메서드를 호출해야 합니다. 이미지는 [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) 메서드에 전달할 수 있습니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음의 코드 스니펫은 PDF 파일의 푸터에 이미지를 추가하는 방법을 보여줍니다.

```java
    public static void AddImageFooter() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // 푸터 추가
            fileStamp.addFooter(fs, 10);

            // 업데이트된 PDF 파일 저장
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // fileStamp 닫기
        fileStamp.close();
    }
```