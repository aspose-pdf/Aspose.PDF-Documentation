---
title: Modificar Anotações no seu PDF 
type: docs
weight: 50
url: /net/modify-annotations/
description: Esta seção explica como modificar anotações de arquivo PDF para XFDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

O método [ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) permite que você altere atributos básicos de uma anotação, ou seja, Assunto, Data de modificação, Autor, Cor da anotação e Flag Aberta. Você também pode definir o Autor diretamente usando o método ModifyAnnotations. Esta classe também fornece dois métodos sobrecarregados para excluir anotações. O primeiro método chamado DeleteAnnotations exclui todas as anotações de um arquivo PDF.

Por exemplo, no código a seguir, considere alterar o autor em nossa anotação usando [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
   public static void ModifyAnnotationsAuthor()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
            annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
        }
```

O segundo método permite que você exclua todas as anotações de um tipo especificado.

```csharp
   public static void ModifyAnnotations()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // Crie um novo objeto do tipo Annotation para modificar atributos de anotação
            var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
            Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
                document.Pages[1],
                new Aspose.Pdf.Rectangle(1, 1, 1, 1),
                defaultAppearance)
            {

                // Defina novos atributos de anotação
                Title = "Aspose.PDF Demo User",
                Subject = "Artigo Técnico"
            };
            // Modifique as anotações no arquivo PDF
            annotationEditor.ModifyAnnotations(1, 1, annotation);
            annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
        }
```

## Veja também

Tente comparar e encontrar uma maneira de trabalhar com anotações que lhe convém. Vamos aprender a seção de [Anotações em PDF](/pdf/net/annotations/).