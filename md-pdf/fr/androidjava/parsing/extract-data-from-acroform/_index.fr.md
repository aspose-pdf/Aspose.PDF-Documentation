---
title:  Extraire des données d'AcroForm 
linktitle:  Extraire des données d'AcroForm
type: docs
weight: 50
url: /androidjava/extract-data-from-acroform/
description: Les AcroForms existent dans de nombreux documents PDF. Cet article vise à vous aider à comprendre comment extraire des données d'AcroForms avec Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire les champs de formulaire d'un document PDF

Aspose.PDF pour Android via Java vous permet non seulement de créer et de remplir des champs de formulaire, mais aussi de faciliter l'extraction des données ou des informations des champs de formulaire à partir de fichiers PDF.

Supposons que nous ne connaissions pas à l'avance les noms des champs de formulaire. Nous devrions alors parcourir chaque page du PDF pour extraire des informations sur tous les AcroForms dans le PDF ainsi que les valeurs des champs de formulaire. Pour accéder au formulaire, nous devons utiliser la méthode [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
 public void extractFormFields () {
        // Ouvrir le document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obtenir les valeurs de tous les champs
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Nom du champ : ");
            sb.append(formField.getPartialName());
            sb.append(" Valeur : ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```


Si vous connaissez le nom des champs de formulaire dont vous souhaitez extraire les valeurs, vous pouvez utiliser l'indexeur dans la collection Documents.Form pour récupérer rapidement ces données.

## Récupérer la valeur d'un champ de formulaire par titre

La propriété Value du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier. Pour obtenir la valeur, récupérez le champ de formulaire à partir de la [collection de champs de formulaire](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Cet exemple sélectionne un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) et récupère sa valeur en utilisant la méthode [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java

    public void extractFormDataByName () {
        // Ouvrir le document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Nom de famille : " + textBoxField1.getValue());

    }
```


## Extraire des données vers XML à partir d'un fichier PDF

La classe Form vous permet d'exporter des données vers un fichier XML à partir du fichier PDF en utilisant la méthode ExportXml. Pour exporter des données vers XML, vous devez créer un objet de la classe Form puis appeler la méthode ExportXml en utilisant l'objet FileStream. Enfin, vous pouvez fermer l'objet FileStream et disposer de l'objet Form. Le code suivant vous montre comment exporter des données vers un fichier XML.

```java
public void extractFormFieldsToXML () {
        // Ouvrir le document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // Créer un fichier XML.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Exporter les données
            form.exportXml(xmlOutputStream);

            // Fermer le flux de fichier
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Fermer le document
        form.dispose();
    }
```


## Exporter des données vers FDF à partir d'un fichier PDF

Pour exporter les données de formulaires PDF vers un fichier XFDF, nous pouvons utiliser la méthode [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) dans la classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Veuillez noter qu'il s'agit d'une classe de `com.aspose.pdf.facades`. Malgré le nom similaire, cette classe a un objectif légèrement différent.

Pour exporter des données vers FDF, vous devez créer un objet de la classe `Form` puis appeler la méthode `exportXfdf` en utilisant l'objet `OutputStream`. Le code suivant vous montre comment exporter des données vers un fichier XFDF.

```java
public void extractFormExportFDF () {
        // Ouvrir le document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Exporter les données
            form.exportFdf(fdfOutputStream);

            // Fermer le flux de fichier
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Exporter des données vers XFDF à partir d'un fichier PDF

Pour exporter les données des formulaires PDF vers un fichier XFDF, nous pouvons utiliser la méthode [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) dans la classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Afin d'exporter des données vers XFDF, vous devez créer un objet de la classe `Form` puis appeler la méthode `exportXfdf` en utilisant l'objet `OutputStream`.
Le fragment de code suivant vous montre comment exporter des données vers un fichier XFDF.

```java
    public void extractFormExportXFDF () {
        // Ouvrir le document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // Exporter les données
            form.exportXfdf(fdfOutputStream);

            // Fermer le flux de fichier
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```