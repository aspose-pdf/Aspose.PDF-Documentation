---
title: PDF/3-A 호환 PDF 생성 및 Java로 ZUGFeRD 송장 첨부
linktitle: PDF에 ZUGFeRD 첨부
type: docs
weight: 10
url: /java/attach-zugferd/
description: ZUGFeRD 송장 XML을 PDF에 첨부하고 Java에서 PDF/A-3A로 변환하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 ZUGFeRD 송장 XML을 PDF 문서에 첨부
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF/A-3A 호환 송장 문서를 만드는 방법을 설명합니다. 송장 XML을 포함된 파일로 첨부하고, MIME 유형 및 관련 파일 관계를 설정하고, PDF를 PDF/A-3A로 변환하고, 최종 ZUGFeRD 지원 문서를 저장하는 방법을 다룹니다.
---
ZUGFeRD 스타일 워크플로를 위해 PDF 내에 송장 XML을 패키지해야 하는 경우 `Document` 및 `FileSpecification` API를 사용하세요.


## 
ZUGFeRD 송장 XML을 PDF에 첨부


1. 
원본 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 엽니다.

1. 
XML 송장 파일에 대한 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/)을 만듭니다.

1. 
MIME 유형 및 [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/)을 포함하여 포함된 파일 메타데이터를 설정합니다.
1. 문서 내장 파일 컬렉션에 [파일 사양](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/)을 추가합니다.

1. 
문서를 [Pdf형식](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/)`PDF_A_3A`으로 변환합니다.

1. 
업데이트된 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 저장합니다.

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            String description = "Invoice metadata conforming to ZUGFeRD standard";
            FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

            fileSpecification.setMIMEType("text/xml");
            fileSpecification.setAFRelationship(AFRelationship.Alternative);

            document.getEmbeddedFiles().add("factur", fileSpecification);

            String outputFileName = outputFile.toString();
            String logPath = outputFileName.replace(".pdf", "_log.xml");
            document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
            document.save(outputFile.toString());
        }
        System.out.println("ZUGFeRD invoice attached to " + outputFile);
    }
```
