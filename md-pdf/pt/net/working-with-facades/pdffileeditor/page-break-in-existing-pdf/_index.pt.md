---
title: Quebra de Página em PDF Existente
type: docs
weight: 30
url: /net/page-break-in-existing-pdf/
description: Esta seção explica como quebrar páginas em um PDF existente usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Como layout padrão, o conteúdo dentro dos arquivos PDF é adicionado em um layout de Canto Superior Esquerdo para Inferior Direito. Uma vez que o conteúdo excede a margem inferior da página, a quebra de página ocorre. No entanto, você pode se deparar com a necessidade de inserir uma quebra de página dependendo da necessidade. Um método chamado AddPageBreak(...) é adicionado na classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) para realizar esse requisito.)

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/addpagebreak)

- src é o documento de origem/caminho para o documento/fluxo com o documento de origem
- dest é o documento de destino/caminho onde o documento será salvo/fluxo onde o documento será salvo
- PageBreak é uma matriz de objetos de quebra de página. Ele tem duas propriedades: índice da página onde a quebra de página deve ser colocada e posição vertical da quebra de página na página.

## Exemplo 1 (Adicionar quebra de página)

```csharp
public static void PageBrakeExample01()
{
    // Instanciar instância do Documento
    Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
    // Instanciar instância de Documento em branco
    Document dest = new Document();
    // Criar objeto PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[]
    {
        new PdfFileEditor.PageBreak(1, 450)
    });
    // Salvar arquivo resultante
    dest.Save(_dataDir + "PageBreak_out.pdf");
}
```
## Exemplo 2

```csharp
public static void PageBrakeExample02()
{
    // Criar objeto PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();

    fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf",
        _dataDir + "PageBreakWithDestPath_out.pdf",
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
}
```

## Exemplo 3

```csharp
public static void PageBrakeExample03()
{
    Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
    Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(src, dest,
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
    dest.Close();
    src.Close();
}
```