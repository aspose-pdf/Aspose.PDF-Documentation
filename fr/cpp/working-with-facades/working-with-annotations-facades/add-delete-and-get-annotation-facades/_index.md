---
title: Ajouter, Supprimer et Obtenir des Annotations - Facades
type: docs
weight: 10
url: /fr/cpp/add-delete-and-get-annotation-facades/
---

## <ins>**Ajouter une Annotation dans un fichier PDF existant en utilisant PdfContentEditor**
**PdfContentEditor** vous permet d'ajouter différents types d'annotations dans un fichier PDF existant. Vous pouvez utiliser la méthode respective de la classe **PdfContentEditor** pour ajouter un type particulier d'annotation dans un document PDF existant. Par exemple, dans les extraits de code suivants, nous avons utilisé les méthodes **CreateText(...)** et **CreateFreeText(...)**, pour ajouter respectivement des commentaires et une annotation de texte libre dans le PDF existant. Vous devez suivre les étapes suivantes, afin d'ajouter des annotations en utilisant la classe **PdfContentEditor** :

- Créer un objet de Facades::PdfContentEditor.
- Utiliser la méthode **BindPdf(...)** pour charger un PDF existant.
- Appeler la méthode respective pour créer une annotation. e.g **CreateText(...),CreateFreeText(...), etc.**
- Enregistrer le document PDF en utilisant la méthode **Save(...)**.
### **Ajouter des Commentaires à un Document PDF Existant**

L'extrait de code suivant vous montre comment ajouter un commentaire dans un fichier PDF existant.
```

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto editor = MakeObject<Facades::PdfContentEditor>();
editor->BindPdf(L"..\\Data\\Annotations\\input.pdf");

editor->CreateText(System::Drawing::Rectangle(400, 700, 100, 100), L"Title", L"Welcome to Aspose", true, L"Comment", 1);	
editor->Save(L"..\\Data\\Annotations\\input_out.pdf");
```
## <ins>**Supprimer toutes les annotations d'un PDF existant**
Aspose.PDF pour C++ a également fourni la classe **PdfAnnotationEditor**, qui vous permet de supprimer toutes les annotations d'un document PDF. Afin de supprimer toutes les annotations du PDF existant, vous devez créer un objet de la classe **PdfAnnotationEditor** et ouvrir le document existant. Après cela, vous pouvez utiliser la méthode **DeleteAnnotations(...)** de la classe PdfAnnotationEditor pour supprimer les annotations. Le code suivant vous montre l'utilisation de PdfAnnotationEditor pour atteindre cet objectif :



```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Annotations\\DeleteAllAnnotations.pdf");
// Delete All Annotations
editor->DeleteAnnotations();
// Save the document
editor->Save(L"..\\Data\\Annotations\\DeleteAllAnnotations_out.pdf");
```
## <ins>**Supprimer toutes les annotations par type spécifié**
Vous pouvez utiliser la classe **PdfAnnotationEditor** pour supprimer toutes les annotations, par un type d'annotation spécifié, du fichier PDF existant. Afin de faire cela, vous devez créer un objet **PdfAnnotationEditor** et lier le fichier PDF d'entrée en utilisant la méthode **BindPdf**. Après cela, appelez la méthode **DeleteAnnotations**, avec le paramètre de chaîne, pour supprimer toutes les annotations du fichier ; le paramètre de chaîne représente le type d'annotation à supprimer. Enfin, utilisez la méthode **Save** pour enregistrer le fichier PDF mis à jour. L'extrait de code suivant vous montre comment supprimer toutes les annotations par type d'annotation spécifié.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load an existing PDF document
editor->BindPdf(L"..\\Data\\Annotations\\DeleteAllAnnotations.pdf");
// Delete All Text Annotations
editor->DeleteAnnotations(L"Text");
// Save the document
editor->Save(L"..\\Data\\Annotations\\DeleteAllAnnotations_out.pdf");
```
## <ins>**Mettre à jour/Modifier les annotations dans un fichier PDF existant**
Pour mettre à jour modifier une annotation dans un document PDF, vous pouvez utiliser la méthode **ModifyAnnotations(...)** de la classe **PdfAnnotationEditor** qui prend un objet Annotation ainsi que l'index de début et de fin des annotations. L'extrait de code suivant démontrera l'utilisation de la méthode **ModifyAnnotations(...)** :

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
auto doc = MakeObject <Aspose::Pdf::Document>(L"..\\Data\\Annotations\\input.pdf");
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor =  System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load an existing PDF document
editor->BindPdf(doc);
// Create an annotation object
System::SharedPtr<Aspose::Pdf::InteractiveFeatures::Annotations::TextAnnotation> annot = System::MakeObject<Aspose::Pdf::InteractiveFeatures::Annotations::TextAnnotation>(doc->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(200, 400, 400, 600));
// Set modified date
annot->set_Modified(System::DateTime::get_Now());
// Set Title
annot->set_Title(L"NEW AUTHOR");
// Set Content
annot->set_Contents(L"NEW CONTENTS");
// Set Color
annot->set_Color(Color::get_Red());
// Set Object
annot->set_Subject(L"NEW SUBJECT");
// Set open flag
annot->set_Open(true);
// Modify Annotation
editor->ModifyAnnotations(1, 1, annot);
// Save the document
editor->Save(L"..\\Data\\Annotations\\output_out.pdf");
```## <ins>**Importer des annotations depuis XFDF dans un fichier PDF**

