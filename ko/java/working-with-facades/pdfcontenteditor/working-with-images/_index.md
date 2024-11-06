---
title: 이미지 작업하기
type: docs
weight: 30
url: ko/java/working-with-image/
description: 이 섹션에서는 PDF와의 인기 있는 작업을 위한 도구 세트인 Aspose.PDF Facades를 사용하여 이미지를 교체하는 방법을 설명합니다.
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF의 특정 페이지에서 이미지 삭제하기 (Facades)

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스는 기존 PDF 파일에서 이미지를 교체할 수 있게 해줍니다.
 [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) 메서드는 이 목표를 달성하는 데 도움이 됩니다. [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스의 객체를 생성하고 bindPdf 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) 메서드를 세 개의 매개변수와 함께 호출해야 합니다: 페이지 번호, 교체할 이미지의 인덱스, 교체할 이미지의 경로.

다음 코드 스니펫은 기존 PDF 파일의 이미지를 교체하는 방법을 보여줍니다.

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## PDF 파일에서 모든 이미지 삭제 (외관)

모든 이미지는 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)의 [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) 메서드를 사용하여 PDF 파일에서 삭제할 수 있습니다. 매개변수가 없는 오버로드된 [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) 메서드를 호출하여 모든 이미지를 삭제한 다음, Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## PDF 파일의 이미지 교체 (외관)

PDF 파일에서 이미지를 교체하려면 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)의 [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) 메서드를 사용할 수 있습니다.

```java
   // 이미지를 교체합니다.
   public static void ReplaceImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        // 페이지 2에서 4로 이미지를 교체합니다.
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        // 파일을 저장합니다.
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```