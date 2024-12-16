---
title: Extraire des données d'AcroForm 
linktitle: Extraire des données d'AcroForm
type: docs
weight: 50
url: /fr/cpp/extract-data-from-acroform/
description: Aspose.PDF facilite l'extraction des données des champs de formulaire à partir de fichiers PDF. Apprenez à extraire des données d'AcroForms et à les enregistrer au format XML ou FDF.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire les champs de formulaire du document PDF

Aspose.PDF pour C++ vous permet non seulement de créer des champs de formulaire et de remplir des champs de formulaire, mais aussi de faciliter l'extraction des données des champs de formulaire ou des informations des champs de formulaire à partir de fichiers PDF.

Dans l'exemple de code ci-dessous, nous démontrons comment itérer sur chaque page d'un PDF pour extraire des informations sur tous les AcroForms dans le PDF ainsi que les valeurs des champs de formulaire. Cet exemple de code suppose que vous ne connaissez pas à l'avance les noms des champs de formulaire.

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom du fichier
    String infilename("StudentInfoFormElectronic.pdf");

    // Ouvrir le document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Obtenez les valeurs de tous les champs
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "Nom du champ :" << formField->get_PartialName() << std::endl;
        std::cout << "Valeur : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extraire des données vers XML à partir d'un fichier PDF

La classe [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) vous permet d'exporter des données vers un fichier XML à partir du fichier PDF en utilisant la méthode ExportXml. Pour exporter des données vers XML, vous devez créer un objet de la classe Form et ensuite appeler la méthode ExportXml en utilisant l'objet FileStream. Ensuite, vous devez fermer l'objet FileStream et disposer de l'objet Form.

Le code suivant vous montre comment exporter des données vers un fichier XML.

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // String pour le nom de chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // String pour le nom de fichier
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // Exporter les données
    form->ExportXml(fdfOutputStream);

    // Fermer le flux de fichier
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Exporter des données vers FDF à partir d'un fichier PDF

La classe [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) vous permet d'exporter des données vers un fichier FDF à partir du fichier PDF en utilisant la méthode ExportFdf. Afin d'exporter des données vers FDF, vous devez créer un objet de la classe Form puis appeler la méthode ExportFdf en utilisant l'objet FileStream. Ensuite, vous pouvez enregistrer le fichier PDF en utilisant la méthode Save de la classe Form.

L'extrait de code suivant vous montre comment exporter des données vers un fichier FDF.

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne de caractères pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne de caractères pour le nom du fichier
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    // Chaîne de caractères fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Exporter des données
    form->ExportFdf(fdfOutputStream);

    // Fermer le flux de fichier
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Exporter des données vers XFDF à partir d'un fichier PDF

Aspose PDF pour C++ avec la classe [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) vous permet d'exporter des données vers un fichier XFDF à partir du fichier PDF en utilisant la méthode ExportXfdf. Afin d'exporter des données vers XFDF, vous devez créer un objet de la classe Form puis appeler la méthode ExportXfdf en utilisant l'objet FileStream.

À la fin, vous pouvez enregistrer le fichier PDF en utilisant la méthode Save de la classe Form.

Le fragment de code suivant vous montre comment exporter des données vers un fichier XFDF.

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // Chaîne pour le nom du chemin
    String _dataDir("C:\\Samples\\Parsing\\");

    // Chaîne pour le nom du fichier
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Exporter des données
    form->ExportXfdf(fdfOutputStream);

    // Fermer le flux de fichiers
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```