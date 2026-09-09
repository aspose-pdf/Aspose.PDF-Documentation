---
title: Java에서 PDF 파일 최적화
linktitle: PDF 최적화
type: docs
weight: 30
url: /java/optimize-pdf/
description: Aspose.PDF를 사용하여 Java에서 PDF 파일 크기를 최적화, 압축 및 줄이는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 리소스를 압축하고 파일 크기를 줄입니다.
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 파일을 최적화하는 방법을 설명합니다. 전체 문서 최적화, 리소스 압축, 이미지 품질 감소, 사용하지 않는 개체 및 스트림 제거, 중복 스트림 연결, 글꼴 포함 취소, 주석 및 양식 병합, 회색조 변환 및 Flate 이미지 압축을 다룹니다.
---
Java용 Aspose.PDF는 `Document.optimize`, `optimizeResources` 및 `OptimizationOptions`을 통해 최적화 기능을 제공합니다.


## 
일반 문서 최적화로 PDF 최적화



Aspose.PDF가 내장된 전체 문서 최적화 루틴을 적용하도록 하려면 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
문서에서 `optimize()`으로 전화하세요.
1. 최적화된 파일을 저장하고 원본 크기와 출력 크기를 비교하세요.


```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
리소스를 최적화하여 PDF 크기 줄이기



이 예에서는 개별 옵션을 수동으로 구성하지 않고 리소스 수준 최적화에 중점을 둡니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
내부 리소스를 최적화하려면 `optimizeResources()`을 실행하세요.
1. 결과를 저장하고 입력 및 출력 파일 크기를 인쇄합니다.


```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
PDF의 모든 이미지 압축



이미지가 많은 문서에 더 작은 파일 크기가 필요하고 일부 이미지 품질 저하가 허용되는 경우 이 접근 방식을 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[최적화 옵션](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/)을 만들고 필요한 품질 수준으로 이미지 압축을 활성화하세요.
1. 해당 설정으로 문서 리소스를 최적화하세요.

1. 
최적화된 파일을 저장하고 파일 크기를 비교하세요.


```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
PDF에서 사용되지 않는 개체 제거



이 예에서는 편집 또는 병합 후 문서 구조에 남아 있을 수 있는 사용되지 않는 개체를 제거합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.
1. [최적화 옵션](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/)을 생성하고 사용하지 않는 개체 제거를 활성화합니다.

1. 
리소스를 최적화하고 업데이트된 파일을 저장합니다.

1. 
원본 및 축소된 파일 크기를 인쇄합니다.


```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
PDF에서 사용하지 않는 스트림 제거



문서에서 더 이상 참조하지 않는 스트림 데이터를 삭제하려는 경우 이 접근 방식을 사용하십시오.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
사용하지 않는 스트림을 제거하려면 [최적화 옵션](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/)을 구성하세요.

1. 
리소스를 최적화하고, 출력 문서를 저장하고, 파일 크기를 비교하세요.


```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
PDF에서 중복 스트림 연결



이 예에서는 동일한 콘텐츠가 한 번만 저장될 수 있도록 반복되는 스트림을 중복 제거합니다.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/)를 생성하고 중복 스트림 연결을 활성화합니다.

1. 
리소스를 최적화하고, 출력 문서를 저장하고, 파일 크기를 인쇄합니다.


```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
PDF에서 글꼴 포함 취소



출력에 포함된 글꼴 데이터를 유지하는 것보다 파일 크기를 줄이는 것이 더 중요한 경우 이 옵션을 사용하십시오.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
글꼴 포함을 취소하려면 [최적화 옵션](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/)을 구성하세요.

1. 
리소스를 최적화하고, 문서를 저장하고, 파일 크기를 비교하세요.


```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
PDF에서 주석 병합



이 예에서는 주석이 더 이상 대화형 개체로 유지되지 않도록 주석을 정적 페이지 콘텐츠로 변환합니다.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
각 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 및 해당 [주석](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 컬렉션을 반복합니다.

1. 
모든 주석을 병합하고 업데이트된 문서를 저장합니다.


```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
PDF 양식 필드 병합



채울 수 있는 양식 필드를 배포 또는 보관하기 전에 고정 콘텐츠로 만들어야 하는 경우 이 접근 방식을 사용하십시오.

1. 원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
문서에 양식 위젯이 포함되어 있는지 확인하세요.

1. 
[WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/)으로 표시되는 각 [필드](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/)를 평면화합니다.

1. 
출력 파일을 저장하고 파일 크기를 인쇄합니다.


```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
PDF를 회색조로 변환

이 예에서는 각 페이지를 회색조로 변경하여 색상 복잡성을 줄이고 보관 또는 인쇄 작업 흐름에 대한 출력을 표준화하는 데 도움이 됩니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
문서의 각 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)를 반복합니다.

1. 
모든 페이지에서 `makeGrayscale()`을 호출하고 출력 파일을 저장합니다.


```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## 
FlateDecode 이미지 압축 사용

PDF 리소스 최적화 중에 Flate 기반 압축을 이미지에 적용하려는 경우 이 패턴을 사용합니다.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
[최적화 옵션](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/)을 생성하고 이미지 인코딩을 [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`으로 설정합니다.

1. 
문서 리소스를 최적화하고 출력 파일을 저장합니다.


```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## 
원본 및 최적화된 파일 크기 인쇄

이 도우미 메서드는 소스 파일과 최적화된 출력 파일 간의 크기 차이를 보고합니다.


1. 
입력 파일의 크기를 읽습니다.

1. 
출력 파일의 크기를 읽습니다.

1. 
단일 상태 메시지에 두 값을 모두 인쇄합니다.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
