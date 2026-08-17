---
title: Java에서 PDF를 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2026-06-16"
description: Aspose.PDF를 사용하여 Java에서 PDF 페이지를 TIFF, BMP, EMF, JPEG, PNG, GIF 및 SVG 파일로 렌더링하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: PDF 페이지를 Java에서 TIFF, PNG, JPEG, GIF, BMP, EMF 및 SVG로 변환
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일을 일반적인 이미지 형식으로 변환하는 방법을 설명합니다. 문서 전체 TIFF 내보내기, 이미지 장치를 사용한 페이지별 래스터 생성, PNG 내보내기 중 선택적 글꼴 대체 및 `SvgSaveOptions`을 사용한 SVG 출력을 다룹니다.
---

Aspose.PDF for Java는 형식별 장치 옵션을 사용하여 PDF 페이지를 래스터 및 벡터 이미지 형식으로 렌더링할 수 있습니다.


## 
PDF를 BMP로 변환



PDF 페이지를 BMP 이미지로 렌더링해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
300 DPI의 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/)을 사용하여 [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/)을 만듭니다.

1. 
`document.getPages()`을 반복하고 각 페이지에 대해 `device.process(...)`을 호출하세요.

1. 
생성된 BMP 이미지를 번호가 매겨진 출력 경로에 저장합니다.


```java
public static void convertPdfToBmp(Path inputFile, Path outputPrefix) {
       try (Document document = new Document(inputFile.toString())) {
           BmpDevice device = new BmpDevice(new Resolution(300));
           for (int page = 1; page <= document.getPages().size(); page++) {
               device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "bmp"));
           }
       }
       System.out.println(inputFile + " converted into " + outputPrefix);
   }
```

## 
PDF를 EMF로 변환



PDF 페이지를 EMF 벡터 이미지로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
300 DPI의 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/)을 사용하여 [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/)을 만듭니다.

1. 
페이지를 반복하고 각 페이지에 대해 `device.process(...)`을 호출하세요.

1. 
EMF 출력을 번호가 매겨진 파일 경로에 저장합니다.


```java
public static void convertPdfToEmf(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        EmfDevice device = new EmfDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "emf"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
PDF를 GIF로 변환



PDF 페이지를 GIF 이미지로 변환해야 하는 경우 이 예를 사용하세요.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
300 DPI의 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/)로 [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/)을 만듭니다.

1. 
페이지를 반복하고 `device.process(...)`을 호출하여 각 페이지를 렌더링합니다.

1. 
번호가 매겨진 출력 경로에 GIF 파일을 저장합니다.


```java
public static void convertPdfToGif(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        GifDevice device = new GifDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "gif"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
PDF를 JPEG로 변환



PDF 페이지를 JPEG 이미지로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
300 DPI의 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/)을 사용하여 [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/)을 만듭니다.

1. 
페이지를 반복하고 `device.process(...)`을 호출하여 각 페이지를 JPEG로 래스터화합니다.

1. 
JPEG 출력 파일을 번호가 매겨진 경로에 저장합니다.


```java
public static void convertPdfToJpeg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        JpegDevice device = new JpegDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "jpeg"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
PDF를 PNG로 변환



PDF 페이지를 PNG 이미지로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
300 DPI의 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/)을 사용하여 [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/)을 만듭니다.

1. 
페이지를 반복하고 각 PDF 페이지에 대해 `device.process(...)`을 호출하세요.

1. 
PNG 출력을 번호가 매겨진 파일 경로에 저장합니다.


```java
public static void convertPdfToPng(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
기본 글꼴 대체를 사용하여 PDF를 PNG로 변환



렌더링 시 누락된 글리프에 대해 대체 글꼴을 사용해야 하는 경우 이 예제를 사용하세요.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
300 DPI의 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/)로 [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/)을 만듭니다.

1. 
`document.setAbsentFontTryToSubstitute(true)`을 활성화하면 누락된 글리프가 렌더링 중에 대체 글꼴로 대체될 수 있습니다.

1. 
페이지를 렌더링하고 PNG 파일을 저장합니다.


```java
public static void convertPdfToPngWithDefaultFont(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        document.setAbsentFontTryToSubstitute(true);
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
PDF를 SVG로 변환



PDF 페이지를 SVG 그래픽으로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
원시 `.svg` 출력이 필요한 경우 [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/)을 만들고 ZIP 압축을 비활성화합니다.

1. 
`setTreatTargetFileNameAsDirectory(true)`을 활성화하면 페이지별 SVG 출력을 대상 경로 아래에 구성할 수 있습니다.

1. 
SVG 출력을 저장합니다.


```java
public static void convertPdfToSvg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        SvgSaveOptions saveOptions = new SvgSaveOptions();
        saveOptions.setCompressOutputToZipArchive(false);
        saveOptions.setTreatTargetFileNameAsDirectory(true);
        document.save(outputPrefix + ".svg", saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## 
PDF를 TIFF로 변환



하나 이상의 PDF 페이지를 TIFF로 내보내야 하는 경우 이 예를 사용하십시오.


1. 
[`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/)을 만들고 압축, 색 농도 및 빈 페이지 동작을 구성합니다.

1. 
300 DPI의 [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/)과 준비된 TIFF 설정을 사용하여 [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/)을 만듭니다.

1. 
페이지를 렌더링하고 TIFF 출력을 저장합니다.

```java
public static void convertPdfToTiff(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.LZW);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setSkipBlankPages(false);

        TiffDevice tiffDevice = new TiffDevice(new Resolution(300), tiffSettings);
        tiffDevice.process(document, outputPrefix + ".tiff");
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```
