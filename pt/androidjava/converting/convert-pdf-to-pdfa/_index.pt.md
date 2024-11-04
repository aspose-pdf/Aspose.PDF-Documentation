---
title: Converter Arquivo PDF para PDF/A 
linktitle: Converter Arquivo PDF para PDF/A 
type: docs
weight: 180
url: /androidjava/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: Este tópico mostra como o Aspose.PDF para Java permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A.  
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF permite que você converta um arquivo PDF em um arquivo PDF compatível com PDF/A. Antes de fazer isso, o arquivo deve ser validado. Este artigo explica como.

Por favor, note que seguimos o Adobe Preflight para validar a conformidade com PDF/A. Todas as ferramentas no mercado têm sua própria "representação" da conformidade com PDF/A. Por favor, consulte este artigo sobre [ferramentas de validação PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) para referência. Escolhemos os produtos Adobe para verificar como o Aspose.PDF produz arquivos PDF porque a Adobe está no centro de tudo o que está relacionado ao PDF.

Antes de converter o PDF para um arquivo compatível com PDF/A, valide o PDF usando o método de validação.
 O resultado da validação é armazenado em um arquivo XML e então esse resultado também é passado para o método de conversão. Você também pode especificar a ação para os elementos que não podem ser convertidos usando a enumeração [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## Conversão de PDF para PDF/A_1b

O trecho de código a seguir mostra como converter arquivos PDF para PDF compatível com PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Converter para documento compatível com PDF/A
        // Durante o processo de conversão, a validação também é realizada
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Salvar documento de saída
        document.save(pdfaFileName.toString());
    }
```

Para realizar apenas a validação, use a seguinte linha de código:

```java
public void ValidatePDF_A_1B() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validar para documento compatível com PDF/A

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Documento é válido");
        }
        else {
            resultMessage.setText("Documento não é válido");
        }
    }
```

## Conversão de PDF para PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Converter para documento compatível com PDF/A
        // Durante o processo de conversão, a validação também é realizada
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Salvar documento de saída
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
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Converter para documento compatível com PDF/A
        // Durante o processo de conversão, a validação também é realizada
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Salvar documento de saída
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
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Converter para documento compatível com PDF/A
        // Durante o processo de conversão, a validação também é realizada
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Salvar documento de saída
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
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Converter para documento compatível com PDF/A
        // Durante o processo de conversão, a validação também é realizada
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Salvar documento de saída
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

Aspose.PDF para Android via Java oferece a funcionalidade de converter arquivos PDF para o formato PDF/A e também suporta as capacidades de adicionar arquivos como anexos ao documento PDF.
 No caso de você ter um requisito para anexar arquivos ao formato de conformidade PDF/A, recomendamos usar o valor PDF_A_3A da enumeração com.aspose.pdf.PdfFormat. O PDF/A_3a é o formato que fornece a funcionalidade de anexar qualquer formato de arquivo como um anexo a um arquivo compatível com PDF/A. No entanto, uma vez que o arquivo está anexado, você deve convertê-lo novamente para o formato Pdf-3a, a fim de corrigir os metadados. Por favor, veja o trecho de código a seguir.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Converter para documento compatível com PDF/A
        // Durante o processo de conversão, a validação também é realizada
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Salvar documento de saída
        try {
            // carregar arquivo XML
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Arquivo xml de exemplo");
            // Adicionar anexo à coleção de anexos do documento
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