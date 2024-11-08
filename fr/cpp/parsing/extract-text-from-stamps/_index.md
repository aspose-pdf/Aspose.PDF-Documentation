---
title: Extraire du Texte à partir de Tampons
linktitle: Extraire du Texte à partir de Tampons
type: docs
weight: 60
url: /fr/cpp/extract-text-from-stamps/
---

## Extraire du Texte des Annotations de Tampons

Aspose.PDF pour C++ vous permet d'extraire du texte à partir des annotations de tampons. Pour extraire du texte des annotations de tampons dans un PDF, les étapes suivantes peuvent être utilisées.

1. Créer un objet de la classe Document
1. Obtenir l'annotation souhaitée à partir de la liste des annotations d'une page
1. Définir un nouvel objet de la classe TextAbsorber
1. Utiliser la méthode visit du TextAbsorber pour obtenir le texte

```cpp
void Parsing::ExtractTextFromStamp()
{
      std::clog << __func__ << ": Start" << std::endl;
      // Chaîne pour le nom de chemin
      String _dataDir("C:\\Samples\\Parsing\\");

      // Chaîne pour le nom de fichier
      String infilename("ExtractStampText.pdf");

      auto document = MakeObject<Document>(_dataDir + infilename);

      auto item = document->get_Pages()->idx_get(1)->get_Annotations()->idx_get(1);
      if (item->get_AnnotationType() == Annotations::AnnotationType::Stamp) {
            auto annot = System::DynamicCast<Aspose::Pdf::Annotations::StampAnnotation>(item);
            auto ta = MakeObject<TextAbsorber>();
            auto ap = annot->get_Appearance()->idx_get(u"N");
            ta->Visit(ap);
            Console::WriteLine(ta->get_Text());
      }
}
```