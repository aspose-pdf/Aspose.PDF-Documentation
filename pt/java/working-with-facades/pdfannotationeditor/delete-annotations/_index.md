---
title: Excluir Anotações (facades)
type: docs
weight: 10
url: pt/java/delete-annotations/
description: Esta seção explica como excluir anotações com Aspose.PDF Facades usando a classe PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Você pode usar a classe [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) para excluir anotações, por um tipo de anotação especificado, de um arquivo PDF existente.
 Para fazer isso, você precisa criar um objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) e vincular o arquivo PDF de entrada usando o método bindPdf. Depois disso, chame o método [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-), com o parâmetro string, para excluir todas as anotações do arquivo; o parâmetro string representa o tipo de anotação a ser excluída. Finalmente, use o método save para salvar o arquivo PDF atualizado.

O trecho de código a seguir mostra como excluir a anotação por tipo de anotação especificado.

```java
public static void DeleteAnnotation() {
        // Abrir documento
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("Por favor, insira o número:");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // Salvar PDF atualizado
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
    ```
[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) permite que você exclua todas as anotações do arquivo PDF existente.

Primeiro, crie um [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) e vincule o arquivo PDF de entrada usando o método BindPdf.

Depois disso, chame o método [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) para excluir todas as anotações do arquivo, e então use o método Save para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como excluir todas as anotações do arquivo PDF.

```java
public static void DeleteAllAnnotations() {
    // Abrir documento
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
    // Excluir todas as anotações
    annotationEditor.deleteAnnotations();
    // Salvar PDF atualizado
    annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
}
```