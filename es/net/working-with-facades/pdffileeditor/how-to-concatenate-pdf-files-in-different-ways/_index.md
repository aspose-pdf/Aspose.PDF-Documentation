---
title: Combinar archivos PDF usando .NET 5
linktitle: Cómo combinar PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 75
url: /es/net/how-to-concatenate-pdf-files-in-different-ways/
description: Este artículo explica las posibles formas de concatenar cualquier número de archivos PDF existentes en un solo archivo PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge PDF files",
    "alternativeHeadline": "Effortlessly Combine Multiple PDFs",
    "abstract": "Combina múltiples archivos PDF en un solo documento sin problemas con la nueva funcionalidad en Aspose.PDF for .NET. Esta característica permite a los desarrolladores concatenar cualquier número de PDFs a través de llamadas a métodos simples, mejorando la productividad en la gestión y manipulación de PDF. Integra sin esfuerzo esta capacidad en varias aplicaciones .NET, incluyendo aplicaciones ASP.NET y de Windows, con enfoques versátiles que se adaptan a diferentes necesidades",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "840",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/how-to-concatenate-pdf-files-in-different-ways/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-concatenate-pdf-files-in-different-ways/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

Este artículo describe cómo puedes [Concatenar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) múltiples documentos PDF en un solo documento PDF con la ayuda del componente [Aspose.PDF for .NET](/pdf/net/). [Aspose.PDF for .NET](/pdf/net/) hace que este trabajo sea pan comido.

{{% /alert %}}

Todo lo que tienes que hacer es llamar al método [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) y todos tus archivos PDF de entrada se concatenarán y se generará un solo archivo PDF. Vamos a crear una aplicación para practicar la concatenación de archivos PDF. Crearemos una aplicación usando Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF for .NET se puede usar en cualquier tipo de aplicación que se ejecute en .NET Framework, ya sea una aplicación web ASP.NET o una aplicación de Windows.

{{% /alert %}}

## Cómo concatenar archivos PDF de diferentes maneras

En el formulario, hay tres cuadros de texto (textBox1, textBox2, textBox3) que tienen sus respectivos enlaces (linkLabel1, linkLabel2, linkLabel3) para buscar los archivos PDF. Al hacer clic en el enlace "Buscar", aparecerá un cuadro de diálogo de archivo de entrada (inputFileDialog1) que nos permitirá elegir los archivos PDF (que se van a concatenar).

```csharp
private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
    if (openFileDialog1.ShowDialog()==DialogResult.OK)
    {
        textBox1.Text=openFileDialog1.FileName;
    }
}
```

Se muestra la vista de una aplicación de formulario de Windows para la demostración de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) para la concatenación de archivos PDF.

![Concatenar archivos PDF](how-to-concatenate-pdf-files-in-different-ways_1.png)

Después de elegir el archivo PDF y hacer clic en el botón Aceptar. El nombre completo del archivo con la ruta se asigna al cuadro de texto relacionado.

![Elegir el archivo PDF](how-to-concatenate-pdf-files-in-different-ways_2.png)

De manera similar, podemos elegir dos o tres archivos PDF de entrada para concatenar, como se muestra a continuación:

![Elegir dos o tres archivos PDF de entrada](how-to-concatenate-pdf-files-in-different-ways_3.png)

El último cuadro de texto (textBox4) tomará la ruta de destino del archivo PDF de salida con su nombre donde se creará este archivo de salida.

![Ruta de destino del archivo PDF de salida](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Método Concatenate](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Método Concatenate()

El método Concatenate() se puede usar de tres maneras. Veamos más de cerca cada una de ellas:

### Enfoque 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Este enfoque es bueno solo si necesitas unir solo dos archivos PDF. Los dos primeros argumentos (firstInputFile y secInputFile) proporcionan los nombres completos de los archivos con su ruta de almacenamiento de los dos archivos PDF de entrada que se van a concatenar. El tercer argumento (outputFile) proporciona el nombre de archivo deseado con la ruta del archivo PDF de salida.

![Concatenar dos PDFs usando nombres de archivo](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Enfoque 2

- Concatenate(Stream firstInputStream, Stream secInputStream, Stream outputStream)

Similar al enfoque anterior, este enfoque también permite unir dos archivos PDF. Los dos primeros argumentos (firstInputStream y secInputStream) proporcionan los dos archivos PDF de entrada como flujos (un flujo es un arreglo de bits/bytes) que se van a concatenar. El tercer argumento (outputStream) proporciona la representación de flujo del archivo PDF de salida deseado.

![Concatenar dos PDFs usando flujos de archivo](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
            {
                var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                pdfEditor.Concatenate(pdf1, pdf2, outputStream);
            }
        }
    }
}
```

### Enfoque 3

- Concatenate(Stream inputStreams[], Stream outputStream)

Si deseas unir más de dos archivos PDF, entonces este enfoque sería tu elección definitiva. El primer argumento (inputStreams[]) proporciona los archivos PDF de entrada en forma de un arreglo de flujos que se van a concatenar. El segundo argumento (outputStream) proporciona la representación de flujo del archivo PDF de salida deseado.

![Concatenar múltiples PDFs usando un arreglo de flujos](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var pdf3 = new FileStream(textBox3.Text, FileMode.Open))
            {
                var pdfStreams = new Stream[] { pdf1, pdf2, pdf3 };
                using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
                {
                    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                    pdfEditor.Concatenate(pdfStreams, outputStream);
                }
            }
        }
    }
}
```