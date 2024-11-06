---
title: Trabalhar com Imagens usando PdfContentEditor
type: docs
weight: 50
url: pt/net/working-with-images-in-pdf
description: Esta seção explica como adicionar e excluir Imagens com Aspose.PDF Facades usando a Classe PdfContentEditor.
lastmod: "2021-06-24"
---

## Excluir Imagens de uma Página Específica do PDF (Facades)

Para excluir as imagens de uma página específica, você precisa chamar o método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) com os parâmetros pageNumber e index. O parâmetro index representa um array de inteiros – os índices das imagens a serem excluídas. Primeiro de tudo, você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) e então chamar o método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1). Depois disso, você pode salvar o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

O seguinte trecho de código mostra como excluir imagens de uma página específica do PDF.

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## Excluir Todas as Imagens de um Arquivo PDF (Facades)

Todas as imagens podem ser excluídas de um arquivo PDF usando o método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) do [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Chame o método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) – a sobrecarga sem nenhum parâmetro – para deletar todas as imagens, e então salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

O trecho de código a seguir mostra como deletar todas as imagens de um arquivo PDF.

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## Substituir Imagem em um Arquivo PDF (Facades)

O [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) permite que você substitua sua imagem em um arquivo PDF, chame para isso o método [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage), e salve o resultado.

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```