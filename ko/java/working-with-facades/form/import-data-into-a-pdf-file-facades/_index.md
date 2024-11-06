---
title: PDF 파일로 데이터 가져오기 - facades
type: docs
weight: 10
url: ko/java/import-data-into-a-pdf-file-facades/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 XML로 데이터를 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
---

## XML에서 PDF 파일로 데이터 가져오기 (facades)

[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 클래스는 importXml 메서드를 사용하여 XML 파일의 데이터를 PDF 파일로 가져올 수 있게 합니다. XML에서 데이터를 가져오기 위해서는 Form 클래스의 객체를 생성하고 FileInputStream 객체를 사용하여 importXml 메서드를 호출해야 합니다. 마지막으로, Form 클래스의 save 메서드를 사용하여 PDF 파일을 저장할 수 있습니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "ImportDataFromXmlInToPdf.java" >}}

## FDF에서 PDF 파일로 데이터 가져오기 (facades)

Form 클래스는 importFdf 메서드를 사용하여 FDF 파일의 데이터를 PDF 파일로 가져올 수 있게 합니다.
 데이터를 FDF에서 가져오기 위해서는 Form 클래스의 객체를 생성하고 FileInputStream 객체를 사용하여 importFdf 메서드를 호출해야 합니다. 마지막으로, Form 클래스의 save 메서드를 사용하여 PDF 파일을 저장할 수 있습니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "ImportDataFromFDFIntoPDF.java" >}}

## XFDF에서 PDF 파일로 데이터 가져오기 (페이사드)

Form 클래스는 importXfdf 메서드를 사용하여 XFDF 파일에서 PDF 파일로 데이터를 가져올 수 있게 해줍니다. XFDF에서 데이터를 가져오기 위해서는 Form 클래스의 객체를 생성하고 FileInputStream 객체를 사용하여 importXfdf 메서드를 호출해야 합니다. 마지막으로, Form 클래스의 save 메서드를 사용하여 PDF 파일을 저장할 수 있습니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "ImportDataFromXFDFInToPDF.java" >}}