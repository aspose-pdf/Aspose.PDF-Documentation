---
title: Java를 사용하여 PDF에 이미지 추가
linktitle: 이미지 추가
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: Java에서 기존 PDF 파일에 이미지를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Java를 사용하여 기존 PDF 파일에 이미지 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 이미지를 추가하는 방법을 보여줍니다. 고정된 좌표에 이미지 배치하기, 낮은 수준의 페이지 연산자를 통해 이미지 추가하기, 접근성을 위한 대체 텍스트 설정하기, Flate 압축으로 이미지 데이터 삽입하기 등을 다룹니다.
---
Aspose.PDF for Java는 높은 수준의 이미지 배치와 낮은 수준의 연산자 기반 그리기를 모두 지원합니다.


## 
페이지 좌표가 포함된 이미지 추가



PDF 페이지의 고정 위치에 이미지를 배치해야 할 때 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지를 추가하세요.

1. 
소스 이미지 경로와 대상 직사각형을 사용하여 `page.addImage()`을 호출하세요.
1. 생성된 PDF 파일을 저장합니다.


```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## 
페이지 연산자를 사용하여 이미지 추가



페이지 연산자를 통해 이미지 배치 및 크기 조정에 대한 낮은 수준의 제어가 필요한 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 소스 이미지 스트림을 엽니다.

1. 
페이지 리소스에 이미지를 추가하고 대상 사각형을 계산합니다.
1. 필요한 그래픽 연산자를 작성하고 문서를 저장합니다.


```java
public static void addImageUsingOperators(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream);
        XImage xImage = resourcesImages.get_Item(resourcesImages.size());

        Rectangle rectangle = new Rectangle(
                0,
                0,
                page.getMediaBox().getWidth(),
                (page.getMediaBox().getWidth() * xImage.getHeight()) / xImage.getWidth(),
                true);

        page.getContents().add(new GSave());

        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLX() + (page.getMediaBox().getHeight() - rectangle.getHeight()) / 2);
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```

## 
이미지 추가 및 대체 텍스트 설정



이미지에 화면 판독기에 대한 접근성 메타데이터가 포함되어야 하는 경우 이 예를 사용하세요.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 페이지에 이미지를 추가하세요.

1. 
페이지 리소스에서 삽입된 [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/)를 가져옵니다.
1. 대체 텍스트를 설정하고 PDF를 저장합니다.


```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        boolean result = xImage.trySetAlternativeText("Alternative text for image", page);
        if (result) {
            System.out.println("Text has been added successfuly");
        }
        document.save(outputFile.toString());
    }
}
```

## 
Flate 압축으로 이미지 추가



Flate 압축을 사용하여 이미지 데이터를 포함하려는 경우 이 예를 사용하십시오.


1. 
새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 만들고 이미지 스트림을 엽니다.

1. 
`ImageFilterType.Flate`을 사용하여 페이지 리소스에 이미지를 추가합니다.
1. 페이지 연산자를 통해 이미지를 그리고 결과를 저장합니다.

```java
public static void addImageToPdfWithFlateCompression(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream, ImageFilterType.Flate);

        page.getContents().add(new GSave());

        Rectangle rectangle = new Rectangle(0, 0, 600, 600, true);
        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY());

        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```
