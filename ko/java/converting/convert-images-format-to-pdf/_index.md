---
title: Java에서 이미지 형식을 PDF로 변환
linktitle: 이미지를 PDF로 변환
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-16"
description: Aspose.PDF를 사용하여 Java에서 BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR 및 기타 이미지 형식을 PDF로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java에서 이미지를 PDF로 변환하는 방법
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 여러 이미지 형식을 PDF로 변환하는 방법을 설명합니다. 새로운 PDF 페이지에 이미지를 직접 배치하는 방법과 CGM, SVG 및 CDR 입력에 대한 파일 유형별 로드 옵션을 다룹니다.
---
Aspose.PDF for Java는 다양한 래스터 및 벡터 이미지 형식을 PDF 문서로 변환할 수 있습니다.


## 
BMP를 PDF로 변환



BMP 이미지를 PDF 문서에 배치해야 하는 경우 이 예를 사용하십시오.


1. 
출력 PDF를 보관할 빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만듭니다.

1. 
[`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 추가하고 `page.addImage(...)`으로 BMP를 배치합니다.
1. 래스터 콘텐츠가 PDF 페이지 영역을 채우도록 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)으로 대상 이미지 직사각형을 정의합니다.

1. 
출력 PDF 파일을 저장합니다.


```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## 
CGM을 PDF로 변환



CGM 그래픽 파일을 PDF로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
파일 경로와 [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/)을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 CGM 소스를 엽니다.
1. 문서를 로드하는 동안 Aspose.PDF가 CGM 그래픽 스트림을 해석하도록 합니다.

1. 
변환된 PDF를 대상 출력 경로에 저장합니다.


```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
DICOM을 PDF로 변환



의료 DICOM 이미지를 PDF 문서로 래핑해야 하는 경우 이 예를 사용하십시오.


1. 
PDF 출력을 위해 빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만듭니다.
1. [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) 객체를 생성하고 해당 [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/)을 `Dicom`으로 설정하고 소스 파일 경로를 할당합니다.

1. 
[`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 추가하고 DICOM 이미지를 페이지 단락 컬렉션에 추가합니다.

1. 
결과를 PDF로 저장하세요.


```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
직접 문서 로딩을 통해 EMF를 PDF로 변환



기본 EMF 로드 경로를 통해 EMF 파일을 PDF로 변환해야 하는 경우 이 예를 사용하십시오.

1. 빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만들고 EMF 소스를 바이너리 스트림으로 엽니다.

1. 
[`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 추가하고 여백을 지워 EMF 아트워크가 전체 페이지 영역을 차지할 수 있도록 합니다.

1. 
[`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/)을 만들고 여기에 EMF 스트림을 바인딩한 다음 페이지 단락 컬렉션에 추가합니다.

1. 
출력 PDF 파일을 저장합니다.


```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
대체 작업 흐름을 사용하여 EMF를 PDF로 변환

대체 설정 또는 페이지 구성 흐름을 사용하여 EMF 컨텐츠를 변환해야 하는 경우 이 예를 사용하십시오.


1. 
Aspose.Imaging을 사용하여 EMF 소스를 로드하고 PDF 배치 전에 메모리 내 PNG 스트림으로 렌더링합니다.

1. 
빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만들고 [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 추가합니다.

1. 
중간 바이트 스트림에서 [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/)을 생성하고 페이지에 추가합니다.

1. 
변환된 PDF를 저장합니다.

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## GIF를 PDF로 변환



PDF 페이지에 GIF 이미지를 추가해야 하는 경우 이 예를 사용하세요.


1. 
PDF 출력을 위해 빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만듭니다.

1. 
[`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 추가하고 `page.addImage(...)`로 GIF를 배치하세요.

1. 
이미지가 페이지 영역을 채우도록 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 사용하여 배치 경계를 정의합니다.
1. 출력 PDF를 저장합니다.


```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
JPEG를 PDF로 변환



JPEG 이미지를 한 페이지짜리 PDF로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
출력 PDF에 대해 빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만듭니다.

1. 
[`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 추가하고 `page.addImage(...)`으로 JPEG 이미지를 삽입합니다.
1. 래스터 이미지가 페이지 좌표에 매핑되는 방식을 제어하려면 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 사용하세요.

1. 
생성된 PDF 파일을 저장합니다.


```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
PNG를 PDF로 변환



PNG 이미지를 PDF 문서로 묶어야 하는 경우 이 예를 사용하십시오.


1. 
변환 출력을 위해 빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만듭니다.
1. [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 추가하고 그 위에 `page.addImage(...)`을 사용하여 PNG 이미지를 배치합니다.

1. 
[`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)을 사용하여 페이지 캔버스에 맞춰 이미지 크기를 조정하세요.

1. 
출력 파일을 저장합니다.


```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
SVG를 PDF로 변환



PDF 문서 내에서 SVG 아트웍을 렌더링해야 하는 경우 이 예를 사용하십시오.

1. 파일 경로와 [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/)을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 SVG 소스를 엽니다.

1. 
Aspose.PDF가 SVG 마크업을 구문 분석하고 로드 중에 해당 PDF 그래픽 모델을 생성하도록 합니다.

1. 
PDF 출력을 대상 파일 경로에 저장합니다.


```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
TIFF를 PDF로 변환



TIFF 이미지를 PDF로 변환해야 하는 경우 이 예를 사용하십시오.

1. PDF 출력을 위해 빈 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)을 만듭니다.

1. 
[`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)을 추가하고 `page.addImage(...)`으로 TIFF 이미지를 배치합니다.

1. 
TIFF 콘텐츠가 페이지 좌표에 매핑되도록 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/)으로 배치 영역을 정의합니다.

1. 
결과를 PDF로 저장하세요.


```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
CDR을 PDF로 변환

CorelDRAW CDR 파일을 PDF로 변환해야 하는 경우 이 예를 사용하십시오.


1. 
파일 경로와 [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/)을 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 생성자에 전달하여 CDR 소스를 엽니다.

1. 
Aspose.PDF가 CorelDRAW 콘텐츠를 PDF 문서 모델에 로드하도록 합니다.

1. 
변환된 PDF 파일을 요청된 출력 경로에 저장합니다.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
