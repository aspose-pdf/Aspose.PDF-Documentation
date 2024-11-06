```
---
title: PDF 파일 변환
type: docs
weight: 30
url: ko/net/convert-pdf-file/
description: 이 섹션에서는 PdfConverter 클래스를 사용하여 Aspose.PDF Facades로 PDF 파일을 변환하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 페이지를 다양한 이미지 형식으로 변환 (Facades)

PDF 페이지를 다양한 이미지 형식으로 변환하려면 [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 PDF 파일을 엽니다.
``` 그 후, 초기화 작업을 위해 [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) 메서드를 호출해야 합니다. 그런 다음, [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) 메서드를 사용하여 모든 페이지를 순회할 수 있습니다. [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) 메서드는 특정 페이지의 이미지를 생성할 수 있게 해줍니다. 이 메서드에 ImageFormat을 전달하여 JPEG, GIF 또는 PNG 등 특정 유형의 이미지를 생성해야 합니다. 마지막으로, [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) 클래스의 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) 메서드를 호출하십시오. 다음 코드 스니펫은 PDF 페이지를 이미지로 변환하는 방법을 보여줍니다.

```csharp
public static void ConvertPdfPagesToImages01()
{
    // Create PdfConverter object
    PdfConverter converter = new PdfConverter();

    // Bind input pdf file
    converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

    // Initialize the converting process
    converter.DoConvert();

    // Check if pages exist and then convert to image one by one
    while (converter.HasNextImage())
        converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

    // Close the PdfConverter object
    converter.Close();
}
```
다음 코드 스니펫에서는 몇 가지 매개 변수를 변경하는 방법을 보여드리겠습니다. [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype)으로 프레임 'CropBox'를 설정합니다. 또한 [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution)을 변경하여 인치당 점 수를 지정할 수 있습니다. 다음은 [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - 폼 프레젠테이션 모드입니다. 그런 다음 변환 시작 페이지 번호가 설정된 [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage)를 지정합니다. 범위를 설정하여 마지막 페이지를 지정할 수도 있습니다.

```csharp
  public static void ConvertPdfPagesToImages02()
        {
            // PdfConverter 객체 생성
            PdfConverter converter = new PdfConverter();

            // 입력 pdf 파일 바인딩
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // 변환 프로세스 초기화
            converter.DoConvert();
            converter.CoordinateType = PageCoordinateType.CropBox;
            converter.Resolution = new Devices.Resolution(600);
            converter.FormPresentationMode = Devices.FormPresentationMode.Production;
            converter.StartPage = 2;
            // converter.EndPage = 3;
            // 페이지가 존재하는지 확인한 후 하나씩 이미지를 변환합니다.
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // PdfConverter 객체 닫기
            converter.Close();
        }
```

## See also

Aspose.PDF for .NET은 PDF 문서를 다양한 형식으로 변환할 수 있으며, 다른 형식에서 PDF로 변환할 수도 있습니다. 또한, Aspose.PDF 변환기의 앱을 사용하여 Aspose.PDF 변환의 품질을 확인하고 결과를 온라인으로 볼 수 있습니다. 작업 해결을 위한 [변환](/pdf/net/converting/) 섹션을 학습하십시오.