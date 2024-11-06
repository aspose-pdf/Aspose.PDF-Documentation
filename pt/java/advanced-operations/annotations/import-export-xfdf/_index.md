---
title: Importar e Exportar Anotações para o formato XFDF
linktitle: Importar e Exportar Anotações para o formato XFDF
type: docs
weight: 40
url: pt/java/import-export-xfdf/
description: Você pode importar e exportar anotações com o formato XFDF usando a biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF significa Formato de Dados de Formulários XML. É um formato de arquivo baseado em XML. Este formato de arquivo é usado para representar dados de formulários ou anotações contidas em um formulário PDF. XFDF pode ser usado para muitos propósitos diferentes, mas, no nosso caso, pode ser usado para enviar ou receber dados de formulários ou anotações para outros computadores ou servidores, etc., ou pode ser usado para arquivar os dados de formulários ou anotações. Neste artigo, veremos como o Aspose.Pdf.Facades considerou este conceito e como podemos importar e exportar dados de anotações para um arquivo XFDF.

{{% /alert %}}

**Aspose.PDF para Java** é um componente rico em recursos quando se trata de editar documentos PDF.
 Como sabemos, XFDF é um aspecto importante da manipulação de formulários PDF, o namespace Aspose.Pdf.Facades no Aspose.PDF para Java considerou isso muito bem e forneceu métodos para importar e exportar dados de anotações para arquivos XFDF.

A classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) contém dois métodos para trabalhar com a importação e exportação de anotações para o arquivo XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) método fornece a funcionalidade para exportar anotações de um documento PDF para um arquivo XFDF, enquanto o método [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) permite que você importe anotações de um arquivo XFDF existente. Para importar ou exportar anotações, precisamos especificar os tipos de anotação. Podemos especificar esses tipos na forma de uma enumeração e, em seguida, passar essa enumeração como um argumento para qualquer um desses métodos. Desta forma, as anotações dos tipos especificados serão importadas ou exportadas para um arquivo XFDF.

O seguinte trecho de código mostra como exportar anotações para um arquivo XFDF:

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * Importando anotações de um arquivo XFDF XML Forms Data Format (XFDF)
     * criado pelo Adobe Acrobat, uma aplicação de criação de PDF; armazena descrições de
     * elementos de formulário de página e seus valores, como os nomes e valores para campos de texto;
     * usado para salvar dados de formulário que podem ser importados em um documento PDF.
     * Você pode importar dados de anotações do arquivo XFDF para PDF usando o
     * método ImportAnnotationsFromXfdf na classe PdfAnnotationEditor.
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // Criar objeto PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // Vincular documento PDF ao Editor de Anotações
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // Exportar anotações
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

O próximo trecho de código descreve como importar anotações para um arquivo XFDF:

```java
public static void ImportAnnotationXFDF()
{
    // Criar objeto PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Criar um novo documento PDF
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Importar anotação
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Salvar PDF de saída
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Outra maneira de exportar/importar anotações de uma vez

No código abaixo, um método ImportAnnotations permite importar anotações diretamente de outro documento PDF.

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // Criar objeto PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // Criar um novo documento PDF
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // Annotation Editor permite importar anotações de vários documentos PDF,
        // mas neste exemplo, usamos apenas um.
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // Salvar PDF de saída
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```