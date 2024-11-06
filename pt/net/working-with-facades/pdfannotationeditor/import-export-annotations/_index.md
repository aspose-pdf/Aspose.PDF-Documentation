---
title: Importar e Exportar Anotações para XFDF 
type: docs
weight: 20
url: pt/net/import-export-annotations/
description: Esta seção explica como importar e exportar anotações de um arquivo PDF para XFDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF significa XML Forms Data Format. É um formato de arquivo baseado em XML. Este formato de arquivo é usado para representar dados de formulários ou anotações contidas em um formulário PDF. XFDF pode ser usado para muitos propósitos diferentes, mas no nosso caso, pode ser usado para enviar ou receber dados de formulários ou anotações para outros computadores ou servidores, etc., ou pode ser usado para arquivar os dados de formulários ou anotações. Neste artigo, veremos como o Aspose.Pdf.Facades considerou este conceito e como podemos importar e exportar dados de anotações para um arquivo XFDF.

## Importando e Exportando Anotações para XFDF

[Aspose.PDF para .NET](/pdf/net/) é um componente rico em recursos quando se trata de editar documentos PDF. Como sabemos, XFDF é um aspecto importante da manipulação de formulários PDF, o [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) no [Aspose.PDF for .NET](/pdf/net/) considerou isso muito bem, e forneceu métodos para importar e exportar dados de anotações para arquivos XFDF.

A classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) contém dois métodos para trabalhar com a importação e exportação de anotações para o arquivo XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) método fornece a funcionalidade para exportar anotações de um documento PDF para um arquivo XFDF, enquanto o método [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) permite importar anotações de um arquivo XFDF existente. Para importar ou exportar anotações, precisamos especificar os tipos de anotações. Podemos especificar esses tipos na forma de uma enumeração e, em seguida, passar essa enumeração como um argumento para qualquer um desses métodos. Dessa forma, as anotações dos tipos especificados serão apenas importadas ou exportadas para um arquivo XFDF.

O snippet de código a seguir mostra como importar anotações para um arquivo XFDF:

```csharp
public static void ImportAnnotation()
        {
            var sources = new string[] { _dataDir + "sample_cats_dogs.pdf" };
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample.pdf");
            annotationEditor.ImportAnnotations(sources);
            annotationEditor.Save(_dataDir + "sample_demo.pdf");
        }
```
O próximo trecho de código descreve como importar/exportar anotações para um arquivo XFDF:

```csharp
public static void ImportExportXFDF01()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.Close();
            var document = new Document();
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```

Dessa forma, as anotações dos tipos especificados serão importadas ou exportadas apenas para um arquivo XFDF.

```csharp
   public static void ImportExportXFDF02()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.Close();

            var document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```