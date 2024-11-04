---
title: Ajouter, Supprimer et Obtenir des Annotations - Facades
type: docs
weight: 10
url: /cpp/add-delete-and-get-annotation-facades/
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

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-AddAnnotation-AddAnnotation.cpp" >}}
## <ins>**Supprimer toutes les annotations d'un PDF existant**
Aspose.PDF pour C++ a également fourni la classe **PdfAnnotationEditor**, qui vous permet de supprimer toutes les annotations d'un document PDF. Afin de supprimer toutes les annotations du PDF existant, vous devez créer un objet de la classe **PdfAnnotationEditor** et ouvrir le document existant. Après cela, vous pouvez utiliser la méthode **DeleteAnnotations(...)** de la classe PdfAnnotationEditor pour supprimer les annotations. Le code suivant vous montre l'utilisation de PdfAnnotationEditor pour atteindre cet objectif :



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteAllAnnotations-1.cpp" >}}
## <ins>**Supprimer toutes les annotations par type spécifié**
Vous pouvez utiliser la classe **PdfAnnotationEditor** pour supprimer toutes les annotations, par un type d'annotation spécifié, du fichier PDF existant. Afin de faire cela, vous devez créer un objet **PdfAnnotationEditor** et lier le fichier PDF d'entrée en utilisant la méthode **BindPdf**. Après cela, appelez la méthode **DeleteAnnotations**, avec le paramètre de chaîne, pour supprimer toutes les annotations du fichier ; le paramètre de chaîne représente le type d'annotation à supprimer. Enfin, utilisez la méthode **Save** pour enregistrer le fichier PDF mis à jour. L'extrait de code suivant vous montre comment supprimer toutes les annotations par type d'annotation spécifié.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteParticularAnnotation-1.cpp" >}}
## <ins>**Mettre à jour/Modifier les annotations dans un fichier PDF existant**
Pour mettre à jour modifier une annotation dans un document PDF, vous pouvez utiliser la méthode **ModifyAnnotations(...)** de la classe **PdfAnnotationEditor** qui prend un objet Annotation ainsi que l'index de début et de fin des annotations. L'extrait de code suivant démontrera l'utilisation de la méthode **ModifyAnnotations(...)** :

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ModifyAnnotations-1.cpp" >}}## <ins>**Importer des annotations depuis XFDF dans un fichier PDF**

La méthode **ImportAnnotationFromXfdf** de la classe **PdfAnnotationEditor** vous permet d'importer des annotations dans un fichier PDF. Pour importer des annotations, vous devez créer un objet **PdfAnnotationEditor** et lier le fichier PDF en utilisant la méthode **BindPdf**. Après cela, vous devez créer une énumération des types d'annotations que vous souhaitez importer dans le fichier PDF. Vous pouvez ensuite utiliser la méthode **ImportAnnotationFromXfdf** pour importer les annotations. Et enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode **Save** de l'objet **PdfAnnotationEditor**. Le code suivant vous montre comment importer des annotations à partir du fichier XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ImportAnnotations-1.cpp" >}}
## **Exporter des annotations depuis un fichier PDF vers XFDF**

La méthode **ExportAnnotationXfdf** vous permet d'exporter des annotations depuis un fichier PDF. Afin d'exporter des annotations, vous devez créer un objet **PdfAnnotationEditor** et lier le fichier PDF en utilisant la méthode **BindPdf**. Après cela, vous devez créer une énumération des types d'annotations que vous souhaitez exporter du fichier PDF. Vous pouvez ensuite utiliser la méthode **ExportAnnotationXfdf** pour importer les annotations. Et enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode **Save** de l'objet **PdfAnnotationEditor**. Le code suivant vous montre comment exporter des annotations vers le fichier XFDF.

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExportAnnotations-1.cpp" >}}
## <ins>**Extraire des annotations d'un fichier PDF existant**
La méthode **ExtractAnnotations** vous permet d'extraire des annotations d'un fichier PDF. Afin d'extraire des annotations, vous devez créer un objet **PdfAnnotationEditor** et lier le fichier PDF en utilisant la méthode **BindPdf**. Après cela, vous devez créer une énumération des types d'annotations que vous souhaitez extraire des fichiers PDF. Vous pouvez ensuite utiliser la méthode **Extract Annotations** pour extraire les annotations vers un ArrayPtr. Ensuite, vous pouvez parcourir cette liste et obtenir des annotations individuelles. Et enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode **Save** de l'objet **PdfAnnotationEditor**. Le extrait de code suivant vous montre comment extraire des annotations à partir de fichiers PDF.



{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExtractAnnotations-1.cpp" >}}