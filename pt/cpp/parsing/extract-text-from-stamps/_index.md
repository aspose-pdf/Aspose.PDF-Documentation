---
title: Extrair Texto De Carimbos 
linktitle: Extrair Texto De Carimbos
type: docs
weight: 60
url: pt/cpp/extract-text-from-stamps/
---

## Extrair Texto de Anotações de Carimbo

Aspose.PDF para C++ permite que você extraia texto de anotações de carimbo. Para extrair texto de Anotações de Carimbo em um PDF, os seguintes passos podem ser utilizados.

1. Crie um objeto da classe Document
1. Obtenha a Anotação desejada da lista de anotações de uma página
1. Defina um novo objeto da classe TextAbsorber
1. Use o método visit do TextAbsorber para obter o Texto

```cpp
void Parsing::ExtractTextFromStamp()
{
      std::clog << __func__ << ": Start" << std::endl;
      // String para nome do caminho
      String _dataDir("C:\\Samples\\Parsing\\");

      // String para nome do arquivo
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