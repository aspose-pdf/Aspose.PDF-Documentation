---
title: PDF 파일 변환
type: docs
weight: 20
url: /java/convert-pdf-file/
description: 이 섹션은 PdfConverter 클래스를 사용하여 Aspose.PDF Facades로 PDF 파일을 변환하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 페이지를 다양한 이미지 형식으로 변환하기 (Facades)

PDF 페이지를 다양한 이미지 형식으로 변환하려면 [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) 객체를 생성하고 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-) 메서드를 사용하여 PDF 파일을 열어야 합니다.

그 후, 초기화 작업을 위해 [doConvert](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--) 메서드를 호출해야 합니다.
 그런 다음, [hasNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) 및 [getNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-) 메서드를 사용하여 모든 페이지를 순회할 수 있습니다. getNextImage 메서드는 특정 페이지의 이미지를 생성할 수 있게 해줍니다. 이 메서드에 JPEG, GIF 또는 PNG 등 특정 유형의 이미지 생성을 위해 ImageType을 전달해야 합니다.

마지막으로, [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) 클래스의 close 메서드를 호출하십시오.

다음 코드 스니펫은 PDF 페이지를 이미지로 변환하는 방법을 보여줍니다.

```java
public static void ConvertPdfPagesToImages01() {
        // PdfConverter 객체 생성
        PdfConverter converter = new PdfConverter();

        // 입력 pdf 파일 바인딩
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // 변환 프로세스 초기화
        converter.doConvert();
        
        int count=0;

        // 페이지가 있는지 확인한 후 하나씩 이미지를 변환
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // PdfConverter 객체 닫기
        converter.close();
    }
```

다음 코드 스니펫에서는 몇 가지 매개변수를 변경하는 방법을 보여드립니다. [setCoordinateType](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-)을 사용하여 프레임 [CropBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox)를 설정합니다. 또한, 인치당 점의 수를 지정하여 [setResolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-)을 변경할 수 있습니다. 다음은 [setFormPresentationMode](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-) - 양식 프레젠테이션 모드입니다. 그런 다음 변환 시작 페이지 번호를 설정하는 [setStartPage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-)를 지정합니다. 범위를 설정하여 마지막 페이지를 지정할 수도 있습니다.

```java
public static void ConvertPdfPagesToImages02()
    {
        // PdfConverter 객체 생성
        PdfConverter converter = new PdfConverter();

        // 입력 pdf 파일 바인딩
        converter.bindPdf(_dataDir + "sample.pdf");

        // 변환 프로세스 초기화
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // 페이지가 존재하는지 확인한 후 하나씩 이미지를 변환
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // PdfConverter 객체 닫기
        converter.close();
    }
```