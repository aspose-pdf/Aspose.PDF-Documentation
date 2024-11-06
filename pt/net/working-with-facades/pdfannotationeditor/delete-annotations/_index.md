---
title: Delete Annotations (facades)
type: docs
weight: 10
url: pt/net/delete-annotations/
description: Esta seção explica como excluir anotações com Aspose.PDF Facades usando a Classe PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Excluir Todas as Anotações de um Arquivo PDF Existente

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) permite que você exclua todas as anotações do arquivo PDF existente. Primeiro, crie um objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) e vincule o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, chame o método [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) para deletar todas as anotações do arquivo e, em seguida, use o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como deletar todas as anotações do arquivo PDF.

```csharp
   public static void DeleteAllAnnotations()
        {
            // Abrir documento
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            // Deletar todas as anotações
            annotationEditor.DeleteAnnotations();
            // Salvar PDF atualizado
        }   
```
## Excluir Todas as Anotações por Tipo Especificado

Você pode usar a classe [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) para excluir todas as anotações, por um tipo de anotação especificado, do arquivo PDF existente. Para fazer isso, você precisa criar um objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, chame o método [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations), com o parâmetro string, para excluir todas as anotações do arquivo; o parâmetro string representa o tipo de anotação a ser excluído. Finalmente, use o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como excluir todas as anotações por tipo de anotação especificado.

```csharp
    public static void DeleteAnnotation()
        {
            // Abrir documento
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            int index;
            for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
            {
                System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
            }
            System.Console.Write("Por favor, insira o número:");
            index = int.Parse(System.Console.ReadLine());

            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // Salvar PDF atualizado
            annotationEditor.Save(_dataDir + "DeleteAnnotation.pdf");
        }
```