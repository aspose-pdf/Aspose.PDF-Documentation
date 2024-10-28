---
title: Extraer Texto de Sellos
linktitle: Extraer Texto de Sellos
type: docs
weight: 60
url: /cpp/extract-text-from-stamps/
---

## Extraer Texto de Anotaciones de Sello

Aspose.PDF para C++ te permite extraer texto de anotaciones de sello. Para extraer texto de Anotaciones de Sello en un PDF, se pueden usar los siguientes pasos.

1. Crear un objeto de la clase Document
1. Obtener la anotación deseada de la lista de anotaciones de una página
1. Definir un nuevo objeto de la clase TextAbsorber
1. Usar el método visit de TextAbsorber para obtener el texto

```cpp
void Parsing::ExtractTextFromStamp()
{
      std::clog << __func__ << ": Start" << std::endl;
      // Cadena para el nombre de la ruta
      String _dataDir("C:\\Samples\\Parsing\\");

      // Cadena para el nombre del archivo
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