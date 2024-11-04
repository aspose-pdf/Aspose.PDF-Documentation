---
title: Converter PDF/A para formato PDF 
linktitle: Converter PDF/A para formato PDF
type: docs
weight: 110
url: /java/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter um arquivo PDF/A para documento PDF com a biblioteca Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter documento PDF/A para PDF

Converter documento PDF/A para PDF significa remover a restrição <abbr title="Portable Document Format Archive">PDF/A</abbr> do documento original. A classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) possui o método RemovePdfaCompliance(..) para remover
as informações de conformidade PDF do arquivo de entrada/fonte.

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Criar objeto Document
    Document document = new Document(pdfaDocumentFileName);

    // Remover informações de conformidade PDF/A
    document.removePdfaCompliance();

    // Salvar saída em formato XML
    document.save(documentFileName);
    document.close();
}
```


Esta informação também é removida se você fizer quaisquer alterações no documento (por exemplo, adicionar páginas). No exemplo a seguir, o documento de saída perde a conformidade com PDF/A após a adição da página.

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Criar objeto Document
    Document document = new Document(pdfaDocumentFileName);

    // Adicionar uma nova página (vazia) remove a informação de conformidade com PDF/A.
    document.getPages().add();

    // Salvar documento atualizado
    document.save(documentFileName);
    document.close();
}
```