---
title: Converter arquivo PDF para PDF/A
linktitle: Converter arquivo PDF para PDF/A
type: docs
weight: 180
url: /pt/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2026-07-01"
description: Este tópico mostra como o Aspose.PDF for Java permite converter um arquivo PDF para um arquivo PDF/A compatível.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

O Aspose.PDF permite converter um arquivo PDF em um arquivo PDF/A compatível. Antes de fazer isso, o arquivo deve ser validado. Este artigo explica como.

Observe que seguimos o Adobe Preflight para validar a conformidade PDF/A. Todas as ferramentas do mercado têm sua própria “representação” da conformidade PDF/A. Por favor, verifique este artigo em [Ferramentas de validação PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) para referência. Escolhemos os produtos da Adobe para verificar como o Aspose.PDF produz arquivos PDF porque a Adobe está no centro de tudo conectado ao PDF.

Antes de converter o PDF para um arquivo compatível com PDF/A, valide o PDF usando o método validate. O resultado da validação é armazenado em um arquivo XML e então esse resultado também é passado para o método convert. Você também pode especificar a ação para os elementos que não podem ser convertidos usando o [Ação de Erro de Conversão](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) enumeração.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## Conversão de PDF para PDF/A_1b

O trecho de código a seguir mostra como converter arquivos PDF em PDF compatível com PDF/A-1b.

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

Para executar apenas a validação, use a seguinte linha de código:

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

## Conversão de PDF para PDF/A_3b

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

## Conversão de PDF para PDF/A_3a

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

## Conversão de PDF para PDF/A_2a

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

## Conversão de PDF para PDF/A_3U

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

## Criar PDF/A-3 e anexar arquivo XML

Aspose.PDF for Android via Java oferece o recurso de converter arquivos PDF para o formato PDF/A e também suporta a capacidade de adicionar arquivos como anexo a um documento PDF. Caso você tenha um requisito de anexar arquivos ao formato de conformidade PDF/A, recomendamos o uso do valor PDF_A_3A da enumeração com.aspose.pdf.PdfFormat; o PDF/A_3a é o formato que fornece o recurso de anexar qualquer formato de arquivo como anexo a um arquivo compatível com PDF/A. Contudo, após o arquivo ser anexado, você deve convertê-lo novamente para o formato Pdf-3a, a fim de corrigir os metadados. Por favor, examine o trecho de código a seguir.

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

