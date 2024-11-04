---
title: Converter PDF/A para PDF 
linktitle: Converter PDF/A para PDF
type: docs
weight: 350
url: /androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: Para converter PDF/A para PDF, você deve remover as restrições do documento original. Aspose.PDF para Android via Java permite que você resolva este problema de forma fácil e simples.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Converter documento PDF/A para PDF significa remover a restrição <abbr title="Portable Document Format Archive
">PDF/A</abbr> do documento original. A classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) possui o método RemovePdfaCompliance(..) para remover
a informação de conformidade PDF do arquivo de entrada/origem.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Criar objeto Document
            document = new Document(pdfaDocumentFileName);

            // Remover informações de conformidade PDF/A
            document.removePdfaCompliance();

            // Salvar saída no formato XML
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```


Esta informação também é removida se você fizer quaisquer alterações no documento (por exemplo, adicionar páginas). No exemplo a seguir, o documento de saída perde a conformidade com PDF/A após a adição de página.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Criar objeto Documento
        document = new Document(pdfaDocumentFileName);

        // Adicionar uma nova página (vazia) remove informações de conformidade com PDF/A.
        document.getPages().add();

        // Salvar documento atualizado
        document.save(pdfDocumentFileName);
    }
```