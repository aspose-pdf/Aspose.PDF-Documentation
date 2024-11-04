---
title: PDF 페이지 스탬프 추가
type: docs
weight: 10
url: /java/add-pdf-page-stamp/
description: 이 섹션에서는 PdfFileStamp 클래스를 사용하여 Aspose.PDF Facades를 사용하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일의 모든 페이지에 PDF 페이지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일의 모든 페이지에 PDF 페이지 스탬프를 추가할 수 있게 합니다.
 In order to add PDF 페이지 스탬프를 추가하려면, 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스와 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 객체를 생성해야 합니다. You also need to create the PDF page stamp using [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)  method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class. You can set other attributes like origin, rotation, background etc. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) object as well. Then you can add the stamp in the PDF file using [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add PDF page stamp on all pages in a PDF file.

```csharp
public static void AddPageStampOnAllPages()
        {
            // PdfFileStamp 객체 생성
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 문서 열기
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 스탬프 생성
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // PDF 파일에 스탬프 추가
            fileStamp.AddStamp(stamp);

            // 업데이트된 PDF 파일 저장
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // fileStamp 닫기
            fileStamp.Close();
        }
```

## 특정 페이지에 PDF 페이지 스탬프 추가하기

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일의 특정 페이지에 PDF 페이지 스탬프를 추가할 수 있도록 합니다.
 In order to add PDF 페이지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 및 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 객체를 생성해야 합니다. 당신은 또한 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) 메서드를 사용하여 PDF 페이지 스탬프를 생성해야 합니다. You can set other attributes like origin, rotation, background etc.  
다른 속성들, 예를 들어 원점, 회전, 배경 등을 설정할 수 있습니다. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 객체도 사용합니다. PDF 파일의 특정 페이지에 PDF 페이지 스탬프를 추가하려면 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 클래스의 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) 속성을 설정해야 합니다. 이 속성은 스탬프를 추가하고자 하는 페이지의 번호를 포함하는 정수 배열이 필요합니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 특정 페이지에 PDF 페이지 스탬프를 추가하는 방법을 보여줍니다.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // PdfFileStamp 객체 생성
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 문서 열기
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 스탬프 생성
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // PDF 파일에 스탬프 추가
            fileStamp.AddStamp(stamp);

            // 업데이트된 PDF 파일 저장
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // fileStamp 닫기
            fileStamp.Close();
        }

        // PDF 페이지 번호 추가
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## PDF 파일에 페이지 번호 추가하기 (facades)

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 파일에 페이지 번호를 추가할 수 있게 해줍니다.
 In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.

페이지 번호를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 객체를 생성해야 합니다. 페이지 번호를 "Page X of N" 형식으로 표시하려면, 여기서 X는 현재 페이지 번호이고 N은 PDF 파일의 총 페이지 수입니다. 먼저 [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 클래스의 getNumberOfpages 속성을 사용하여 페이지 수를 얻어야 합니다. 현재 페이지 번호를 얻으려면 텍스트 어디에나 **#** 기호를 사용할 수 있습니다. [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) 클래스를 사용하여 페이지 번호 텍스트를 서식화할 수 있습니다. 특정 번호에서 페이지 번호를 시작하려면 setStartingNumber 속성을 설정할 수 있습니다. 파일에 페이지 번호를 추가할 준비가 되면 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 addPageNumber 메서드를 호출해야 합니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스의 Save 메서드를 사용하여 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일에 페이지 번호를 추가하는 방법을 보여줍니다.
```java
 public static void AddPageNumberInPdfFile() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 총 페이지 수 가져오기
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // 페이지 번호에 대한 서식 있는 텍스트 생성
        FormattedText formattedText = new FormattedText("Page # of " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // 첫 페이지의 시작 번호 설정; 2 이상으로 시작할 수 있음
        fileStamp.setStartingNumber(1);

        // 페이지 번호 추가
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // 업데이트된 PDF 파일 저장
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // fileStamp 닫기
        fileStamp.close();
    }
```


### 사용자 정의 번호 매기기 스타일

The [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 클래스는 PDF 문서 안에 페이지 번호 정보를 스탬프 객체로 추가하는 기능을 제공합니다. 이번 릴리스 이전에는 클래스가 페이지 번호 스타일로 1,2,3,4만 지원했습니다. 그러나 일부 고객들로부터 PDF 문서 안에 페이지 번호 스탬프를 배치할 때 사용자 정의 번호 스타일을 사용하고 싶다는 요구가 있었습니다. 이 요구를 충족하기 위해, [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) 속성이 도입되었으며, 이는 [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) 열거형에서 값을 수용합니다. 아래에 이 열거형에서 제공하는 값들이 명시되어 있습니다.

```java
 public static void AddCustomPageNumberInPdfFile() {
        // PdfFileStamp 객체 생성
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 문서 열기
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 총 페이지 수 가져오기
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // 페이지 번호에 대한 서식 있는 텍스트 생성
        FormattedText formattedText = new FormattedText("Page # of " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // 숫자 스타일을 로마 숫자 대문자로 지정
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // 첫 페이지의 시작 번호 설정; 2 또는 그 이상에서 시작할 수 있음
        fileStamp.setStartingNumber(1);

        // 페이지 번호 추가
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // 업데이트된 PDF 파일 저장
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // fileStamp 닫기
        fileStamp.close();
    }
```