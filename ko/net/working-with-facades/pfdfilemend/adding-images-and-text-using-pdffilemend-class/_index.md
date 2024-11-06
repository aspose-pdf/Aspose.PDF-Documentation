```
---
title: 이미지 및 텍스트 추가
type: docs
weight: 10
url: ko/net/adding-images-and-text-using-pdffilemend-class/
description: 이 섹션에서는 PdfFileMend 클래스를 사용하여 이미지 및 텍스트를 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 클래스는 지정된 위치에 기존 PDF 문서에 이미지와 텍스트를 추가하는 데 도움이 될 수 있습니다.
``` It provides two methods with the names [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) and [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). 

두 가지 메서드를 제공합니다. 이름은 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 및 [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index)입니다. [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 메서드는 JPG, GIF, PNG 및 BMP 형식의 이미지를 추가할 수 있게 해줍니다. [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) 메서드는 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 클래스 형식의 인수를 받아 기존 PDF 파일에 추가합니다. 이미지와 텍스트는 왼쪽 하단과 오른쪽 상단 점의 좌표로 지정된 사각형 영역에 추가될 수 있습니다. 이미지를 추가할 때 이미지 파일 경로 또는 이미지 파일의 스트림을 지정할 수 있습니다. 이미지나 텍스트를 추가할 페이지 번호를 지정하기 위해 두 메서드는 페이지 번호 인수를 제공합니다. 따라서 지정된 위치에 이미지를 추가할 수 있을 뿐만 아니라 지정된 페이지에도 추가할 수 있습니다.

이미지는 PDF 문서 내용의 중요한 부분입니다. 이미지를 조작하는 것은 PDF 파일을 다루는 사람들에게 일반적인 요구 사항입니다. 이 문서에서는 [Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)의 도움으로 기존 PDF 파일에서 이미지를 어떻게 조작할 수 있는지 탐색해보겠습니다. [Aspose.PDF for .NET](/pdf/net/)의 모든 이미지 관련 작업은 이 기사에 통합되어 있습니다.

## 구현 세부 사항

[Aspose.Pdf.Facades 네임스페이스](https://reference.aspose.com/pdf/net/aspose.pdf.facades)를 사용하면 기존 PDF 파일에 새로운 이미지를 추가할 수 있습니다. 기존 이미지를 교체하거나 제거할 수도 있습니다. PDF 파일은 이미지로 변환할 수도 있습니다. 개별 페이지를 각각 하나의 이미지로 변환하거나 전체 PDF 파일을 하나의 이미지로 변환할 수 있습니다. JPEG, BMP, PNG 및 TIFF 등의 형식을 지원합니다. PDF 파일에서 이미지를 추출할 수도 있습니다. 이러한 작업을 구현하기 위해 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)의 네 가지 클래스를 사용할 수 있습니다. 즉, [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 및 [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter)입니다.

## 이미지 작업

이 섹션에서는 이러한 이미지 작업에 대해 자세히 살펴보겠습니다. 우리는 관련된 클래스와 메서드의 사용을 보여주기 위해 코드 스니펫도 볼 것입니다. 먼저, 기존 PDF 파일에 이미지를 추가하는 방법을 살펴보겠습니다. 우리는 [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 클래스의 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 메서드를 사용하여 새 이미지를 추가할 수 있습니다. 이 메서드를 사용하면 이미지를 추가하고자 하는 페이지 번호를 지정할 수 있을 뿐만 아니라 이미지의 위치도 지정할 수 있습니다.

## 기존 PDF 파일에 이미지 추가 (Facades)

당신은 [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 클래스의 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) 메서드를 사용할 수 있습니다. [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) 메서드는 추가할 이미지, 이미지를 추가할 페이지 번호 및 좌표 정보를 필요로 합니다. 그런 다음 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 예제에서는 imageStream을 사용하여 페이지에 이미지를 추가합니다:

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

![Add Image](/pdf/net/images/add_image1.png)

[CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1)를 사용하면 하나의 이미지를 다른 이미지 위에 겹쳐 놓을 수 있습니다.
```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // 이미지를 스트림에 로드
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // 출력 파일 저장
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

![Add Image](/pdf/net/images/add_image2.png)

이미지를 PDF 파일에 저장하는 여러 가지 방법이 있습니다. 다음 예제에서 그 중 하나를 보여드리겠습니다:

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // 이미지를 스트림에 로드
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // 출력 파일 저장
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Load image into stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## 기존 PDF 파일에 텍스트 추가하기 (facades)

여러 가지 방법으로 텍스트를 추가할 수 있습니다. 첫 번째를 고려하십시오. 우리는 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)를 가져와 페이지에 추가합니다. 그 후, 우리는 왼쪽 하단 모서리의 좌표를 지정하고, 그런 다음 페이지에 텍스트를 추가합니다.

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

어떻게 보이는지 확인하십시오:

![텍스트 추가](/pdf/net/images/add_text.png)

두 번째 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)를 추가하는 방법. 추가적으로, 우리는 텍스트가 맞아야 하는 직사각형을 지정합니다.

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // save the output file
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```
세 번째 예제는 지정된 페이지에 텍스트를 추가할 수 있는 기능을 제공합니다. 예제에서는 문서의 1페이지와 3페이지에 캡션을 추가합니다.

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("Welcome to Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // 출력 파일 저장
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```