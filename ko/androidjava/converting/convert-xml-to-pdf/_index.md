---
title: XML을 PDF로 변환
linktitle: XML을 PDF로 변환
type: docs
weight: 320
url: /ko/androidjava/convert-xml-to-pdf/
lastmod: "2026-07-01"
description: Aspose.PDF 라이브러리는 XML을 PDF로 변환하는 여러 방법을 제공합니다. XslFoLoadOptions를 사용할 수 있거나 잘못된 파일 구조로도 수행할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

구조화된 데이터를 저장하는 데 사용되는 XML 형식입니다. 변환하는 방법은 여러 가지가 있습니다. <abbr title="Extensible Markup Language">XML</abbr> Aspose.PDF에서 PDF로.

XSL-FO 표준을 기반으로 하는 XML 문서를 사용하는 옵션을 고려하십시오.

## XSL-FO를 PDF로 변환

XSL-FO 파일을 PDF로 변환하는 작업은 다음을 사용하여 구현할 수 있습니다 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 다음과 같은 객체 [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions),  하지만 때때로 잘못된 파일 구조를 만날 수 있습니다. 

```java
// Convert XML to PDF
    public void convertXMLtoPDF() {
        // Initialize document object
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // Save resultant PDF file
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
    ```
    
