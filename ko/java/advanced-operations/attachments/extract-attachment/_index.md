---
title: PDF에서 첨부 파일 추출
linktitle: 첨부파일 추출
type: docs
weight: 50
url: /java/extract-attachment/
description: Aspose.PDF를 사용하여 Java의 PDF 문서에서 포함된 파일 및 파일 첨부 주석을 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에서 포함된 파일 하나 또는 모두 추출
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 첨부 파일을 추출하는 방법을 설명합니다. 여기에는 이름이 지정된 단일 첨부 파일 추출, 포함된 모든 파일을 출력 폴더에 저장, 파일 메타데이터 읽기, 페이지의 FileAttachment 주석에서 콘텐츠 내보내기 등이 포함됩니다.
---
Aspose.PDF for Java는 첨부 파일이 문서에 저장되는 방식에 따라 여러 추출 흐름을 지원합니다.


## 
이름별로 단일 첨부 파일 추출



PDF에 포함된 특정 파일 하나를 저장해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
필요한 첨부 파일 이름을 찾을 때까지 포함된 파일 컬렉션을 반복합니다.
1. 첨부 스트림을 출력 파일에 복사하고 추출 후 중지합니다.


```java
public static void extractSingleAttachment(Path inputFile, String attachmentName, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Extracting attachment: " + attachmentName);

        boolean attachmentFound = false;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            if (attachmentName.equals(fileSpecification.getName())) {
                try (InputStream inputStream = fileSpecification.getContents();
                     OutputStream outputStream = Files.newOutputStream(outputFile)) {
                    inputStream.transferTo(outputStream);
                }
                System.out.println("Attachment extracted successfully");
                attachmentFound = true;
                break;
            }
        }

        if (!attachmentFound) {
            throw new IllegalArgumentException("Attachment '" + attachmentName + "' not found in PDF");
        }
    }
}
```

## 
포함된 파일 매개변수 인쇄



이 도우미 메서드는 [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/) 개체에 저장된 메타데이터를 인쇄합니다.


1. 
파일 매개변수 객체가 존재하는지 확인하세요.

1. 
사용 가능한 체크섬, 생성 날짜, 수정 날짜 및 크기 값을 읽습니다.
1. 값을 콘솔에 인쇄합니다.


```java
public static void printFileParams(FileParams params) {
    if (params != null) {
        try {
            System.out.println("CheckSum: " + params.getCheckSum());
        } catch (Exception ex) {
            System.out.println("CheckSum: null");
        }
        System.out.println("Creation Date: " + params.getCreationDate());
        System.out.println("Modification Date: " + params.getModDate());
        System.out.println("Size: " + params.getSize());
    }
}
```

## 
포함된 모든 첨부 파일을 추출합니다.



PDF에 포함된 모든 파일을 출력 디렉터리에 기록해야 하는 경우 이 예를 사용하세요.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
포함된 파일 컬렉션을 반복하고 각 항목에 대한 안전한 출력 파일 이름을 결정합니다.
1. 메타데이터를 인쇄하고 각 첨부 파일 스트림을 저장한 다음 모든 파일을 내보낼 때까지 계속합니다.


```java
public static void extractAttachments(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Total files: " + document.getEmbeddedFiles().size());

        int fileIndex = 1;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            String fileName = fileSpecification.getName();
            if (fileName == null || fileName.isBlank()) {
                fileName = fileSpecification.getUnicodeName();
            }
            if (fileName == null || fileName.isBlank()) {
                fileName = "attachment_" + fileIndex + ".bin";
            }

            System.out.println("Name: " + fileName);
            System.out.println("Description: " + fileSpecification.getDescription());
            System.out.println("Mime Type: " + fileSpecification.getMIMEType());
            printFileParams(fileSpecification.getParams());

            Path outputPath = outputDir.resolve(fileName);
            try (InputStream inputStream = fileSpecification.getContents();
                 OutputStream outputStream = Files.newOutputStream(outputPath)) {
                inputStream.transferTo(outputStream);
            }
            fileIndex++;
        }
    }
}
```

## 
파일 첨부 주석 추출



파일이 포함된 파일 컬렉션을 통해서만 첨부되는 것이 아니라 페이지 주석을 통해 첨부되는 경우 이 예를 사용하십시오.


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
페이지에서 첫 번째 [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/)을 찾으세요.
1. 파일 사양을 읽고, 내용을 내보내고, 대상 경로를 인쇄합니다.

```java
public static void extractFileAttachmentAnnotation(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        FileAttachmentAnnotation fileAttachment = null;
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FileAttachment) {
                fileAttachment = (FileAttachmentAnnotation) annotation;
                break;
            }
        }

        if (fileAttachment == null) {
            System.out.println("File attachment annotation not found.");
            return;
        }

        FileSpecification fileSpecification = fileAttachment.getFile();
        System.out.println("File name: " + fileSpecification.getName());

        Path outputPath = outputDir.resolve("extracted-" + fileSpecification.getName());
        try (InputStream inputStream = fileSpecification.getContents();
             OutputStream outputStream = Files.newOutputStream(outputPath)) {
            inputStream.transferTo(outputStream);
        }

        System.out.println("Extracted to: " + outputPath);
    }
}
```
