---
title:  Extraire les données d'AcroForm
linktitle:  Extraire les données d'AcroForm
type: docs
weight: 50
url: /fr/androidjava/extract-data-from-acroform/
description: Les AcroForms existent dans de nombreux documents PDF. Cet article vise à vous aider à comprendre comment extraire les données des AcroForms avec Aspose.PDF.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire les champs de formulaire du document PDF

Aspose.PDF for Android via Java vous permet non seulement de créer et remplir des champs de formulaire, mais facilite également l'extraction des données des champs de formulaire ou des informations sur les champs de formulaire à partir de fichiers PDF.

Supposons que nous ne connaissions pas les noms des champs de formulaire à l'avance. Nous devons alors parcourir chaque page du PDF pour extraire les informations sur tous les AcroForms du PDF ainsi que les valeurs des champs de formulaire. Pour accéder au formulaire, nous devons utiliser [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) méthode.

```java
 public void extractFormFields () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get values from all fields
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```

Si vous connaissez le nom des champs de formulaire dont vous souhaitez extraire les valeurs, vous pouvez alors utiliser l'indexeur dans la collection Documents.Form pour récupérer rapidement ces données.

## Récupérer la valeur du champ de formulaire par titre

La propriété Value du form field\u0027s vous permet d'obtenir la valeur d'un champ particulier. Pour obtenir la valeur, récupérez le champ de formulaire depuis le [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objet [collection de champs de formulaire](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). Cet exemple sélectionne un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) et récupère sa valeur en utilisant le [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) méthode.

```java

    public void extractFormDataByName () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```

## Extraire des données en XML à partir d'un fichier PDF

La classe Form vous permet d'exporter des données vers un fichier XML à partir du fichier PDF à l'aide de la méthode ExportXml. Pour exporter des données vers XML, vous devez créer un objet de la classe Form, puis appeler la méthode ExportXml en utilisant l'objet FileStream. Enfin, vous pouvez fermer l'objet FileStream et libérer l'objet Form. Le fragment de code suivant vous montre comment exporter des données vers un fichier XML.

```java
public void extractFormFieldsToXML () {
        // Open document
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
            // Create xml file.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Export data
            form.exportXml(xmlOutputStream);

            // Close file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Close the document
        form.dispose();
    }
```

## Exporter les données au format FDF depuis un fichier PDF

Pour exporter les données des formulaires PDF vers un fichier XFDF, nous pouvons utiliser le [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) méthode dans le [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) classe.

Veuillez noter que c'est une classe de `com.aspose.pdf.facades`. Malgré le nom similaire, cette classe a un but légèrement différent.

Pour exporter des données vers le FDF, vous devez créer un objet de `Form` classe et ensuite appeler le `exportXfdf` méthode utilisant le `OutputStream` objet. Le fragment de code suivant vous montre comment exporter des données vers un fichier XFDF.

```java
public void extractFormExportFDF () {
        // Open document
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

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Exporter les données en XFDF depuis un fichier PDF

Pour exporter les données des formulaires PDF vers un fichier XFDF, nous pouvons utiliser le [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) méthode dans le [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) classe.

Afin d'exporter des données vers XFDF, vous devez créer un objet de `Form` classe et ensuite appeler le `exportXfdf` méthode utilisant le `OutputStream` objet. 
Le fragment de code suivant vous montre comment exporter des données vers un fichier XFDF.

```java
    public void extractFormExportXFDF () {
        // Open document
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

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

