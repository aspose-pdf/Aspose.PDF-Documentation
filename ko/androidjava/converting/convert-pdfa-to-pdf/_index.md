---
title: PDF/A를 PDF로 변환
linktitle: PDF/A를 PDF로 변환
type: docs
weight: 350
url: /ko/androidjava/convert-pdfa-to-pdf/
lastmod: "2026-07-01"
description: PDF/A를 PDF로 변환하려면 원본 문서의 제한을 제거해야 합니다. Aspose.PDF for Android via Java를 사용하면 이 문제를 쉽고 간단하게 해결할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF/A 문서를 PDF로 변환한다는 것은 제거하는 것을 의미합니다 \u003Cabbr title=\u0022Portable Document Format Archive
\">PDF/A</abbr> 원본 문서에서의 제한. 클래스 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) RemovePdfaCompliance(..) 메서드가 있어 제거합니다
입력/소스 파일의 PDF 규정 준수 정보를.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

문서에 변경을 가하면(예: 페이지 추가) 이 정보도 제거됩니다. 다음 예제에서는 페이지를 추가한 후 출력 문서가 PDF/A 준수를 잃게 됩니다.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```




