---
title: Извлечение текста из штампов
linktitle: Извлечение текста из штампов
type: docs
weight: 60
url: /ru/cpp/extract-text-from-stamps/
---

## Извлечение текста из аннотаций штампов

Aspose.PDF for C++ позволяет извлекать текст из аннотаций штампов. Чтобы извлечь текст из аннотаций штампов в PDF, можно использовать следующие шаги.

1. Создайте объект класса Document
1. Получите желаемую аннотацию из списка аннотаций страницы
1. Определите новый объект класса TextAbsorber
1. Используйте метод visit класса TextAbsorber, чтобы получить текст

```cpp
void Parsing::ExtractTextFromStamp()
{
      std::clog << __func__ << ": Start" << std::endl;
      // Строка для имени пути
      String _dataDir("C:\\Samples\\Parsing\\");

      // Строка для имени файла
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