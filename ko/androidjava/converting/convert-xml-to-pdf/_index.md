---
title: XML을 PDF로 변환하기
linktitle: XML을 PDF로 변환하기
type: docs
weight: 320
url: ko/androidjava/convert-xml-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF 라이브러리는 XML을 PDF로 변환하는 여러 가지 방법을 제공합니다. XslFoLoadOptions를 사용하거나 잘못된 파일 구조로 이 작업을 수행할 수 있습니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

온라인으로 시도해보세요. 이 링크에서 Aspose.PDF 변환의 품질을 확인하고 결과를 온라인으로 볼 수 있습니다 [products.aspose.app/pdf/conversion/xml-to-pdf](https://products.aspose.app/pdf/conversion/xml-to-pdf)

{{% /alert %}}

XML 형식은 구조화된 데이터를 저장하는 데 사용됩니다. Aspose.PDF에서 <abbr title="Extensible Markup Language">XML</abbr>을 PDF로 변환하는 여러 가지 방법이 있습니다.

XSL-FO 표준을 기반으로 하는 XML 문서를 사용하는 옵션을 고려하십시오.

## XSL-FO를 PDF로 변환하기

XSL-FO 파일을 PDF로 변환하는 것은 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) 객체와 [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions)를 사용하여 구현할 수 있지만, 때때로 잘못된 파일 구조를 만날 수 있습니다.
 
// XML을 PDF로 변환
    public void convertXMLtoPDF() {
        // 문서 객체 초기화
        String pdfDocumentFileName = new File(fileStorage,"XML-to-PDF.pdf").toString();
        String xmlDocumentFileName = new File(fileStorage,"Conversion/employees.xml").toString();
        String xsltDocumentFileName = new File(fileStorage, "Conversion/employees.xslt").toString();

        try {
            XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);
            document = new Document(xmlDocumentFileName,options);
            // 결과 PDF 파일 저장
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }    
    ```