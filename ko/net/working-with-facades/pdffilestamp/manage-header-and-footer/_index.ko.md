---
title: 헤더 및 푸터 관리
type: docs
weight: 40
url: /net/manage-header-and-footer/
description: 이 섹션에서는 PdfFileStamp 클래스를 사용하여 Aspose.PDF Facades로 헤더 및 푸터를 관리하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일에 헤더 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스는 PDF 파일에 헤더를 추가할 수 있도록 합니다. In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.

헤더를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 객체를 생성해야 합니다. 다음 코드는 PDF 파일에 헤더를 추가하는 방법을 보여줍니다.

```csharp
 public static void AddHeader()
        {
            // PdfFileStamp 객체 생성
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 문서 열기
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 페이지 번호에 대한 서식있는 텍스트 생성
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Yellow,
                System.Drawing.Color.Black,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // 헤더 추가
            fileStamp.AddHeader(formattedText, 10);

            // 업데이트된 PDF 파일 저장
            fileStamp.Save(_dataDir + "AddHeader_out.pdf");

            // fileStamp 닫기
            fileStamp.Close();
        }
```
## Add Footer in a PDF File

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스는 PDF 파일에 바닥글을 추가할 수 있게 해줍니다. In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class.  

푸터를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 객체를 생성해야 합니다. You can format the footer text using [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) class. Once you’re ready to add footer in the file, you need to call [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. You also need to specify at least the bottom margin in the [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) method. Finally, save the output PDF file using [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) method of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) class. The following code snippet shows you how to add footer in a PDF file.

```csharp
 public static void AddFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create formatted text for page number
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Blue,
                System.Drawing.Color.Gray,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Add footer
            fileStamp.AddFooter(formattedText, 10);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddFooter_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```

당신은 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 클래스를 사용하여 바닥글 텍스트를 서식화할 수 있습니다. 파일에 바닥글을 추가할 준비가 되면 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 메서드를 호출해야 합니다. 또한 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 메서드에서 적어도 아래쪽 여백을 지정해야 합니다. 마지막으로 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에 바닥글을 추가하는 방법을 보여줍니다.
## 기존 PDF 파일의 헤더에 이미지 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스는 PDF 파일의 헤더에 이미지를 추가할 수 있도록 합니다. 문서의 헤더에 이미지를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 객체를 생성해야 합니다. 그 다음, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main) 클래스의 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 메소드를 호출해야 합니다. 이미지를 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 메소드에 전달할 수 있습니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메소드를 사용하여 출력 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일의 헤더에 이미지를 추가하는 방법을 보여줍니다.

```csharp
public static void AddImageHeader()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add Header
                fileStamp.AddHeader(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
                // Close fileStamp
                fileStamp.Close();
            }
        }
```
## 기존 PDF 파일의 바닥글에 이미지 추가

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스는 PDF 파일의 바닥글에 이미지를 추가할 수 있습니다. 문서의 바닥글에 이미지를 추가하려면 먼저 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 객체를 생성해야 합니다. 그 후, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 메서드를 호출해야 합니다. 이미지를 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 메서드에 전달할 수 있습니다. 마지막으로, [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 메서드를 사용하여 출력 PDF 파일을 저장하십시오. 다음 코드 스니펫은 PDF 파일의 바닥글에 이미지를 추가하는 방법을 보여줍니다.

```csharp
public static void AddImageFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add footer
                fileStamp.AddFooter(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

                // Close fileStamp
                fileStamp.Close();
            }
        }
```