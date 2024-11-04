---
title: PDF 파일에서 첨부 파일 추출
type: docs
weight: 10
url: /java/extract-attachments/
description: 이 섹션에서는 PdfExtractor 클래스를 사용하여 pdf에서 첨부 파일을 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

[com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame)의 추출 기능 중 주요 범주 중 하나는 첨부 파일 추출입니다.
 이 카테고리는 첨부 파일을 추출하는 데 도움이 되는 메서드 세트를 제공할 뿐만 아니라 첨부 파일 관련 정보를 제공할 수 있는 메서드도 제공합니다. 즉, [GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) 및 [GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) 메서드는 각각 첨부 정보와 첨부 이름을 제공합니다. 첨부 파일을 추출한 다음 얻기 위해 [ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) 및 [GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--) 메서드를 사용합니다.

다음 코드 스니펫은 PdfExtractor 메서드를 사용하는 방법을 보여줍니다:

```java
  public static void ExtractAttachments() {
        PdfExtractor pdfExtractor = new PdfExtractor();
        pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

        // 첨부 파일 추출
        pdfExtractor.extractAttachment();

        // 첨부 파일 이름 가져오기
        if (pdfExtractor.getAttachNames().size() > 0) {
            System.out.println("추출 및 저장 중...");
            // 추출된 첨부 파일 가져오기
            pdfExtractor.getAttachment(_dataDir);
        }
    }
```