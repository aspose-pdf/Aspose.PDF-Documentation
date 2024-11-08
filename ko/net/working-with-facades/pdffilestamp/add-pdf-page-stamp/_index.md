---
title: PDF 페이지 스탬프 추가
type: docs
weight: 10
url: /ko/net/add-pdf-page-stamp/
description: 이 섹션은 PdfFileStamp 클래스를 사용하여 Aspose.PDF Facades를 다루는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일의 모든 페이지에 PDF 페이지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 모든 페이지에 PDF 페이지 스탬프를 추가할 수 있도록 합니다. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

PDF 페이지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 문서에 PDF 페이지 스탬프를 생성하려면 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 메서드를 사용해야 합니다. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 객체를 사용하여 원점, 회전, 배경 등과 같은 다른 속성을 설정할 수 있습니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지에 PDF 페이지 스탬프를 추가하는 방법을 보여줍니다.

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

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 특정 페이지에 PDF 페이지 스탬프를 추가할 수 있도록 해줍니다. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. PDF 페이지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 당신은 또한 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 PDF 페이지 스탬프를 생성해야 합니다. You can set other attributes like origin, rotation, background etc.  
다른 속성들을 설정할 수 있습니다, 원점, 회전, 배경 등. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 객체 또한 사용합니다. As you want to add PDF page stamp on particular pages of the PDF file, you also need to set the [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) property of the [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) class. This property requires an integer array containing numbers of the pages on which you want to add the stamp. Then you can add the stamp in the PDF file using [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. The following code snippet shows you how to add PDF page stamp on particular pages in a PDF file.

PDF 파일의 특정 페이지에 PDF 페이지 스탬프를 추가하려면 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 속성을 설정해야 합니다. 이 속성은 스탬프를 추가하려는 페이지의 번호를 포함하는 정수 배열이 필요합니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 특정 페이지에 PDF 페이지 스탬프를 추가하는 방법을 보여줍니다.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }

        // Add PDF Page Numbers
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```
## PDF 파일에 페이지 번호 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일에 페이지 번호를 추가할 수 있도록 합니다. In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class. 

페이지 번호를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 객체를 생성해야 합니다. If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) property of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class.

페이지 번호를 "Page X of N"처럼 표시하려면, 여기서 X는 현재 페이지 번호이고 N은 PDF 파일의 총 페이지 수입니다. 먼저 [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 클래스의 [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) 속성을 사용하여 페이지 수를 가져와야 합니다. 현재 페이지 번호를 얻기 위해서는 **#** 기호를 원하는 곳에 텍스트에 사용할 수 있습니다. 페이지 번호 텍스트는 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 클래스를 사용하여 형식을 지정할 수 있습니다. 특정 번호에서 페이지 번호 매기기를 시작하려면 [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber) 속성을 설정할 수 있습니다. 파일에 페이지 번호를 추가할 준비가 되면 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) 메서드를 호출해야 합니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에 페이지 번호를 추가하는 방법을 보여줍니다.

```csharp
 public static void AddPageNumberInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Get total number of pages
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Create formatted text for page number
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Set starting number for first page; you might want to start from 2 or more
            fileStamp.StartingNumber = 1;

            // Add page number
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
### 사용자 지정 번호 스타일

PdfFileStamp 클래스는 PDF 문서 내에 페이지 번호 정보를 스탬프 개체로 추가하는 기능을 제공합니다. 이 릴리스 이전에는 클래스가 1,2,3,4만 페이지 번호 스타일로 지원했습니다. 그러나 PDF 문서 내에 페이지 번호 스탬프를 배치할 때 사용자 지정 번호 스타일을 사용하려는 일부 고객의 요구가 있었습니다. 이 요구 사항을 충족하기 위해 [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) 속성이 도입되었으며, 이는 [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) 열거형의 값을 수락합니다. 아래에 이 열거형에서 제공하는 값이 나와 있습니다.

- LettersLowercase
- LettersUppercase
- NumeralsArabic
- NumeralsRomanLowercase
- NumeralsRomanUppercase

```csharp
 public static void AddCustomPageNumberInPdfFile()
        {
            // PdfFileStamp 객체 생성
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 문서 열기
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 총 페이지 수 가져오기
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // 페이지 번호에 대한 서식 있는 텍스트 생성
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // 로마 숫자 대문자로 번호 스타일 지정
            fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

            // 첫 페이지의 시작 번호 설정; 2부터 시작할 수도 있음
            fileStamp.StartingNumber = 1;

            // 페이지 번호 추가
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // 업데이트된 PDF 파일 저장
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // fileStamp 닫기
            fileStamp.Close();
        }
```