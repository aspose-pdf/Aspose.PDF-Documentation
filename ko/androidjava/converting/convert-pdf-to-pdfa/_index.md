---
title: PDF 파일을 PDF/A 로 변환
linktitle: PDF 파일을 PDF/A 로 변환
type: docs
weight: 180
url: /ko/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2026-07-01"
description: 이 주제에서는 Aspose.PDF for Java를 사용하여 PDF 파일을 PDF/A 호환 PDF 파일로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF를 사용하면 PDF 파일을 PDF/A 규격을 준수하는 PDF 파일로 변환할 수 있습니다. 변환하기 전에 파일을 검증해야 합니다. 이 문서에서는 그 방법을 설명합니다.

PDF/A 적합성을 검증하기 위해 Adobe Preflight를 따르고 있음을 알려드립니다. 시장에 있는 모든 도구들은 PDF/A 적합성에 대한 자체적인 “representation”(표현)을 가지고 있습니다. 이 문서에서 확인해 주세요. [PDF/A 검증 도구](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) 참고용. Adobe가 PDF와 연결된 모든 것의 중심에 있기 때문에 Aspose.PDF가 PDF 파일을 생성하는 방식을 확인하기 위해 Adobe 제품을 선택했습니다.

PDF를 PDF/A 호환 파일로 변환하기 전에, validate 메서드를 사용하여 PDF를 검증합니다. 검증 결과는 XML 파일에 저장되고, 이 결과는 convert 메서드에도 전달됩니다. 변환할 수 없는 요소에 대해 수행할 작업을 지정할 수도 있습니다. [변환오류동작](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) 열거.

{{% alert color="primary" %}}

온라인으로 시도해 보세요. Aspose.PDF 변환 품질을 확인하고 이 링크에서 결과를 온라인으로 볼 수 있습니다. [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## PDF를 PDF/A_1b로 변환

다음 코드 스니펫은 PDF 파일을 PDF/A-1b 준수 PDF로 변환하는 방법을 보여줍니다.

```java
public void convertPDFtoPDFa1b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save output document
        document.save(pdfaFileName.toString());
    }
```

검증만 수행하려면, 다음 코드를 사용하세요:

```java
public void ValidatePDF_A_1B() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validate to PDF/A compliant document

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Document is valid");
        }
        else {
            resultMessage.setText("Document is not valid");
        }
    }
```

## PDF를 PDF/A_3b로 변환

```java
    public void convertPDFtoPDFa3b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDF를 PDF/A_3a로 변환

```java
public void convertPDFtoPDFa3a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDF를 PDF/A_2a 변환

```java
public void convertPDFtoPDFa2a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## PDF to PDF/A_3U 변환

```java
 public void convertPDFtoPDFa3u() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Save output document
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## PDF/A-3를 만들고 XML 파일을 첨부하세요

Aspose.PDF for Android via Java은 PDF 파일을 PDF/A 형식으로 변환하는 기능을 제공하며 PDF 문서에 파일을 첨부하는 기능도 지원합니다. PDF/A 준수 형식에 파일을 첨부해야 하는 경우에는 com.aspose.pdf.PdfFormat 열거형에서 PDF_A_3A 값을 사용하는 것을 권장합니다. PDF/A_3a는 모든 파일 형식을 PDF/A 준수 파일에 첨부할 수 있는 기능을 제공하는 형식입니다. 그러나 파일을 첨부한 후에는 메타데이터를 수정하기 위해 다시 Pdf-3a 형식으로 변환해야 합니다. 아래 코드 스니펫을 확인해 보세요.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Save output document
        try {
            // load XML file
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Sample xml file");
            // Add attachment to document's attachment collection
            document.getEmbeddedFiles().add(fileSpecification);
            document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

