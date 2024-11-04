---
title: Déplacer des Pages PDF par programmation C++
linktitle: Déplacer des Pages PDF
type: docs
weight: 20
url: /cpp/move-pages/
description: Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF en utilisant Aspose.PDF pour C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Déplacer une Page d'un Document PDF à un Autre

Déplacer des pages PDF dans un document est une tâche très intéressante et populaire.
Ce sujet explique comment déplacer une page d'un document PDF à la fin d'un autre document en utilisant C++.
Pour déplacer une page, nous devons :

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le fichier PDF source.
1. Obtenir une Page de la collection [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Ajouter](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) la page au document de destination.
1. Enregistrer le PDF de sortie en utilisant la méthode Save.
1. [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) page dans le document source.
1. Enregistrez le PDF source à l'aide de la méthode Save.

L'extrait de code suivant vous montre comment déplacer une page.

```cpp
void MovePage()
{
    // Ouvrir le document
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    dstDocument->get_Pages()->Add(page);
    // Enregistrer le fichier de sortie
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(dstFileName);
}
```

## Déplacement d'un ensemble de pages d'un document PDF à un autre

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le fichier PDF source.
1. Définissez un tableau avec les numéros de pages à déplacer.
1. Exécuter la boucle à travers le tableau :
1. Obtenez Page de la collection de [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Ajoutez](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) la page au document de destination.
1. Enregistrez le PDF de sortie en utilisant la méthode Save.
1. [Supprimez](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) la page dans le document source.
1. Enregistrez le PDF source en utilisant la méthode Save.

L'extrait de code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```cpp
void MoveBunchPages()
{
    // Ouvrir le document
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();


    auto pages = MakeArray<int>({ 1,3 });

    for (auto pageIndex : pages)
    {
        auto page = srcDocument->get_Pages()->idx_get(pageIndex);
        dstDocument->get_Pages()->Add(page);
    }
    // Enregistrez les fichiers de sortie
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete();
    srcDocument->Save(dstFileName);
}
```
## Déplacer une Page à un nouvel emplacement dans le document PDF actuel

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) avec le fichier PDF source.
1. Obtenez la page de la collection [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Ajoutez](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) la page au nouvel emplacement (par exemple à la fin).
1. [Supprimez](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) la page à l'emplacement précédent.
1. Enregistrez le PDF de sortie en utilisant la méthode Save.

```cpp
void MovePagesInOnePDF()
{
    // Ouvrir le document
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    srcDocument->get_Pages()->Add(page);
    srcDocument->get_Pages()->Delete(2);

    // Enregistrer le fichier de sortie
    srcDocument->Save(dstFileName);
}
```