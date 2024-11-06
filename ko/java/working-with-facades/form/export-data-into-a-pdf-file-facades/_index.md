---
title: PDF 파일에서 XML로 데이터 내보내기 (Facades)
type: docs
weight: 20
url: ko/java/export-data-into-a-pdf-file-facades/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 XML로 데이터를 내보내는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 클래스는 exportXml 메서드를 사용하여 PDF 파일에서 XML 파일로 데이터를 내보낼 수 있게 해줍니다. 데이터를 XML로 내보내기 위해서는 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 클래스의 객체를 생성하고, bindPDF 메서드를 사용하여 원본 PDF 양식을 열고, OutputStream 객체를 사용하여 exportXml 메서드를 호출해야 합니다. 마지막으로 OutputStream 객체를 닫고 Form 객체를 폐기할 수 있습니다. 다음 코드 스니펫은 XML 파일로 데이터를 내보내는 방법을 보여줍니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Forms-ExportDataToXMLFromAPDFFile-.java" >}}