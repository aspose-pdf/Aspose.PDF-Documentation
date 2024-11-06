```
---
title: 텍스트 및 이미지 스탬프 추가
type: docs
weight: 20
url: ko/net/add-text-and-image-stamp/
description: 이 섹션에서는 PdfFileStamp 클래스를 사용하여 Aspose.PDF Facades로 텍스트 및 이미지 스탬프를 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일의 모든 페이지에 텍스트 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 모든 페이지에 텍스트 스탬프를 추가할 수 있습니다.
``` In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.  
  
텍스트 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 당신은 또한 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) 메소드를 사용하여 텍스트 스탬프를 생성해야 합니다. 원점, 회전, 배경 등과 같은 다른 속성도 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 객체를 사용하여 설정할 수 있습니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 메소드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메소드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```csharp
 public static void AddTextStampOnAllPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Stamp stamp = new Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddTextStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## 특정 페이지에 텍스트 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 특정 페이지에 텍스트 스탬프를 추가할 수 있도록 합니다. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

텍스트 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 당신은 또한 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) 메서드를 사용하여 텍스트 스탬프를 만들어야 합니다. You can set other attributes like origin, rotation, background etc.  
다른 속성으로 원점, 회전, 배경 등을 설정할 수 있습니다. 
[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 개체도 사용.
``` PDF 파일의 특정 페이지에 텍스트 스탬프를 추가하려면 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 속성도 설정해야 합니다. 이 속성은 스탬프를 추가하려는 페이지의 번호를 포함하는 정수 배열이 필요합니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 아래 코드 스니펫은 PDF 파일의 특정 페이지에 텍스트 스탬프를 추가하는 방법을 보여줍니다.

```csharp
 public static void AddTextStampOnParticularPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Set particular pages
            stamp.Pages = new int[] { 2 };

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddTextStamp-Page_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## PDF 파일의 모든 페이지에 이미지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 모든 페이지에 이미지 스탬프를 추가할 수 있게 해줍니다. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.  
이미지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 당신은 또한 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) 메서드를 사용하여 이미지 스탬프를 생성해야 합니다. 원점, 회전, 배경 등과 같은 다른 속성들을 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 객체를 사용하여 설정할 수 있습니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 모든 페이지에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Set particular pages
            stamp.Pages = new int[] { 2 };

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddImageStamp-Page_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
### 스탬프로 추가할 때 이미지 품질 제어

이미지를 스탬프 객체로 추가할 때 이미지의 품질을 제어할 수도 있습니다. 이 요구 사항을 충족하기 위해 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스에 Quality 속성이 추가되었습니다. 이는 이미지의 품질을 백분율로 나타냅니다 (유효한 값은 0..100입니다).

## PDF 파일의 특정 페이지에 이미지 스탬프 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스는 PDF 파일의 특정 페이지에 이미지 스탬프를 추가할 수 있도록 합니다. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

이미지 스탬프를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 및 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 객체를 생성해야 합니다. 당신은 또한 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) 메서드를 사용하여 이미지 스탬프를 생성해야 합니다. You can set other attributes like origin, rotation, background etc.

다음과 같은 다른 속성을 설정할 수 있습니다: origin, rotation, background 등. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 객체도 사용합니다. PDF 파일의 특정 페이지에 이미지 스탬프를 추가하려면 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 클래스의 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 속성을 설정해야 합니다. 이 속성은 스탬프를 추가하고 싶은 페이지의 번호를 포함하는 정수 배열이 필요합니다. 그런 다음 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 메서드를 사용하여 PDF 파일에 스탬프를 추가할 수 있습니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 특정 페이지에 이미지 스탬프를 추가하는 방법을 보여줍니다.

```csharp
 public static void AddImageStampOnParticularPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddImageStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```