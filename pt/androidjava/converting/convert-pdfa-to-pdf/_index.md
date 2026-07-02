---
title: Converter PDF/A para PDF
linktitle: Converter PDF/A para PDF
type: docs
weight: 350
url: /pt/androidjava/convert-pdfa-to-pdf/
lastmod: "2026-07-01"
description: Para converter PDF/A para PDF, você deve remover restrições do documento original. Aspose.PDF for Android via Java permite que você resolva esse problema de forma fácil e simples.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Converter documento PDF/A para PDF significa remover <abbr title="Portable Document Format Archive"
\"\u003EPDF/A</abbr> restrição do documento original. Classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) tem o método RemovePdfaCompliance(..) para remover
as informações de conformidade PDF do arquivo de entrada/fonte.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

Esta informação também é removida se você fizer quaisquer alterações no documento (por exemplo, adicionar páginas). No exemplo a seguir, o documento de saída perde a conformidade PDF/A após a adição da página.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```




