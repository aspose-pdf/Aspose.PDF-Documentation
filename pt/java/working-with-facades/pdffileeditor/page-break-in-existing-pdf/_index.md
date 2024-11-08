---
title: Quebra de Página em PDF Existente
type: docs
weight: 30
url: /pt/java/page-break-in-existing-pdf/
description: Esta seção explica como quebrar páginas em um PDF existente usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Como layout padrão, o conteúdo dentro dos arquivos PDF é adicionado no layout de Superior-Esquerdo para Inferior-Direito. Uma vez que o conteúdo excede a margem inferior da página, ocorre a quebra de página. No entanto, você pode se deparar com a necessidade de inserir uma quebra de página dependendo da necessidade. Um método chamado AddPageBreak(...) é adicionado na classe [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) para cumprir este requisito.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-com.aspose.pdf.IDocument-com.aspose.pdf.IDocument-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)

1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#addPageBreak-java.lang.String-java.lang.String-com.aspose.pdf.facades.PdfFileEditor.PageBreak:A-)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html?is-external=true)

- src é o documento de origem/caminho para o documento/fluxo com o documento de origem
- dest é o documento de destino/caminho onde o documento será salvo/fluxo onde o documento será salvo
- PageBreak é um array de objetos de quebra de página. Ele tem duas propriedades: índice da página onde a quebra de página deve ser colocada e posição vertical da quebra de página na página.

## Exemplo 1 (Adicionar quebra de página)

```java
   public static void PageBrakeExample01() {
        // Instanciar instância do Documento
        Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
        // Instanciar instância do Documento em branco
        Document dest = new Document();
        // Criar objeto PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        // Salvar arquivo resultante
        dest.Save(_dataDir + "PageBreak_out.pdf");
    }
```


## Exemplo 2

```java
  public static void PageBrakeExample02() {
        // Criar objeto PdfFileEditor
        PdfFileEditor fileEditor = new PdfFileEditor();

        fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf", _dataDir + "PageBreakWithDestPath_out.pdf",
                new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
    }
```

## Exemplo 3

```java
 public static void PageBrakeExample03() {
        Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
        Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
        PdfFileEditor fileEditor = new PdfFileEditor();
        fileEditor.AddPageBreak(src, dest, new PdfFileEditor.PageBreak[] { new PdfFileEditor.PageBreak(1, 450) });
        dest.Close();
        src.Close();
    }
```