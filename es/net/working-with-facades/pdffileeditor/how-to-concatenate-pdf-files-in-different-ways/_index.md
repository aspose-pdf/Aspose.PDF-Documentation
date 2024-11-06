---
title: Merge PDF files using .NET 5 
linktitle: How to merge PDF
type: docs
weight: 75
url: es/net/how-to-concatenate-pdf-files-in-different-ways/
description: Este artículo explica las posibles formas de concatenar cualquier número de archivos PDF existentes en un solo archivo PDF.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Este artículo describe cómo puede [Concatenar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) múltiples documentos PDF en un solo documento PDF con la ayuda del componente [Aspose.PDF for .NET](/pdf/net/). [Aspose.PDF for .NET](/pdf/net/) hace este trabajo como si fuera pan comido.

{{% /alert %}}

Todo lo que tiene que hacer es llamar al método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) y todos sus archivos PDF de entrada se concatenarán juntos y se generará un solo archivo PDF. Vamos a crear una aplicación para practicar la concatenación de archivos PDF. Crearemos una aplicación usando Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF para .NET se puede usar en cualquier tipo de aplicación que se ejecute en .NET Framework, ya sea una aplicación web ASP.NET o una aplicación de Windows

{{% /alert %}}

## Cómo Concatenar Archivos PDF de Diferentes Maneras

En el formulario, hay tres Cajas de Texto (textBox1, textBox2, textBox3) que tienen sus respectivas Etiquetas de Enlace (linkLabel1, linkLabel2, linkLabel3) para navegar los archivos PDF. Al hacer clic en la Etiqueta de Enlace "Browse", aparecerá un Cuadro de Diálogo de Archivo de Entrada (inputFileDialog1) que nos permitirá elegir los archivos PDF (para ser concatenados).

```csharp

private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
  if(openFileDialog1.ShowDialog()==DialogResult.OK)
  {
     textBox1.Text=openFileDialog1.FileName;
  }
}
```

Se muestra la vista de una aplicación de formulario de Windows para la demostración de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) para la Concatenación de Archivos PDF.
![Concatenate PDF Files](how-to-concatenate-pdf-files-in-different-ways_1.png)

Después de elegir el archivo PDF y hacer clic en el botón OK. El nombre completo del archivo con la ruta se asigna al Cuadro de Texto relacionado.

![Choose the PDF file](how-to-concatenate-pdf-files-in-different-ways_2.png)

De manera similar, podemos elegir dos o tres archivos PDF de entrada para concatenar como se muestra a continuación:

![Choose two or three Input PDF Files](how-to-concatenate-pdf-files-in-different-ways_3.png)

El último Cuadro de Texto (textBox4) tomará la Ruta de Destino del archivo PDF de salida con su nombre donde se creará este archivo de salida.

![Destination Path of the Output PDF file](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenate method](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Método Concatenate()

El método Concatenate() se puede usar de tres maneras. Vamos a echar un vistazo más de cerca a cada una de ellas:

### Enfoque 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Este enfoque es bueno solo si necesitas unir solo dos archivos PDF. Primeros dos argumentos (firstInputFile y secInputFile) proporcionan los nombres completos de archivo con su ruta de almacenamiento de los dos archivos PDF de entrada que van a ser concatenados. El tercer argumento (outputFile) proporciona el nombre de archivo deseado con la ruta del archivo PDF de salida.

![Concatenar dos PDFs usando Nombres de Archivo](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Enfoque 2

- Concatenate(System.IO.Stream firstInputStream, System.IO.Stream secInputStream, System.IO.Stream outputStream)

Similar al enfoque anterior, este método también permite unir dos archivos PDF. Primeros dos argumentos (firstInputStream y secInputStream) proporcionan los dos archivos PDF de entrada como Streams (un stream es un array de bits/bytes) que deben ser concatenados. El tercer argumento (outputStream) proporciona la representación del flujo del archivo PDF de salida deseado.

![Concatenar dos PDFs usando flujos de archivos](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdf1,pdf2,outputPDF);
  outputPDF.Close();
}
```

### Enfoque 3

- Concatenate(System.IO.Stream inputStreams[], System.IO.Stream outputStream)

Si deseas unir más de dos archivos PDF, entonces este enfoque sería tu elección definitiva. Primer argumento (inputStreams[]) proporciona los archivos PDF de entrada en forma de un Array de Streams que se van a concatenar. Segundo argumento (outputStream) proporciona la representación del flujo del archivo PDF de salida deseado.

![Concatenar múltiples PDFs usando Array de Streams](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
  FileStream pdf1 = new FileStream(textBox1.Text,FileMode.Open);
  FileStream pdf2 = new FileStream(textBox2.Text,FileMode.Open);
  FileStream pdf3 = new FileStream(textBox3.Text,FileMode.Open);
  Stream[] pdfStreams = new Stream[]{pdf1,pdf2,pdf3};
  FileStream outputPDF = new FileStream(textBox4.Text,FileMode.Create);
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(pdfStreams,outputPDF);
  outputPDF.Close();
}
```