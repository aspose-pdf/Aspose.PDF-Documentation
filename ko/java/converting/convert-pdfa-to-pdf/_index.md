---
title: PDF/A를 PDF 형식으로 변환 
linktitle: PDF/A를 PDF 형식으로 변환
type: docs
weight: 110
url: ko/java/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF가 Java 라이브러리를 사용하여 PDF/A 파일을 PDF 문서로 변환하는 방법을 보여줍니다. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/A 문서를 PDF로 변환

PDF/A 문서를 PDF로 변환하는 것은 원본 문서에서 <abbr title="Portable Document Format Archive">PDF/A</abbr> 제한을 제거하는 것을 의미합니다. 클래스 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)는 입력/소스 파일에서 PDF 준수 정보를 제거하기 위한 방법 RemovePdfaCompliance(..)를 가지고 있습니다.

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Document 객체 생성
    Document document = new Document(pdfaDocumentFileName);

    // PDF/A 준수 정보 제거
    document.removePdfaCompliance();

    // XML 형식으로 출력 저장
    document.save(documentFileName);
    document.close();
}
```


이 정보는 문서에 변경 사항을 가할 경우에도 제거됩니다 (예: 페이지 추가). 다음 예제에서는 페이지를 추가한 후 출력 문서가 PDF/A 적합성을 잃습니다.

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Document 객체 생성
    Document document = new Document(pdfaDocumentFileName);

    // 새로운 (빈) 페이지를 추가하면 PDF/A 적합성 정보가 제거됩니다.
    document.getPages().add();

    // 업데이트된 문서 저장
    document.save(documentFileName);
    document.close();
}
```