La méthode **ImportAnnotationFromXfdf** de la classe **PdfAnnotationEditor** vous permet d'importer des annotations dans un fichier PDF. Pour importer des annotations, vous devez créer un objet **PdfAnnotationEditor** et lier le fichier PDF en utilisant la méthode **BindPdf**. Après cela, vous devez créer une énumération des types d'annotations que vous souhaitez importer dans le fichier PDF. Vous pouvez ensuite utiliser la méthode **ImportAnnotationFromXfdf** pour importer les annotations. Et enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode **Save** de l'objet **PdfAnnotationEditor**. Le code suivant vous montre comment importer des annotations à partir du fichier XFDF.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load Document where you want to import document
editor->BindPdf(L"..\\Data\\Annotations\\ImportAnnotations.pdf");
// Import annotations from XFDF file
editor->ImportAnnotationFromXfdf(L"..\\Data\\Annotations\\annotations.xfdf");
// Save the document
editor->Save(L"..\\Data\\Annotations\\ImportAnnotations_out.pdf");
```
## **Exporter des annotations depuis un fichier PDF vers XFDF**

La méthode **ExportAnnotationXfdf** vous permet d'exporter des annotations depuis un fichier PDF. Afin d'exporter des annotations, vous devez créer un objet **PdfAnnotationEditor** et lier le fichier PDF en utilisant la méthode **BindPdf**. Après cela, vous devez créer une énumération des types d'annotations que vous souhaitez exporter du fichier PDF. Vous pouvez ensuite utiliser la méthode **ExportAnnotationXfdf** pour importer les annotations. Et enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode **Save** de l'objet **PdfAnnotationEditor**. Le code suivant vous montre comment exporter des annotations vers le fichier XFDF.

```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load Document where you want to import document
editor->BindPdf(L"..\\Data\\Annotations\\ExportAnnotations.pdf");
System::ArrayPtr<System::String> annotTypes = System::MakeArray<System::String>({ L"Text", L"Highlight" });
{
	System::SharedPtr<System::IO::Stream> stream = System::IO::File::Create(L"..\\Data\\Annotations\\Exported_out.xfdf");
	editor->ExportAnnotationsXfdf(stream, 1, 2, annotTypes);
}
```
## <ins>**Extraire des annotations d'un fichier PDF existant**
La méthode **ExtractAnnotations** vous permet d'extraire des annotations d'un fichier PDF. Afin d'extraire des annotations, vous devez créer un objet **PdfAnnotationEditor** et lier le fichier PDF en utilisant la méthode **BindPdf**. Après cela, vous devez créer une énumération des types d'annotations que vous souhaitez extraire des fichiers PDF. Vous pouvez ensuite utiliser la méthode **Extract Annotations** pour extraire les annotations vers un ArrayPtr. Ensuite, vous pouvez parcourir cette liste et obtenir des annotations individuelles. Et enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode **Save** de l'objet **PdfAnnotationEditor**. Le extrait de code suivant vous montre comment extraire des annotations à partir de fichiers PDF.



```cpp
For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-C
System::SharedPtr<Aspose::Pdf::Facades::PdfAnnotationEditor> editor = System::MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();
// Load Document where you want to import document
editor->BindPdf(L"..\\Data\\Annotations\\ExtractAnnotations.pdf");
System::ArrayPtr<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType> annotTypes = System::MakeArray<Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType>({ Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Text, Aspose::Pdf::InteractiveFeatures::Annotations::AnnotationType::Highlight }); 
// Extract Annotations
System::SharedPtr<System::Collections::Generic::IList<System::SharedPtr<Aspose::Pdf::InteractiveFeatures::Annotations::Annotation>>> annotList = editor->ExtractAnnotations(1, 2, annotTypes);
```