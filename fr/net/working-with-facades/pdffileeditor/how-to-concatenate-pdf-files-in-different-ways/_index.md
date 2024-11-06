---
title: Fusionner des fichiers PDF en utilisant .NET 5 
linktitle: Comment fusionner des PDF
type: docs
weight: 75
url: fr/net/how-to-concatenate-pdf-files-in-different-ways/
description: Cet article explique les différentes manières de concaténer un nombre quelconque de fichiers PDF existants en un seul fichier PDF.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Cet article décrit comment vous pouvez [Concaténer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) plusieurs documents PDF en un seul document PDF à l'aide du composant [Aspose.PDF for .NET](/pdf/net/). [Aspose.PDF for .NET](/pdf/net/) rend cette tâche comme un jeu d'enfant.

{{% /alert %}}

Tout ce que vous avez à faire est d'appeler la méthode [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) et tous vos fichiers PDF d'entrée seront concaténés ensemble et un seul fichier PDF sera généré. Let's create an application to practice the concatenation of PDF files. We will create an application using Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF for .NET peut être utilisé dans tout type d'application fonctionnant sur le .NET Framework, que ce soit une application web ASP.NET ou une application Windows

{{% /alert %}}

## Comment concaténer des fichiers PDF de différentes manières

Dans le formulaire, il y a trois Text Boxes (textBox1, textBox2, textBox3) ayant leurs Link Labels respectifs (linkLabel1, linkLabel2, linkLabel3) pour parcourir les fichiers PDF. En cliquant sur le Link Label "Browse", une boîte de dialogue de fichier d'entrée (inputFileDialog1) apparaîtra, ce qui nous permettra de choisir les fichiers PDF (à concaténer).

```csharp

private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
  if(openFileDialog1.ShowDialog()==DialogResult.OK)
  {
     textBox1.Text=openFileDialog1.FileName;
  }
}
```

Une vue de l'application Windows Form est présentée pour la démonstration de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) pour la concaténation de fichiers PDF.
![Concatenate PDF Files](how-to-concatenate-pdf-files-in-different-ways_1.png)

Après avoir choisi le fichier PDF et cliqué sur le bouton OK. Le nom complet du fichier avec le chemin est attribué à la zone de texte correspondante.

![Choose the PDF file](how-to-concatenate-pdf-files-in-different-ways_2.png)

De même, nous pouvons choisir deux ou trois fichiers PDF d'entrée à concaténer comme indiqué ci-dessous :

![Choose two or three Input PDF Files](how-to-concatenate-pdf-files-in-different-ways_3.png)

La dernière zone de texte (textBox4) prendra le chemin de destination du fichier PDF de sortie avec son nom où ce fichier de sortie sera créé.

![Destination Path of the Output PDF file](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Concatenate method](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Méthode Concatenate()

La méthode Concatenate() peut être utilisée de trois manières. Examinons de plus près chacune d'elles :

### Approche 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Cette approche est bonne uniquement si vous avez besoin de joindre seulement deux fichiers PDF. Les deux premiers arguments (firstInputFile et secInputFile) fournissent les noms complets des fichiers avec leur chemin de stockage des deux fichiers PDF d'entrée qui doivent être concaténés. Le troisième argument (outputFile) fournit le nom de fichier souhaité avec le chemin du fichier PDF de sortie.

![Concaténer deux PDFs en utilisant les noms de fichiers](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
  PdfFileEditor pdfEditor = new PdfFileEditor();
  pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Approche 2

- Concatenate(System.IO.Stream firstInputStream, System.IO.Stream secInputStream, System.IO.Stream outputStream)

Similaire à l'approche ci-dessus, cette approche permet également de joindre deux fichiers PDF. Les deux premiers arguments (firstInputStream et secInputStream) fournissent les deux fichiers PDF d'entrée sous forme de flux (un flux est un tableau de bits/octets) qui doivent être concaténés. Le troisième argument (outputStream) fournit la représentation en flux du fichier PDF de sortie souhaité.

![Concaténer deux PDFs en utilisant des flux de fichiers](how-to-concatenate-pdf-files-in-different-ways_7.png)

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

### Approche 3

- Concatenate(System.IO.Stream inputStreams[], System.IO.Stream outputStream)

Si vous souhaitez joindre plus de deux fichiers PDF, alors cette approche serait votre choix ultime. First argument (inputStreams[]) fournit les fichiers PDF d'entrée sous forme de tableau de flux qui doivent être concaténés. Second argument (outputStream) fournit la représentation du flux du fichier PDF de sortie souhaité.

![Concaténer plusieurs PDF en utilisant un tableau de flux](how-to-concatenate-pdf-files-in-different-ways_8.png)

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