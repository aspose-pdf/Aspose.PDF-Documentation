---
title: PDF를 PDF/A 형식으로 변환
linktitle: PDF를 PDF/A 형식으로 변환
type: docs
weight: 100
url: /ko/java/convert-pdf-to-pdfa/
lastmod: "2021-11-19"
description: 이 주제에서는 Aspose.PDF를 사용하여 PDF 파일을 PDF/A 호환 PDF 파일로 변환하는 방법을 설명합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Java**를 사용하면 PDF 파일을 PDF/A 호환 PDF 파일로 변환할 수 있습니다. 그러나 그 전에 파일을 검증해야 합니다. 이 글에서는 그 방법을 설명합니다.

PDF/A 적합성을 검증하기 위해 Adobe Preflight을 따르고 있음을 유의하십시오. 시장의 모든 도구는 PDF/A 적합성에 대한 자체 "표현"을 가지고 있습니다. 참조를 위해 [PDF/A 검증 도구](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results)에 대한 이 기사를 확인하십시오. 우리는 Aspose.PDF가 PDF 파일을 생성하는 방법을 확인하기 위해 Adobe 제품을 선택했으며, Adobe는 PDF와 관련된 모든 것의 중심에 있기 때문입니다.

PDF를 PDF/A 호환 파일로 변환하기 전에 validate 메서드를 사용하여 PDF를 검증하십시오.
 검증 결과는 XML 파일에 저장되고, 이 결과는 convert 메서드로도 전달됩니다. [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) 열거형을 사용하여 변환할 수 없는 요소에 대한 작업을 지정할 수도 있습니다.

## PDF를 PDF/A_1b로 변환

다음 코드 스니펫은 PDF 파일을 PDF/A-1b 규격의 PDF로 변환하는 방법을 보여줍니다.

```java
// 문서 열기
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// PDF/A 규격 문서로 변환
// 변환 과정 중에 검증도 수행됩니다.
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// 출력 문서 저장
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

검증만 수행하려면 다음 코드 줄을 사용하십시오:

```java
// 문서 열기
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// PDF/A-1a에 대해 PDF 검증
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("Valid");
} else {
    System.out.println("Non valid");
}
document.close();
```

## PDF to PDF/A_3b Conversion

[Aspose.PDF for Java 9.3.0](https://downloads.aspose.com/pdf/java)부터 API는 PDF 파일을 PDF/A_3b 형식으로 변환하는 것도 지원합니다.

```java
// 문서 열기
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// PDF/A 호환 문서로 변환
// 변환 과정에서 유효성 검사도 수행됩니다
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// 출력 문서 저장
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## PDF to PDF/A_3a Conversion

[Aspose.PDF for Java 10.6.0](https://downloads.aspose.com/pdf/java)부터 API는 PDF 파일을 PDF/A_3a 형식으로 변환하는 것도 지원합니다.

```java
// 문서 열기
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// PDF/A 호환 문서로 변환
// 변환 과정에서 유효성 검사도 수행됩니다
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// 출력 문서 저장
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```


## PDF to PDF/A_2a Conversion

[Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java) 릴리스부터, API는 PDF 파일을 PDF/A3 형식으로 변환하는 기능을 제공합니다.

```java
    public static void ConvertPDFtoPDFa2a() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // PDF/A 준수 문서로 변환
        // 변환 과정 중에 유효성 검사도 수행됩니다
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // 출력 문서 저장
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## PDF to PDF/A_3U Conversion

Aspose.PDF for Java 17.2.0 릴리스부터, API는 PDF 파일을 PDF/A_3U 형식으로 변환하는 기능을 제공합니다.

```java
    public static void ConvertPDFtoPDFa3u() {
        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // PDF/A 준수 문서로 변환
        // 변환 과정 중에 유효성 검사도 수행됩니다
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // 출력 문서 저장
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```


## PDF/A-3 만들기 및 XML 파일 첨부

Aspose.PDF for Java는 PDF 파일을 PDF/A 형식으로 변환하는 기능을 제공하며, PDF 문서에 파일을 첨부하는 기능도 지원합니다. PDF/A 준수 형식에 파일을 첨부해야 하는 경우, com.aspose.pdf.PdfFormat 열거형에서 PDF_A_3A 값을 사용하는 것을 권장합니다. PDF/A_3a는 PDF/A 준수 파일에 첨부 파일로 어떤 파일 형식이든 첨부할 수 있는 기능을 제공합니다. 하지만, 파일을 첨부한 후에는 메타데이터를 수정하기 위해 다시 PDF-3a 형식으로 변환해야 합니다. 다음 코드 스니펫을 확인하십시오.

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // PDF 파일에 페이지 추가
        doc.getPages().add();
        // XML 파일 로드
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "샘플 xml 파일");
        // 문서의 첨부 파일 컬렉션에 첨부 파일 추가
        doc.getEmbeddedFiles().add(fileSpecification);
        // PDF/A_3a 변환 수행
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* or PDF_A_3B */, ConvertErrorAction.Delete);
        // 최종 PDF 파일 저장
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```


{{% alert color="primary" %}}
**PDF를 PDF/A로 온라인 변환 시도**

Aspose.PDF for Java는 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)라는 온라인 무료 애플리케이션을 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 PDF/A로 무료 앱](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}