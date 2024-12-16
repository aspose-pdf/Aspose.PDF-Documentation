---
title: Modificar Anotações no seu Arquivo PDF (facades)
type: docs
weight: 50
url: /pt/java/modify-annotations/
description: Esta seção explica como modificar anotações de arquivo PDF para XFDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

O método [modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) permite que você altere atributos básicos de uma anotação, ou seja, Assunto, Data de modificação, Autor, Cor da anotação e Flag de abertura. Você também pode definir o Autor diretamente usando o método ModifyAnnotations. Esta classe também fornece dois métodos sobrecarregados para excluir anotações. O primeiro método chamado DeleteAnnotations exclui todas as anotações de um arquivo PDF.

Por exemplo, no código a seguir, considere alterar o autor em nossa anotação usando [modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-).

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Usuário Aspose", "Usuário Aspose.PDF");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

O segundo método permite que você exclua todas as anotações de um tipo especificado.

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Cria um novo objeto do tipo Anotação para modificar os atributos da anotação
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Usuário de Demonstração Aspose.PDF");
        annotation.setSubject("Artigo Técnico");

        // Modifica as anotações no arquivo PDF
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```


## Veja também

Tente comparar e encontrar uma maneira de trabalhar com anotações que seja adequada para você. Vamos aprender a seção de [Anotações em PDF](/pdf/pt/java/annotations/).