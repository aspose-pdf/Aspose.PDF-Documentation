---
title: PdfContentEditor를 사용하여 이미지 작업
type: docs
weight: 50
url: ko/net/working-with-images-in-pdf
description: 이 섹션에서는 PdfContentEditor 클래스를 사용하여 Aspose.PDF Facades로 이미지를 추가하고 삭제하는 방법을 설명합니다.
lastmod: "2021-06-24"
---

## PDF의 특정 페이지에서 이미지 삭제 (Facades)

특정 페이지에서 이미지를 삭제하려면 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) 메서드를 pageNumber 및 index 매개변수와 함께 호출해야 합니다. The index 매개변수는 삭제할 이미지의 인덱스인 정수 배열을 나타냅니다. 먼저, [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성한 다음, [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) 메서드를 호출해야 합니다. 그런 다음, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메서드를 사용하여 업데이트된 PDF 파일을 저장할 수 있습니다.

다음 코드 스니펫은 PDF의 특정 페이지에서 이미지를 삭제하는 방법을 보여줍니다.

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## PDF 파일에서 모든 이미지 삭제 (Facades)

모든 이미지는 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) 메서드를 사용하여 PDF 파일에서 삭제할 수 있습니다. [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) 메서드를 호출하여 모든 이미지를 삭제한 다음 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일에서 모든 이미지를 삭제하는 방법을 보여줍니다.

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## PDF 파일에서 이미지 교체 (Facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)를 사용하여 PDF 파일의 이미지를 교체할 수 있으며, 이를 위해 [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) 메서드를 호출하고 결과를 저장합니다.

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```