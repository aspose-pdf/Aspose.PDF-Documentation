```
---
title: PdfExtractor를 사용하여 이미지 추출
type: docs
weight: 20
url: ko/net/extract-images/
description: 이 섹션은 PdfExtractor 클래스를 사용하여 Aspose.PDF Facades로 이미지를 추출하는 방법을 설명합니다.
lastmod: "2021-07-15"
---

## 전체 PDF에서 파일로 이미지 추출 (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스는 PDF 파일에서 이미지를 추출할 수 있게 해줍니다.
``` First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.

우선, [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메소드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출하여 메모리에 모든 이미지를 추출합니다. 이미지가 추출되면 [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 사용하여 해당 이미지를 얻을 수 있습니다. while 루프를 사용하여 모든 추출된 이미지를 반복해야 합니다. 이미지를 디스크에 저장하려면 파일 경로를 인수로 사용하는 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드의 오버로드를 호출할 수 있습니다. 다음 코드 스니펫은 전체 PDF에서 파일로 이미지를 추출하는 방법을 보여줍니다.

```csharp
   public static void ExtractImagesWholePDF()
        {
            // 입력 PDF 열기
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // 모든 이미지 추출
            pdfExtractor.ExtractImage();

            // 모든 추출된 이미지 가져오기
            while (pdfExtractor.HasNextImage())
                pdfExtractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
```
## Extract Images from the Whole PDF to Streams (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스는 PDF 파일에서 이미지를 스트림으로 추출할 수 있도록 합니다. 
우선, [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다.
``` 그 후, 모든 이미지를 메모리로 추출하기 위해 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출합니다. 이미지가 추출되면, [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드의 도움으로 이러한 이미지를 가져올 수 있습니다. while 루프를 사용하여 추출된 모든 이미지를 반복해야 합니다. 이미지를 스트림에 저장하기 위해 Stream을 인수로 받는 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드의 오버로드를 호출할 수 있습니다. 다음 코드 조각은 전체 PDF에서 이미지를 스트림으로 추출하는 방법을 보여줍니다.

```csharp
    public static void ExtractImagesWholePDFStreams()
        {
            // 입력 PDF 열기
            PdfExtractor pdfExtractor = new PdfExtractor();
            pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

            // 이미지 추출
            pdfExtractor.ExtractImage();
            // 모든 추출된 이미지 가져오기
            while (pdfExtractor.HasNextImage())
            {
                // 메모리 스트림으로 이미지 읽기
                MemoryStream memoryStream = new MemoryStream();
                pdfExtractor.GetNextImage(memoryStream);

                // 디스크에 저장하거나 다른 용도로 사용
                FileStream fileStream = new
                FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
                memoryStream.WriteTo(fileStream);
                fileStream.Close();
            }
        }
```
## Extract Images from a Particular Page of a PDF (Facades)

특정 페이지의 PDF 파일에서 이미지를 추출할 수 있습니다. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) and [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties to the particular page you want to extract images from.

그렇게 하려면 [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) 및 [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) 속성을 이미지 추출을 원하는 특정 페이지로 설정해야 합니다. 먼저, [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) * 및 [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) 속성을 설정해야 합니다. 그 후, [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출하여 모든 이미지를 메모리에 추출합니다. 이미지가 추출되면, [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 사용하여 이미지를 얻을 수 있습니다. while 루프를 사용하여 추출된 모든 이미지를 반복해야 합니다. 이미지를 디스크에 저장하거나 스트림에 저장할 수 있습니다. [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드의 적절한 오버로드를 호출하기만 하면 됩니다. 다음 코드 스니펫은 PDF의 특정 페이지에서 스트림으로 이미지를 추출하는 방법을 보여줍니다.

```csharp
public static void ExtractImagesParticularPage()
{
    // 입력 PDF 열기
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // 추출하려는 페이지 번호에 StartPage 및 EndPage 속성 설정
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // 이미지 추출
    pdfExtractor.ExtractImage();
    // 추출된 이미지 가져오기
    while (pdfExtractor.HasNextImage())
    {
        // 메모리 스트림에 이미지를 읽습니다.
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // 원한다면 디스크에 쓰거나 다른 용도로 사용합니다.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## Extract Images from a Range of Pages of a PDF (Facades)

PDF 파일의 여러 페이지 범위에서 이미지를 추출할 수 있습니다. In order to do that, you need to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)  and [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties to the range of pages you want to extract images from.

그렇게 하려면 [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) 및 [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) 속성을 이미지 추출을 원하는 페이지 범위로 설정해야 합니다. 첫째로, [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인드해야 합니다. Secondly, you have to set [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage)  and [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) properties.

둘째로, [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) 및 [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) 속성을 설정해야 합니다. 그런 다음 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출하여 모든 이미지를 메모리로 추출합니다. 이미지가 추출되면 [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 사용하여 해당 이미지를 얻을 수 있습니다. while 루프를 사용하여 추출된 모든 이미지를 반복해야 합니다. 이미지를 디스크에 저장하거나 스트림으로 저장할 수 있습니다. [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드의 적절한 오버로드를 호출하기만 하면 됩니다. 다음 코드 조각은 PDF의 여러 페이지에서 스트림으로 이미지를 추출하는 방법을 보여줍니다.

```csharp
public static void ExtractImagesRangePages()
{
    // 입력 PDF 열기
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // StartPage 및 EndPage 속성을 페이지 번호로 설정하여
    // 이미지 추출을 원하는 페이지
    pdfExtractor.StartPage = 2;
    pdfExtractor.EndPage = 2;

    // 이미지 추출
    pdfExtractor.ExtractImage();
    // 추출된 이미지 가져오기
    while (pdfExtractor.HasNextImage())
    {
        // 메모리 스트림으로 이미지 읽기
        MemoryStream memoryStream = new MemoryStream();
        pdfExtractor.GetNextImage(memoryStream);

        // 디스크에 쓰거나 원하는 경우 사용하십시오.
        FileStream fileStream = new
        FileStream(_dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create);
        memoryStream.WriteTo(fileStream);
        fileStream.Close();
    }
}
```
## 이미지 추출 모드 사용하여 이미지 추출 (파사드)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스는 PDF 파일에서 이미지를 추출할 수 있게 해줍니다. Aspose.PDF는 두 가지 추출 모드를 지원합니다. 첫 번째는 PDF 문서에 실제로 사용된 이미지를 추출하는 ActuallyUsedImage입니다. ```
Second mode is [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode) which extract the images defined in the resources of the PDF document (default extraction mode).
```

두 번째 모드는 PDF 문서의 리소스에 정의된 이미지를 추출하는 [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode)입니다 (기본 추출 모드). First, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method.  
먼저, [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메소드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음, [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode) 속성을 사용하여 이미지 추출 모드를 지정하세요. 그런 다음 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출하여 지정한 모드에 따라 모든 이미지를 메모리로 추출합니다. 이미지가 추출되면, [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 사용하여 이미지를 얻을 수 있습니다. while 루프를 사용하여 모든 추출된 이미지를 반복해야 합니다. 이미지를 디스크에 저장하려면 파일 경로를 인수로 취하는 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드의 오버로드를 호출할 수 있습니다.

다음 코드 스니펫은 ExtractImageMode 옵션을 사용하여 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.
```csharp
public static void ExtractImagesImageExtractionMode()
{
    // 입력 PDF 열기
    PdfExtractor extractor = new PdfExtractor();
    extractor.BindPdf(_dataDir + "sample_cats_dogs.pdf");

    // 이미지 추출 모드 지정
    //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
    extractor.ExtractImageMode = ExtractImageMode.DefinedInResources;

    // 이미지 추출 모드에 따라 이미지 추출
    extractor.ExtractImage();

    // 추출된 모든 이미지 가져오기
    while (extractor.HasNextImage())
    {
        extractor.GetNextImage(_dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
    }
}
```

PDF가 텍스트 또는 이미지를 포함하는지 확인하려면 다음 코드 스니펫을 사용하십시오:

```csharp
public static void CheckIfPdfContainsTextOrImages()
        {
            // 문서에서 추출된 텍스트를 보관할 memoryStream 객체 인스턴스화
            MemoryStream ms = new MemoryStream();
            // PdfExtractor 객체 인스턴스화
            PdfExtractor extractor = new PdfExtractor();

            // 입력 PDF 문서를 추출기에 바인딩
            extractor.BindPdf(_dataDir + "FilledForm.pdf");
            // 입력 PDF 문서에서 텍스트 추출
            extractor.ExtractText();
            // 추출된 텍스트를 텍스트 파일에 저장
            extractor.GetText(ms);
            // MemoryStream 길이가 1 이상인지 확인

            bool containsText = ms.Length >= 1;

            // 입력 PDF 문서에서 이미지 추출
            extractor.ExtractImage();

            // while 루프에서 HasNextImage 메서드 호출. 이미지가 끝나면 루프 종료
            bool containsImage = extractor.HasNextImage();

            // 이제 이 PDF가 텍스트만 포함하는지, 이미지만 포함하는지 확인

            if (containsText && !containsImage)
                Console.WriteLine("PDF는 텍스트만 포함합니다.");
            else if (!containsText && containsImage)
                Console.WriteLine("PDF는 이미지만 포함합니다.");
            else if (containsText && containsImage)
                Console.WriteLine("PDF는 텍스트와 이미지를 모두 포함합니다.");
            else if (!containsText && !containsImage)
                Console.WriteLine("PDF는 텍스트나 이미지를 포함하지 않습니다.");
        }

    }
```