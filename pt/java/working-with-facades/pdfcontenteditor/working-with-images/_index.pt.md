---
title: Trabalhando com Imagens
type: docs
weight: 30
url: /java/working-with-image/
description: Esta seção explica como substituir imagem com Aspose.PDF Facades - um conjunto de ferramentas para operações populares com PDF.
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Excluir Imagens de uma Página Específica do PDF (Facades)

A classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) permite substituir imagem em um arquivo PDF existente.
 O método [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) ajuda você a alcançar esse objetivo. Você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) e vincular o arquivo PDF de entrada usando o método bindPdf. Depois disso, você precisa chamar o método [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) com três parâmetros: um número de página, índice da imagem a ser substituída e o caminho da imagem a ser substituída.

O trecho de código a seguir mostra como substituir uma imagem em um arquivo PDF existente.

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## Excluir Todas as Imagens de um Arquivo PDF (Facades)

Todas as imagens podem ser excluídas de um arquivo PDF usando o método [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) do [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). Chame o método [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) – a sobrecarga sem nenhum parâmetro – para excluir todas as imagens e, em seguida, salve o arquivo PDF atualizado usando o método Save.

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## Substituir Imagens em Arquivo PDF (Facades)

Você pode substituir imagens em um arquivo PDF usando o método [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) do [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
   public static void ReplaceImage()
    {
        // Substituir imagem no documento PDF
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```