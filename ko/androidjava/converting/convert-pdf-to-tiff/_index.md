---
title: PDF를 TIFF로 변환
linktitle: PDF를 TIFF로 변환
type: docs
weight: 30
url: /ko/androidjava/convert-pdf-to-tiff/
lastmod: "2026-07-01"
description: 이 문서는 PDF 문서의 페이지를 TIFF 이미지로 변환하는 방법을 설명합니다. Aspose.PDF for Android via Android via Java를 사용하여 모든 페이지 또는 단일 페이지를 TIFF 이미지로 변환하는 방법을 배우게 됩니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java**는 PDF 페이지를 TIFF  이미지로 변환할 수 있게 합니다.

그 [TiffDevice 클래스](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) PDF 페이지를 TIFF 이미지로 변환할 수 있습니다. 이 클래스는 Process라는 메서드를 제공하며, 이를 사용하면 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환할 수 있습니다.

{{% alert color="primary" %}}

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/pdf-to-tiff](https://products.aspose.app/pdf/conversion/pdf-to-tiff)

{{% /alert %}}

## PDF 페이지를 하나의 TIFF 이미지로 변환

Aspose.PDF for Android via Java는 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환하는 방법을 설명합니다:

1. Document 클래스의 객체를 생성합니다.
1. 문서를 변환하려면 Process 메서드를 호출합니다.
1. 출력 파일의 속성을 설정하려면 TiffSettings 클래스를 사용합니다.

다음 코드 스니펫은 모든 PDF 페이지를 단일 TIFF 이미지로 변환하는 방법을 보여줍니다.

```java
public void convertPDFtoTiffSinglePage() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "PDF-to-TIFF.tiff");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, 1, 1, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## 단일 페이지를 TIFF 이미지로 변환

Aspose.PDF for Android via Java는 PDF 파일의 특정 페이지를 TIFF 이미지로 변환할 수 있도록 하며, 변환을 위해 페이지 번호를 인수로 받는 Process(..) 메서드의 오버로드된 버전을 사용합니다. 다음 코드 스니펫은 PDF의 첫 번째 페이지를 TIFF 형식으로 변환하는 방법을 보여줍니다.

```java
public void convertPDFtoTiffAllPages() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // Create Resolution object
        Resolution resolution = new Resolution(300);

        // Create TiffSettings object
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.None);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setShape(ShapeType.Landscape);
        tiffSettings.setSkipBlankPages(false);

        // Create TIFF device
        TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
        File file = new File(fileStorage, "AllPagesToTIFF_out.tif");
        try {
            // Convert a particular page and save the image to stream
            tiffDevice.process(document, file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## 변환 중에 Bradley 알고리즘을 사용합니다.

Aspose.PDF for Android via Java은 LZW 압축을 사용하여 PDF를 TIFF로 변환하는 기능을 지원하고 있으며, AForge를 사용하여 이진화를 적용할 수 있습니다. 하지만 고객 중 한 명이 일부 이미지에 대해 Otsu를 사용하여 임계값을 얻어야 한다고 요청했으며, 따라서 Bradley도 사용하고 싶어 합니다.

```java
public void convertPDFtoTiffBradleyBinarization() {
        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }

    public static void convertPDFtoTIFF_Pixelated() {

        //Not implemented in Aspose.PDF for Android
        throw new NotImplementedException();
    }
```

