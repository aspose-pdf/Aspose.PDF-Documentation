---
title: PDF/A를 PDF로 변환
linktitle: PDF/A를 PDF로 변환
type: docs
weight: 350
url: /ko/androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: PDF/A를 PDF로 변환하려면 원본 문서에서 제한을 제거해야 합니다. Aspose.PDF for Android via Java를 사용하면 이 문제를 쉽게 해결할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF/A 문서를 PDF로 변환한다는 것은 원본 문서에서 <abbr title="Portable Document Format Archive">PDF/A</abbr> 제한을 제거하는 것을 의미합니다. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스는 입력/소스 파일에서 PDF 준수 정보를 제거하는 RemovePdfaCompliance(..) 메서드를 가지고 있습니다.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Document 객체 생성
            document = new Document(pdfaDocumentFileName);

            // PDF/A 준수 정보 제거
            document.removePdfaCompliance();

            // 출력을 XML 형식으로 저장
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```


이 정보는 문서에 변경 사항을 가할 경우 (예: 페이지 추가) 제거됩니다. 다음 예제에서는 페이지 추가 후 출력 문서가 PDF/A 준수성을 잃습니다.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Document 객체 생성
        document = new Document(pdfaDocumentFileName);

        // 새로운 (빈) 페이지를 추가하면 PDF/A 준수 정보가 제거됩니다.
        document.getPages().add();

        // 업데이트된 문서 저장
        document.save(pdfDocumentFileName);
    }
```