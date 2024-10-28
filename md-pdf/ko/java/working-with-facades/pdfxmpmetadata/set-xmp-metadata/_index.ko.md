---
title: 기존 PDF의 XMP 메타데이터 설정 - facades
type: docs
weight: 20
url: /java/set-xmp-metadata/
description: 이 섹션에서는 PdfXmpMetadata 클래스를 사용하여 Aspose.PDF Facades로 XMP 메타데이터를 설정하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDF 파일에 XMP 메타데이터를 설정하려면 [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) 객체를 생성하고 [bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) 메서드를 사용하여 PDF 파일을 바인딩해야 합니다.
 You can use setByDefaultMetadataProperties(..) method of the [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) class to add different properties. Finally, call the [save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) method of [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) class.

다음 코드 스니펫은 PDF 파일에 XMP 메타데이터를 추가하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}