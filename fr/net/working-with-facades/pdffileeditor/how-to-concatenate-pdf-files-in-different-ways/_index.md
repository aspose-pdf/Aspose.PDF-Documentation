---
title: Fusionner des fichiers PDF en utilisant .NET 5
linktitle: Comment fusionner des PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 75
url: /fr/net/how-to-concatenate-pdf-files-in-different-ways/
description: Cet article explique les différentes manières de concaténer un nombre quelconque de fichiers PDF existants en un seul fichier PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge PDF files",
    "alternativeHeadline": "Effortlessly Combine Multiple PDFs",
    "abstract": "Fusionnez plusieurs fichiers PDF en un seul document sans effort grâce à la nouvelle fonctionnalité de Aspose.PDF for .NET. Cette fonctionnalité permet aux développeurs de concaténer n'importe quel nombre de PDF par des appels de méthode simples, améliorant ainsi la productivité dans la gestion et la manipulation des PDF. Intégrez facilement cette capacité dans diverses applications .NET, y compris les applications ASP.NET et Windows, avec des approches polyvalentes qui répondent à différents besoins.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

{{% alert color="primary" %}}

Cet article décrit comment vous pouvez [Concaténer](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) plusieurs documents PDF en un seul document PDF avec l'aide du composant [Aspose.PDF for .NET](/pdf/fr/net/). [Aspose.PDF for .NET](/pdf/fr/net/) rend cette tâche aussi simple qu'un jeu d'enfant.

{{% /alert %}}

Tout ce que vous avez à faire est d'appeler la méthode [Concatenate](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) et tous vos fichiers PDF d'entrée seront concaténés ensemble et un fichier PDF unique sera généré. Créons une application pour pratiquer la concaténation de fichiers PDF. Nous allons créer une application en utilisant Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF for .NET peut être utilisé dans tout type d'application fonctionnant sur le .NET Framework, que ce soit une application web ASP.NET ou une application Windows.

{{% /alert %}}

## Comment concaténer des fichiers PDF de différentes manières

Dans le formulaire, il y a trois zones de texte (textBox1, textBox2, textBox3) ayant leurs étiquettes de lien respectives (linkLabel1, linkLabel2, linkLabel3) pour parcourir les fichiers PDF. En cliquant sur l'étiquette de lien "Parcourir", une boîte de dialogue de fichier d'entrée (inputFileDialog1) apparaîtra, ce qui nous permettra de choisir les fichiers PDF (à concaténer).

```csharp
private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
    if (openFileDialog1.ShowDialog()==DialogResult.OK)
    {
        textBox1.Text=openFileDialog1.FileName;
    }
}
```

Une vue de l'application de formulaire Windows est montrée pour la démonstration de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) pour la concaténation de fichiers PDF.

![Concaténer des fichiers PDF](how-to-concatenate-pdf-files-in-different-ways_1.png)

Après avoir choisi le fichier PDF et cliqué sur le bouton OK, le nom complet du fichier avec le chemin est attribué à la zone de texte correspondante.

![Choisir le fichier PDF](how-to-concatenate-pdf-files-in-different-ways_2.png)

De même, nous pouvons choisir deux ou trois fichiers PDF d'entrée à concaténer comme montré ci-dessous :

![Choisir deux ou trois fichiers PDF d'entrée](how-to-concatenate-pdf-files-in-different-ways_3.png)

La dernière zone de texte (textBox4) prendra le chemin de destination du fichier PDF de sortie avec son nom où ce fichier de sortie sera créé.

![Chemin de destination du fichier PDF de sortie](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Méthode Concatenate](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Méthode Concatenate()

La méthode Concatenate() peut être utilisée de trois manières. Examinons de plus près chacune d'elles :

### Approche 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Cette approche est bonne uniquement si vous devez joindre seulement deux fichiers PDF. Les deux premiers arguments (firstInputFile et secInputFile) fournissent les noms de fichiers complets avec leur chemin de stockage des deux fichiers PDF d'entrée à concaténer. Le troisième argument (outputFile) fournit le nom de fichier souhaité avec le chemin du fichier PDF de sortie.

![Concaténer deux PDFs en utilisant les noms de fichiers](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Approche 2

- Concatenate(Stream firstInputStream, Stream secInputStream, Stream outputStream)

Semblable à l'approche ci-dessus, cette approche permet également de joindre deux fichiers PDF. Les deux premiers arguments (firstInputStream et secInputStream) fournissent les deux fichiers PDF d'entrée sous forme de flux (un flux est un tableau de bits/octets) à concaténer. Le troisième argument (outputStream) fournit la représentation en flux du fichier PDF de sortie souhaité.

![Concaténer deux PDFs en utilisant des flux de fichiers](how-to-concatenate-pdf-files-in-different-ways_7.png)

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

### Approche 3

- Concatenate(Stream inputStreams[], Stream outputStream)

Si vous souhaitez joindre plus de deux fichiers PDF, cette approche serait votre choix ultime. Le premier argument (inputStreams[]) fournit les fichiers PDF d'entrée sous forme de tableau de flux à concaténer. Le deuxième argument (outputStream) fournit la représentation en flux du fichier PDF de sortie souhaité.

![Concaténer plusieurs PDFs en utilisant un tableau de flux](how-to-concatenate-pdf-files-in-different-ways_8.png)

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