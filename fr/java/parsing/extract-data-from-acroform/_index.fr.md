---
title:  Extraire des données d'AcroForm 
linktitle:  Extraire des données d'AcroForm
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: Les AcroForms existent dans de nombreux documents PDF. Cet article vise à vous aider à comprendre comment extraire des données des AcroForms en utilisant Java et Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire les champs de formulaire d'un document PDF

Aspose.PDF pour Java vous permet non seulement de créer et de remplir des champs de formulaire, mais facilite également l'extraction des données ou des informations des champs de formulaire à partir de fichiers PDF.

Supposons que nous ne connaissons pas les noms des champs de formulaire à l'avance. Nous devrons alors parcourir chaque page du PDF pour extraire des informations sur tous les AcroForms dans le PDF ainsi que les valeurs des champs de formulaire. Pour accéder au formulaire, nous devons utiliser la méthode [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // Obtenez les valeurs de tous les champs
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("Nom du champ :" + formField.getPartialName());
        System.out.println("Valeur : " + formField.getValue());
    }
}
```


Si vous connaissez le nom des champs de formulaire dont vous souhaitez extraire les valeurs, vous pouvez utiliser l'indexeur dans la collection Documents.Form pour récupérer rapidement ces données.

## Récupérer la valeur d'un champ de formulaire par titre

La propriété Value du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier. Pour obtenir la valeur, récupérez le champ de formulaire de la [collection de champs de formulaire](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Cet exemple sélectionne un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) et récupère sa valeur en utilisant la méthode [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Last Name :" + textBoxField1.getValue());
}
```


## Extraire les champs de formulaire d'un document PDF vers JSON

Pour exporter les données de formulaire vers JSON, nous recommandons d'utiliser une bibliothèque tierce comme [Gson](https://github.com/google/gson). Les extraits suivants montrent comment exporter `Name` et `Value` vers JSON :

```java
public static void ExtractFormFieldsToJson() {
    String path = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);

    java.util.List<FormElement> formData = new java.util.ArrayList<FormElement>();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        formData.add(new FormElement(formField.getPartialName(), formField.getValue()));
    }

    Gson gson = new Gson();
    String jsonString = gson.toJson(formData);
    System.out.println(jsonString);
}
```

Dans cet exemple, nous avons utilisé une classe supplémentaire

```java
public class FormElement {
    public FormElement(String partialName, String Value) {
        this.Name = partialName;
        this.Value = Value;
    }
    public String Name;
    public String Value;
}
```


## Extraire des données vers XML à partir d'un fichier PDF

La classe Form permet d'exporter des données vers un fichier XML à partir du fichier PDF en utilisant la méthode ExportXml. Pour exporter des données vers XML, vous devez créer un objet de la classe Form, puis appeler la méthode ExportXml en utilisant l'objet FileStream. Enfin, vous pouvez fermer l'objet FileStream et disposer de l'objet Form. Le snippet de code suivant vous montre comment exporter des données vers un fichier XML.

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // Ouvrir le document
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // Créer un fichier XML.
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // Exporter les données
        form.exportXml(xmlOutputStream);

        // Fermer le flux de fichiers
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // Fermer le document
    form.dispose();
    ;
}
```


## Exporter des données vers FDF à partir d'un fichier PDF

Pour exporter les données des formulaires PDF vers un fichier XFDF, nous pouvons utiliser la méthode [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) dans la classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Veuillez noter qu'il s'agit d'une classe de `com.aspose.pdf.facades`. Malgré le nom similaire, cette classe a un objectif légèrement différent.

Pour exporter des données vers FDF, vous devez créer un objet de la classe `Form` puis appeler la méthode `exportXfdf` en utilisant l'objet `OutputStream`. Le fragment de code suivant vous montre comment exporter des données vers un fichier XFDF.

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Exporter les données
            form.exportFdf(fdfOutputStream);

            // Fermer le flux de fichiers
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: gérer l'exception
            e.printStackTrace();
        }

    }
```


## Exporter des données vers XFDF à partir d'un fichier PDF

Pour exporter les données des formulaires PDF vers un fichier XFDF, nous pouvons utiliser la méthode [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) dans la classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Afin d'exporter des données vers XFDF, vous devez créer un objet de la classe `Form` puis appeler la méthode `exportXfdf` en utilisant l'objet `OutputStream`. 
Le snippet de code suivant vous montre comment exporter des données vers un fichier XFDF.

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // Exporter les données
            form.exportXfdf(fdfOutputStream);

            // Fermer le flux de fichier
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: gérer l'exception
            e.printStackTrace();
        }
    }
```